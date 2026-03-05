import datetime
server_dto = {'id': '119439-M64+8899119439364561',  'selfUri': '/api/compute/v1/servers/119439-M64+8899119439364561', 'resourceUri': '/api/compute/v1/servers/119439-M64+8899119439364561', 'displayName': '8899119439364561', 'name': '8899119439364561', 'createdAt': datetime.datetime(2023, 8, 5, 15, 27, 5, 40547, tzinfo=datetime.timezone.utc), 'modifiedAt': datetime.datetime(2023, 8, 9, 11, 36, 16, 273312, tzinfo=datetime.timezone.utc), 'updatedAt': datetime.datetime(2023, 8, 9, 11, 36, 16, 273312, tzinfo=datetime.timezone.utc), 'generation': 16,  'oneview': {'applianceUri': None, 'maintenanceMode': True, 'name': None, 'state': None, 'license': None, 'platform': None, 'formFactor': None}}

print(server_dto.get("oneview"))
print(server_dto.get("oneview", None))
oneview = server_dto.get("oneview", None)
print(oneview.get("applianceUri"))

if oneview.get("applianceUri"):
    print("SIRISH")
else:
    print("N V A SIRISH")