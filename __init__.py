import logging

DOMAIN = "formation_video"

_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    _LOGGER.warning("Intégration formation vidéo initialisé !")
    return True
