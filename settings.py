import configparser
import requests
from dataclasses import dataclass

@dataclass
class TelegramSettings:
    token: str
    chat_id: str

@dataclass
class ChartinkSettings:
    base_url: str
    process_url: str

@dataclass
class Settings:
    telegram: TelegramSettings
    chartink: ChartinkSettings

def load_settings_from_url(url: str) -> Settings:
    # Step 1: Fetch the config content as string
    response = requests.get(url)
    response.raise_for_status()
    config_text = response.text

    # Step 2: Parse it using configparser
    config = configparser.ConfigParser()
    config.read_string(config_text)

    # Step 3: Create settings objects
    telegram = TelegramSettings(
        token=config['telegram']['token'],
        chat_id=config['telegram']['chat_id']
    )

    chartink = ChartinkSettings(
        base_url=config['chartink']['base_url'],
        process_url=config['chartink']['process_url']
    )

    return Settings(telegram=telegram, chartink=chartink)
