from coreir.base import CoreIRType
from coreir.lib import libcoreir_c


class MetaData(CoreIRType):
    def add_metadata(self, key, value):
        libcoreir_c.COREWireableAddMetaDataStr(self.ptr, str.encode(key),
                                               str.encode(value))
