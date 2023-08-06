from zeep import Client
from zeep import xsd
import json


SERVER_IP = '192.168.1.254'
class RemoteControl_v01:
    def __init__(self, 
        server_address='192.168.1.254',
        manager_id='AILAB',
        manager_password='ailab2018',
        station_id='ST3',
        thermal_in_point='/ST3/OFa3/LPa13',
        thermal_out_point='/ST3/OFa3/LPa14',
        cooling_valve_point='/ST3/OFa3/LPa22',
        heating_valve_point='/ST3/OFa3/LPa23',
        mode_station_point='/ST3/OFa3/LPa49'):

        # Services
        self.system_service_endpoint = Client('http://' + server_address + ':9999/bms/ws/SystemService?wsdl')
        self.user_service_endpoint = Client('http://' + server_address + ':9999/bms/ws/UserService?wsdl')
        self.point_service_endpoint = Client('http://' + server_address + ':9999/bms/ws/PointService?wsdl')
        self.id = manager_id
        self.password = manager_password
        self.station_id = station_id
        self.client_type = 'tm'
        self.country = 'ko'
        self.client_id = ''
        
        # Thermal In sensor
        thermal_in_station_path = 'point:' + thermal_in_point
        self.thermal_in_station_paths = []
        self.thermal_in_station_paths.append(thermal_in_station_path)

        # Thermal OUT sensor
        thermal_out_station_path = 'point:' + thermal_out_point
        self.thermal_out_station_paths = []
        self.thermal_out_station_paths.append(thermal_out_station_path)

        # Cooling Valve controller
        cooling_valve_station_path = 'point:' + cooling_valve_point
        self.cooling_valve_station_paths = []
        self.cooling_valve_station_paths.append(cooling_valve_station_path)
        self.set_cooling_valve_station_path = cooling_valve_point

        # Heating Valve controller
        heating_valve_station_path = 'point:' + heating_valve_point
        self.heating_valve_station_paths = []
        self.heating_valve_station_paths.append(heating_valve_station_path)
        self.set_heating_valve_station_path = heating_valve_point

        # Mode switcher
        mode_station_path = 'point:' + heating_valve_point
        self.mode_station_paths = []
        self.mode_station_paths.append(mode_station_path)
        self.set_mode_station_path = heating_valve_point


    def login(self):
        encrypted_password = self.system_service_endpoint.service.getEncryptString(self.password)
        response = self.user_service_endpoint.service.forcedLogin(self.id, encrypted_password, self.client_type, self.country)
        self.client_id = response.clientId

        if (response == 1):
            print('log in success.')
        else:
            print('Error: log in fail.')


    def logout(self):
        response = self.user_service_endpoint.service.logout(self.client_id)
        if (response == 1):
            print('log out success.')
        else:
            print('Error: log out fail.')


    def get_temperatue(self):
        # [1] Get current thermal value
        response = self.point_service_endpoint.service.getPointValues(self.client_id, self.station_id, self.thermal_out_station_paths)
        # print('[Thermal status]')
        # print(thermal_response)
        print(response['pointValues'])
        temperature = response['pointValues'][0]['presentValue']
        print('.'*50)

        return float(temperature)


    def set_mode(self, mode='manual'):
        # On: manual, Off: automatic
        if mode=='manual':
            mode_value='On'
        elif mode=='automatic':
            mode_value='Off'

        value = {
            'presentValue': '0.0',
            'settingValue': mode_value,  # On: manual, Off: automatic
            'pointPath': self.set_mode_station_path,
            'pointState': 'NORMAL',
            'settingPriority': 11,
            'ddcAlarmStatus': '0',
            'ddcCorrectionValue': 0
            }

        values = []
        values.append(value)
        self.point_service_endpoint.service.setPointValues(self.client_id, self.station_id, values)


    def get_mode(self):
        response = self.point_service_endpoint.service.getPointValues(self.client_id, self.station_id, self.mode_station_paths)
        print('[Mode status]')
        # print(mode_response)
        print(response['pointValues'])
        mode = response['pointValues'][0]['presentValue']
        print('Mode: ', mode)
        print('.'*50)


    def set_output(self, valve='cooling', output=0):
        # [4] Set valve output
        valve_station_path = None
        if valve=='cooling':
            valve_station_path = self.set_cooling_valve_station_path
        elif valve=='heating':
            valve_station_path = self.set_heating_valve_station_path

        value = {
            'presentValue': '0.0',
            'settingValue': str(output),
            'pointPath': valve_station_path,
            'pointState': 'NORMAL',
            'settingPriority': 11,  # 11
            'ddcAlarmStatus': '0',
            'ddcCorrectionValue': 0
        }
        values = []
        values.append(value)
        self.point_service_endpoint.service.setPointValues(self.client_id, self.station_id, values)


    def get_output(self, valve='cooling'):
        valve_response = None
        if valve == 'cooling':
            valve_response = self.point_service_endpoint.service.getPointValues(self.client_id, self.station_id, self.cooling_valve_station_paths)
        elif valve == 'heating':
            valve_response = self.point_service_endpoint.service.getPointValues(self.client_id, self.station_id, self.heating_valve_station_paths)

        output = valve_response['pointValues'][0]['presentValue']

        return output



