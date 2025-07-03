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
    res_json = res.json()
    print("Token response:", res_json)
    return res_json.get("tenant_access_token")

def create_doc(title: str, content: str):
    token = get_tenant_token()
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "title": title,
        "content": {
            "elements": [
                {
                    "type": "text",
                    "text": {"content": content}
                }
            ]
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print("Docx API response:", response.text)
