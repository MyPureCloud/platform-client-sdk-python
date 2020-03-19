from enum import Enum


class PureCloudRegionHosts(Enum):
    us_east_1 = "https://api.mypurecloud.com"
    eu_west_1 = "https://api.mypurecloud.ie"
    ap_southeast_2 = "https://api.mypurecloud.com.au"
    ap_northeast_1 = "https://api.mypurecloud.jp"
    eu_central_1 = "https://api.mypurecloud.de"
    us_west_2 = "https://api.usw2.pure.cloud"
    ca_central_1 = "https://api.cac1.pure.cloud"
    ap_northeast_2 = "https://api.apne2.pure.cloud"
    eu_west_2 = "https://api.euw2.pure.cloud"

    def __init__(self, apihost):
        self.apihost = apihost

    def get_api_host(self):
        return self.apihost



