from configparser import ConfigParser
from click import echo

VERSION = '0.0.67'
ROOT_DIR = '/root'

HOST_ADDRESS = 'eubflow.eubchain.com'
HTTP_ADDRESS = 'https://%s' % HOST_ADDRESS
WS_ADDRESS = 'wss://%s:54188/' % HOST_ADDRESS
EUBC_SERVER_ADDRESS = 'http://localhost:8088'

ENABLE_VERBOSE = False
DOCKER_WHITE_LIST = ['rancher_agent']
CONFIG_FILE_LOCATION = '.eubc_config.ini'

DEFAULT_CONFIG = {
    'HOST_ADDRESS': HOST_ADDRESS,
    'HTTP_ADDRESS': HTTP_ADDRESS,
    'WS_ADDRESS': WS_ADDRESS,
    'EUBC_ADDRESS': None,
    'EUBC_ADDRESS_PRIVATE': None,
    'EUBC_SERVER_ADDRESS': EUBC_SERVER_ADDRESS
}


class Config:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFIG_FILE_LOCATION)

    def set(self, key, value):
        if key in DEFAULT_CONFIG.keys():
            self.config.set('DEFAULT', key, value)
            with open(CONFIG_FILE_LOCATION, 'w+') as config_file:
                self.config.write(config_file)
        else:
            echo('Unsupported configuration information')

    def get(self, key):
        value = self.config.get('DEFAULT', key, fallback=DEFAULT_CONFIG[key])
        return value
