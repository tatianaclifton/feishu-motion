import os
import requests

def create_record(fields):
    token = os.getenv("O6TtbrlFEaxdxwscAAZuRMZnsBb")
    url = "https://open.feishu.cn/open-apis/bitable/v1/apps/O6TtbrlFEaxdxwscAAZuRMZnsBb/tables/tbl12nnf1XtAdOcR/records"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = { "fields": fields }

    response = requests.post(url, headers=headers, json=data)
    print("Bitable API response:", response.json())
