import subprocess
from homeassistant.helpers.entity import Entity

DOMAIN = 'raspberry_pi_temperature'


def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([RaspberryPiTemperature()])


class RaspberryPiTemperature(Entity):
    @property
    def name(self):
        return "Raspberry Pi Temperature"

    @property
    def unit_of_measurement(self):
        return "°C"

    def update(self):
        temperature_raw = subprocess.check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"])
        temperature = float(temperature_raw) / 1000
        self._state = round(temperature, 2)
