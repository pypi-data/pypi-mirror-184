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
lib.set_library_names("snmpapi.dll")
prototypes = \
    {
        #
        'SnmpUtilOidCpy': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pOidDst", "pOidSrc"]),
        #
        'SnmpUtilOidAppend': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pOidDst", "pOidSrc"]),
        #
        'SnmpUtilOidNCmp': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pOid1", "pOid2", "nSubIds"]),
        #
        'SnmpUtilOidCmp': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pOid1", "pOid2"]),
        #
        'SnmpUtilOidFree': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pOid"]),
        #
        'SnmpUtilOctetsCmp': SimTypeFunction([SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pOctets1", "pOctets2"]),
        #
        'SnmpUtilOctetsNCmp': SimTypeFunction([SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pOctets1", "pOctets2", "nChars"]),
        #
        'SnmpUtilOctetsCpy': SimTypeFunction([SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pOctetsDst", "pOctetsSrc"]),
        #
        'SnmpUtilOctetsFree': SimTypeFunction([SimTypePointer(SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pOctets"]),
        #
        'SnmpUtilAsnAnyCpy': SimTypeFunction([SimTypePointer(SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pAnyDst", "pAnySrc"]),
        #
        'SnmpUtilAsnAnyFree': SimTypeFunction([SimTypePointer(SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pAny"]),
        #
        'SnmpUtilVarBindCpy': SimTypeFunction([SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pVbDst", "pVbSrc"]),
        #
        'SnmpUtilVarBindFree': SimTypeFunction([SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pVb"]),
        #
        'SnmpUtilVarBindListCpy': SimTypeFunction([SimTypePointer(SimStruct({"list": SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0), "len": SimTypeInt(signed=False, label="UInt32")}, name="SnmpVarBindList", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"list": SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0), "len": SimTypeInt(signed=False, label="UInt32")}, name="SnmpVarBindList", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pVblDst", "pVblSrc"]),
        #
        'SnmpUtilVarBindListFree': SimTypeFunction([SimTypePointer(SimStruct({"list": SimTypePointer(SimStruct({"name": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "value": SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None)}, name="SnmpVarBind", pack=False, align=None), offset=0), "len": SimTypeInt(signed=False, label="UInt32")}, name="SnmpVarBindList", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pVbl"]),
        #
        'SnmpUtilMemFree': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pMem"]),
        #
        'SnmpUtilMemAlloc': SimTypeFunction([SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["nBytes"]),
        #
        'SnmpUtilMemReAlloc': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["pMem", "nBytes"]),
        #
        'SnmpUtilOidToA': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0)], SimTypePointer(SimTypeChar(label="Byte"), offset=0), arg_names=["Oid"]),
        #
        'SnmpUtilIdsToA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeChar(label="Byte"), offset=0), arg_names=["Ids", "IdLength"]),
        #
        'SnmpUtilPrintOid': SimTypeFunction([SimTypePointer(SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["Oid"]),
        #
        'SnmpUtilPrintAsnAny': SimTypeFunction([SimTypePointer(SimStruct({"asnType": SimTypeChar(label="Byte"), "asnValue": SimUnion({"number": SimTypeInt(signed=True, label="Int32"), "unsigned32": SimTypeInt(signed=False, label="UInt32"), "counter64": SimTypeBottom(label="ULARGE_INTEGER"), "string": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "bits": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "object": SimStruct({"idLength": SimTypeInt(signed=False, label="UInt32"), "ids": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AsnObjectIdentifier", pack=False, align=None), "sequence": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "address": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None), "counter": SimTypeInt(signed=False, label="UInt32"), "gauge": SimTypeInt(signed=False, label="UInt32"), "ticks": SimTypeInt(signed=False, label="UInt32"), "arbitrary": SimStruct({"stream": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "length": SimTypeInt(signed=False, label="UInt32"), "dynamic": SimTypeInt(signed=True, label="Int32")}, name="AsnOctetString", pack=False, align=None)}, name="<anon>", label="None")}, name="AsnAny", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pAny"]),
        #
        'SnmpSvcGetUptime': SimTypeFunction([], SimTypeInt(signed=False, label="UInt32")),
        #
        'SnmpSvcSetLogLevel': SimTypeFunction([SimTypeInt(signed=False, label="SNMP_LOG")], SimTypeBottom(label="Void"), arg_names=["nLogLevel"]),
        #
        'SnmpSvcSetLogType': SimTypeFunction([SimTypeInt(signed=False, label="SNMP_OUTPUT_LOG_TYPE")], SimTypeBottom(label="Void"), arg_names=["nLogType"]),
        #
        'SnmpUtilDbgPrint': SimTypeFunction([SimTypeInt(signed=False, label="SNMP_LOG"), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeBottom(label="Void"), arg_names=["nLogLevel", "szFormat"]),
    }

lib.set_prototypes(prototypes)
