from dataclasses import dataclass
from typing import Optional
from io import StringIO
import requests
import csv


@dataclass
class ChartingData:
    active: int
    message: Optional[str]
    alert_message: Optional[str]
    screener_name: str
    scan_clause: str
    debug_clause: str


def load_charting_data_from_url(url: str) -> list[ChartingData]:
    # Fetch the CSV content
    response = requests.get(url)
    response.raise_for_status()
    csv_text = response.text

    # Use StringIO to make it file-like
    csv_file = StringIO(csv_text)

    # Parse CSV rows
    reader = csv.DictReader(csv_file)
    objects = []
    for row in reader:
        obj = ChartingData(
            active=int(row["active"]),
            message=row["message"] or None,
            alert_message=row["alert_message"] or None,
            screener_name=row["screener_name"],
            scan_clause=row["scan_clause"],
            debug_clause=row["debug_clause"]
        )
        objects.append(obj)

    return objects