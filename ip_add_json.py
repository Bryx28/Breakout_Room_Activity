import requests

#Class for Getting the IP Address Information of the User
class Own_IP_Address:

    #Initialization of API to get Public IP Address of the User
    def __init__(self):
        self.main_url = 'https://ipapi.co/json/'
        self.loc = requests.get(self.main_url)
        self.ip_info = self.loc.json()

    #Get the Public IP Address of the User
    def get_ip(self):

        #Getting the IP Address and it's version
        self.public_ip = self.ip_info['ip']
        self.public_ip_type = self.ip_info['version']

        #Display of IP Address Information
        return (self.public_ip, self.public_ip_type)

    #Get the Geological Location of the User
    def get_geological_info(self):

        #Getting the Information of the Location
        self.ip_loc_country_code = self.ip_info['country_code']
        self.ip_loc_country = self.ip_info['country_name']
        self.ip_loc_region = self.ip_info['region']
        self.ip_loc_latitute = self.ip_info['latitude']
        self.ip_loc_longitude = self.ip_info['longitude']

        return (self.ip_loc_country_code,
                self.ip_loc_country,
                self.ip_loc_region,
                self.ip_loc_latitute,
                self.ip_loc_longitude)
    
    #Getting the ISP and ASN of the User IP Address
    def get_isp_info(self):
        #Getting the ISP and ASN
        self.ip_isp = self.ip_info['org']
        self.ip_asn = self.ip_info['asn']

        return (self.ip_isp, self.ip_asn)
