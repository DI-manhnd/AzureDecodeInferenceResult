#   latest_inference_data = base64.b64decode(raw_data["Inferences"][0]["O"])
#     print(latest_inference_data)
#     ppl_out = UploadData.GetRootAsUploadData(latest_inference_data, 0)
#     num_dead_tracks = ppl_out.ListDeadTrackLength()
#     print(ppl_out)
#     print(num_dead_tracks)

#     raw, ect, raw_all = decode_od_result(latest_inference_data, raw_data["DeviceID"])

#     print("Raw data:", raw)
#     print("Ect:", ect)
#     print("Raw all:", raw_all)
#     print(raw_all[0]['timestamp'])

#     json_data = json.dumps(raw_all, indent=4, cls=CustomEncoder)

#     # Write JSON data to a file
#     with open('raw_all_data3.json', 'w') as json_file:
#         json_file.write(json_data)

#     print("JSON file has been created.")
