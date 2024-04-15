import requests
import json

# Define the URL of your locally running Azure Function endpoint
function_url = "http://localhost:7071/api/process_inference"

# JSON data to send
data = {
    "DeviceID": "sid-100A50500A2001079164012000000000",
    "ModelID": "0305010019290100",
    "Image": True,
    "Inferences": [
        {
            "T": "20240415060027240",
            "O": "FAAAAAAAAAAMABQABAAIAAwAEAAMAAAANAAAABwAAAAIAAAAMAAAAAoAAABzdG9yZS04MTIzAAAMAAAAY3VzdG9tZXItMjMxAAAAAAAAAAAAAAAAAgAAAKQAAAAcAAAAGAAsAAoADAAHAAgACQAYACAAEAAAABQAGAAAAAAAABIGAf//XAAAABwAAAAgAAAAikgAAAAAAAA81VbgjgEAAAAAAAABAAAAOQAAAIL///8kAAAAFAAAAAQAAABg////qgB7ABAAEQBs////vgBfABEAFgB4////qwB7AA4AEQAAAAAAGAAoAAYACAAEAAUAAAAUABwADAAAABAAGAAAABIG//9wAAAAHAAAACgAAABAagAAAAAAAHyzVuCOAQAAAAAAAAEAAAA4AAoAEAAEAAgADAAKAAAAMAAAABQAAAAEAAAA6P///xcBegAWABkA9P///+0AaAASABUADAAMAAQABgAIAAoADAAAABsBewATABcAAAAAAA=="
        }
    ],
    "project_id": "00g41cphzymjZzSSJ697",
    "id": "2546918313368_27641088_001_1713160829.974",
    "_rid": "0V4zAMNx9-Kn3XAQAAAACQ==",
    "_self": "dbs/0V4zAA==/colls/0V4zAMNx9-I=/docs/0V4zAMNx9-Kn3XAQAAAACQ==/",
    "_etag": "\"1a006184-0000-2300-0000-661cc27e0000\"",
    "_attachments": "attachments/",
    "_ts": 1713160830
}

# Send POST request to locally running Azure Function endpoint
response = requests.post(function_url, json=data)

# Print the response from locally running Azure Function
print(response.text)

# Save JSON data from response to a file
if response.status_code == 200:
    with open('response_data.txt', 'w') as json_file:
        json_file.write(response.text)
        print("JSON data saved to 'response_data.txt'")
else:
    print("Failed to save JSON data. Response status code:", response.status_code)
