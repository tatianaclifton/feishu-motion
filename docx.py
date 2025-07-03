import os
import requests

def create_doc(title, content):
    token = os.getenv("O6TtbrlFEaxdxwscAAZuRMZnsBb")
    url = "https://open.feishu.cn/open-apis/docx/v1/documents"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    body = {
        "title": title,
        "content": {
            "elements": [
                {"type": "text", "text": content}
            ]
        }
    }

    response = requests.post(url, headers=headers, json=body)
    print("Docx API response:", response.json())
