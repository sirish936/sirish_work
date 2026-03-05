storage_inv = {
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DA000005/",
    "@odata.type": "#Storage.v1_12_0.Storage",
    "Id": "DA000005",
    "Controllers": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DA000005#/StorageControllers/0/",
            "FirmwareVersion": None,
            "Location": {"PartLocation": {"ServiceLabel": "System Board"}},
            "Manufacturer": "",
            "MemberId": "0",
            "Model": "Embedded SATA Controller #1",
            "Name": "SATA Storage Controller",
            "PartNumber": "",
            "SerialNumber": "",
            "Status": {"Health": None, "State": None},
            "SupportedDeviceProtocols": ["SATA"],
        }
    ],
    "Drives": [
        None,
        {
            "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
            "@odata.etag": 'W/"67E86D92"',
            "@odata.id": "/redfish/v1/Systems/1/Storage/DA000005/Drives/020BFFCC/",
            "@odata.type": "#Drive.v1_16_0.Drive",
            "Id": "020BFFCC",
            "Actions": {
                "#Drive.Reset": {
                    "ResetValue@Redfish.AllowableValues": [
                        "ForceOff",
                        "ForceOn",
                        "PowerCycle",
                    ],
                    "target": "/redfish/v1/Systems/1/Storage/DA000005/Drives/020BFFCC/Actions/Drive.Reset/",
                }
            },
            "CapacityBytes": 1000204000000,
            "Identifiers": [],
            "Location": [{"Info": "N/A", "InfoFormat": "BayNumber"}],
            "MediaType": "HDD",
            "Model": "MB001000GWWQE",
            "Name": "Secondary Storage Device",
            "Oem": {
                "Hpe": {
                    "@odata.context": "/redfish/v1/$metadata#HpeiLODriveExt.HpeiLODriveExt",
                    "@odata.type": "#HpeiLODriveExt.v2_0_1.HpeiLODriveExt",
                    "DriveStatus": {},
                    "TemperatureStatus": {},
                }
            },
            "Operations": [],
            "PhysicalLocation": {
                "PartLocation": {
                    "LocationOrdinalValue": 0,
                    "LocationType": "Bay",
                    "ServiceLabel": "N/A",
                }
            },
            "Revision": "HPG6",
            "SerialNumber": "WRF0598F",
            "Status": {"Health": "OK"},
        },
        None,
    ],
    "Links": {"Enclosures": [{"@odata.id": "/redfish/v1/Chassis/1/"}]},
    "Name": "SATA Storage System",
    "Status": {"Health": "OK", "State": "Enabled"},
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DA000005#/StorageControllers/0/",
            "FirmwareVersion": None,
            "Location": {"PartLocation": {"ServiceLabel": "System Board"}},
            "Manufacturer": "",
            "MemberId": "0",
            "Model": "Embedded SATA Controller #1",
            "Name": "SATA Storage Controller",
            "PartNumber": "",
            "SerialNumber": "",
            "Status": {"Health": None, "State": None},
            "SupportedDeviceProtocols": ["SATA"],
        }
    ],
    "Annotations": {},
}


drives = []
ODATA_CONTEXT = "@odata.context"
ODATA_ID = "@odata.id"
ODATA_TYPE = "@odata.type"
ID = "Id"
NAME = "Name"
VERSION = "Version"
DEVICE_CONTEXT = "DeviceContext"
OEM = "Oem"
HPE = "Hpe"
CONTROLLERS = "Controllers"
STORAGE_CONTROLLERS = "StorageControllers"
MODEL = "Model"
DESCRIPTION = "Description"
FIRMWARE_VERSION = "FirmwareVersion"
SUPPORTED_RAID_TYPES = "SupportedRAIDTypes"
NOT_APPLICABLE = "N/A"
POWER_DETAIL = "PowerDetail"
SAMPLES = "Samples"
DRIVES = "Drives"
CAPACITY_BYTES = "CapacityBytes"
STATUS = "Status"
HEALTH = "Health"
STATE = "State"
HOT_SPARE_TYPE = "HotspareType"
OPERATIONS = "Operations"
PROTOCOL = "Protocol"
MEDIA_TYPE = "MediaType"
VOLUMES = "Volumes"
DISPLAY_NAME = "DisplayName"
RAID_TYPE = "RAIDType"

for drive in storage_inv[DRIVES]:
    try:
        if drive:
            state = drive.get(STATUS, {}).get(STATE, "Unknown")
            if state == "Absent":
                continue
            drives.append(
                {
                    "id": drive[ID],
                    "uri": drive[ODATA_ID],
                    "capacityBytes": drive[CAPACITY_BYTES],
                    "health": drive[STATUS][HEALTH],
                    "state": state,
                    "hotspareType": drive[HOT_SPARE_TYPE],
                    "operations": drive[OPERATIONS],
                    "protocol": drive[PROTOCOL],
                    "mediaType": drive[MEDIA_TYPE],
                }
            )
    except Exception:
        # try to collect some information regarding attached drives
        drive_uri = drive.get(ODATA_ID, "")
        if drive_uri:
            drive_id = drive_uri.split("/")
            drive_id = drive_id[-2] if len(drive_id) > 1 else drive_id
            drives.append(
                {
                    "id": drive_id,
                    "uri": drive_uri,
                }
            )
        else:
            print(
                "Ignoring exception parsing storage id %s drive %s with inventory %s",
                "storage_id",
                drive,
                storage_inv,
            )
