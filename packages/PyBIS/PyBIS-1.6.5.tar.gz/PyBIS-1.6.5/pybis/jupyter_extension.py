from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler
from pybis import Openbis

o = Openbis(url='https://sprint-openbis.ethz.ch')
o.login('vermeul', 'tea4you2')

import json
import os
import urllib
from subprocess import check_output
from urllib.parse import urlsplit, urlunsplit


def _jupyter_server_extension_paths():
    return [{'module': 'gitlab_commit_push'}]


def load_jupyter_server_extension(nb_server_app):
    """Call when the extension is loaded.

    :param nb_server_app: Handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'

    route_pattern = url_path_join(web_app.settings['base_url'], '/openbis/dataset')
    web_app.add_handlers(host_pattern, [(route_pattern, DataSetHandler)])
    print("pybis loaded: {}".format(Openbis))


class DataSetHandler(IPythonHandler):
    """Download the requested DataSet"""


    def put(self):
        """Handle a user PUT request."""

        permId = self.get_json_body()

        try:
            ds = o.get_dataset(permId)
        except ValueError:
            self.write({
                'status':
                    404,
                'statusText':
                    'DataSet {} could not be found.'.format(permId)
            })
            return

        try: 
            destination = ds.download()
        except Exception as e:
            self.write({
                'status':
                    404,
                'statusText':
                    'DataSet {} could not be downloaded: {}'.format(permId, e)
            })
            return
            
        path = os.path.join(destination, ds.permId)

        self.write({
            'status':
                200,
            'permId': ds.permId,
            'statusText':
                'DataSet was successfully downloaded to {}.'.format(path)
        })
