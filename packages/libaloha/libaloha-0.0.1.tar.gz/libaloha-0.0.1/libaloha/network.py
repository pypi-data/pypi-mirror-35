#!/usr/bin/env python3

import logging
import os
import re
import requests
import requests.exceptions
import socket
import subprocess

logger = logging.getLogger(__name__)


def get_hostname():
    """Récupère le nom d'hôte de la machine"""
    return socket.getfqdn()


def get_public_ip():
    """Récupère l'adresse IP publique de la machine grâce au service ipify.org"""
    
    url = 'https://api.ipify.org'
    try:
        ip = requests.get(url, timeout=5).text
    except requests.exceptions.ConnectionError as e:
        logger.warning("get_public_ip: Erreur à la récupération de l'adresse IP publique")
        logger.warning(e)
        return
        
    return ip.strip()


def resolve_hostname(hostname):
    """Retourne l'adresse IP associée au nom de domaine donné en paramètre."""
    
    if not is_valid_hostname(hostname):
        logger.warning("resolve_hostname: Nom d'hôte incorrect : {}"
                     .format(hostname))
        return False
        
    try:
        ip_addr = socket.gethostbyname(hostname)
        logger.debug("resolve_hostname: Résolution de {} en {}"
                    .format(hostname, ip_addr))
        return ip_addr
    except socket.gaierror:
        logger.warning("resolve_hostname: Résolution d'un hôte impossible : {}"
                     .format(hostname))
        return False


def is_valid_hostname(hostname):
    """Retourne True si le nom de l'hôte passé en paramètre est correct"""
    
    if len(hostname) > 255:
        return False
    hostname = hostname.rstrip(".")
    allowed = re.compile("(?!-)[A-Z\d\-\_]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))


def is_alive(hostname):
    """Retourne True si l'hôte passé en paramètre répond à un PING standart"""
    
    # On vérifie d'abord si l'hôte peut être résolu en IP
    if not resolve_hostname(hostname):
        logger.warning("is_alive: Nom d'hôte incorrect : {}".format(hostname))
        return False
        
    ret_code = subprocess.call(['ping', '-c', '1', '-W', '2', hostname],
        stdout=open(os.devnull, 'w'),
        stderr=open(os.devnull, 'w'))
    
    return ret_code == 0


def is_http_alive(hostname, timeout=10):
    """Retourne True si l'hôte passé en paramètre possède un serveur HTTP valide"""
    
    if not hostname.startswith('http://') and not hostname.startswith('https://'):
        hostname = 'http://{}'.format(hostname)

    try:
        resp = requests.head(hostname, timeout=timeout)
    except requests.exceptions.ReadTimeout:
        logger.warning("is_http_alive: {} ne répond pas (timeout: {})"
                       .format(hostname, timeout))
        return False

    # Si on subit une redirection
    if resp.status_code == 301 or resp.status_code == 302:
        redirect = resp.headers['Location']
        logger.info("is_http_alive: {} est redirigé vers {}"
                    .format(hostname, redirect))
        return is_http_alive(redirect, timeout=timeout)
        
    if resp.status_code != 200:
        logger.warning("is_http_alive: {} retourne le code {}"
                       .format(hostname, resp.status_code))

    return resp.status_code == 200
