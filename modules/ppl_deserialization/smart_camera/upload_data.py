# automatically generated by the FlatBuffers compiler, do not modify

# namespace: SmartCamera

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class UploadData(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UploadData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUploadData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    # UploadData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UploadData
    def DeviceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UploadData
    def CustomerId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UploadData
    def StoreId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UploadData
    def ListDeadTrack(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .dead_track_data import DeadTrackData

            obj = DeadTrackData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UploadData
    def ListDeadTrackLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UploadData
    def ListDeadTrackIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0


def UploadDataStart(builder):
    builder.StartObject(4)


def Start(builder):
    return UploadDataStart(builder)


def UploadDataAddDeviceId(builder, deviceId):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(deviceId), 0
    )


def AddDeviceId(builder, deviceId):
    return UploadDataAddDeviceId(builder, deviceId)


def UploadDataAddCustomerId(builder, customerId):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(customerId), 0
    )


def AddCustomerId(builder, customerId):
    return UploadDataAddCustomerId(builder, customerId)


def UploadDataAddStoreId(builder, storeId):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(storeId), 0
    )


def AddStoreId(builder, storeId):
    return UploadDataAddStoreId(builder, storeId)


def UploadDataAddListDeadTrack(builder, listDeadTrack):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(listDeadTrack), 0
    )


def AddListDeadTrack(builder, listDeadTrack):
    return UploadDataAddListDeadTrack(builder, listDeadTrack)


def UploadDataStartListDeadTrackVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def StartListDeadTrackVector(builder, numElems):
    return UploadDataStartListDeadTrackVector(builder, numElems)


def UploadDataEnd(builder):
    return builder.EndObject()


def End(builder):
    return UploadDataEnd(builder)
