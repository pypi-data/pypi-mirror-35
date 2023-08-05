import sys
import libaloha.network
import libaloha.sms

from .check_ip import App


def check_ip():
    return App().run()


def send_sms():
    if len(sys.argv) <= 1:
        print("Usage: {} <message>".format(sys.argv[0]))
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    libaloha.sms.send_to_me(text)


def check_website_alive():
    if len(sys.argv) != 2:
        print("Usage: {} <domain-name>".format(sys.argv[0]))
        sys.exit(2)

    hostname = sys.argv[1]
    if not libaloha.network.is_valid_hostname(hostname):
        print("Le nom de domaine fourni ne semble pas valide")
        sys.exit(2)

    if libaloha.network.is_http_alive(hostname):
        print("Le serveur oueb est vivant :-)")
        sys.exit(0)
    else:
        print("Le serveur oueb ne répond pas :-(")
        sys.exit(1)
