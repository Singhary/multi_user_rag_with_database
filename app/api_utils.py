import requests
import streamlit as st

def get_api_response(question , session_id , model):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {"question":question , "model":model}
    
    if session_id:
        data["session_id"] = session_id
        
    try:
        response = requests.post("https://rag-backend-ej9k.onrender.com/chat", headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API request failed with status code {response.status_code}")
            return None
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    
def upload_document(file):
    try:
        files = {"file": (file.name , file , file.type)}
        print(f"files_info_in api_utils: {files}")
        response = requests.post("https://rag-backend-ej9k.onrender.com/upload-doc", files=files)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to uploadfile.Error:{response.status_code}")
            return None
        
    except Exception as e:
        st.error(f"An error occured while uploading the document: {str(e)}")
        return None
    
def list_documents():
    try:
        response = requests.get("https://rag-backend-ej9k.onrender.com/list-docs")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch document list. Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching the document list: {str(e)}")
        return []

def delete_document(file_id):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {"file_id": file_id}

    try:
        response = requests.post("https://rag-backend-ej9k.onrender.com/delete-doc", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to delete document. Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred while deleting the document: {str(e)}")
        return None