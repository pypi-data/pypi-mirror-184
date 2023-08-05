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
lib.set_library_names("spoolss.dll")
prototypes = \
    {
        #
        'GetJobAttributes': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"dmDeviceName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 32), "dmSpecVersion": SimTypeShort(signed=False, label="UInt16"), "dmDriverVersion": SimTypeShort(signed=False, label="UInt16"), "dmSize": SimTypeShort(signed=False, label="UInt16"), "dmDriverExtra": SimTypeShort(signed=False, label="UInt16"), "dmFields": SimTypeInt(signed=False, label="UInt32"), "Anonymous1": SimUnion({"Anonymous1": SimStruct({"dmOrientation": SimTypeShort(signed=True, label="Int16"), "dmPaperSize": SimTypeShort(signed=True, label="Int16"), "dmPaperLength": SimTypeShort(signed=True, label="Int16"), "dmPaperWidth": SimTypeShort(signed=True, label="Int16"), "dmScale": SimTypeShort(signed=True, label="Int16"), "dmCopies": SimTypeShort(signed=True, label="Int16"), "dmDefaultSource": SimTypeShort(signed=True, label="Int16"), "dmPrintQuality": SimTypeShort(signed=True, label="Int16")}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimStruct({"dmPosition": SimStruct({"x": SimTypeInt(signed=True, label="Int32"), "y": SimTypeInt(signed=True, label="Int32")}, name="POINTL", pack=False, align=None), "dmDisplayOrientation": SimTypeInt(signed=False, label="UInt32"), "dmDisplayFixedOutput": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous2_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), "dmColor": SimTypeShort(signed=True, label="Int16"), "dmDuplex": SimTypeShort(signed=True, label="Int16"), "dmYResolution": SimTypeShort(signed=True, label="Int16"), "dmTTOption": SimTypeShort(signed=True, label="Int16"), "dmCollate": SimTypeShort(signed=True, label="Int16"), "dmFormName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 32), "dmLogPixels": SimTypeShort(signed=False, label="UInt16"), "dmBitsPerPel": SimTypeInt(signed=False, label="UInt32"), "dmPelsWidth": SimTypeInt(signed=False, label="UInt32"), "dmPelsHeight": SimTypeInt(signed=False, label="UInt32"), "Anonymous2": SimUnion({"dmDisplayFlags": SimTypeInt(signed=False, label="UInt32"), "dmNup": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None"), "dmDisplayFrequency": SimTypeInt(signed=False, label="UInt32"), "dmICMMethod": SimTypeInt(signed=False, label="UInt32"), "dmICMIntent": SimTypeInt(signed=False, label="UInt32"), "dmMediaType": SimTypeInt(signed=False, label="UInt32"), "dmDitherType": SimTypeInt(signed=False, label="UInt32"), "dmReserved1": SimTypeInt(signed=False, label="UInt32"), "dmReserved2": SimTypeInt(signed=False, label="UInt32"), "dmPanningWidth": SimTypeInt(signed=False, label="UInt32"), "dmPanningHeight": SimTypeInt(signed=False, label="UInt32")}, name="DEVMODEW", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"dwJobNumberOfPagesPerSide": SimTypeInt(signed=False, label="UInt32"), "dwDrvNumberOfPagesPerSide": SimTypeInt(signed=False, label="UInt32"), "dwNupBorderFlags": SimTypeInt(signed=False, label="UInt32"), "dwJobPageOrderFlags": SimTypeInt(signed=False, label="UInt32"), "dwDrvPageOrderFlags": SimTypeInt(signed=False, label="UInt32"), "dwJobNumberOfCopies": SimTypeInt(signed=False, label="UInt32"), "dwDrvNumberOfCopies": SimTypeInt(signed=False, label="UInt32"), "dwColorOptimization": SimTypeInt(signed=False, label="UInt32"), "dmPrintQuality": SimTypeShort(signed=True, label="Int16"), "dmYResolution": SimTypeShort(signed=True, label="Int16")}, name="ATTRIBUTE_INFO_3", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pPrinterName", "pDevmode", "pAttributeInfo"]),
        #
        'GetJobAttributesEx': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"dmDeviceName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 32), "dmSpecVersion": SimTypeShort(signed=False, label="UInt16"), "dmDriverVersion": SimTypeShort(signed=False, label="UInt16"), "dmSize": SimTypeShort(signed=False, label="UInt16"), "dmDriverExtra": SimTypeShort(signed=False, label="UInt16"), "dmFields": SimTypeInt(signed=False, label="UInt32"), "Anonymous1": SimUnion({"Anonymous1": SimStruct({"dmOrientation": SimTypeShort(signed=True, label="Int16"), "dmPaperSize": SimTypeShort(signed=True, label="Int16"), "dmPaperLength": SimTypeShort(signed=True, label="Int16"), "dmPaperWidth": SimTypeShort(signed=True, label="Int16"), "dmScale": SimTypeShort(signed=True, label="Int16"), "dmCopies": SimTypeShort(signed=True, label="Int16"), "dmDefaultSource": SimTypeShort(signed=True, label="Int16"), "dmPrintQuality": SimTypeShort(signed=True, label="Int16")}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimStruct({"dmPosition": SimStruct({"x": SimTypeInt(signed=True, label="Int32"), "y": SimTypeInt(signed=True, label="Int32")}, name="POINTL", pack=False, align=None), "dmDisplayOrientation": SimTypeInt(signed=False, label="UInt32"), "dmDisplayFixedOutput": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous2_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), "dmColor": SimTypeShort(signed=True, label="Int16"), "dmDuplex": SimTypeShort(signed=True, label="Int16"), "dmYResolution": SimTypeShort(signed=True, label="Int16"), "dmTTOption": SimTypeShort(signed=True, label="Int16"), "dmCollate": SimTypeShort(signed=True, label="Int16"), "dmFormName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 32), "dmLogPixels": SimTypeShort(signed=False, label="UInt16"), "dmBitsPerPel": SimTypeInt(signed=False, label="UInt32"), "dmPelsWidth": SimTypeInt(signed=False, label="UInt32"), "dmPelsHeight": SimTypeInt(signed=False, label="UInt32"), "Anonymous2": SimUnion({"dmDisplayFlags": SimTypeInt(signed=False, label="UInt32"), "dmNup": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None"), "dmDisplayFrequency": SimTypeInt(signed=False, label="UInt32"), "dmICMMethod": SimTypeInt(signed=False, label="UInt32"), "dmICMIntent": SimTypeInt(signed=False, label="UInt32"), "dmMediaType": SimTypeInt(signed=False, label="UInt32"), "dmDitherType": SimTypeInt(signed=False, label="UInt32"), "dmReserved1": SimTypeInt(signed=False, label="UInt32"), "dmReserved2": SimTypeInt(signed=False, label="UInt32"), "dmPanningWidth": SimTypeInt(signed=False, label="UInt32"), "dmPanningHeight": SimTypeInt(signed=False, label="UInt32")}, name="DEVMODEW", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pPrinterName", "pDevmode", "dwLevel", "pAttributeInfo", "nSize", "dwFlags"]),
        #
        'RevertToPrinterSelf': SimTypeFunction([], SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)),
        #
        'ImpersonatePrinterClient': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hToken"]),
        #
        'ReplyPrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "fdwChangeFlags", "pdwResult", "pPrinterNotifyInfo"]),
        #
        'ReplyPrinterChangeNotificationEx': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hNotify", "dwColor", "fdwFlags", "pdwResult", "pPrinterNotifyInfo"]),
        #
        'PartialReplyPrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Field": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeInt(signed=False, label="UInt32"), "Id": SimTypeInt(signed=False, label="UInt32"), "NotifyData": SimUnion({"adwData": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 2), "Data": SimStruct({"cbBuf": SimTypeInt(signed=False, label="UInt32"), "pBuf": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="_Data_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="PRINTER_NOTIFY_INFO_DATA", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "pDataSrc"]),
        #
        'RouterAllocPrinterNotifyInfo': SimTypeFunction([SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "aData": SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Field": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeInt(signed=False, label="UInt32"), "Id": SimTypeInt(signed=False, label="UInt32"), "NotifyData": SimUnion({"adwData": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 2), "Data": SimStruct({"cbBuf": SimTypeInt(signed=False, label="UInt32"), "pBuf": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="_Data_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="PRINTER_NOTIFY_INFO_DATA", pack=False, align=None), offset=0)}, name="PRINTER_NOTIFY_INFO", pack=False, align=None), offset=0), arg_names=["cPrinterNotifyInfoData"]),
        #
        'RouterFreePrinterNotifyInfo': SimTypeFunction([SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "aData": SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Field": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeInt(signed=False, label="UInt32"), "Id": SimTypeInt(signed=False, label="UInt32"), "NotifyData": SimUnion({"adwData": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 2), "Data": SimStruct({"cbBuf": SimTypeInt(signed=False, label="UInt32"), "pBuf": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="_Data_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="PRINTER_NOTIFY_INFO_DATA", pack=False, align=None), offset=0)}, name="PRINTER_NOTIFY_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pInfo"]),
        #
        'RouterAllocBidiResponseContainer': SimTypeFunction([SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "aData": SimTypePointer(SimStruct({"dwResult": SimTypeInt(signed=False, label="UInt32"), "dwReqNumber": SimTypeInt(signed=False, label="UInt32"), "pSchema": SimTypePointer(SimTypeChar(label="Char"), offset=0), "data": SimStruct({"dwBidiType": SimTypeInt(signed=False, label="UInt32"), "u": SimUnion({"bData": SimTypeInt(signed=True, label="Int32"), "iData": SimTypeInt(signed=True, label="Int32"), "sData": SimTypePointer(SimTypeChar(label="Char"), offset=0), "fData": SimTypeFloat(size=32), "biData": SimStruct({"cbBuf": SimTypeInt(signed=False, label="UInt32"), "pData": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="BINARY_CONTAINER", pack=False, align=None)}, name="<anon>", label="None")}, name="BIDI_DATA", pack=False, align=None)}, name="BIDI_RESPONSE_DATA", pack=False, align=None), offset=0)}, name="BIDI_RESPONSE_CONTAINER", pack=False, align=None), offset=0), arg_names=["Count"]),
        #
        'RouterAllocBidiMem': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["NumBytes"]),
        #
        'RouterFreeBidiMem': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pMemPointer"]),
        #
        'AppendPrinterNotifyInfoData': SimTypeFunction([SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "aData": SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Field": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeInt(signed=False, label="UInt32"), "Id": SimTypeInt(signed=False, label="UInt32"), "NotifyData": SimUnion({"adwData": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 2), "Data": SimStruct({"cbBuf": SimTypeInt(signed=False, label="UInt32"), "pBuf": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="_Data_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="PRINTER_NOTIFY_INFO_DATA", pack=False, align=None), offset=0)}, name="PRINTER_NOTIFY_INFO", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Field": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeInt(signed=False, label="UInt32"), "Id": SimTypeInt(signed=False, label="UInt32"), "NotifyData": SimUnion({"adwData": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 2), "Data": SimStruct({"cbBuf": SimTypeInt(signed=False, label="UInt32"), "pBuf": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="_Data_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="PRINTER_NOTIFY_INFO_DATA", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pInfoDest", "pDataSrc", "fdwFlags"]),
        #
        'CallRouterFindFirstPrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "pTypes": SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Reserved0": SimTypeShort(signed=False, label="UInt16"), "Reserved1": SimTypeInt(signed=False, label="UInt32"), "Reserved2": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)}, name="PRINTER_NOTIFY_OPTIONS_TYPE", pack=False, align=None), offset=0)}, name="PRINTER_NOTIFY_OPTIONS", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hPrinterRPC", "fdwFilterFlags", "fdwOptions", "hNotify", "pPrinterNotifyOptions"]),
        #
        'ProvidorFindFirstPrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "fdwFlags", "fdwOptions", "hNotify", "pPrinterNotifyOptions", "pvReserved1"]),
        #
        'ProvidorFindClosePrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter"]),
        #
        'SpoolerFindFirstPrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "fdwFilterFlags", "fdwOptions", "pPrinterNotifyOptions", "pvReserved", "pNotificationConfig", "phNotify", "phEvent"]),
        #
        'SpoolerFindNextPrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "pfdwChange", "pPrinterNotifyOptions", "ppPrinterNotifyInfo"]),
        #
        'SpoolerRefreshPrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "pTypes": SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Reserved0": SimTypeShort(signed=False, label="UInt16"), "Reserved1": SimTypeInt(signed=False, label="UInt32"), "Reserved2": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "pFields": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)}, name="PRINTER_NOTIFY_OPTIONS_TYPE", pack=False, align=None), offset=0)}, name="PRINTER_NOTIFY_OPTIONS", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "aData": SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Field": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeInt(signed=False, label="UInt32"), "Id": SimTypeInt(signed=False, label="UInt32"), "NotifyData": SimUnion({"adwData": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 2), "Data": SimStruct({"cbBuf": SimTypeInt(signed=False, label="UInt32"), "pBuf": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="_Data_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="PRINTER_NOTIFY_INFO_DATA", pack=False, align=None), offset=0)}, name="PRINTER_NOTIFY_INFO", pack=False, align=None), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "dwColor", "pOptions", "ppInfo"]),
        #
        'SpoolerFreePrinterNotifyInfo': SimTypeFunction([SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeInt(signed=False, label="UInt32"), "aData": SimTypePointer(SimStruct({"Type": SimTypeShort(signed=False, label="UInt16"), "Field": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeInt(signed=False, label="UInt32"), "Id": SimTypeInt(signed=False, label="UInt32"), "NotifyData": SimUnion({"adwData": SimTypeFixedSizeArray(SimTypeInt(signed=False, label="UInt32"), 2), "Data": SimStruct({"cbBuf": SimTypeInt(signed=False, label="UInt32"), "pBuf": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="_Data_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="PRINTER_NOTIFY_INFO_DATA", pack=False, align=None), offset=0)}, name="PRINTER_NOTIFY_INFO", pack=False, align=None), offset=0)], SimTypeBottom(label="Void"), arg_names=["pInfo"]),
        #
        'SpoolerFindClosePrinterChangeNotification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter"]),
        #
        'SplPromptUIInUsersSession': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"UIType": SimTypeInt(signed=False, label="UI_TYPE"), "MessageBoxParams": SimStruct({"cbSize": SimTypeInt(signed=False, label="UInt32"), "pTitle": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pMessage": SimTypePointer(SimTypeChar(label="Char"), offset=0), "Style": SimTypeInt(signed=False, label="UInt32"), "dwTimeout": SimTypeInt(signed=False, label="UInt32"), "bWait": SimTypeInt(signed=True, label="Int32")}, name="MESSAGEBOX_PARAMS", pack=False, align=None)}, name="SHOWUIPARAMS", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "JobId", "pUIParams", "pResponse"]),
        #
        'SplIsSessionZero': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hPrinter", "JobId", "pIsSessionZero"]),
        #
        'AddPrintDeviceObject': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "phDeviceObject"]),
        #
        'UpdatePrintDeviceObject': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hPrinter", "hDeviceObject"]),
        #
        'RemovePrintDeviceObject': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hDeviceObject"]),
    }

lib.set_prototypes(prototypes)
