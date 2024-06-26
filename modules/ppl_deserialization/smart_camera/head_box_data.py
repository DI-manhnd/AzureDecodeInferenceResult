# automatically generated by the FlatBuffers compiler, do not modify

# namespace: SmartCamera

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class HeadBoxData(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = HeadBoxData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsHeadBoxData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    # HeadBoxData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # HeadBoxData
    def First(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .bounding_box import BoundingBox

            obj = BoundingBox()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # HeadBoxData
    def Last(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .bounding_box import BoundingBox

            obj = BoundingBox()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # HeadBoxData
    def Conf(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .bounding_box import BoundingBox

            obj = BoundingBox()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None


def HeadBoxDataStart(builder):
    builder.StartObject(3)


def Start(builder):
    return HeadBoxDataStart(builder)


def HeadBoxDataAddFirst(builder, first):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(first), 0
    )


def AddFirst(builder, first):
    return HeadBoxDataAddFirst(builder, first)


def HeadBoxDataAddLast(builder, last):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(last), 0
    )


def AddLast(builder, last):
    return HeadBoxDataAddLast(builder, last)


def HeadBoxDataAddConf(builder, conf):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(conf), 0
    )


def AddConf(builder, conf):
    return HeadBoxDataAddConf(builder, conf)


def HeadBoxDataEnd(builder):
    return builder.EndObject()


def End(builder):
    return HeadBoxDataEnd(builder)
