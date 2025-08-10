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
