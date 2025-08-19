import requests
from settings import TelegramSettings


class TelegramClient:
    def __init__(self, settings: TelegramSettings):
        self.token = settings.token
        self.chat_id = settings.chat_id
        self.base_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send_message(self, message: str) -> str:
        if not message or message == "{}" or not message.strip():
            return "empty message"
        
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML",  # optional
        }
        try:           
            response = requests.post(self.base_url, data=payload)
            response.raise_for_status()
            return "success"
        except requests.RequestException as e:            
            return f"error:{e}"
        
        
    def send_long_messages(self, message: str) -> str:
        if not message or message == "{}" or not message.strip():
            return "empty message"
        
        max_len = 4000
        for i in range(0, len(message), max_len):
            chunk = message[i:i + max_len]
            self.send_message(chunk)
            

