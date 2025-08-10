import json
import requests
import logger
import time
from bs4 import BeautifulSoup
from chart_data import ChartingData
from settings import ChartinkSettings

def get_chartink_scan_results(chartingData: ChartingData,chartinkSettings : ChartinkSettings):
        
    url = chartinkSettings.base_url.format(chartingData.screener_name)
            
    # 1. Start session
    session = requests.Session()
    response = session.get(url)
    response.raise_for_status()

    # 2. Extract CSRF token from HTML <meta>
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find("meta", attrs={"name": "csrf-token"})["content"]
    
    # 3. Extract cookies
    xsrf_token = session.cookies.get("XSRF-TOKEN")
    ci_session = session.cookies.get("ci_session")

    # 4. Prepare headers & payload
    cookie_header = f"XSRF-TOKEN={xsrf_token}; ci_session={ci_session}"

    headers = {
        "X-CSRF-TOKEN": csrf_token,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": cookie_header,
        "Origin": "https://chartink.com",
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
        
    logger.info(f"scan_clause: {chartingData.scan_clause}")
    logger.info(f"debug_clause: {chartingData.debug_clause}")
    
    payload = {
        "scan_clause": chartingData.scan_clause,
        "debug_clause": chartingData.debug_clause
    }

    # 5. POST request
    response = session.post(chartinkSettings.process_url, headers=headers, data=payload)
    response.raise_for_status()

    # 6. Parse JSON safely
    try:
        data = response.json()  # cleaner than json.loads(response.text)
    except json.JSONDecodeError:
        raise ValueError("Chartink response was not valid JSON")

    return data.get("data", [])


def run_multiple_scans_from_csv(csv_data: list[ChartingData], chartink_settings: ChartinkSettings):    
    all_results = {}
    for row in csv_data:
        if row.active != 1:
            continue
        logger.processing(f"Running scan for: {row.screener_name}") # Optional logging
        results = get_chartink_scan_results(row, chartink_settings)       
        if results:
            key = row.message if row.message else row.screener_name
            all_results[key] = results            
        time.sleep(10)
    return all_results