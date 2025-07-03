import os
import requests

def get_tenant_access_token():
    app_id = os.environ.get("cli_a8efc5c01310100e")
    app_secret = os.environ.get("APP_SECRET")  # You'll need to define this in Replit Secrets
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    payload = {"app_id": app_id, "app_secret": app_secret}
    res = requests.post(url, json=payload)
    return res.json().get("tenant_access_token")
