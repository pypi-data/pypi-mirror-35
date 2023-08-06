import json
from .location import *
import requests


class GardenaSmartAccount:
    def __init__(self, email_address=None, password=None):
        self.locations = set()
        self.raw_locations = None
        self.s = requests.session()
        self.email_address = email_address
        self.password = password
        self.update_authtokens()


    def load_locations(self):
        url = "https://smart.gardena.com/sg-1/locations/"
        params = (
            ('user_id', self.userID),
        )
        headers = self.create_header(Token=self.AuthToken)
        response = self.s.get(url, headers=headers, params=params)
        response_data = json.loads(response.content.decode('utf-8'))
        self.raw_locations = response_data
        for location in response_data['locations']:
            self.locations.add(GardenaSmartLocation(self, location))

    def get_locations(self):
        if len(self.locations) == 0:
            self.load_locations()
        return self.locations

    def get_raw_location_data(self, location_id):
        for location in self.raw_locations:
            if location.id == location_id:
                return location
        # @todo trow exception if not found

    def update_devices(self):
        for location in self.locations:
            location.update_devices()

    def create_header(self, Token=None, ETag=None):
        headers={
            'Content-Type': 'application/json',
        }
        if Token is not None:
            headers['X-Session']=Token
        if ETag is not None:
            headers['If-None-Match'] = ETag
        return headers

    def update_authtokens(self):
        """Get authentication token from servers"""
        data = '{"sessions":{"email":"' + self.email_address + '","password":"' + self.password + '"}}'
        url = 'https://smart.gardena.com/sg-1/sessions'
        headers = self.create_header()
        response = self.s.post(url, headers=headers, data=data)
        response_data = json.loads(response.content.decode('utf-8'))
        self.AuthToken = response_data['sessions']['token']
        self.refreshToken = response_data['sessions']['refresh_token']
        self.userID = response_data['sessions']['user_id']

    def get_all_mowers(self):
        all_mowers = set()
        for location in self.get_locations():
            for mower in location.get_mowers():
                all_mowers.add(mower)
        return all_mowers

    def get_all_sensors(self):
        all_sensors = set()
        for location in self.get_locations():
            for sensor in location.get_sensors():
                all_sensors.add(sensor)
        return all_sensors

    def get_all_watering_computers(self):
        all_sensors = set()
        for location in self.get_locations():
            for watering_computer in location.get_watering_computers():
                all_sensors.add(watering_computer)
        return all_sensors


