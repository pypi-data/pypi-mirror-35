from .device import Device
from .trip import Trip
from .authentication import Authentication
import requests

class API:

    def __init__(self, client_id, client_secret, username, password):
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password
        self.authentication_info = None

    def logged_in(self):
        if (self.authentication_info is None):
            return False
        else:
            return self.authentication_info.is_valid()

    def login(self):
        import requests

        data_url = "https://api.ritassist.nl/api/session/login"

        body = {
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'username': self._username,
            'password': self._password
        }

        response = requests.post(data_url, json=body)

        self.authentication_info = Authentication()
        self.authentication_info.set_json(response.json())
        return self.logged_in()

    def get_devices(self):
        if (self.authentication_info is None or
            not self.authentication_info.is_valid()):
            return []

        data_url = "https://api.ritassist.nl/api/equipment/Getfleet"
        query = "?groupId=0&hasDeviceOnly=false"

        header = self.authentication_info.create_header()
        response = requests.get(data_url + query, headers=header)
        data = response.json()
        return self.parse_devices(data)

    def parse_devices(self, json):
        """Parse result from API."""
        result = []

        for json_device in json:
            license_plate = json_device['EquipmentHeader']['SerialNumber']

            device = Device(self, license_plate)
            device.update_from_json(json_device)
            result.append(device)

        return result