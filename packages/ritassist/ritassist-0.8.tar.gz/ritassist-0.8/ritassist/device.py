from .trip import Trip
from .address import Address

class Device:
    """Entity used to store device information."""

    def __init__(self, data, license_plate):
        """Initialize a RitAssist device, also a vehicle."""
        self.attributes = {}
        self._data = data
        self._license_plate = license_plate

        self._identifier = None
        self._make = None
        self._model = None
        self._active = False
        self._odo = 0
        self._latitude = 0
        self._longitude = 0
        self._altitude = 0
        self._speed = 0
        self._last_seen = None
        self._equipment_id = None

        self._malfunction_light = False
        self._fuel_level = -1
        self._coolant_temperature = 0
        self._power_voltage = 0

        self._current_maximum_speed = 0
        self._current_address = None

    @property
    def identifier(self):
        """Return the internal identifier for this device."""
        return self._identifier

    @property
    def plate_as_id(self):
        """Format the license plate so it can be used as identifier."""
        return self._license_plate.replace('-', '')

    @property
    def license_plate(self):
        """Return the license plate of the vehicle."""
        return self._license_plate

    @property
    def equipment_id(self):
        """Return the equipment_id of the vehicle."""
        return self._equipment_id

    @property
    def latitude(self):
        """Return the latitude of the vehicle."""
        return self._latitude

    @property
    def longitude(self):
        """Return the longitude of the vehicle."""
        return self._longitude

    @property
    def state_attributes(self):
        """Return all attributes of the vehicle."""

        address_attributes = None
        if (self._current_address is not None):
            address_attributes = self._current_address.state_attributes()

        return {
            'id': self._identifier,
            'make': self._make,
            'model': self._model,
            'license_plate': self._license_plate,
            'active': self._active,
            'odo': self._odo,
            'latitude': self._latitude,
            'longitude': self._longitude,
            'altitude': self._altitude,
            'speed': self._speed,
            'last_seen': self._last_seen,
            'friendly_name': self._license_plate,
            'equipment_id': self._equipment_id,
            'fuel_level': self._fuel_level,
            'malfunction_light': self._malfunction_light,
            'coolant_temperature': self._coolant_temperature,
            'power_voltage': self._power_voltage,
            'current_max_speed': self._current_maximum_speed,
            'current_address': address_attributes
        }

    def get_trips(self, authentication_info, start, end):
        """Get trips for this device between start and end."""
        import requests

        if (authentication_info is None or
            not authentication_info.is_valid()):
            return []

        data_url = "https://api.ritassist.nl/api/trips/GetTrips"
        query = f"?equipmentId={self.identifier}&from={start}&to={end}&extendedInfo=True"
        header = authentication_info.create_header()
        response = requests.get(data_url + query, headers=header)
        trips = response.json()

        result = []
        for trip_json in trips:
            trip = Trip(trip_json)
            result.append(trip)
        return result

    def get_extra_vehicle_info(self, authentication_info):
        """Get extra data from the API."""
        import requests

        base_url = "https://secure.ritassist.nl/GenericServiceJSONP.ashx"
        query = "?f=CheckExtraVehicleInfo" \
                "&token={token}" \
                "&equipmentId={identifier}" \
                "&lastHash=null&padding=false"

        parameters = {
            'token': authentication_info.access_token,
            'identifier': str(self.identifier)
        }

        response = requests.get(base_url + query.format(**parameters))
        json = response.json()

        self._malfunction_light = json['MalfunctionIndicatorLight']
        self._fuel_level = json['FuelLevel']
        self._coolant_temperature = json['EngineCoolantTemperature']
        self._power_voltage = json['PowerVoltage']

    def update_from_json(self, json_device):
        """Set all attributes based on API response."""
        self._identifier = json_device['Id']
        self._license_plate = json_device['EquipmentHeader']['SerialNumber']
        self._make = json_device['EquipmentHeader']['Make']
        self._model = json_device['EquipmentHeader']['Model']
        self._equipment_id = json_device['EquipmentHeader']['EquipmentID']
        self._active = json_device['EngineRunning']
        self._odo = json_device['Odometer']
        self._latitude = json_device['Location']['Latitude']
        self._longitude = json_device['Location']['Longitude']
        self._altitude = json_device['Location']['Altitude']
        self._speed = json_device['Speed']
        self._last_seen = json_device['Location']['DateTime']

    def get_map_details(self):
        import requests

        url = "https://overpass-api.de/api/interpreter"
        query = f"[out:json][timeout:25]; ( way(around:25, {self.latitude}, {self.longitude})[maxspeed]; node(around:100, {self.latitude}, {self.longitude})['addr:city']; ); out;"
        response = requests.post(url, query)
        data = response.json()

        way = self.get_closest_way(data)

        if (way is not None):
            self._current_maximum_speed = way['tags']['maxspeed']
        else:
            self._current_maximum_speed = 0

        street = self.get_closest_street(data)
        if (street is not None):
            self._current_address = Address(None)

            self._current_address.city = street['tags']['addr:city']
            self._current_address.address = street['tags']['addr:street']
            self._current_address.house_number = street['tags']['addr:housenumber']
            self._current_address.postal_code = street['tags']['addr:postcode']
        else:
            self._current_address = None

    def get_closest_way(self, json):
        for element in json['elements']:
            if (element['type'] == 'way'):
                return element

        return None
    
    def get_closest_street(self, json):
        result = []

        for element in json['elements']:
            if (element['type'] == 'node'):
                result.append(element)
        
        return self.get_closest_element(result)

    def get_closest_element(self, elements):
        import geopy.distance

        if (len(elements) > 0):
            min_distance = 99999999
            result = elements[0]

            for element in elements:
                d_position = (self.latitude, self.longitude)
                e_position = (element['lat'], element['lon'])
                distance = geopy.distance.vincenty(d_position, e_position).km

                if (distance < min_distance):
                    result = element
                    min_distance = distance
            
            return result
        else:
            return None