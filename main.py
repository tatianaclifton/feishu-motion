from bitable import create_record
from docx import create_doc

if __name__ == "__main__":
    print("Feishu Motion Starter")
    create_doc("Welcome", "This is your first document.")
    create_record({"Task": "Set up project", "Status": "Done"})
