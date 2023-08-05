
# Envoi de SMS via FreeMobile
FREE_USER = ''
FREE_PASSWORD = ''

try:
    # try to override settings
    from .local_settings import *
except ImportError:
    pass
