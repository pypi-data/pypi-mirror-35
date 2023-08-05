class Address:
    def __init__(self, json):
        self.country = None
        self.address = None
        self.city = None
        self.postal_code = None
        self.house_number = None

        if (json is not None):
            self.parse_json(json)
    
    def parse_json(self, json):
        self.country = json['Country']
        self.address = json['Address']
        self.city = json['City']
        self.postal_code = json['PostalCode']

    def __str__(self):
        return f"{self.address}, {self.postal_code}, {self.city}, {self.country}"

    def state_attributes(self):
        return {
            'address': self.address,
            'house_number': self.house_number,
            'postal_code': self.postal_code,
            'city': self.city,
            'country': self.country
        }

