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
lib.set_library_names("virtdisk.dll")
prototypes = \
    {
        #
        'OpenVirtualDisk': SimTypeFunction([SimTypePointer(SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="VIRTUAL_DISK_ACCESS_MASK"), SimTypeInt(signed=False, label="OPEN_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="OPEN_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"RWDepth": SimTypeInt(signed=False, label="UInt32")}, name="_Version1_e__Struct", pack=False, align=None), "Version2": SimStruct({"GetInfoOnly": SimTypeInt(signed=True, label="Int32"), "ReadOnly": SimTypeInt(signed=True, label="Int32"), "ResiliencyGuid": SimTypeBottom(label="Guid")}, name="_Version2_e__Struct", pack=False, align=None), "Version3": SimStruct({"GetInfoOnly": SimTypeInt(signed=True, label="Int32"), "ReadOnly": SimTypeInt(signed=True, label="Int32"), "ResiliencyGuid": SimTypeBottom(label="Guid"), "SnapshotId": SimTypeBottom(label="Guid")}, name="_Version3_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="OPEN_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualStorageType", "Path", "VirtualDiskAccessMask", "Flags", "Parameters", "Handle"]),
        #
        'CreateVirtualDisk': SimTypeFunction([SimTypePointer(SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="VIRTUAL_DISK_ACCESS_MASK"), SimTypePointer(SimStruct({"Revision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "Control": SimTypeShort(signed=False, label="UInt16"), "Owner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Group": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Sacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0), "Dacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0)}, name="SECURITY_DESCRIPTOR", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="CREATE_VIRTUAL_DISK_FLAG"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="CREATE_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"UniqueId": SimTypeBottom(label="Guid"), "MaximumSize": SimTypeLongLong(signed=False, label="UInt64"), "BlockSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "SectorSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "ParentPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "SourcePath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_Version1_e__Struct", pack=False, align=None), "Version2": SimStruct({"UniqueId": SimTypeBottom(label="Guid"), "MaximumSize": SimTypeLongLong(signed=False, label="UInt64"), "BlockSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "SectorSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "PhysicalSectorSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "ParentPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "SourcePath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "OpenFlags": SimTypeInt(signed=False, label="OPEN_VIRTUAL_DISK_FLAG"), "ParentVirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "SourceVirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "ResiliencyGuid": SimTypeBottom(label="Guid")}, name="_Version2_e__Struct", pack=False, align=None), "Version3": SimStruct({"UniqueId": SimTypeBottom(label="Guid"), "MaximumSize": SimTypeLongLong(signed=False, label="UInt64"), "BlockSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "SectorSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "PhysicalSectorSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "ParentPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "SourcePath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "OpenFlags": SimTypeInt(signed=False, label="OPEN_VIRTUAL_DISK_FLAG"), "ParentVirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "SourceVirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "ResiliencyGuid": SimTypeBottom(label="Guid"), "SourceLimitPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "BackingStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None)}, name="_Version3_e__Struct", pack=False, align=None), "Version4": SimStruct({"UniqueId": SimTypeBottom(label="Guid"), "MaximumSize": SimTypeLongLong(signed=False, label="UInt64"), "BlockSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "SectorSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "PhysicalSectorSizeInBytes": SimTypeInt(signed=False, label="UInt32"), "ParentPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "SourcePath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "OpenFlags": SimTypeInt(signed=False, label="OPEN_VIRTUAL_DISK_FLAG"), "ParentVirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "SourceVirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "ResiliencyGuid": SimTypeBottom(label="Guid"), "SourceLimitPath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "BackingStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "PmemAddressAbstractionType": SimTypeBottom(label="Guid"), "DataAlignment": SimTypeLongLong(signed=False, label="UInt64")}, name="_Version4_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="CREATE_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualStorageType", "Path", "VirtualDiskAccessMask", "SecurityDescriptor", "Flags", "ProviderSpecificFlags", "Parameters", "Overlapped", "Handle"]),
        #
        'AttachVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Revision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "Control": SimTypeShort(signed=False, label="UInt16"), "Owner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Group": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Sacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0), "Dacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0)}, name="SECURITY_DESCRIPTOR", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="ATTACH_VIRTUAL_DISK_FLAG"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="ATTACH_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"Reserved": SimTypeInt(signed=False, label="UInt32")}, name="_Version1_e__Struct", pack=False, align=None), "Version2": SimStruct({"RestrictedOffset": SimTypeLongLong(signed=False, label="UInt64"), "RestrictedLength": SimTypeLongLong(signed=False, label="UInt64")}, name="_Version2_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="ATTACH_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "SecurityDescriptor", "Flags", "ProviderSpecificFlags", "Parameters", "Overlapped"]),
        #
        'DetachVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="DETACH_VIRTUAL_DISK_FLAG"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Flags", "ProviderSpecificFlags"]),
        #
        'GetVirtualDiskPhysicalPath': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "DiskPathSizeInBytes", "DiskPath"]),
        #
        'GetAllAttachedVirtualDiskPhysicalPaths': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["PathsBufferSizeInBytes", "PathsBuffer"]),
        #
        'GetStorageDependencyInformation': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="GET_STORAGE_DEPENDENCY_FLAG"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="STORAGE_DEPENDENCY_INFO_VERSION"), "NumberEntries": SimTypeInt(signed=False, label="UInt32"), "Anonymous": SimUnion({"Version1Entries": SimTypePointer(SimStruct({"DependencyTypeFlags": SimTypeInt(signed=False, label="DEPENDENT_DISK_FLAG"), "ProviderSpecificFlags": SimTypeInt(signed=False, label="UInt32"), "VirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None)}, name="STORAGE_DEPENDENCY_INFO_TYPE_1", pack=False, align=None), offset=0), "Version2Entries": SimTypePointer(SimStruct({"DependencyTypeFlags": SimTypeInt(signed=False, label="DEPENDENT_DISK_FLAG"), "ProviderSpecificFlags": SimTypeInt(signed=False, label="UInt32"), "VirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "AncestorLevel": SimTypeInt(signed=False, label="UInt32"), "DependencyDeviceName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "HostVolumeName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "DependentVolumeName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "DependentVolumeRelativePath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="STORAGE_DEPENDENCY_INFO_TYPE_2", pack=False, align=None), offset=0)}, name="<anon>", label="None")}, name="STORAGE_DEPENDENCY_INFO", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["ObjectHandle", "Flags", "StorageDependencyInfoSize", "StorageDependencyInfo", "SizeUsed"]),
        #
        'GetVirtualDiskInformation': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="GET_VIRTUAL_DISK_INFO_VERSION"), "Anonymous": SimUnion({"Size": SimStruct({"VirtualSize": SimTypeLongLong(signed=False, label="UInt64"), "PhysicalSize": SimTypeLongLong(signed=False, label="UInt64"), "BlockSize": SimTypeInt(signed=False, label="UInt32"), "SectorSize": SimTypeInt(signed=False, label="UInt32")}, name="_Size_e__Struct", pack=False, align=None), "Identifier": SimTypeBottom(label="Guid"), "ParentLocation": SimStruct({"ParentResolved": SimTypeInt(signed=True, label="Int32"), "ParentLocationBuffer": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_ParentLocation_e__Struct", pack=False, align=None), "ParentIdentifier": SimTypeBottom(label="Guid"), "ParentTimestamp": SimTypeInt(signed=False, label="UInt32"), "VirtualStorageType": SimStruct({"DeviceId": SimTypeInt(signed=False, label="UInt32"), "VendorId": SimTypeBottom(label="Guid")}, name="VIRTUAL_STORAGE_TYPE", pack=False, align=None), "ProviderSubtype": SimTypeInt(signed=False, label="UInt32"), "Is4kAligned": SimTypeInt(signed=True, label="Int32"), "IsLoaded": SimTypeInt(signed=True, label="Int32"), "PhysicalDisk": SimStruct({"LogicalSectorSize": SimTypeInt(signed=False, label="UInt32"), "PhysicalSectorSize": SimTypeInt(signed=False, label="UInt32"), "IsRemote": SimTypeInt(signed=True, label="Int32")}, name="_PhysicalDisk_e__Struct", pack=False, align=None), "VhdPhysicalSectorSize": SimTypeInt(signed=False, label="UInt32"), "SmallestSafeVirtualSize": SimTypeLongLong(signed=False, label="UInt64"), "FragmentationPercentage": SimTypeInt(signed=False, label="UInt32"), "VirtualDiskId": SimTypeBottom(label="Guid"), "ChangeTrackingState": SimStruct({"Enabled": SimTypeInt(signed=True, label="Int32"), "NewerChanges": SimTypeInt(signed=True, label="Int32"), "MostRecentId": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_ChangeTrackingState_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="GET_VIRTUAL_DISK_INFO", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "VirtualDiskInfoSize", "VirtualDiskInfo", "SizeUsed"]),
        #
        'SetVirtualDiskInformation': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="SET_VIRTUAL_DISK_INFO_VERSION"), "Anonymous": SimUnion({"ParentFilePath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "UniqueIdentifier": SimTypeBottom(label="Guid"), "ParentPathWithDepthInfo": SimStruct({"ChildDepth": SimTypeInt(signed=False, label="UInt32"), "ParentFilePath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_ParentPathWithDepthInfo_e__Struct", pack=False, align=None), "VhdPhysicalSectorSize": SimTypeInt(signed=False, label="UInt32"), "VirtualDiskId": SimTypeBottom(label="Guid"), "ChangeTrackingEnabled": SimTypeInt(signed=True, label="Int32"), "ParentLocator": SimStruct({"LinkageId": SimTypeBottom(label="Guid"), "ParentFilePath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_ParentLocator_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="SET_VIRTUAL_DISK_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "VirtualDiskInfo"]),
        #
        'EnumerateVirtualDiskMetadata': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), label="LPArray", offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "NumberOfItems", "Items"]),
        #
        'GetVirtualDiskMetadata': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Item", "MetaDataSize", "MetaData"]),
        #
        'SetVirtualDiskMetadata': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Item", "MetaDataSize", "MetaData"]),
        #
        'DeleteVirtualDiskMetadata': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Item"]),
        #
        'GetVirtualDiskOperationProgress': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"OperationStatus": SimTypeInt(signed=False, label="UInt32"), "CurrentValue": SimTypeLongLong(signed=False, label="UInt64"), "CompletionValue": SimTypeLongLong(signed=False, label="UInt64")}, name="VIRTUAL_DISK_PROGRESS", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Overlapped", "Progress"]),
        #
        'CompactVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="COMPACT_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="COMPACT_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"Reserved": SimTypeInt(signed=False, label="UInt32")}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="COMPACT_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"]),
        #
        'MergeVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="MERGE_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="MERGE_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"MergeDepth": SimTypeInt(signed=False, label="UInt32")}, name="_Version1_e__Struct", pack=False, align=None), "Version2": SimStruct({"MergeSourceDepth": SimTypeInt(signed=False, label="UInt32"), "MergeTargetDepth": SimTypeInt(signed=False, label="UInt32")}, name="_Version2_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="MERGE_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"]),
        #
        'ExpandVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="EXPAND_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="EXPAND_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"NewSize": SimTypeLongLong(signed=False, label="UInt64")}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="EXPAND_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"]),
        #
        'ResizeVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="RESIZE_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="RESIZE_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"NewSize": SimTypeLongLong(signed=False, label="UInt64")}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="RESIZE_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"]),
        #
        'MirrorVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="MIRROR_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="MIRROR_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"MirrorVirtualDiskPath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="MIRROR_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"]),
        #
        'BreakMirrorVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle"]),
        #
        'AddVirtualDiskParent': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "ParentPath"]),
        #
        'QueryChangesVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64"), SimTypeInt(signed=False, label="QUERY_CHANGES_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"ByteOffset": SimTypeLongLong(signed=False, label="UInt64"), "ByteLength": SimTypeLongLong(signed=False, label="UInt64"), "Reserved": SimTypeLongLong(signed=False, label="UInt64")}, name="QUERY_CHANGES_VIRTUAL_DISK_RANGE", pack=False, align=None), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "ChangeTrackingId", "ByteOffset", "ByteLength", "Flags", "Ranges", "RangeCount", "ProcessedLength"]),
        #
        'TakeSnapshotVhdSet': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="TAKE_SNAPSHOT_VHDSET_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"SnapshotId": SimTypeBottom(label="Guid")}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="TAKE_SNAPSHOT_VHDSET_PARAMETERS", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="TAKE_SNAPSHOT_VHDSET_FLAG")], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Parameters", "Flags"]),
        #
        'DeleteSnapshotVhdSet': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="DELETE_SNAPSHOT_VHDSET_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"SnapshotId": SimTypeBottom(label="Guid")}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="DELETE_SNAPSHOT_VHDSET_PARAMETERS", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="DELETE_SNAPSHOT_VHDSET_FLAG")], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Parameters", "Flags"]),
        #
        'ModifyVhdSet': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="MODIFY_VHDSET_VERSION"), "Anonymous": SimUnion({"SnapshotPath": SimStruct({"SnapshotId": SimTypeBottom(label="Guid"), "SnapshotFilePath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_SnapshotPath_e__Struct", pack=False, align=None), "SnapshotId": SimTypeBottom(label="Guid"), "DefaultFilePath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="<anon>", label="None")}, name="MODIFY_VHDSET_PARAMETERS", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="MODIFY_VHDSET_FLAG")], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Parameters", "Flags"]),
        #
        'ApplySnapshotVhdSet': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="APPLY_SNAPSHOT_VHDSET_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"SnapshotId": SimTypeBottom(label="Guid"), "LeafSnapshotId": SimTypeBottom(label="Guid")}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="APPLY_SNAPSHOT_VHDSET_PARAMETERS", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="APPLY_SNAPSHOT_VHDSET_FLAG")], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Parameters", "Flags"]),
        #
        'RawSCSIVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="RAW_SCSI_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"RSVDHandle": SimTypeInt(signed=True, label="Int32"), "DataIn": SimTypeChar(label="Byte"), "CdbLength": SimTypeChar(label="Byte"), "SenseInfoLength": SimTypeChar(label="Byte"), "SrbFlags": SimTypeInt(signed=False, label="UInt32"), "DataTransferLength": SimTypeInt(signed=False, label="UInt32"), "DataBuffer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "SenseInfo": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "Cdb": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="RAW_SCSI_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="RAW_SCSI_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="RAW_SCSI_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"ScsiStatus": SimTypeChar(label="Byte"), "SenseInfoLength": SimTypeChar(label="Byte"), "DataTransferLength": SimTypeInt(signed=False, label="UInt32")}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="RAW_SCSI_VIRTUAL_DISK_RESPONSE", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Parameters", "Flags", "Response"]),
        #
        'ForkVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="FORK_VIRTUAL_DISK_FLAG"), SimTypePointer(SimStruct({"Version": SimTypeInt(signed=False, label="FORK_VIRTUAL_DISK_VERSION"), "Anonymous": SimUnion({"Version1": SimStruct({"ForkedVirtualDiskPath": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="_Version1_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="FORK_VIRTUAL_DISK_PARAMETERS", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"Internal": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "InternalHigh": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Anonymous": SimUnion({"Anonymous": SimStruct({"Offset": SimTypeInt(signed=False, label="UInt32"), "OffsetHigh": SimTypeInt(signed=False, label="UInt32")}, name="_Anonymous_e__Struct", pack=False, align=None), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="<anon>", label="None"), "hEvent": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="OVERLAPPED", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"]),
        #
        'CompleteForkVirtualDisk': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["VirtualDiskHandle"]),
    }

lib.set_prototypes(prototypes)
