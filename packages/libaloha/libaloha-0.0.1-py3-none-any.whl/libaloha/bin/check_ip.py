#!/usr/bin/env python3

import os
import sys
import logging
import textwrap
import libaloha.sms
import libaloha.network

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.INFO)
logger = logging.getLogger()


class App:
    
    def __init__(self):
        
        # Fichier de sauvegarde
        try:
            self.save_file = os.path.join(os.environ['HOME'], '.my-public-ip')
        except KeyError:
            logger.warning("La variable d'environnement 'HOME' n'est pas définie.")
            logger.warning("Enregistrement du fichier dans le répertoire courant.")
            self.save_file = '.my-public-ip'
        
    def get_last_known_ip(self):
        """Lire la dernière IP connue depuis le fichier de sauvegarde"""
        
        if not os.path.isfile(self.save_file):
            return None
        
        with open(self.save_file, 'r') as f:
            ip = f.read()
        return ip.strip()

    def save_current_ip(self, ip):
        """Enregistre l'IP courant dans le fichier de sauvegarde"""
        
        with open(self.save_file, 'w') as f:
            f.write(ip)

    def run(self):
        """Exécute le programme"""
        
        ip = libaloha.network.get_public_ip()
        if not ip:
            logger.error("Impossible de récupérer l'IP publique de la machine !")
            sys.exit(1)
        
        hostname = libaloha.network.get_hostname()
        if not hostname:
            logger.error("Impossible de récupérer le nom de la machine !")
        
        last_ip = self.get_last_known_ip()
        if ip == last_ip:
            logger.info("L'adresse IP n'a pas été modifiée !")
            return
            
        if not last_ip:
            logger.info("Aucune IP connue à ce jour")
            
        elif ip != last_ip:
            logger.info("L'IP a été modifiée !")
            message = textwrap.dedent("""\
                L'adresse IP de la machine {} a été modifiée !
                
                Ancienne adresse : {}
                Nouvelle adresse : {}

                Merci de faire le nécessaire.
                Biz !""".format(hostname, last_ip, ip))
            libaloha.sms.send_to_me(message)
            
        self.save_current_ip(ip)
        

if __name__ == '__main__':
    app = App()
    app.run()
