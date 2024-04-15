import logging
import json
import logging
import os
import traceback
import azure.functions as func
import base64
import json
import requests
from datetime import datetime, timezone, timedelta
from modules.ppl_deserialization.ppl_decoderv2 import decode_od_result
from modules.ppl_deserialization.smart_camera.upload_data import UploadData


app = func.FunctionApp()
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
    
@app.route(route="process_inference", auth_level=func.AuthLevel.ANONYMOUS)
def process_inference(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing inference data.')
    # Check if the request body is empty
    if not req.get_body():
        return func.HttpResponse("Empty request body", status_code=400)
    try:
        raw_data = req.get_json()
        print('Data inference', raw_data)
    except ValueError:
        return func.HttpResponse("Invalid JSON data in request body", status_code=400)

    latest_inference_data = base64.b64decode(raw_data["Inferences"][0]["O"])
    ppl_out = UploadData.GetRootAsUploadData(latest_inference_data, 0)
    num_dead_tracks = ppl_out.ListDeadTrackLength()
    raw, ect, raw_all = decode_od_result(latest_inference_data, raw_data["DeviceID"])

    # print("Raw data:", raw)
    print("Ect:", ect)
    print("Data decode", raw_all)
    print(raw_all[0]['timestamp'])

    json_data = json.dumps(raw_all, indent=4, cls=CustomEncoder)

    # Write JSON data to a file
    with open('raw_all_data3.json', 'w') as json_file:
        json_file.write(json_data)

    print("JSON file has been created.")
    # --------------------- #
    return func.HttpResponse(
        "Inference data processed successfully.",
        status_code=200
    )



