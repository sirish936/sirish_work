# req_uri_new = "/redfish/v1/Systems/1/Storage/DE040000"
# storage_id = req_uri_new.split("/")[6].split("?")[0]
# print(storage_id)

req_uri = "/redfish/v1/Systems/1/Storage/DE040000/Drives/1"
storage_id = req_uri.split("/")[6]
drive_id = req_uri.split("/")[8]
print(storage_id)
print(drive_id)

SYSTEM_STORAGE_DE040000 = "/redfish/v1/Systems/1/Storage/DE040000/"
SYSTEM_STORAGE_DE040000_VOLUME = SYSTEM_STORAGE_DE040000 + "Volumes"
SYSTEM_STORAGE_DE040000_VOLUME_1 = SYSTEM_STORAGE_DE040000_VOLUME + "/1"

req_uri = SYSTEM_STORAGE_DE040000_VOLUME

if req_uri in (
    
    SYSTEM_STORAGE_DE040000_VOLUME_1
):
    print("Hello")

a = None,
b = True
if a and b is True:
    print("WORKING")