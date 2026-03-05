import json
raw_inv_resp = {
	"id": "baacb1ea-1eb9-446b-3e73-5acc52278a74",
	"name": "GET_INVENTORY",
	"startTime": "2023/07/26 17:35:14",
	"taskMonitor": "/redfish-adapter/tasks/baacb1ea-1eb9-446b-3e73-5acc52278a74",
	"percentComplete": 100,
	"taskState": "Completed",
	"taskStatus": "Warning",
	"messages": [
		{
			"message": "Starting GET_INVENTORY execution.",
			"messageArgs": [
				"GET_INVENTORY"
			],
			"messageId": "ASYNC_TASK_START",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource Managers inventory successful.",
			"messageArgs": [
				"Managers"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource BiosSpecialSettings inventory successful.",
			"messageArgs": [
				"BiosSpecialSettings"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource mpEthernetInterfaces inventory successful.",
			"messageArgs": [
				"mpEthernetInterfaces"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource License inventory successful.",
			"messageArgs": [
				"License"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource Chassis inventory successful.",
			"messageArgs": [
				"Chassis"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource Systems inventory successful.",
			"messageArgs": [
				"Systems"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource Processor inventory successful.",
			"messageArgs": [
				"Processor"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource remoteSupport inventory successful.",
			"messageArgs": [
				"remoteSupport"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource securityDashboard inventory successful.",
			"messageArgs": [
				"securityDashboard"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource advancedMemoryProtection inventory successful.",
			"messageArgs": [
				"advancedMemoryProtection"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource memory inventory successful.",
			"messageArgs": [
				"memory"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource memoryList inventory successful.",
			"messageArgs": [
				"memoryList"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource devicesV2 inventory successful.",
			"messageArgs": [
				"devicesV2"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource firmware inventory successful.",
			"messageArgs": [
				"firmware"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource devices inventory successful.",
			"messageArgs": [
				"devices"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource localStorage inventory successful.",
			"messageArgs": [
				"localStorage"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource localStorageV2 inventory successful.",
			"messageArgs": [
				"localStorageV2"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource powerSupplies inventory successful.",
			"messageArgs": [
				"powerSupplies"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Resource fans inventory successful.",
			"messageArgs": [
				"fans"
			],
			"messageId": "RESOURCE_INVENTORY_SUCCESSFUL",
			"resolution": "null",
			"severity": "OK"
		},
		{
			"message": "Inventory for the software sub-resource  was not attempted as the precondition AmsDeviceDiscovery is not met. (RAS_016)",
			"messageArgs": [
				"software",
				"AmsDeviceDiscovery"
			],
			"messageId": "SUB_RESOURCE_INVENTORY_UNATTEMPTED_PRECONDITIONS_FAILURE",
			"resolution": "Ensure the server is powered on and that POST has completed successfully. For resources that need AMS, ensure that AMS service is up and running on the Operating system",
			"severity": "Warning"
		},
		{
			"message": "GET_INVENTORY execution complete.",
			"messageArgs": [
				"GET_INVENTORY"
			],
			"messageId": "ASYNC_TASK_END",
			"resolution": "null",
			"severity": "OK"
		}
	],
	"endTime": "2023/07/26 17:36:20",
	"payload": {
		"httpHeaders": {
			"serialNumber": "8899082305627868",
			"productId": "082305-Y27",
			"deviceId": "608a1f3d-656f-4127-a742-57d77e1eb0ee",
			"requestId": "e5029182fc6842638032f28f6d98d131"
		},
		"body": {
			"redfishResources": {
				"Managers": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#Manager.Manager",
							"@odata.etag": "W/\"9B2BFFAA\"",
							"@odata.id": "/redfish/v1/Managers/1",
							"@odata.type": "#Manager.v1_5_1.Manager",
							"Id": "1",
							"Actions": {
								"#Manager.Reset": {
									"ResetType@Redfish.AllowableValues": [
										"ForceRestart",
										"GracefulRestart"
									],
									"target": "/redfish/v1/Managers/1/Actions/Manager.Reset"
								}
							},
							"CommandShell": {
								"ConnectTypesSupported": [
									"SSH",
									"Oem"
								],
								"MaxConcurrentSessions": 9,
								"ServiceEnabled": True
							},
							"DateTime": "2022-11-24T16:18:53Z",
							"DateTimeLocalOffset": "+00:00",
							"EthernetInterfaces": {
								"@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces"
							},
							"FirmwareVersion": "iLO 5 v2.72",
							"GraphicalConsole": {
								"ConnectTypesSupported": [
									"KVMIP"
								],
								"MaxConcurrentSessions": 10,
								"ServiceEnabled": True
							},
							"HostInterfaces": {
								"@odata.id": "/redfish/v1/Managers/1/HostInterfaces"
							},
							"Links": {
								"ManagerInChassis": {
									"@odata.id": "/redfish/v1/Chassis/1"
								},
								"ManagerForServers": [
									{
										"@odata.id": "/redfish/v1/Systems/1"
									}
								],
								"ManagerForChassis": [
									{
										"@odata.id": "/redfish/v1/Chassis/1"
									}
								]
							},
							"LogServices": {
								"@odata.id": "/redfish/v1/Managers/1/LogServices"
							},
							"ManagerType": "BMC",
							"Model": "iLO 5",
							"Name": "Manager",
							"NetworkProtocol": {
								"@odata.id": "/redfish/v1/Managers/1/NetworkProtocol"
							},
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeiLO.HpeiLO",
									"@odata.type": "#HpeiLO.v2_8_1.HpeiLO",
									"Actions": {
										"#HpeiLO.ClearHotKeys": {
											"target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.ClearHotKeys"
										},
										"#HpeiLO.ClearRestApiState": {
											"target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.ClearRestApiState"
										},
										"#HpeiLO.DisableCloudConnect": {
											"target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.DisableCloudConnect"
										},
										"#HpeiLO.DisableiLOFunctionality": {
											"target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.DisableiLOFunctionality"
										},
										"#HpeiLO.EnableCloudConnect": {
											"target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.EnableCloudConnect"
										},
										"#HpeiLO.RequestFirmwareAndOsRecovery": {
											"target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.RequestFirmwareAndOsRecovery"
										},
										"#HpeiLO.ResetToFactoryDefaults": {
											"ResetType@Redfish.AllowableValues": [
												"Default"
											],
											"target": "/redfish/v1/Managers/1/Actions/Oem/Hpe/HpeiLO.ResetToFactoryDefaults"
										}
									},
									"ClearRestApiStatus": "DataPresent",
									"CloudConnect": {
										"ActivationKey": "427275fcddef11ebaeaea25b204e9436",
										"CloudConnectStatus": "Connected"
									},
									"ConfigurationLimitations": "None",
									"ConfigurationSettings": "Current",
									"FederationConfig": {
										"IPv6MulticastScope": "Site",
										"MulticastAnnouncementInterval": 600,
										"MulticastDiscovery": "Enabled",
										"MulticastTimeToLive": 5,
										"iLOFederationManagement": "Enabled"
									},
									"Firmware": {
										"Current": {
											"Date": "Sep 04 2022",
											"DebugBuild": False,
											"MajorVersion": 2,
											"MinorVersion": 72,
											"VersionString": "iLO 5 v2.72"
										}
									},
									"FrontPanelUSB": {
										"State": "Ready"
									},
									"IdleConnectionTimeoutMinutes": 30,
									"IntegratedRemoteConsole": {
										"HotKeys": [
											{
												"KeySequence": [
													"NONE",
													"NONE",
													"NONE",
													"NONE",
													"NONE"
												],
												"Name": "Ctrl-T"
											},
											{
												"KeySequence": [
													"NONE",
													"NONE",
													"NONE",
													"NONE",
													"NONE"
												],
												"Name": "Ctrl-U"
											},
											{
												"KeySequence": [
													"NONE",
													"NONE",
													"NONE",
													"NONE",
													"NONE"
												],
												"Name": "Ctrl-V"
											},
											{
												"KeySequence": [
													"NONE",
													"NONE",
													"NONE",
													"NONE",
													"NONE"
												],
												"Name": "Ctrl-W"
											},
											{
												"KeySequence": [
													"NONE",
													"NONE",
													"NONE",
													"NONE",
													"NONE"
												],
												"Name": "Ctrl-X"
											},
											{
												"KeySequence": [
													"NONE",
													"NONE",
													"NONE",
													"NONE",
													"NONE"
												],
												"Name": "Ctrl-Y"
											}
										],
										"LockKey": {
											"CustomKeySequence": [
												"NONE",
												"NONE",
												"NONE",
												"NONE",
												"NONE"
											],
											"LockOption": "Disabled"
										},
										"TrustedCertificateRequired": False
									},
									"License": {
										"LicenseKey": "XXXXX-XXXXX-XXXXX-XXXXX-GGQYW",
										"LicenseString": "iLO Advanced limited-distribution test",
										"LicenseType": "Internal"
									},
									"Links": {
										"DateTimeService": {
											"@odata.id": "/redfish/v1/Managers/1/DateTime"
										},
										"LicenseService": {
											"@odata.id": "/redfish/v1/Managers/1/LicenseService"
										},
										"EmbeddedMediaService": {
											"@odata.id": "/redfish/v1/Managers/1/EmbeddedMedia"
										},
										"SNMPService": {
											"@odata.id": "/redfish/v1/Managers/1/SnmpService"
										},
										"FederationPeers": {
											"@odata.id": "/redfish/v1/Managers/1/FederationPeers"
										},
										"FederationGroups": {
											"@odata.id": "/redfish/v1/Managers/1/FederationGroups"
										},
										"ActiveHealthSystem": {
											"@odata.id": "/redfish/v1/Managers/1/ActiveHealthSystem"
										},
										"SecurityService": {
											"@odata.id": "/redfish/v1/Managers/1/SecurityService"
										},
										"BackupRestoreService": {
											"@odata.id": "/redfish/v1/Managers/1/BackupRestoreService"
										},
										"RemoteSupport": {
											"@odata.id": "/redfish/v1/Managers/1/RemoteSupportService"
										},
										"GUIService": {
											"@odata.id": "/redfish/v1/Managers/1/GUIService"
										},
										"FederationDispatch": {
											"extref": "/dispatch"
										},
										"VSPLogLocation": {
											"extref": "/sol.log.gz"
										},
										"Thumbnail": {
											"extref": "/images/thumbnail.bmp"
										}
									},
									"PersistentMouseKeyboardEnabled": False,
									"PhysicalMonitorHealthStatusEnabled": True,
									"RIBCLEnabled": True,
									"RemoteConsoleThumbnailEnabled": True,
									"RequireHostAuthentication": False,
									"RequiredLoginForiLORBSU": False,
									"SerialCLISpeed": 9600,
									"SerialCLIStatus": "EnabledAuthReq",
									"SerialCLIUART": "Present",
									"VSPDlLoggingEnabled": False,
									"VSPLogDownloadEnabled": False,
									"VideoPresenceDetectOverride": True,
									"VideoPresenceDetectOverrideSupported": True,
									"VirtualNICEnabled": False,
									"WebGuiEnabled": True,
									"iLOFunctionalityEnabled": True,
									"iLOFunctionalityRequired": False,
									"iLOIPduringPOSTEnabled": True,
									"iLORBSUEnabled": True,
									"iLOSelfTestResults": [
										{
											"Notes": "",
											"SelfTestName": "NVRAMData",
											"Status": "OK"
										},
										{
											"Notes": "Controller firmware revision  2.11.00  ",
											"SelfTestName": "EmbeddedFlash",
											"Status": "OK"
										},
										{
											"Notes": "Device or content issue: status 0x1000 mode ",
											"SelfTestName": "EEPROM",
											"Status": "Degraded"
										},
										{
											"Notes": "",
											"SelfTestName": "HostRom",
											"Status": "OK"
										},
										{
											"Notes": "",
											"SelfTestName": "SupportedHost",
											"Status": "OK"
										},
										{
											"Notes": "Version 1.0.8",
											"SelfTestName": "PowerManagementController",
											"Status": "Informational"
										},
										{
											"Notes": "ProLiant DL380 Gen10 System Programmable Logic Device 0x31",
											"SelfTestName": "CPLDPAL0",
											"Status": "Informational"
										},
										{
											"Notes": "",
											"SelfTestName": "ASICFuses",
											"Status": "OK"
										}
									],
									"iLOServicePort": {
										"MassStorageAuthenticationRequired": False,
										"USBEthernetAdaptersEnabled": True,
										"USBFlashDriveEnabled": True,
										"iLOServicePortEnabled": True
									}
								}
							},
							"SerialConsole": {
								"ConnectTypesSupported": [
									"SSH",
									"IPMI",
									"Oem"
								],
								"MaxConcurrentSessions": 13,
								"ServiceEnabled": True
							},
							"SerialInterfaces": {
								"@odata.id": "/redfish/v1/Managers/1/SerialInterfaces"
							},
							"Status": {
								"Health": "Warning",
								"State": "Enabled"
							},
							"UUID": "202686d6-a444-50c7-9afa-df274e4ebd43",
							"VirtualMedia": {
								"@odata.id": "/redfish/v1/Managers/1/VirtualMedia"
							}
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"BiosSpecialSettings": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#Bios.Bios",
							"@odata.etag": "W/\"56D7D7410668BDBDBDD675F75EB10F77\"",
							"@odata.id": "/redfish/v1/systems/1/bios/oem/hpe/special/settings/",
							"@odata.type": "#Bios.v1_0_4.Bios",
							"AttributeRegistry": "BiosAttributeRegistryA43.v1_2_50",
							"Attributes": {
								"VirtualSerialNum": "",
								"VirtualUUID": ""
							},
							"Id": "settings",
							"Name": "BIOS Pending Settings (Special)"
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"mpEthernetInterfaces": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
							"@odata.etag": "W/\"6E5EF7E6\"",
							"@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/1",
							"@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
							"Id": "1",
							"AutoNeg": True,
							"DHCPv4": {
								"DHCPEnabled": True,
								"UseDNSServers": True,
								"UseDomainName": True,
								"UseGateway": True,
								"UseNTPServers": False,
								"UseStaticRoutes": True
							},
							"DHCPv6": {
								"OperatingMode": "Stateful",
								"UseDNSServers": True,
								"UseDomainName": True,
								"UseNTPServers": False,
								"UseRapidCommit": False
							},
							"Description": "Configuration of this Manager Network Interface",
							"FQDN": "ILOMXQ1450J66.eml.lab",
							"FullDuplex": True,
							"HostName": "ILOMXQ1450J66",
							"IPv4Addresses": [
								{
									"Address": "172.20.3.120",
									"AddressOrigin": "DHCP",
									"Gateway": "172.20.0.1",
									"SubnetMask": "255.255.248.0"
								}
							],
							"IPv4StaticAddresses": [],
							"IPv6AddressPolicyTable": [
								{
									"Label": "null",
									"Precedence": 35,
									"Prefix": "::ffff:0:0/96"
								}
							],
							"IPv6Addresses": [
								{
									"Address": "FE80::B67A:F1FF:FEC2:6AA4",
									"AddressOrigin": "SLAAC",
									"AddressState": "Preferred",
									"PrefixLength": 64
								},
								{
									"Address": "172:20::B67A:F1FF:FEC2:6AA4",
									"AddressOrigin": "SLAAC",
									"AddressState": "Preferred",
									"PrefixLength": 64
								},
								{
									"Address": "172:20::454B:D8D7:D235:CDF1",
									"AddressOrigin": "DHCP",
									"AddressState": "Preferred",
									"PrefixLength": 64
								}
							],
							"IPv6DefaultGateway": "FE80::5E8A:38FF:FEA8:15A4",
							"IPv6StaticAddresses": [
								{
									"Address": "::",
									"PrefixLength": "null"
								},
								{
									"Address": "::",
									"PrefixLength": "null"
								},
								{
									"Address": "::",
									"PrefixLength": "null"
								},
								{
									"Address": "::",
									"PrefixLength": "null"
								}
							],
							"IPv6StaticDefaultGateways": [
								{
									"Address": "::"
								}
							],
							"InterfaceEnabled": True,
							"LinkStatus": "LinkUp",
							"MACAddress": "B4:7A:F1:C2:6A:A4",
							"MaxIPv6StaticAddresses": 4,
							"Name": "Manager Dedicated Network Interface",
							"NameServers": [
								"172.20.0.11"
							],
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeiLOEthernetNetworkInterface.HpeiLOEthernetNetworkInterface",
									"@odata.type": "#HpeiLOEthernetNetworkInterface.v2_2_1.HpeiLOEthernetNetworkInterface",
									"ConfigurationSettings": "Current",
									"DHCPv4": {
										"ClientIdType": "Default",
										"Enabled": True,
										"UseDNSServers": True,
										"UseDomainName": True,
										"UseGateway": True,
										"UseNTPServers": False,
										"UseStaticRoutes": True,
										"UseWINSServers": True
									},
									"DHCPv6": {
										"StatefulModeEnabled": True,
										"StatelessModeEnabled": True,
										"UseDNSServers": True,
										"UseDomainName": True,
										"UseNTPServers": False,
										"UseRapidCommit": False
									},
									"DomainName": "eml.lab",
									"HostName": "ILOMXQ1450J66",
									"IPv4": {
										"DDNSRegistration": True,
										"DNSServers": [
											"172.20.0.11",
											"0.0.0.0",
											"0.0.0.0"
										],
										"StaticRoutes": [
											{
												"Destination": "0.0.0.0",
												"Gateway": "0.0.0.0",
												"SubnetMask": "0.0.0.0"
											},
											{
												"Destination": "0.0.0.0",
												"Gateway": "0.0.0.0",
												"SubnetMask": "0.0.0.0"
											},
											{
												"Destination": "0.0.0.0",
												"Gateway": "0.0.0.0",
												"SubnetMask": "0.0.0.0"
											}
										],
										"WINSRegistration": True,
										"WINSServers": [
											"0.0.0.0",
											"0.0.0.0"
										]
									},
									"IPv6": {
										"DDNSRegistration": True,
										"DNSServers": [
											"::",
											"::",
											"::"
										],
										"SLAACEnabled": True,
										"StaticDefaultGateway": "::",
										"StaticRoutes": [
											{
												"Destination": "::",
												"Gateway": "::",
												"PrefixLength": "null",
												"Status": "Unknown"
											},
											{
												"Destination": "::",
												"Gateway": "::",
												"PrefixLength": "null",
												"Status": "Unknown"
											},
											{
												"Destination": "::",
												"Gateway": "::",
												"PrefixLength": "null",
												"Status": "Unknown"
											}
										]
									},
									"InterfaceType": "Dedicated",
									"NICEnabled": True,
									"NICSupportsIPv6": True,
									"PingGatewayOnStartup": True
								}
							},
							"PermanentMACAddress": "B4:7A:F1:C2:6A:A4",
							"SpeedMbps": 1000,
							"StatelessAddressAutoConfig": {
								"IPv6AutoConfigEnabled": True
							},
							"StaticNameServers": [
								"0.0.0.0",
								"0.0.0.0",
								"0.0.0.0",
								"::",
								"::",
								"::"
							],
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							},
							"VLAN": {
								"VLANEnable": False,
								"VLANId": "null"
							}
						},
						{
							"@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
							"@odata.etag": "W/\"0AFA4BEB\"",
							"@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces/2",
							"@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
							"Id": "2",
							"AutoNeg": "null",
							"DHCPv4": {
								"DHCPEnabled": True,
								"UseDNSServers": True,
								"UseDomainName": True,
								"UseGateway": True,
								"UseNTPServers": True,
								"UseStaticRoutes": True
							},
							"DHCPv6": {
								"OperatingMode": "Stateful",
								"UseDNSServers": True,
								"UseDomainName": True,
								"UseNTPServers": True,
								"UseRapidCommit": False
							},
							"Description": "Configuration of this Manager Network Interface",
							"FQDN": "null",
							"FullDuplex": False,
							"HostName": "ILOMXQ1450J66",
							"IPv4Addresses": [
								{
									"Address": "0.0.0.0",
									"AddressOrigin": "DHCP",
									"Gateway": "0.0.0.0",
									"SubnetMask": "255.255.255.255"
								}
							],
							"IPv4StaticAddresses": [],
							"IPv6AddressPolicyTable": [
								{
									"Label": "null",
									"Precedence": 35,
									"Prefix": "::ffff:0:0/96"
								}
							],
							"IPv6Addresses": [],
							"IPv6DefaultGateway": "::",
							"IPv6StaticAddresses": [
								{
									"Address": "::",
									"PrefixLength": "null"
								},
								{
									"Address": "::",
									"PrefixLength": "null"
								},
								{
									"Address": "::",
									"PrefixLength": "null"
								},
								{
									"Address": "::",
									"PrefixLength": "null"
								}
							],
							"IPv6StaticDefaultGateways": [
								{
									"Address": "::"
								}
							],
							"InterfaceEnabled": False,
							"LinkStatus": "null",
							"MACAddress": "B4:7A:F1:C2:6A:A5",
							"MaxIPv6StaticAddresses": 4,
							"Name": "Manager Shared Network Interface",
							"NameServers": [],
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeiLOEthernetNetworkInterface.HpeiLOEthernetNetworkInterface",
									"@odata.type": "#HpeiLOEthernetNetworkInterface.v2_2_1.HpeiLOEthernetNetworkInterface",
									"ConfigurationSettings": "Current",
									"DHCPv4": {
										"ClientIdType": "Default",
										"Enabled": True,
										"UseDNSServers": True,
										"UseDomainName": True,
										"UseGateway": True,
										"UseNTPServers": True,
										"UseStaticRoutes": True,
										"UseWINSServers": True
									},
									"DHCPv6": {
										"StatefulModeEnabled": True,
										"StatelessModeEnabled": True,
										"UseDNSServers": True,
										"UseDomainName": True,
										"UseNTPServers": True,
										"UseRapidCommit": False
									},
									"DomainName": "",
									"HostName": "ILOMXQ1450J66",
									"IPv4": {
										"DDNSRegistration": True,
										"DNSServers": [
											"0.0.0.0",
											"0.0.0.0",
											"0.0.0.0"
										],
										"StaticRoutes": [
											{
												"Destination": "0.0.0.0",
												"Gateway": "0.0.0.0",
												"SubnetMask": "0.0.0.0"
											},
											{
												"Destination": "0.0.0.0",
												"Gateway": "0.0.0.0",
												"SubnetMask": "0.0.0.0"
											},
											{
												"Destination": "0.0.0.0",
												"Gateway": "0.0.0.0",
												"SubnetMask": "0.0.0.0"
											}
										],
										"WINSRegistration": True,
										"WINSServers": [
											"0.0.0.0",
											"0.0.0.0"
										]
									},
									"IPv6": {
										"DDNSRegistration": True,
										"DNSServers": [
											"::",
											"::",
											"::"
										],
										"SLAACEnabled": True,
										"StaticDefaultGateway": "::",
										"StaticRoutes": [
											{
												"Destination": "::",
												"Gateway": "::",
												"PrefixLength": "null",
												"Status": "Unknown"
											},
											{
												"Destination": "::",
												"Gateway": "::",
												"PrefixLength": "null",
												"Status": "Unknown"
											},
											{
												"Destination": "::",
												"Gateway": "::",
												"PrefixLength": "null",
												"Status": "Unknown"
											}
										]
									},
									"InterfaceType": "Shared",
									"NICEnabled": False,
									"NICSupportsIPv6": True,
									"PingGatewayOnStartup": True,
									"SharedNetworkPortOptions": {
										"Port": 1
									},
									"SupportsFlexibleLOM": True,
									"SupportsLOM": False
								}
							},
							"PermanentMACAddress": "B4:7A:F1:C2:6A:A5",
							"SpeedMbps": "null",
							"StatelessAddressAutoConfig": {
								"IPv6AutoConfigEnabled": True
							},
							"StaticNameServers": [
								"0.0.0.0",
								"0.0.0.0",
								"0.0.0.0",
								"::",
								"::",
								"::"
							],
							"Status": {
								"Health": "null",
								"State": "Disabled"
							},
							"VLAN": {
								"VLANEnable": False,
								"VLANId": "null"
							}
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"License": {
					"data": [],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"Chassis": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
							"@odata.etag": "W/\"96C96426\"",
							"@odata.id": "/redfish/v1/Chassis/1/",
							"@odata.type": "#Chassis.v1_10_2.Chassis",
							"Id": "1",
							"AssetTag": "",
							"ChassisType": "RackMount",
							"IndicatorLED": "Off",
							"Links": {
								"ManagedBy": [
									{
										"@odata.id": "/redfish/v1/Managers/1/"
									}
								],
								"ComputerSystems": [
									{
										"@odata.id": "/redfish/v1/Systems/1/"
									}
								]
							},
							"Manufacturer": "HPE",
							"Model": "ProLiant DL325 Gen10 Plus",
							"Name": "Computer System Chassis",
							"NetworkAdapters": {
								"@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/"
							},
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerChassis.HpeServerChassis",
									"@odata.type": "#HpeServerChassis.v2_3_1.HpeServerChassis",
									"Actions": {
										"#HpeServerChassis.DisableMCTPOnServer": {
											"target": "/redfish/v1/Chassis/1/Actions/Oem/Hpe/HpeServerChassis.DisableMCTPOnServer/"
										},
										"#HpeServerChassis.FactoryResetMCTP": {
											"target": "/redfish/v1/Chassis/1/Actions/Oem/Hpe/HpeServerChassis.FactoryResetMCTP/"
										}
									},
									"ElConfigOverride": False,
									"Firmware": {
										"PlatformDefinitionTable": {
											"Current": {
												"VersionString": "8.2.0 Build 36"
											}
										},
										"PowerManagementController": {
											"Current": {
												"VersionString": "1.0.8"
											}
										},
										"PowerManagementControllerBootloader": {
											"Current": {
												"Family": "25",
												"VersionString": "1.1"
											}
										},
										"SystemProgrammableLogicDevice": {
											"Current": {
												"VersionString": "0x19"
											}
										}
									},
									"Links": {
										"Devices": {
											"@odata.id": "/redfish/v1/Chassis/1/Devices/"
										}
									},
									"SystemMaintenanceSwitches": {
										"Sw1": "Off",
										"Sw10": "Off",
										"Sw11": "Off",
										"Sw12": "Off",
										"Sw2": "Off",
										"Sw3": "Off",
										"Sw4": "Off",
										"Sw5": "Off",
										"Sw6": "Off",
										"Sw7": "Off",
										"Sw8": "Off",
										"Sw9": "Off"
									}
								}
							},
							"PCIeDevices": {
								"@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/"
							},
							"PCIeSlots": {
								"@odata.id": "/redfish/v1/Chassis/1/PCIeSlots/"
							},
							"Power": {
								"@odata.id": "/redfish/v1/Chassis/1/Power/"
							},
							"PowerState": "On",
							"SKU": "P18603-B21",
							"SerialNumber": "MXQ1450J66",
							"Status": {
								"Health": "OK",
								"State": "Starting"
							},
							"Thermal": {
								"@odata.id": "/redfish/v1/Chassis/1/Thermal/"
							}
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"Systems": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
							"@odata.etag": "W/\"C249DB19\"",
							"@odata.id": "/redfish/v1/Systems/1/",
							"@odata.type": "#ComputerSystem.v1_4_0.ComputerSystem",
							"Id": "1",
							"Actions": {
								"#ComputerSystem.Reset": {
									"ResetType@Redfish.AllowableValues": [
										"On",
										"ForceOff",
										"GracefulShutdown",
										"ForceRestart",
										"Nmi",
										"PushPowerButton"
									],
									"target": "/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/"
								}
							},
							"AssetTag": "",
							"Bios": {
								"@odata.id": "/redfish/v1/systems/1/bios/"
							},
							"BiosVersion": "A41 v2.30 (10/18/2019)",
							"Boot": {
								"BootOptions": {
									"@odata.id": "/redfish/v1/Systems/1/BootOptions/"
								},
								"BootOrder": [
									"Boot000A",
									"Boot000C",
									"Boot0010",
									"Boot000D",
									"Boot000E",
									"Boot000F"
								],
								"BootSourceOverrideEnabled": "Disabled",
								"BootSourceOverrideMode": "UEFI",
								"BootSourceOverrideTarget": "None",
								"BootSourceOverrideTarget@Redfish.AllowableValues": [
									"None",
									"Cd",
									"Hdd",
									"Usb",
									"SDCard",
									"Utilities",
									"Diags",
									"BiosSetup",
									"Pxe",
									"UefiShell",
									"UefiHttp",
									"UefiTarget"
								],
								"UefiTargetBootSourceOverride": "None",
								"UefiTargetBootSourceOverride@Redfish.AllowableValues": [
									"UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)",
									"PciRoot(0x3)/Pci(0x1,0x2)/Pci(0x0,0x0)/Scsi(0x0,0x4000)",
									"PciRoot(0x0)/Pci(0x3,0x3)/Pci(0x0,0x0)/MAC(20677CE91D0C,0x1)/IPv4(0.0.0.0)",
									"PciRoot(0x0)/Pci(0x3,0x3)/Pci(0x0,0x0)/MAC(20677CE91D0C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()",
									"PciRoot(0x0)/Pci(0x3,0x3)/Pci(0x0,0x0)/MAC(20677CE91D0C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)",
									"PciRoot(0x0)/Pci(0x3,0x3)/Pci(0x0,0x0)/MAC(20677CE91D0C,0x1)/IPv4(0.0.0.0)/Uri()"
								]
							},
							"EthernetInterfaces": {
								"@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/"
							},
							"HostName": "localhost",
							"IndicatorLED": "Off",
							"Links": {
								"HpServerSettings": {
									"@odata.id": "/redfish/v1/systems/1/hpserversettings/"
								},
								"ManagedBy": [
									{
										"@odata.id": "/redfish/v1/Managers/1/"
									}
								],
								"Chassis": [
									{
										"@odata.id": "/redfish/v1/Chassis/1/"
									}
								]
							},
							"LogServices": {
								"@odata.id": "/redfish/v1/Systems/1/LogServices/"
							},
							"Manufacturer": "HPE",
							"Memory": {
								"@odata.id": "/redfish/v1/Systems/1/Memory/"
							},
							"MemoryDomains": {
								"@odata.id": "/redfish/v1/Systems/1/MemoryDomains/"
							},
							"MemorySummary": {
								"Status": {
									"HealthRollup": "OK"
								},
								"TotalSystemMemoryGiB": 16,
								"TotalSystemPersistentMemoryGiB": 0
							},
							"Model": "ProLiant DL325 Gen10",
							"Name": "Computer System",
							"NetworkInterfaces": {
								"@odata.id": "/redfish/v1/Systems/1/NetworkInterfaces/"
							},
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeComputerSystemExt.HpeComputerSystemExt",
									"@odata.type": "#HpeComputerSystemExt.v2_7_0.HpeComputerSystemExt",
									"Actions": {
										"#HpeComputerSystemExt.PowerButton": {
											"PushType@Redfish.AllowableValues": [
												"Press",
												"PressAndHold"
											],
											"target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.PowerButton/"
										},
										"#HpeComputerSystemExt.SecureSystemErase": {
											"target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.SecureSystemErase/"
										},
										"#HpeComputerSystemExt.SystemReset": {
											"ResetType@Redfish.AllowableValues": [
												"ColdBoot",
												"AuxCycle"
											],
											"target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.SystemReset/"
										}
									},
									"AggregateHealthStatus": {
										"AgentlessManagementService": "Unavailable",
										"AggregateServerHealth": "OK",
										"BiosOrHardwareHealth": {
											"Status": {
												"Health": "OK"
											}
										},
										"FanRedundancy": "Redundant",
										"Fans": {
											"Status": {
												"Health": "OK"
											}
										},
										"Memory": {
											"Status": {
												"Health": "OK"
											}
										},
										"PowerSupplies": {
											"PowerSuppliesMismatch": False,
											"Status": {
												"Health": "OK"
											}
										},
										"Processors": {
											"Status": {
												"Health": "OK"
											}
										},
										"SmartStorageBattery": {
											"Status": {
												"Health": "OK"
											}
										},
										"Storage": {
											"Status": {
												"Health": "OK"
											}
										},
										"Temperatures": {
											"Status": {
												"Health": "OK"
											}
										}
									},
									"Bios": {
										"Backup": {
											"Date": "10/18/2019",
											"Family": "A41",
											"VersionString": "A41 v2.30 (10/18/2019)"
										},
										"Current": {
											"Date": "10/18/2019",
											"Family": "A41",
											"VersionString": "A41 v2.30 (10/18/2019)"
										},
										"UefiClass": 2
									},
									"CurrentPowerOnTimeSeconds": "null",
									"DeviceDiscoveryComplete": {
										"AMSDeviceDiscovery": "NoAMS",
										"DeviceDiscovery": "vMainDeviceDiscoveryComplete",
										"SmartArrayDiscovery": "Complete"
									},
									"ElapsedEraseTimeInMinutes": 0,
									"EndOfPostDelaySeconds": "null",
									"EstimatedEraseTimeInMinutes": 0,
									"IntelligentProvisioningAlwaysOn": True,
									"IntelligentProvisioningIndex": 8,
									"IntelligentProvisioningLocation": "System Board",
									"IntelligentProvisioningVersion": "3.30.213",
									"IsColdBooting": False,
									"Links": {
										"SUT": {
											"@odata.id": "/redfish/v1/systems/1/hpsut/"
										},
										"PCIDevices": {
											"@odata.id": "/redfish/v1/Systems/1/PCIDevices/"
										},
										"PCISlots": {
											"@odata.id": "/redfish/v1/Systems/1/PCISlots/"
										},
										"NetworkAdapters": {
											"@odata.id": "/redfish/v1/Systems/1/BaseNetworkAdapters/"
										},
										"SmartStorage": {
											"@odata.id": "/redfish/v1/Systems/1/SmartStorage/"
										},
										"USBPorts": {
											"@odata.id": "/redfish/v1/Systems/1/USBPorts/"
										},
										"USBDevices": {
											"@odata.id": "/redfish/v1/Systems/1/USBDevices/"
										},
										"EthernetInterfaces": {
											"@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/"
										},
										"WorkloadPerformanceAdvisor": {
											"@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor/"
										}
									},
									"PCAPartNumber": "P04664-001",
									"PCASerialNumber": "PWTGH0CRHC0028",
									"PostDiscoveryCompleteTimeStamp": "null",
									"PostDiscoveryMode": "null",
									"PostMode": "null",
									"PostState": "FinishedPost",
									"PowerAllocationLimit": 500,
									"PowerAutoOn": "Restore",
									"PowerOnDelay": "Minimum",
									"PowerOnMinutes": 543260,
									"PowerRegulatorMode": "Unknown",
									"PowerRegulatorModesSupported": [
										"OSControl",
										"Max"
									],
									"SMBIOS": {
										"extref": "/smbios"
									},
									"ServerFQDN": "",
									"SmartStorageConfig": [
										{
											"@odata.id": "/redfish/v1/systems/1/smartstorageconfig/"
										}
									],
									"SystemROMAndiLOEraseComponentStatus": {
										"BIOSSettingsEraseStatus": "Idle",
										"iLOSettingsEraseStatus": "Idle"
									},
									"SystemROMAndiLOEraseStatus": "Idle",
									"UserDataEraseComponentStatus": {},
									"UserDataEraseStatus": "Idle",
									"VirtualProfile": "Inactive"
								}
							},
							"PowerState": "On",
							"ProcessorSummary": {
								"Count": 1,
								"Model": "AMD EPYC 7261 8-Core Processor                 ",
								"Status": {
									"HealthRollup": "OK"
								}
							},
							"Processors": {
								"@odata.id": "/redfish/v1/Systems/1/Processors/"
							},
							"SKU": "P04654-B21",
							"SecureBoot": {
								"@odata.id": "/redfish/v1/Systems/1/SecureBoot/"
							},
							"SerialNumber": "Q981SWGDS2V",
							"Status": {
								"Health": "OK",
								"HealthRollup": "OK",
								"State": "Enabled"
							},
							"Storage": {
								"@odata.id": "/redfish/v1/Systems/1/Storage/"
							},
							"SystemType": "Physical",
							"TrustedModules": [
								{
									"FirmwareVersion": "73.0",
									"InterfaceType": "TPM2_0",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeTrustedModuleExt.HpeTrustedModuleExt",
											"@odata.type": "#HpeTrustedModuleExt.v2_0_0.HpeTrustedModuleExt",
											"VendorName": "STMicro"
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									}
								}
							],
							"UUID": "608a1f3d-656f-4127-a742-57d77e1eb0ee"
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"Processor": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#Processor.Processor",
							"@odata.etag": "W/\"58543C56\"",
							"@odata.id": "/redfish/v1/Systems/1/Processors/1",
							"@odata.type": "#Processor.v1_7_2.Processor",
							"Id": "1",
							"InstructionSet": "x86-64",
							"Manufacturer": "Advanced Micro Devices, Inc.",
							"MaxSpeedMHz": 4100,
							"Model": "AMD EPYC 7262 8-Core Processor                 ",
							"Name": "Processors",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeProcessorExt.HpeProcessorExt",
									"@odata.type": "#HpeProcessorExt.v2_0_1.HpeProcessorExt",
									"AssetTag": "Unknown",
									"Cache": [
										{
											"Associativity": "8waySetAssociative",
											"CacheSpeedns": 1,
											"CurrentSRAMType": [
												"PipelineBurst"
											],
											"EccType": "MultiBitECC",
											"InstalledSizeKB": 512,
											"Location": "Internal",
											"MaximumSizeKB": 512,
											"Name": "L1-Cache",
											"Policy": "WriteBack",
											"Socketed": False,
											"SupportedSRAMType": [
												"PipelineBurst"
											],
											"SystemCacheType": "Unified"
										},
										{
											"Associativity": "8waySetAssociative",
											"CacheSpeedns": 1,
											"CurrentSRAMType": [
												"PipelineBurst"
											],
											"EccType": "MultiBitECC",
											"InstalledSizeKB": 4096,
											"Location": "Internal",
											"MaximumSizeKB": 4096,
											"Name": "L2-Cache",
											"Policy": "WriteBack",
											"Socketed": False,
											"SupportedSRAMType": [
												"PipelineBurst"
											],
											"SystemCacheType": "Unified"
										},
										{
											"Associativity": "16waySetAssociative",
											"CacheSpeedns": 1,
											"CurrentSRAMType": [
												"PipelineBurst"
											],
											"EccType": "MultiBitECC",
											"InstalledSizeKB": 131072,
											"Location": "Internal",
											"MaximumSizeKB": 131072,
											"Name": "L3-Cache",
											"Policy": "WriteBack",
											"Socketed": False,
											"SupportedSRAMType": [
												"PipelineBurst"
											],
											"SystemCacheType": "Unified"
										}
									],
									"Characteristics": [
										"64Bit",
										"MultiCore",
										"HwThread",
										"ExecuteProtection",
										"EnhancedVirtualization",
										"PowerPerfControl"
									],
									"ConfigStatus": {
										"Populated": True,
										"State": "Enabled"
									},
									"CoresEnabled": 8,
									"ExternalClockMHz": 100,
									"MicrocodePatches": [
										{
											"CpuId": "0x00008310",
											"Date": "2022-02-15T00:00:00Z",
											"PatchId": "0x08301055"
										},
										{
											"CpuId": "0x00008300",
											"Date": "2019-04-01T00:00:00Z",
											"PatchId": "0x08300027"
										}
									],
									"PartNumber": "",
									"RatedSpeedMHz": 3200,
									"SerialNumber": "",
									"VoltageVoltsX10": 11
								}
							},
							"PartNumber": "",
							"ProcessorArchitecture": "x86",
							"ProcessorId": {
								"EffectiveFamily": "107",
								"EffectiveModel": "1",
								"IdentificationRegisters": "0x0f100083fbff178b",
								"MicrocodeInfo": "null",
								"Step": "0",
								"VendorId": "Advanced Micro Devices, Inc."
							},
							"ProcessorType": "CPU",
							"SerialNumber": "",
							"Socket": "Proc 1",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							},
							"TotalCores": 8,
							"TotalThreads": 16
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"remoteSupport": {
					"data": [],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"securityDashboard": {
					"data": [],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"advancedMemoryProtection": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#HpeAdvancedMemoryProtection.HpeAdvancedMemoryProtection",
							"@odata.type": "#HpeAdvancedMemoryProtection.v2_0_0.HpeAdvancedMemoryProtection",
							"AmpModeActive": "AdvancedECC",
							"AmpModeStatus": "AdvancedECC",
							"AmpModeSupported": [
								"AdvancedECC"
							]
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"memory": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#Memory.Memory",
							"@odata.etag": "W/\"E6EC3A2C\"",
							"@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm1",
							"@odata.type": "#Memory.v1_7_1.Memory",
							"Id": "proc1dimm1",
							"BaseModuleType": "RDIMM",
							"BusWidthBits": 72,
							"CacheSizeMiB": 0,
							"CapacityMiB": 16384,
							"DataWidthBits": 64,
							"DeviceLocator": "PROC 1 DIMM 1",
							"ErrorCorrection": "MultiBitECC",
							"LogicalSizeMiB": 0,
							"Manufacturer": "Hynix",
							"MemoryDeviceType": "DDR4",
							"MemoryLocation": {
								"Channel": 3,
								"MemoryController": 3,
								"Slot": 1,
								"Socket": 1
							},
							"MemoryMedia": [
								"DRAM"
							],
							"MemoryType": "DRAM",
							"Name": "proc1dimm1",
							"NonVolatileSizeMiB": 0,
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
									"@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
									"Attributes": [
										"HpeSmartMemory"
									],
									"BaseModuleType": "RDIMM",
									"DIMMStatus": "GoodInUse",
									"MaxOperatingSpeedMTs": 3200,
									"MinimumVoltageVoltsX10": 12,
									"PartNumber": "P11442-191",
									"VendorName": "SK Hynix"
								}
							},
							"OperatingMemoryModes": [
								"Volatile"
							],
							"OperatingSpeedMhz": 3200,
							"PartNumber": "HMA82GR7CJR4N-XN",
							"PersistentRegionSizeLimitMiB": 0,
							"RankCount": 1,
							"SecurityCapabilities": {},
							"SerialNumber": "73E50EBC",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							},
							"VendorID": "44288",
							"VolatileRegionSizeLimitMiB": 16384,
							"VolatileSizeMiB": 16384
						},
						{
							"@odata.context": "/redfish/v1/$metadata#Memory.Memory",
							"@odata.etag": "W/\"6165906D\"",
							"@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm2",
							"@odata.type": "#Memory.v1_7_1.Memory",
							"Id": "proc1dimm2",
							"BusWidthBits": 72,
							"CacheSizeMiB": 0,
							"CapacityMiB": 0,
							"DataWidthBits": 64,
							"DeviceLocator": "PROC 1 DIMM 2",
							"ErrorCorrection": "MultiBitECC",
							"LogicalSizeMiB": 0,
							"MemoryLocation": {
								"Channel": 3,
								"MemoryController": 3,
								"Slot": 2,
								"Socket": 1
							},
							"MemoryMedia": [
								"DRAM"
							],
							"MemoryType": "DRAM",
							"Name": "proc1dimm2",
							"NonVolatileSizeMiB": 0,
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
									"@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
									"DIMMStatus": "NotPresent",
									"MinimumVoltageVoltsX10": 0,
									"PartNumber": "Unknown"
								}
							},
							"OperatingMemoryModes": [
								"Volatile"
							],
							"PersistentRegionSizeLimitMiB": 0,
							"RankCount": "null",
							"SecurityCapabilities": {},
							"Status": {
								"Health": "OK",
								"State": "Absent"
							},
							"VendorID": "0",
							"VolatileRegionSizeLimitMiB": 0,
							"VolatileSizeMiB": 0
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"memoryList": {
					"data": [
						{
							"BoardCpuNumber": 1,
							"BoardNumberOfSockets": 2,
							"BoardOperationalFrequency": 3200,
							"BoardOperationalVoltage": 1200,
							"BoardTotalMemorySize": 16384
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"devicesV2": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
							"@odata.etag": "W/\"4DA55F10\"",
							"@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/131",
							"@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
							"Id": "131",
							"FirmwareVersion": "2.5",
							"Manufacturer": "",
							"Model": "",
							"Name": "Embedded Video Controller",
							"PCIeFunctions": [
								{
									"@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
									"@odata.etag": "W/\"A3A6BF43\"",
									"@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/131/PCIeFunctions/1",
									"@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
									"Id": "1",
									"ClassCode": "3",
									"DeviceClass": "DisplayController",
									"DeviceId": "1336",
									"FunctionId": 1,
									"FunctionType": "Physical",
									"Name": "Function 1",
									"RevisionId": "2.5",
									"SubsystemId": "228",
									"SubsystemVendorId": "5520",
									"VendorId": "4139"
								}
							],
							"PartNumber": "",
							"SKU": "",
							"SerialNumber": "",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							}
						},
						{
							"@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
							"@odata.etag": "W/\"4DA55F10\"",
							"@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/135",
							"@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
							"Id": "135",
							"FirmwareVersion": "1.2839.0",
							"Manufacturer": "Intel Corporation",
							"Model": "K53978-004",
							"Name": "Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0",
							"PCIeFunctions": [
								{
									"@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
									"@odata.etag": "W/\"A3A6BF43\"",
									"@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/135/PCIeFunctions/1",
									"@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
									"Id": "1",
									"ClassCode": "2",
									"DeviceClass": "NetworkController",
									"DeviceId": "5409",
									"FunctionId": 1,
									"FunctionType": "Physical",
									"Name": "Function 1",
									"RevisionId": "1.2839.0",
									"SubsystemId": "163",
									"SubsystemVendorId": "32902",
									"VendorId": "32902"
								}
							],
							"PartNumber": "K53978-004",
							"SKU": "MM#999HCV",
							"SerialNumber": "6805CAEACCCC",
							"Status": {
								"Health": "null",
								"State": "null"
							}
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"firmware": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						},
						{
							"@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"@odata.etag": "W/\"3CE905E1\"",
							"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/",
							"@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
							"Description": "Firmware Inventory Collection",
							"Name": "Firmware Inventory Collection",
							"Members": [
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "1",
									"Description": "SystemBMC",
									"Name": "iLO 5",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
											"DeviceContext": "System Board",
											"Targets": [
												"4764a662-b342-4fc7-9ce9-258c5d99e815",
												"c0bcf2b9-1141-49af-aab8-c73791f0349c"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "2.72 Sept 4 2022"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "2",
									"Description": "SystemRomActive",
									"Name": "System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "H09 v1.32 (05/13/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "3",
									"Description": "PlatformDefinitionTable",
									"Name": "Intelligent Platform Abstraction Data",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a",
												"00000000-0000-0000-0000-000001483039"
											]
										}
									},
									"Version": "1.7.0 Build 1"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "4",
									"Description": "SystemProgrammableLogicDevice",
									"Name": "System Programmable Logic Device",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
											"DeviceContext": "System Board",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Status": {
										"Health": "OK",
										"State": "Enabled"
									},
									"Version": "0x05"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "5",
									"Description": "Chassis",
									"Name": "Chassis Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "42fc70be-bb87-4bdb-8e7c-db1c9af52957",
											"DeviceContext": "Chassis",
											"Targets": [
												"00000000-0000-0000-0000-00000000022a"
											]
										}
									},
									"Version": "2.1.65535"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "6",
									"Description": "SystemRomBackup",
									"Name": "Redundant System ROM",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "System Board"
										}
									},
									"Version": "H09 v1.00 (01/10/2020)"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "7",
									"Description": "SPSFirmwareVersionData",
									"Name": "Server Platform Services (SPS) Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "8e59d79d-ae28-4e35-8d63-3c0d75bee62e",
											"DeviceContext": "System Board",
											"Targets": [
												"a6b1a447-382a-5a4f-8086-a3601590028d"
											]
										}
									},
									"Version": "12.0.34.1425"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "8",
									"Description": "TrustedPlatformModule20",
									"Name": "TPM Firmware",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "fcbe6477-5c25-4488-b197-695bb8123b11",
											"DeviceContext": "System Board",
											"Targets": [
												"1118c237-4924-4fb4-a6d0-1402ac4e2c01"
											]
										}
									},
									"Version": "73.8"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9/",
									"@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
									"Id": "9",
									"Description": "15b31015103c2300",
									"Name": "Mellanox Network Adapter - 08:F1:EA:FB:21:37",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded LOM",
											"DeviceInstance": "PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-15b3-1015103c2300"
											]
										}
									},
									"Version": "14.25.10.20"
								},
								{
									"@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
									"@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10/",
									"@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
									"Id": "10",
									"Description": "9005028f103c0602",
									"Name": "HPE Smart Array P408i-a SR Gen10",
									"Oem": {
										"Hpe": {
											"@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
											"@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
											"DeviceClass": "null",
											"DeviceContext": "Embedded RAID",
											"DeviceInstance": "PciRoot(0x3)/Pci(0x0,0x0)/Pci(0x0,0x0)",
											"Targets": [
												"a6b1a447-382a-5a4f-9005-028f103c0602"
											]
										}
									},
									"Version": "3.00"
								}
							],
							"Members@odata.count": 10
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"devices": {
					"data": [
						{
							"@odata.context": "/redfish/v1/$metadata#HpeServerDevice.HpeServerDevice",
							"@odata.etag": "W/\"025CB615\"",
							"@odata.id": "/redfish/v1/Chassis/1/Devices/1/",
							"@odata.type": "#HpeServerDevice.v2_0_0.HpeServerDevice",
							"Id": "1",
							"DeviceType": "Unknown",
							"FirmwareVersion": {
								"Current": {
									"VersionString": "N/A"
								}
							},
							"Links": {
								"PCISlot": {
									"@odata.id": "/redfish/v1/Systems/1/PCISlots/1/"
								}
							},
							"Location": "PCI-E Slot 1",
							"MCTPProtocolDisabled": False,
							"Manufacturer": "",
							"Name": "Empty slot 1",
							"PartNumber": "",
							"ProductPartNumber": "",
							"ProductVersion": "",
							"SerialNumber": "",
							"Status": {
								"State": "Absent"
							},
							"PCISlot": {
								"@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
								"@odata.etag": "W/\"FE0AC9DA\"",
								"@odata.id": "/redfish/v1/Systems/1/PCISlots/1/",
								"@odata.type": "#HpeServerPCISlot.v2_1_1.HpeServerPCISlot",
								"Id": "1",
								"BusNumber": 133,
								"Characteristics": {
									"Provides3_3Volts": True,
									"SupportsPowerManagementEventSignal": True
								},
								"DeviceNumber": 0,
								"FunctionNumber": 0,
								"Length": "Long",
								"LinkLanes": "x16",
								"Name": "PCI-E Slot 1",
								"Status": {
									"OperationalStatus": [
										{
											"Status": "InUse"
										}
									]
								},
								"SupportsHotPlug": False,
								"Technology": "PCIExpressGen4",
								"UEFIDevicePath": "PciRoot(0x1)/Pci(0x3,0x1)/Pci(0x0,0x0)"
							}
						},
						{
							"@odata.context": "/redfish/v1/$metadata#HpeServerDevice.HpeServerDevice",
							"@odata.etag": "W/\"22A717A6\"",
							"@odata.id": "/redfish/v1/Chassis/1/Devices/2/",
							"@odata.type": "#HpeServerDevice.v2_0_0.HpeServerDevice",
							"Id": "2",
							"DeviceType": "Unknown",
							"FirmwareVersion": {
								"Current": {
									"VersionString": "N/A"
								}
							},
							"Links": {
								"PCISlot": {
									"@odata.id": "/redfish/v1/Systems/1/PCISlots/2/"
								}
							},
							"Location": "PCI-E Slot 2",
							"MCTPProtocolDisabled": False,
							"Manufacturer": "",
							"Name": "Empty slot 2",
							"PartNumber": "",
							"ProductPartNumber": "",
							"ProductVersion": "",
							"SerialNumber": "",
							"Status": {
								"State": "Absent"
							},
							"PCISlot": {
								"@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
								"@odata.etag": "W/\"4E49D6D1\"",
								"@odata.id": "/redfish/v1/Systems/1/PCISlots/2/",
								"@odata.type": "#HpeServerPCISlot.v2_1_1.HpeServerPCISlot",
								"Id": "2",
								"BusNumber": 3,
								"Characteristics": {
									"Provides3_3Volts": True,
									"SupportsPowerManagementEventSignal": True
								},
								"DeviceNumber": 0,
								"FunctionNumber": 0,
								"Length": "Long",
								"LinkLanes": "x16",
								"Name": "PCI-E Slot 2",
								"Status": {
									"OperationalStatus": [
										{
											"Status": "Empty"
										}
									]
								},
								"SupportsHotPlug": False,
								"Technology": "PCIExpressGen4",
								"UEFIDevicePath": "PciRoot(0x3)/Pci(0x3,0x1)/Pci(0x0,0x0)"
							}
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"localStorage": {
					"data": [],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"localStorageV2": {
					"data": [
						{
							"@odata.etag": "W/\"43200452\"",
							"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000",
							"@odata.type": "#Storage.v1_13_0.Storage",
							"Id": "DE040000",
							"Name": "HPE NS204i-p Gen10+ Boot Controller",
							"Actions": {
								"#Storage.ResetToDefaults": {
									"target": "/redfish/v1/Systems/1/Storage/DE040000/Actions/Storage.ResetToDefaults",
									"ResetType@Redfish.AllowableValues": [
										"ResetAll",
										"PreserveVolumes"
									]
								}
							},
							"Status": {
								"State": "Enabled",
								"HealthRollup": "OK"
							},
							"Drives@odata.count": 2,
							"Drives": [
								{
									"@odata.etag": "W/\"b829e489\"",
									"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Drives/1",
									"@odata.type": "#Drive.v1_15_0.Drive",
									"Id": "1",
									"Name": "480GB 16G NVMe SSD",
									"Status": {
										"State": "Enabled",
										"Health": "OK"
									},
									"BlockSizeBytes": 512,
									"CapableSpeedGbs": 16.0,
									"CapacityBytes": 480103981056,
									"EncryptionAbility": "None",
									"EncryptionStatus": "Unencrypted",
									"FailurePredicted": False,
									"HotspareType": "None",
									"Identifiers": [
										{
											"DurableNameFormat": "EUI",
											"DurableName": "ac:e4:2e:00:06:04:6e:1d"
										}
									],
									"LocationIndicatorActive": False,
									"Links": {
										"Storage": {
											"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000"
										},
										"Volumes": [
											{
												"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Volumes/1"
											}
										],
										"Volumes@odata.count": 1
									},
									"MediaType": "SSD",
									"Model": "VS000480KXALB",
									"Multipath": False,
									"NegotiatedSpeedGbs": 16.0,
									"PhysicalLocation": {
										"PartLocation": {
											"LocationOrdinalValue": 1,
											"LocationType": "Bay",
											"ServiceLabel": "Slot=1:Bay=1"
										}
									},
									"PredictedMediaLifeLeftPercent": 100.0,
									"Protocol": "NVMe",
									"Revision": "85032G00",
									"SerialNumber": "FJ0AN6904I120AI14",
									"StatusIndicator": "OK",
									"WriteCacheEnabled": False,
									"Operations": []
								},
								{
									"@odata.etag": "W/\"6e483443\"",
									"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Drives/2",
									"@odata.type": "#Drive.v1_15_0.Drive",
									"Id": "2",
									"Name": "480GB 16G NVMe SSD",
									"Status": {
										"State": "Enabled",
										"Health": "OK"
									},
									"BlockSizeBytes": 512,
									"CapableSpeedGbs": 16.0,
									"CapacityBytes": 480103981056,
									"EncryptionAbility": "None",
									"EncryptionStatus": "Unencrypted",
									"FailurePredicted": False,
									"HotspareType": "None",
									"Identifiers": [
										{
											"DurableNameFormat": "EUI",
											"DurableName": "ac:e4:2e:00:06:04:6e:13"
										}
									],
									"LocationIndicatorActive": False,
									"Links": {
										"Storage": {
											"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000"
										},
										"Volumes": [
											{
												"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Volumes/1"
											}
										],
										"Volumes@odata.count": 1
									},
									"MediaType": "SSD",
									"Model": "VS000480KXALB",
									"Multipath": False,
									"NegotiatedSpeedGbs": 16.0,
									"PhysicalLocation": {
										"PartLocation": {
											"LocationOrdinalValue": 2,
											"LocationType": "Bay",
											"ServiceLabel": "Slot=1:Bay=2"
										}
									},
									"PredictedMediaLifeLeftPercent": 100.0,
									"Protocol": "NVMe",
									"Revision": "85032G00",
									"SerialNumber": "FJ0AN6904I120AI0U",
									"StatusIndicator": "OK",
									"WriteCacheEnabled": False,
									"Operations": []
								}
							],
							"Volumes": [
								{
									"@odata.etag": "W/\"88913cca\"",
									"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Volumes/1",
									"@odata.type": "#Volume.v1_8_0.Volume",
									"Id": "1",
									"Name": "NS Volume",
									"Status": {
										"State": "Enabled",
										"Health": "OK"
									},
									"BlockSizeBytes": 512,
									"CapacityBytes": 480036519936,
									"DisplayName": "VD_1",
									"Encrypted": False,
									"Identifiers": [
										{
											"DurableNameFormat": "EUI",
											"DurableName": "00:50:43:3c:00:00:00:01"
										}
									],
									"InitializeMethod": "Background",
									"IsBootCapable": True,
									"IOPerfModeEnabled": False,
									"Links": {
										"Drives@odata.count": 2,
										"Drives": [
											{
												"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Drives/1"
											},
											{
												"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Drives/2"
											}
										],
										"DedicatedSpareDrives@odata.count": 0,
										"DedicatedSpareDrives": []
									},
									"LogicalUnitNumber": 1,
									"OptimumIOSizeBytes": 131072,
									"RAIDType": "RAID1",
									"ReadCachePolicy": "Off",
									"StripSizeBytes": 131072,
									"VolumeUsage": "Data",
									"WriteCachePolicy": "Off",
									"Operations": []
								}
							],
							"Controllers": [
								{
									"@odata.etag": "W/\"d8730d20\"",
									"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Controllers/0",
									"@odata.type": "#StorageController.v1_5_0.StorageController",
									"Id": "0",
									"Name": "HPE NS204i-p Gen10+ Boot Controller",
									"CacheSummary": {
										"TotalCacheSizeMiB": 0,
										"PersistentCacheSizeMiB": 0,
										"Status": {
											"Health": "OK",
											"State": "Absent"
										}
									},
									"ControllerRates": {
										"ConsistencyCheckRatePercent": 100,
										"RebuildRatePercent": 100,
										"TransformationRatePercent": 100
									},
									"FirmwareVersion": "1.2.14.1010",
									"Identifiers": [
										{
											"DurableName": "534800d000bb0a28",
											"DurableNameFormat": "NAA"
										}
									],
									"Location": {
										"PartLocation": {
											"ServiceLabel": "Slot 1",
											"LocationType": "Slot",
											"LocationOrdinalValue": 1
										}
									},
									"Manufacturer": "HPE",
									"Model": "HPE NS204i-p Gen10+ Boot Controller",
									"PartNumber": "P14379-001",
									"PCIeInterface": {
										"MaxPCIeType": "Gen3",
										"PCIeType": "Gen3",
										"MaxLanes": 4,
										"LanesInUse": 4
									},
									"SKU": "P12965-B21",
									"SerialNumber": "PWWVF0BSTEB5GK",
									"SpeedGbps": 16,
									"Status": {
										"State": "Enabled",
										"Health": "OK"
									},
									"SupportedControllerProtocols": [
										"PCIe"
									],
									"SupportedDeviceProtocols": [
										"NVMe"
									],
									"SupportedRAIDTypes": [
										"RAID1"
									]
								}
							],
							"Annotations": {},
							"StorageControllers": [
								{
									"@odata.etag": "W/\"d8730d20\"",
									"@odata.id": "/redfish/v1/Systems/1/Storage/DE040000/Controllers/0",
									"@odata.type": "#StorageController.v1_5_0.StorageController",
									"Id": "0",
									"Name": "HPE NS204i-p Gen10+ Boot Controller",
									"CacheSummary": {
										"TotalCacheSizeMiB": 0,
										"PersistentCacheSizeMiB": 0,
										"Status": {
											"Health": "OK",
											"State": "Absent"
										}
									},
									"ControllerRates": {
										"ConsistencyCheckRatePercent": 100,
										"RebuildRatePercent": 100,
										"TransformationRatePercent": 100
									},
									"FirmwareVersion": "1.2.14.1010",
									"Identifiers": [
										{
											"DurableName": "534800d000bb0a28",
											"DurableNameFormat": "NAA"
										}
									],
									"Location": {
										"PartLocation": {
											"ServiceLabel": "Slot 1",
											"LocationType": "Slot",
											"LocationOrdinalValue": 1
										}
									},
									"Manufacturer": "HPE",
									"Model": "HPE NS204i-p Gen10+ Boot Controller",
									"PartNumber": "P14379-001",
									"PCIeInterface": {
										"MaxPCIeType": "Gen3",
										"PCIeType": "Gen3",
										"MaxLanes": 4,
										"LanesInUse": 4
									},
									"SKU": "P12965-B21",
									"SerialNumber": "PWWVF0BSTEB5GK",
									"SpeedGbps": 16,
									"Status": {
										"State": "Enabled",
										"Health": "OK"
									},
									"SupportedControllerProtocols": [
										"PCIe"
									],
									"SupportedDeviceProtocols": [
										"NVMe"
									],
									"SupportedRAIDTypes": [
										"RAID1"
									]
								}
							]
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"powerSupplies": {
					"data": [
						{
							"@odata.id": "/redfish/v1/Chassis/1/Power/#PowerSupplies/0",
							"FirmwareVersion": "0.00",
							"LastPowerOutputWatts": 0,
							"LineInputVoltage": 0,
							"LineInputVoltageType": "Unknown",
							"MemberId": "0",
							"Name": "HpeServerPowerSupply",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerPowerSupply.HpeServerPowerSupply",
									"@odata.type": "#HpeServerPowerSupply.v2_0_0.HpeServerPowerSupply",
									"AveragePowerOutputWatts": 0,
									"BayNumber": 1,
									"HotplugCapable": False,
									"MaxPowerOutputWatts": 0,
									"Mismatched": False,
									"PowerSupplyStatus": {
										"State": "Unknown"
									},
									"iPDUCapable": False
								}
							},
							"PowerCapacityWatts": 0,
							"PowerSupplyType": "AC",
							"SparePartNumber": "",
							"Status": {
								"Health": "Warning",
								"State": "Absent"
							}
						},
						{
							"@odata.id": "/redfish/v1/Chassis/1/Power/#PowerSupplies/1",
							"FirmwareVersion": "0.00",
							"LastPowerOutputWatts": 0,
							"LineInputVoltage": 0,
							"LineInputVoltageType": "Unknown",
							"MemberId": "1",
							"Name": "HpeServerPowerSupply",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerPowerSupply.HpeServerPowerSupply",
									"@odata.type": "#HpeServerPowerSupply.v2_0_0.HpeServerPowerSupply",
									"AveragePowerOutputWatts": 0,
									"BayNumber": 2,
									"HotplugCapable": False,
									"MaxPowerOutputWatts": 0,
									"Mismatched": False,
									"PowerSupplyStatus": {
										"State": "Unknown"
									},
									"iPDUCapable": False
								}
							},
							"PowerCapacityWatts": 0,
							"PowerSupplyType": "AC",
							"SparePartNumber": "",
							"Status": {
								"Health": "Warning",
								"State": "Absent"
							}
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"fans": {
					"data": [
						{
							"@odata.id": "/redfish/v1/Chassis/1/Thermal#Fans/0",
							"MemberId": "0",
							"Name": "Fan 1",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerFan.HpeServerFan",
									"@odata.type": "#HpeServerFan.v2_0_0.HpeServerFan",
									"HotPluggable": True,
									"Location": "System",
									"Redundant": True
								}
							},
							"Reading": 13,
							"ReadingUnits": "Percent",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							}
						},
						{
							"@odata.id": "/redfish/v1/Chassis/1/Thermal#Fans/1",
							"MemberId": "1",
							"Name": "Fan 2",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerFan.HpeServerFan",
									"@odata.type": "#HpeServerFan.v2_0_0.HpeServerFan",
									"HotPluggable": True,
									"Location": "System",
									"Redundant": False
								}
							},
							"Reading": 0,
							"ReadingUnits": "Percent",
							"Status": {
								"State": "Absent"
							}
						},
						{
							"@odata.id": "/redfish/v1/Chassis/1/Thermal#Fans/2",
							"MemberId": "2",
							"Name": "Fan 3",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerFan.HpeServerFan",
									"@odata.type": "#HpeServerFan.v2_0_0.HpeServerFan",
									"HotPluggable": True,
									"Location": "System",
									"Redundant": True
								}
							},
							"Reading": 13,
							"ReadingUnits": "Percent",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							}
						},
						{
							"@odata.id": "/redfish/v1/Chassis/1/Thermal#Fans/3",
							"MemberId": "3",
							"Name": "Fan 4",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerFan.HpeServerFan",
									"@odata.type": "#HpeServerFan.v2_0_0.HpeServerFan",
									"HotPluggable": True,
									"Location": "System",
									"Redundant": True
								}
							},
							"Reading": 13,
							"ReadingUnits": "Percent",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							}
						},
						{
							"@odata.id": "/redfish/v1/Chassis/1/Thermal#Fans/4",
							"MemberId": "4",
							"Name": "Fan 5",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerFan.HpeServerFan",
									"@odata.type": "#HpeServerFan.v2_0_0.HpeServerFan",
									"HotPluggable": True,
									"Location": "System",
									"Redundant": True
								}
							},
							"Reading": 13,
							"ReadingUnits": "Percent",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							}
						},
						{
							"@odata.id": "/redfish/v1/Chassis/1/Thermal#Fans/5",
							"MemberId": "5",
							"Name": "Fan 6",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerFan.HpeServerFan",
									"@odata.type": "#HpeServerFan.v2_0_0.HpeServerFan",
									"HotPluggable": True,
									"Location": "System",
									"Redundant": True
								}
							},
							"Reading": 13,
							"ReadingUnits": "Percent",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							}
						},
						{
							"@odata.id": "/redfish/v1/Chassis/1/Thermal#Fans/6",
							"MemberId": "6",
							"Name": "Fan 7",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerFan.HpeServerFan",
									"@odata.type": "#HpeServerFan.v2_0_0.HpeServerFan",
									"HotPluggable": True,
									"Location": "System",
									"Redundant": False
								}
							},
							"Reading": 0,
							"ReadingUnits": "Percent",
							"Status": {
								"State": "Absent"
							}
						},
						{
							"@odata.id": "/redfish/v1/Chassis/1/Thermal#Fans/7",
							"MemberId": "7",
							"Name": "Fan 8",
							"Oem": {
								"Hpe": {
									"@odata.context": "/redfish/v1/$metadata#HpeServerFan.HpeServerFan",
									"@odata.type": "#HpeServerFan.v2_0_0.HpeServerFan",
									"HotPluggable": True,
									"Location": "System",
									"Redundant": True
								}
							},
							"Reading": 13,
							"ReadingUnits": "Percent",
							"Status": {
								"Health": "OK",
								"State": "Enabled"
							}
						}
					],
					"status": "Success",
					"messages": [
						"RESOURCE_INVENTORY_SUCCESSFUL"
					],
					"postActuationActions": []
				},
				"software": {
					"data": [],
					"status": "NotAttempted",
					"messages": [
						"SUB_RESOURCE_INVENTORY_UNATTEMPTED_PRECONDITIONS_FAILURE"
					],
					"postActuationActions": []
				}
			},
			"redfishSupportedDevice": "SUPPORTED",
			"redfishCacSessionStatus": False
		},
		"targetUri": "null"
	}
}

print(type(raw_inv_resp))
assert "taskStatus" in raw_inv_resp
if "taskStatus" in raw_inv_resp:
    print("taskStatus exists in inventory and value is %s", raw_inv_resp["taskStatus"])

data = {}
msg = json.dumps(raw_inv_resp)
print("sirish")
print(type(msg))
key = '/api/v1/servers/productid+serial'
bkey = key.encode()
print(type(key.encode()))
bin_value = bytes(key,'UTF-8')
print(bin_value)



