#!/usr/bin/env python3

import requests
from requests.packages import urllib3
from . import settings

import logging
logger = logging.getLogger(__name__)


class FreeClient:
    BASE_URL = 'https://smsapi.free-mobile.fr/sendmsg'
    
    def __init__(self, user, passwd):
        """
        Create a new Free Mobile SMS API client. Each client is tied to a phone number.
        https://github.com/bfontaine/freesms
        """
        self._user = user
        self._passwd = passwd

    def send_sms(self, text, **kwargs):
        """
        Send an SMS. Since Free only allows us to send SMSes to ourselves you
        don't have to provide your phone number.
        """

        if not self._user or not self._passwd:
            raise AttributeError("User '{}' or password '{}' is null".format(
                self._user, self._passwd
            ))

        params = {
            'user': self._user,
            'pass': self._passwd,
            'msg': text
        }

        if not kwargs.get('verify', False):
            # remove SSL warning
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        res = requests.get(FreeClient.BASE_URL, params=params, **kwargs)
        
        if res.status_code == 200:
            return True
        
        if res.status_code == 400:
            logger.error("Un des paramètres obligatoires est manquant")
        elif res.status_code == 402:
            logger.error("Trop de SMS ont été envoyés en trop peu de temps")
        elif res.status_code == 403:
            logger.error("Le service n'est pas activé sur l'espace abonné, ou login / clé incorrect")
        elif res.status_code == 500:
            logger.error("Error côté serveur. Veuillez réessayer ultérieurement")
            
        return False
        

def send_to_me(text):
    logger.debug("Envoi d'un SMS à moi-même: {}".format(text))
    client = FreeClient(settings.FREE_USER, settings.FREE_PASSWORD)
    return client.send_sms(text)
