import logging
from thunderpush.messenger import Messenger

logger = logging.getLogger()

class SortingStation(object):
    """ Handles dispatching messages to Messengers. """

    _instance = None

    def __init__(self, *args, **kwargs):
        if self._instance:
            raise Exception("SortingStation already initialized.")

        self.messengers_by_apikey = {}
        self.messengers_by_apisecret = {}

        SortingStation._instance = self

    @staticmethod
    def instance():
        return SortingStation._instance

    def create_messenger(self, apikey, apisecret):
        messenger = Messenger(apikey, apisecret)

        self.messengers_by_apikey[apikey] = messenger
        self.messengers_by_apisecret[apisecret] = messenger

    def delete_messenger(self, messenger):
        del self.messengers_by_apikey[messenger.apikey]
        del self.messengers_by_apisecret[messenger.apisecret]

    def get_messenger_by_apikey(self, apikey):
        return self.messengers_by_apikey.get(apikey, None)
