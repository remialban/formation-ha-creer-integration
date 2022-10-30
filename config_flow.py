from homeassistant import config_entries
from homeassistant.helpers import config_validation as cv

import voluptuous as vol

DOMAIN = "formation_video"

class ExampleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    async def async_step_user(self, info):
        if info is not None:
            return self.async_create_entry(title=info["zone_jours_ferries"] + " - " + info["zone_vacances"], data=info)


        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(
                {
                    vol.Required("zone_jours_ferries"): vol.In([
                        "alsace-moselle", "guadeloupe", "guyane", "la-reunion", "martinique", "mayotte", "metropole", "nouvelle-caledonie", "polynesie-francaise", "saint-barthelemy", "saint-martin", "saint-pierre-et-miquelon", "wallis-et-futuna"
                    ]),
                    vol.Required("zone_vacances"): vol.In([
                        "Zone A",
                        "Zone B",
                        "Zone C",
                        "Corse",
                        "Guadeloupe",
                        "Guyane",
                        "Martinique",
                        "Mayotte",
                        "Nouvelle Calédonie",
                        "Polynésie",
                        "Réunion",
                        "Saint Pierre et Miquelon",
                        "Wallis et Futuna"
                    ]),
                }
            )
        )
