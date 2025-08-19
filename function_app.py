import azure.functions as func
import datetime
import json
import logger
from blob_settings import BlobSettings
from settings import load_settings_from_url
from chart_data import load_charting_data_from_url
from telegram_client import TelegramClient
from chartink_scraper import run_multiple_scans_from_csv

app = func.FunctionApp()
blobSettings = BlobSettings()
settings = load_settings_from_url(blobSettings.get_setting_url())   
telegram_client = TelegramClient(settings.telegram)  

@app.timer_trigger(schedule="0 1,16,31,46 4-9 * * 1-5", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def charting_alert_timer_trigger(myTimer: func.TimerRequest) -> None:
       
    if myTimer.past_due:
        logger.info('The timer is past due!')

    #logging.info('Python timer trigger function executed.')            
    #logging.info(f"process URL234: {csv_chart_data[0].screener_name}")
    csv_chart_data = load_charting_data_from_url(blobSettings.get_csv_url())          
    results = run_multiple_scans_from_csv(csv_chart_data, settings.chartink,telegram_client) 
    message_text = json.dumps(results, indent=2)
    #telegram_client.send_message("Telegram setup working successfully.")
    telegram_client.send_long_messages(message_text)    
    logger.complete(f"Job completed: {datetime.datetime.now().isoformat()}")
    #func azure functionapp publish test-alert-func-app-example

