class BlobSettings:
    def __init__(self):       
       self.setting_url = "https://xxxxx.blob.core.windows.net/settings/settings.txt"
       self.csv_url= "https://xxxxx.blob.core.windows.net/settings/data.csv"           
       self.blob_sas_token = "sp=xxxxxxxyyyy3D"
        
    def get_setting_url(self):
        return f"{self.setting_url}?{self.blob_sas_token}"
    
    def get_csv_url(self):
        return f"{self.csv_url}?{self.blob_sas_token}"