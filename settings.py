class Settings:
    def __init__(self):       
        self.setting_url = "https://api.example.com/data"
        self.azure_storage_connection_string = "your_connection_string"       

    def get_setting_url(self):
        return f"DefaultEndpointsProtocol=https;AccountName={self.azure_storage_connection_string};EndpointSuffix=core.windows.net"
    
    def get_storage_connection_string(self):
        return f"DefaultEndpointsProtocol=https;AccountName={self.azure_storage_connection_string};AccountKey={self.storage_account_key};EndpointSuffix=core.windows.net"