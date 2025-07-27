class Settings:
    def __init__(self):       
        self.setting_url = "XXXX"
        self.csv_url= "XXXX"
        self.azure_storage_connection_string = "your_connection_string"       
        self.blob_sas_token = "XXX"
        
    def get_setting_url(self):
        return f"{self.setting_url}?{self.blob_sas_token}"
    
    def get_storage_connection_string(self):
        return f"{self.azure_storage_connection_string}"
    
    def get_csv_url(self):
        return f"{self.csv_url}?{self.blob_sas_token}"