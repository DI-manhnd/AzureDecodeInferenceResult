"""
author: anhnt
update: 20230508
"""

from datetime import datetime
from typing import List

from modules.converter import convert_unixtime_to_datetime
from modules.ppl_deserialization.smart_camera.upload_data import UploadData


def decode_od_result(ori_buf) -> List[datetime]:
    """
    This function decodes and extracts information from a binary buffer and populates a
    dictionary with the extracted data.

    :param buf: A dictionary containing inferences for a video stream, including information
    about people detected in the stream
    :param gender_head_age: It is a dictionary that maps gender and head age codes to their
    corresponding values. This is used to decode the gender and age information of the people
    detected in the input buffer
    :return: the modified `buf` dictionary with additional information about dead tracks, including
    track ID, timestamp, watch start time, watch time, age, gender, status, customer ID, store ID,
    device ID, detail watch time, and maximum watch duration.
    """
    timestamps = []
    # Deserialize
    ppl_out = UploadData.GetRootAsUploadData(ori_buf, 0)
    num_dead_tracks = ppl_out.ListDeadTrackLength()

    # Deserialize
    for i in range(num_dead_tracks):
        dead_track_data = ppl_out.ListDeadTrack(i)
        timestamp = dead_track_data.Timestamp()
        timestamps.append(convert_unixtime_to_datetime(timestamp))

    return timestamps
