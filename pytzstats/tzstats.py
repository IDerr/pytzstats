import requests
class Pytzstats:
    BASE_URL = ""
    def __init__(self, base_url='https://api.tzstats.com/'):
        super().__init__()
        self.BASE_URL = base_url
    # Explorer requests
    def get_explorer_status(self):
        PAGE_URL = "/explorer/status"
        return requests.get(self.BASE_URL + PAGE_URL).json()

    def get_explorer_config(self, id):
        PAGE_URL = f"/explorer/config/{id}"
        return requests.get(self.BASE_URL + PAGE_URL).json()
    
    def get_explorer_tip(self):
        PAGE_URL = f"/explorer/tip"
        return requests.get(self.BASE_URL + PAGE_URL).json()
    
    def get_explorer_protocols(self):
        PAGE_URL = f"/explorer/protocols"
        return requests.get(self.BASE_URL + PAGE_URL).json()

    def get_explorer_metadata(self):
        PAGE_URL = f"/explorer/metadata"
        return requests.get(self.BASE_URL + PAGE_URL).json()
    
    def get_explorer_metadata(self):
        PAGE_URL = f"/explorer/bakers"
        return requests.get(self.BASE_URL + PAGE_URL).json()
    # TODO: Finish Explorer requests
    # Accounts requests
    def get_account(self, hash):
        PAGE_URL = f"/explorer/account/{hash}"
        return requests.get(self.BASE_URL + PAGE_URL).json()
    
    def get_account_operations(self, hash):
        PAGE_URL = f"/explorer/account/{hash}/operations"
        return requests.get(self.BASE_URL + PAGE_URL).json()

    def get_account_contracts(self, hash):
        PAGE_URL = f"/explorer/account/{hash}/operations"
        return requests.get(self.BASE_URL + PAGE_URL).json()
    
    def get_account_ballots(self, hash):
        PAGE_URL = f"/explorer/account/{hash}/operations"
        return requests.get(self.BASE_URL + PAGE_URL).json()
    # Bakers