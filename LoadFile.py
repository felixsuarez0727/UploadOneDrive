import os
import requests
import json
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID='57531bfd-82b3-4dbd-a75a-bd0212115eb5' #App ID on Azure
SCOPES=['Files.ReadWrite.All'] #Privileges

access_token = generate_access_token(APP_ID, SCOPES) #Login, it will ask to do it by a code, shown in terminal

headers = {
    'Authorization' : 'Bearer ' + access_token['access_token']
}

file_path = r'C:\Users\Usuario\source\SANDBOX\felix\PyOne\normalizacion.pdf' #file path
file_name = os.path.basename(file_path) #get file name

with open(file_path, 'rb') as upload: #open file to read binary
    media_content = upload.read()
 
#request for uploading file
response = requests.put(
    GRAPH_API_ENDPOINT + f'/me/drive/items/root:/{file_name}:/content',
    headers=headers,
    data=media_content
)

if response.status_code == 201:
    print("File uploaded successfully!")
else:
    print(f"Error uploading file: {response.text}")
