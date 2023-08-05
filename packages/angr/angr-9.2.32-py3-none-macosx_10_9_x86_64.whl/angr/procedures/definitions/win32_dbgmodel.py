# pylint:disable=line-too-long
import logging

from ...sim_type import SimTypeFunction,     SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat,     SimTypePointer,     SimTypeChar,     SimStruct,     SimTypeFixedSizeArray,     SimTypeBottom,     SimUnion,     SimTypeBool
from ...calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from .. import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.set_default_cc('X86', SimCCStdcall)
lib.set_default_cc('AMD64', SimCCMicrosoftAMD64)
lib.set_library_names("dbgmodel.dll")
prototypes = \
    {
        #
        'CreateDataModelManager': SimTypeFunction([SimTypeBottom(label="IDebugHost"), SimTypePointer(SimTypeBottom(label="IDataModelManager"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["debugHost", "manager"]),
    }

lib.set_prototypes(prototypes)
