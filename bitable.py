import os
import requests

def get_tenant_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    headers = {"Content-Type": "application/json"}
    data = {
        "app_id": os.getenv("APP_ID"),
        "app_secret": os.getenv("APP_SECRET")
    }
    res = requests.post(url, json=data, headers=headers)
    return res.json().get("tenant_access_token")

def create_record(fields: dict):
    token = get_tenant_token()
    base_url = "https://open.feishu.cn/open-apis/bitable/v1/apps"
    app_token = os.getenv("APP_ID")  # Replace if you have a different APP_TOKEN (not APP_ID)
    table_id = os.getenv("TABLE_ID")

    url = f"{base_url}/{app_token}/tables/{table_id}/records"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {"records": [{"fields": fields}]}
    response = requests.post(url, headers=headers, json=data)
    print("Bitable API response:", response.text)
