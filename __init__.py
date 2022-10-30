from __future__ import annotations

import logging
import voluptuous as vol

from homeassistant.helpers import config_validation as cv

DOMAIN = "formation_video"

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required("prenom"): cv.string,
                vol.Optional("pays", default="France"): str,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)


def setup(hass, config):
    _LOGGER.warning("Intégration formation vidéo initialisé !")
    _LOGGER.warning("Bonjour " + config[DOMAIN]["prenom"])
    _LOGGER.warning("Pays : " + config[DOMAIN]["pays"])
    return True

async def async_setup_entry(hass, config):
    _LOGGER.warning(config)
    return True
