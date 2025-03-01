import os

import requests
from dotenv import load_dotenv

load_dotenv()

VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/files"
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")


def virustotal_report(file_path):
    files = {"file": (file_path, open(file_path, "rb"), "application/octet-stream")}
    headers = {"accept": "application/json", "x-apikey": VIRUSTOTAL_API_KEY}

    response = requests.post(VIRUSTOTAL_URL, files=files, headers=headers).json()

    analysis_link = response["data"]["links"]["self"]
    analysis_report = requests.get(analysis_link, headers=headers).json()
    return analysis_report
