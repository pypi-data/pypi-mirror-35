from .config import Config
from requests import get, post
from jwt import encode
from click import echo


class EubcServerApi:
    def __init__(self):
        config = Config()
        self.config = config
        self.eubc_server_url = config.get('EUBC_SERVER_ADDRESS')

    def get_eubc_server_url(self, url):
        return "%s/%s" % (self.eubc_server_url, url)

    def get_eubc_account(self):
        return get(self.get_eubc_server_url('/account')).json()

    def generate_secret_data(self, url, data={}):
        account = self.get_eubc_account()
        return encode(data, account.address + '/' + url)

    def create_eubc_account(self, url='/account/create'):
        return post(self.get_eubc_server_url(url), {'data': self.generate_secret_data(url)}).json()

    def import_private_key(self, url='/account/importPrivateKey'):
        address_private_key = self.config.get('EUBC_ADDRESS_PRIVATE')
        if address_private_key:
            return post(self.get_eubc_server_url(url),
                        {'data': self.generate_secret_data(url, {'privateKey': address_private_key})}).json()
        else:
            account = self.create_eubc_account()
            self.config.set('EUBC_ADDRESS', account.address)
            self.config.set('EUBC_ADDRESS_PRIVATE', account.privateKey)
            echo('Eubc address created ,address :%s,privateKey:%s' % (
                account.address, account.privateKey))
            self.import_private_key()
