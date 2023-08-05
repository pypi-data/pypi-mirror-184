import os

import requests

from src.cli.commands.parse_analysis.results import validade_analysis_response

BASE_URL = os.getenv("BASE_URL")


def parse_analysis(id):
    data = {"pre_config_id": id}
    response = requests.post(f"{BASE_URL}analysis", json=data)

    validade_analysis_response(response.status_code, response.json())
