from jsonrpc2_base.client import Client
from metal_cloud_sdk.objects.utils.deserializer import Deserializer
from metal_cloud_sdk.objects.utils.serializer import Serializer
from jsonrpc2_base.jsonrpc_exception import JSONRPCException

class ExtendedAPI(Client):
	__instance = None

	def __init__(self, dictParams, arrFilterPlugins = []):
		super(ExtendedAPI, self).__init__(dictParams, arrFilterPlugins)

	@staticmethod
	def getInstance(dictParams, arrFilterPlugins = []):
		"""
		This is a static function for using the ExtendedAPI class as a singleton.
		In order to work with only an instance, instead of instantiating the class,
		call this method.

		@return object ExtendedAPI.__instance. It will return the same instance, no matter
		how many times this function is called.
		"""
		if ExtendedAPI.__instance is None :
			ExtendedAPI.__instance = ExtendedAPI(dictParams, arrFilterPlugins)

		return ExtendedAPI.__instance


	""" 230 functions available on endpoint. """

	def cluster_create(self, strInfrastructureID, objCluster):

		objCluster = Serializer.serialize(objCluster)

		arrParams = [
			strInfrastructureID,
			objCluster,
		]

		return Deserializer.deserialize(self.rpc("cluster_create", arrParams))

	def cluster_get(self, strClusterID, bAccessSaaSAPI = True, nAccessSaaSAPITimeoutSeconds = 10):

		arrParams = [
			strClusterID,
			bAccessSaaSAPI,
			nAccessSaaSAPITimeoutSeconds,
		]

		return Deserializer.deserialize(self.rpc("cluster_get", arrParams))

	def cluster_edit(self, strClusterID, objClusterOperation):

		objClusterOperation = Serializer.serialize(objClusterOperation)

		arrParams = [
			strClusterID,
			objClusterOperation,
		]

		return Deserializer.deserialize(self.rpc("cluster_edit", arrParams))

	def cluster_stop(self, strClusterID):

		arrParams = [
			strClusterID,
		]

		return Deserializer.deserialize(self.rpc("cluster_stop", arrParams))

	def cluster_start(self, strClusterID):

		arrParams = [
			strClusterID,
		]

		return Deserializer.deserialize(self.rpc("cluster_start", arrParams))

	def cluster_delete(self, strClusterID):

		arrParams = [
			strClusterID,
		]

		return Deserializer.deserialize(self.rpc("cluster_delete", arrParams))

	def clusters(self, strInfrastructureID, arrClusterIDs = None, bAccessSaaSAPI = False, nAccessSaaSAPITimeoutSeconds = 10):

		arrParams = [
			strInfrastructureID,
			arrClusterIDs,
			bAccessSaaSAPI,
			nAccessSaaSAPITimeoutSeconds,
		]

		objCluster = self.rpc("clusters", arrParams)
		for strKeyCluster in objCluster:
			objCluster[strKeyCluster] = Deserializer.deserialize(objCluster[strKeyCluster])
		return objCluster

	def datacenters(self, strUserID = None, bOnlyActive = False):

		arrParams = [
			strUserID,
			bOnlyActive,
		]

		objDatacenter = self.rpc("datacenters", arrParams)
		for strKeyDatacenter in objDatacenter:
			objDatacenter[strKeyDatacenter] = Deserializer.deserialize(objDatacenter[strKeyDatacenter])
		return objDatacenter

	def events_delete(self, strInfrastructureID, arrEventIDs):

		arrParams = [
			strInfrastructureID,
			arrEventIDs,
		]

		self.rpc("events_delete", arrParams)


	def infrastructure_create(self, strUserID, objInfrastructure, strInfrastructureIDAsTemplate = None):

		objInfrastructure = Serializer.serialize(objInfrastructure)

		arrParams = [
			strUserID,
			objInfrastructure,
			strInfrastructureIDAsTemplate,
		]

		return Deserializer.deserialize(self.rpc("infrastructure_create", arrParams))

	def infrastructure_deploy(self, strInfrastructureID, objShutdownOptions = None, objDeployOptions = None, bAllowDataLoss = False, bSkipAnsible = False):

		objShutdownOptions = Serializer.serialize(objShutdownOptions)
		objDeployOptions = Serializer.serialize(objDeployOptions)

		arrParams = [
			strInfrastructureID,
			objShutdownOptions,
			objDeployOptions,
			bAllowDataLoss,
			bSkipAnsible,
		]

		return Deserializer.deserialize(self.rpc("infrastructure_deploy", arrParams))

	def infrastructure_operation_cancel(self, strInfrastructureID):

		arrParams = [
			strInfrastructureID,
		]

		self.rpc("infrastructure_operation_cancel", arrParams)


	def infrastructure_user_add(self, strInfrastructureID, strUserEmail, objInfrastructurePermissions = None, bCreateUserIfNotExists = False):

		objInfrastructurePermissions = Serializer.serialize(objInfrastructurePermissions)

		arrParams = [
			strInfrastructureID,
			strUserEmail,
			objInfrastructurePermissions,
			bCreateUserIfNotExists,
		]

		self.rpc("infrastructure_user_add", arrParams)


	def infrastructure_user_remove(self, strInfrastructureID, strUserID):

		arrParams = [
			strInfrastructureID,
			strUserID,
		]

		return self.rpc("infrastructure_user_remove", arrParams)


	def infrastructure_user_update(self, strInfrastructureID, strUserEmail, objInfrastructurePermissions):

		objInfrastructurePermissions = Serializer.serialize(objInfrastructurePermissions)

		arrParams = [
			strInfrastructureID,
			strUserEmail,
			objInfrastructurePermissions,
		]

		self.rpc("infrastructure_user_update", arrParams)


	def infrastructure_user_ssh_keys(self, strInfrastructureID):

		arrParams = [
			strInfrastructureID,
		]

		return self.rpc("infrastructure_user_ssh_keys", arrParams)


	def infrastructure_users(self, strInfrastructureID, arrUserIDs = None):

		arrParams = [
			strInfrastructureID,
			arrUserIDs,
		]

		objUser = self.rpc("infrastructure_users", arrParams)
		for strKeyUser in objUser:
			objUser[strKeyUser] = Deserializer.deserialize(objUser[strKeyUser])
		return objUser

	def infrastructure_edit(self, strInfrastructureID, objInfrastructureOperation):

		objInfrastructureOperation = Serializer.serialize(objInfrastructureOperation)

		arrParams = [
			strInfrastructureID,
			objInfrastructureOperation,
		]

		return Deserializer.deserialize(self.rpc("infrastructure_edit", arrParams))

	def infrastructure_deploy_options(self, strInfrastructureID, bReplaceServerTypes = False):

		arrParams = [
			strInfrastructureID,
			bReplaceServerTypes,
		]

		return self.rpc("infrastructure_deploy_options", arrParams)


	def infrastructure_deploy_overview(self, strInfrastructureID, objDeployOptions = None):

		objDeployOptions = Serializer.serialize(objDeployOptions)

		arrParams = [
			strInfrastructureID,
			objDeployOptions,
		]

		return Deserializer.deserialize(self.rpc("infrastructure_deploy_overview", arrParams))

	def infrastructure_delete(self, strInfrastructureID):

		arrParams = [
			strInfrastructureID,
		]

		return Deserializer.deserialize(self.rpc("infrastructure_delete", arrParams))

	def infrastructure_user_limits(self, strInfrastructureID):

		arrParams = [
			strInfrastructureID,
		]

		return Deserializer.deserialize(self.rpc("infrastructure_user_limits", arrParams))

	def infrastructure_gui_settings_save(self, strInfrastructureID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strInfrastructureID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("infrastructure_gui_settings_save", arrParams)


	def instance_edit(self, strInstanceID, objInstanceOperation):

		objInstanceOperation = Serializer.serialize(objInstanceOperation)

		arrParams = [
			strInstanceID,
			objInstanceOperation,
		]

		return Deserializer.deserialize(self.rpc("instance_edit", arrParams))

	def instance_delete(self, strInstanceID, bKeepDetachingDrives):

		arrParams = [
			strInstanceID,
			bKeepDetachingDrives,
		]

		return Deserializer.deserialize(self.rpc("instance_delete", arrParams))

	def instance_array_instances(self, strInstanceArrayID, arrInstanceIDs = None):

		arrParams = [
			strInstanceArrayID,
			arrInstanceIDs,
		]

		objInstance = self.rpc("instance_array_instances", arrParams)
		for strKeyInstance in objInstance:
			objInstance[strKeyInstance] = Deserializer.deserialize(objInstance[strKeyInstance])
		return objInstance

	def instance_server_power_get(self, strInstanceID):

		arrParams = [
			strInstanceID,
		]

		return self.rpc("instance_server_power_get", arrParams)


	def instance_server_power_set(self, strInstanceID, strPowerCommand):

		arrParams = [
			strInstanceID,
			strPowerCommand,
		]

		self.rpc("instance_server_power_set", arrParams)


	def instance_array_create(self, strInfrastructureID, objInstanceArray):

		objInstanceArray = Serializer.serialize(objInstanceArray)

		arrParams = [
			strInfrastructureID,
			objInstanceArray,
		]

		return Deserializer.deserialize(self.rpc("instance_array_create", arrParams))

	def instance_array_edit(self, strInstanceArrayID, objInstanceArrayOperation, bSwapExistingInstancesHardware = False, bKeepDetachingDrives = None, objServerTypeMatches = None, arrInstancesToBeDeleted = None):

		objInstanceArrayOperation = Serializer.serialize(objInstanceArrayOperation)
		objServerTypeMatches = Serializer.serialize(objServerTypeMatches)

		arrParams = [
			strInstanceArrayID,
			objInstanceArrayOperation,
			bSwapExistingInstancesHardware,
			bKeepDetachingDrives,
			objServerTypeMatches,
			arrInstancesToBeDeleted,
		]

		return Deserializer.deserialize(self.rpc("instance_array_edit", arrParams))

	def instance_array_delete(self, strInstanceArrayID):

		arrParams = [
			strInstanceArrayID,
		]

		return Deserializer.deserialize(self.rpc("instance_array_delete", arrParams))

	def instance_array_stop(self, strInstanceArrayID):

		arrParams = [
			strInstanceArrayID,
		]

		return Deserializer.deserialize(self.rpc("instance_array_stop", arrParams))

	def instance_array_start(self, strInstanceArrayID):

		arrParams = [
			strInstanceArrayID,
		]

		return Deserializer.deserialize(self.rpc("instance_array_start", arrParams))

	def instance_arrays(self, strInfrastructureID, arrInstanceArrayIDs = None):

		arrParams = [
			strInfrastructureID,
			arrInstanceArrayIDs,
		]

		objInstanceArray = self.rpc("instance_arrays", arrParams)
		for strKeyInstanceArray in objInstanceArray:
			objInstanceArray[strKeyInstanceArray] = Deserializer.deserialize(objInstanceArray[strKeyInstanceArray])
		return objInstanceArray

	def instance_array_interface_attach_network(self, strInstanceArrayID, nInstanceArrayInterfaceIndex, strNetworkID):

		arrParams = [
			strInstanceArrayID,
			nInstanceArrayInterfaceIndex,
			strNetworkID,
		]

		return Deserializer.deserialize(self.rpc("instance_array_interface_attach_network", arrParams))

	def instance_array_interface_detach(self, strInstanceArrayID, nInstanceArrayInterfaceIndex):

		arrParams = [
			strInstanceArrayID,
			nInstanceArrayInterfaceIndex,
		]

		return Deserializer.deserialize(self.rpc("instance_array_interface_detach", arrParams))

	def subnet_create(self, strNetworkID, objSubnet):

		objSubnet = Serializer.serialize(objSubnet)

		arrParams = [
			strNetworkID,
			objSubnet,
		]

		return Deserializer.deserialize(self.rpc("subnet_create", arrParams))

	def subnet_delete(self, strSubnetID):

		arrParams = [
			strSubnetID,
		]

		return Deserializer.deserialize(self.rpc("subnet_delete", arrParams))

	def subnets(self, strNetworkID, arrSubnetIDs = None):

		arrParams = [
			strNetworkID,
			arrSubnetIDs,
		]

		objSubnet = self.rpc("subnets", arrParams)
		for strKeySubnet in objSubnet:
			objSubnet[strKeySubnet] = Deserializer.deserialize(objSubnet[strKeySubnet])
		return objSubnet

	def data_lake_create(self, strInfrastructureID, objDataLake):

		objDataLake = Serializer.serialize(objDataLake)

		arrParams = [
			strInfrastructureID,
			objDataLake,
		]

		return Deserializer.deserialize(self.rpc("data_lake_create", arrParams))

	def data_lake_get(self, strDataLakeID):

		arrParams = [
			strDataLakeID,
		]

		return Deserializer.deserialize(self.rpc("data_lake_get", arrParams))

	def data_lake_edit(self, strDataLakeID, objDataLakeOperation):

		objDataLakeOperation = Serializer.serialize(objDataLakeOperation)

		arrParams = [
			strDataLakeID,
			objDataLakeOperation,
		]

		return self.rpc("data_lake_edit", arrParams)


	def data_lake_stop(self, strDataLakeID):

		arrParams = [
			strDataLakeID,
		]

		return Deserializer.deserialize(self.rpc("data_lake_stop", arrParams))

	def data_lake_start(self, strDataLakeID):

		arrParams = [
			strDataLakeID,
		]

		return Deserializer.deserialize(self.rpc("data_lake_start", arrParams))

	def data_lake_delete(self, strDataLakeID):

		arrParams = [
			strDataLakeID,
		]

		return Deserializer.deserialize(self.rpc("data_lake_delete", arrParams))

	def data_lakes(self, strInfrastructureID, arrDataLakeIDs = None):

		arrParams = [
			strInfrastructureID,
			arrDataLakeIDs,
		]

		objDataLake = self.rpc("data_lakes", arrParams)
		for strKeyDataLake in objDataLake:
			objDataLake[strKeyDataLake] = Deserializer.deserialize(objDataLake[strKeyDataLake])
		return objDataLake

	def data_lake_krb_conf_download_url(self):

		arrParams = [
		]

		return self.rpc("data_lake_krb_conf_download_url", arrParams)


	def network_create(self, strInfrastructureID, objNetwork):

		objNetwork = Serializer.serialize(objNetwork)

		arrParams = [
			strInfrastructureID,
			objNetwork,
		]

		return Deserializer.deserialize(self.rpc("network_create", arrParams))

	def network_edit(self, strNetworkID, objNetworkOperation):

		objNetworkOperation = Serializer.serialize(objNetworkOperation)

		arrParams = [
			strNetworkID,
			objNetworkOperation,
		]

		return Deserializer.deserialize(self.rpc("network_edit", arrParams))

	def network_delete(self, strNetworkID):

		arrParams = [
			strNetworkID,
		]

		return Deserializer.deserialize(self.rpc("network_delete", arrParams))

	def network_stop(self, strNetworkID):

		arrParams = [
			strNetworkID,
		]

		return Deserializer.deserialize(self.rpc("network_stop", arrParams))

	def network_start(self, strNetworkID):

		arrParams = [
			strNetworkID,
		]

		return Deserializer.deserialize(self.rpc("network_start", arrParams))

	def networks(self, strInfrastructureID, arrNetworkIDs = None):

		arrParams = [
			strInfrastructureID,
			arrNetworkIDs,
		]

		objNetwork = self.rpc("networks", arrParams)
		for strKeyNetwork in objNetwork:
			objNetwork[strKeyNetwork] = Deserializer.deserialize(objNetwork[strKeyNetwork])
		return objNetwork

	def network_join(self, strNetworkID, strNetworkToBeDeletedID):

		arrParams = [
			strNetworkID,
			strNetworkToBeDeletedID,
		]

		return Deserializer.deserialize(self.rpc("network_join", arrParams))

	def resource_utilization_summary(self, strUserIDOwner, strStartTimestamp, strEndTimestamp, arrInfrastructureIDs = None):

		arrParams = [
			strUserIDOwner,
			strStartTimestamp,
			strEndTimestamp,
			arrInfrastructureIDs,
		]

		return self.rpc("resource_utilization_summary", arrParams)


	def resource_utilization_detailed(self, strUserIDOwner, strStartTimestamp, strEndTimestamp, arrInfrastructureIDs = None):

		arrParams = [
			strUserIDOwner,
			strStartTimestamp,
			strEndTimestamp,
			arrInfrastructureIDs,
		]

		return self.rpc("resource_utilization_detailed", arrParams)


	def server_type_reservation_create(self, strUserID, objReservation, nQuantity = 1):

		objReservation = Serializer.serialize(objReservation)

		arrParams = [
			strUserID,
			objReservation,
			nQuantity,
		]

		arrServerTypeReservations = self.rpc("server_type_reservation_create", arrParams)
		for index in range(len(arrServerTypeReservations)):
			arrServerTypeReservations[index] = Deserializer.deserialize(arrServerTypeReservations[index])
		return arrServerTypeReservations

	def server_type_reservation_get(self, nServerTypeReservationID):

		arrParams = [
			nServerTypeReservationID,
		]

		return Deserializer.deserialize(self.rpc("server_type_reservation_get", arrParams))

	def server_type_reservation_edit(self, nServerTypeReservationID, objServerTypeReservation):

		objServerTypeReservation = Serializer.serialize(objServerTypeReservation)

		arrParams = [
			nServerTypeReservationID,
			objServerTypeReservation,
		]

		return Deserializer.deserialize(self.rpc("server_type_reservation_edit", arrParams))

	def user_server_type_reservations(self, strUserID):

		arrParams = [
			strUserID,
		]

		return self.rpc("user_server_type_reservations", arrParams)


	def instance_server_power_set_batch(self, strInfrastructureID, arrInstanceIDs, strPowerCommand):

		arrParams = [
			strInfrastructureID,
			arrInstanceIDs,
			strPowerCommand,
		]

		self.rpc("instance_server_power_set_batch", arrParams)


	def instance_server_power_get_batch(self, strInfrastructureID, arrInstanceIDs):

		arrParams = [
			strInfrastructureID,
			arrInstanceIDs,
		]

		return self.rpc("instance_server_power_get_batch", arrParams)


	def infrastructure_deploy_shutdown_required(self, strInfrastructureID, strPowerCommand = "none", bOnlyPoweredOn = True):

		arrParams = [
			strInfrastructureID,
			strPowerCommand,
			bOnlyPoweredOn,
		]

		return self.rpc("infrastructure_deploy_shutdown_required", arrParams)


	def server_types(self, strDatacenterName = None):

		arrParams = [
			strDatacenterName,
		]

		objServerType = self.rpc("server_types", arrParams)
		for strKeyServerType in objServerType:
			objServerType[strKeyServerType] = Deserializer.deserialize(objServerType[strKeyServerType])
		return objServerType

	def server_type_matches(self, strInfrastructureID, objHardwareConfiguration, strInstanceArrayID = None, bAllowServerSwap = False):

		objHardwareConfiguration = Serializer.serialize(objHardwareConfiguration)

		arrParams = [
			strInfrastructureID,
			objHardwareConfiguration,
			strInstanceArrayID,
			bAllowServerSwap,
		]

		return self.rpc("server_type_matches", arrParams)


	def shared_drive_create(self, strInfrastructureID, objSharedDrive):

		objSharedDrive = Serializer.serialize(objSharedDrive)

		arrParams = [
			strInfrastructureID,
			objSharedDrive,
		]

		return Deserializer.deserialize(self.rpc("shared_drive_create", arrParams))

	def shared_drive_edit(self, strSharedDriveID, objSharedDriveOperation):

		objSharedDriveOperation = Serializer.serialize(objSharedDriveOperation)

		arrParams = [
			strSharedDriveID,
			objSharedDriveOperation,
		]

		return Deserializer.deserialize(self.rpc("shared_drive_edit", arrParams))

	def shared_drive_delete(self, strSharedDriveID):

		arrParams = [
			strSharedDriveID,
		]

		return Deserializer.deserialize(self.rpc("shared_drive_delete", arrParams))

	def shared_drive_stop(self, strSharedDriveID):

		arrParams = [
			strSharedDriveID,
		]

		return Deserializer.deserialize(self.rpc("shared_drive_stop", arrParams))

	def shared_drive_start(self, strSharedDriveID):

		arrParams = [
			strSharedDriveID,
		]

		return Deserializer.deserialize(self.rpc("shared_drive_start", arrParams))

	def shared_drive_instance_arrays(self, strSharedDriveID):

		arrParams = [
			strSharedDriveID,
		]

		return self.rpc("shared_drive_instance_arrays", arrParams)


	def instance_array_shared_drives(self, strInstanceArrayID):

		arrParams = [
			strInstanceArrayID,
		]

		return self.rpc("instance_array_shared_drives", arrParams)


	def shared_drives(self, strInfrastructureID, arrSharedDriveIDs = None):

		arrParams = [
			strInfrastructureID,
			arrSharedDriveIDs,
		]

		objSharedDrive = self.rpc("shared_drives", arrParams)
		for strKeySharedDrive in objSharedDrive:
			objSharedDrive[strKeySharedDrive] = Deserializer.deserialize(objSharedDrive[strKeySharedDrive])
		return objSharedDrive

	def search(self, strUserID, strKeywords, arrTables = None, objTablesColumns = None, strCollapseType = "array_subrows", arrOrderBy = [], arrLimit = None):

		objTablesColumns = Serializer.serialize(objTablesColumns)

		arrParams = [
			strUserID,
			strKeywords,
			arrTables,
			objTablesColumns,
			strCollapseType,
			arrOrderBy,
			arrLimit,
		]

		return self.rpc("search", arrParams)


	def query(self, strUserID, strSQLQuery, strCollapseType = "array_subrows"):

		arrParams = [
			strUserID,
			strSQLQuery,
			strCollapseType,
		]

		return self.rpc("query", arrParams)


	def drive_edit(self, strDriveID, objDriveOperation):

		objDriveOperation = Serializer.serialize(objDriveOperation)

		arrParams = [
			strDriveID,
			objDriveOperation,
		]

		return Deserializer.deserialize(self.rpc("drive_edit", arrParams))

	def drive_delete(self, strDriveID):

		arrParams = [
			strDriveID,
		]

		return Deserializer.deserialize(self.rpc("drive_delete", arrParams))

	def drive_attach_instance(self, strDriveID, strInstanceID):

		arrParams = [
			strDriveID,
			strInstanceID,
		]

		return Deserializer.deserialize(self.rpc("drive_attach_instance", arrParams))

	def drive_detach_instance(self, strDriveID):

		arrParams = [
			strDriveID,
		]

		return Deserializer.deserialize(self.rpc("drive_detach_instance", arrParams))

	def drive_snapshot_create(self, strDriveID):

		arrParams = [
			strDriveID,
		]

		return Deserializer.deserialize(self.rpc("drive_snapshot_create", arrParams))

	def drive_snapshot_rollback(self, strSnapshotID):

		arrParams = [
			strSnapshotID,
		]

		self.rpc("drive_snapshot_rollback", arrParams)


	def drive_snapshot_delete(self, strSnapshotID):

		arrParams = [
			strSnapshotID,
		]

		self.rpc("drive_snapshot_delete", arrParams)


	def drive_snapshots(self, strDriveID, arrSnapshotIDs = None):

		arrParams = [
			strDriveID,
			arrSnapshotIDs,
		]

		objSnapshot = self.rpc("drive_snapshots", arrParams)
		for strKeySnapshot in objSnapshot:
			objSnapshot[strKeySnapshot] = Deserializer.deserialize(objSnapshot[strKeySnapshot])
		return objSnapshot

	def volume_templates_public(self, arrVolumeTemplateIDs = None):

		arrParams = [
			arrVolumeTemplateIDs,
		]

		objVolumeTemplate = self.rpc("volume_templates_public", arrParams)
		for strKeyVolumeTemplate in objVolumeTemplate:
			objVolumeTemplate[strKeyVolumeTemplate] = Deserializer.deserialize(objVolumeTemplate[strKeyVolumeTemplate])
		return objVolumeTemplate

	def drive_array_create(self, strInfrastructureID, objDriveArray):

		objDriveArray = Serializer.serialize(objDriveArray)

		arrParams = [
			strInfrastructureID,
			objDriveArray,
		]

		return Deserializer.deserialize(self.rpc("drive_array_create", arrParams))

	def drive_array_edit(self, strDriveArrayID, objDriveArrayOperation, objDriveArrayEditOptions = {"update_active_drives_size":False}):

		objDriveArrayOperation = Serializer.serialize(objDriveArrayOperation)
		objDriveArrayEditOptions = Serializer.serialize(objDriveArrayEditOptions)

		arrParams = [
			strDriveArrayID,
			objDriveArrayOperation,
			objDriveArrayEditOptions,
		]

		return Deserializer.deserialize(self.rpc("drive_array_edit", arrParams))

	def drive_array_delete(self, strDriveArrayID):

		arrParams = [
			strDriveArrayID,
		]

		return Deserializer.deserialize(self.rpc("drive_array_delete", arrParams))

	def drive_array_stop(self, strDriveArrayID):

		arrParams = [
			strDriveArrayID,
		]

		return Deserializer.deserialize(self.rpc("drive_array_stop", arrParams))

	def drive_array_start(self, strDriveArrayID):

		arrParams = [
			strDriveArrayID,
		]

		return Deserializer.deserialize(self.rpc("drive_array_start", arrParams))

	def drive_array_drives(self, strDriveArrayID, arrDriveIDs = None):

		arrParams = [
			strDriveArrayID,
			arrDriveIDs,
		]

		objDrive = self.rpc("drive_array_drives", arrParams)
		for strKeyDrive in objDrive:
			objDrive[strKeyDrive] = Deserializer.deserialize(objDrive[strKeyDrive])
		return objDrive

	def drive_arrays(self, strInfrastructureID, arrDriveArrayIDs = None):

		arrParams = [
			strInfrastructureID,
			arrDriveArrayIDs,
		]

		objDriveArray = self.rpc("drive_arrays", arrParams)
		for strKeyDriveArray in objDriveArray:
			objDriveArray[strKeyDriveArray] = Deserializer.deserialize(objDriveArray[strKeyDriveArray])
		return objDriveArray

	def user_create(self, strDisplayName, strLoginEmail, strRedirectURL = None, strAESKey = None):

		arrParams = [
			strDisplayName,
			strLoginEmail,
			strRedirectURL,
			strAESKey,
		]

		return Deserializer.deserialize(self.rpc("user_create", arrParams))

	def user_get(self, strUserID):

		arrParams = [
			strUserID,
		]

		return Deserializer.deserialize(self.rpc("user_get", arrParams))

	def infrastructures(self, strUserID, arrInfrastructureIDs = None):

		arrParams = [
			strUserID,
			arrInfrastructureIDs,
		]

		objInfrastructure = self.rpc("infrastructures", arrParams)
		for strKeyInfrastructure in objInfrastructure:
			objInfrastructure[strKeyInfrastructure] = Deserializer.deserialize(objInfrastructure[strKeyInfrastructure])
		return objInfrastructure

	def user_authenticate_password(self, strLoginEmail, strPassword, strOneTimePassword = None, bRememberLogin = False, bTestCredentials = False, bRenewKerberosTicket = False):

		arrParams = [
			strLoginEmail,
			strPassword,
			strOneTimePassword,
			bRememberLogin,
			bTestCredentials,
			bRenewKerberosTicket,
		]

		return self.rpc("user_authenticate_password", arrParams)


	def user_authenticate_api_key(self, strUserID, strAPIKey, strOneTimePassword = None, bRememberLogin = False):

		arrParams = [
			strUserID,
			strAPIKey,
			strOneTimePassword,
			bRememberLogin,
		]

		return Deserializer.deserialize(self.rpc("user_authenticate_api_key", arrParams))

	def user_change_password(self, strUserID, strNewPassword, strOldPassword = None):

		arrParams = [
			strUserID,
			strNewPassword,
			strOldPassword,
		]

		self.rpc("user_change_password", arrParams)


	def user_infrastructure_default_set(self, strUserID, strInfrastructureID):

		arrParams = [
			strUserID,
			strInfrastructureID,
		]

		return self.rpc("user_infrastructure_default_set", arrParams)


	def user_infrastructure_default_unset(self, strUserID):

		arrParams = [
			strUserID,
		]

		self.rpc("user_infrastructure_default_unset", arrParams)


	def user_ssh_key_create(self, strUserID, strSSHKey):

		arrParams = [
			strUserID,
			strSSHKey,
		]

		return Deserializer.deserialize(self.rpc("user_ssh_key_create", arrParams))

	def user_ssh_keys(self, strUserID):

		arrParams = [
			strUserID,
		]

		arrSSHKeys = self.rpc("user_ssh_keys", arrParams)
		for index in range(len(arrSSHKeys)):
			arrSSHKeys[index] = Deserializer.deserialize(arrSSHKeys[index])
		return arrSSHKeys

	def user_ssh_key_delete(self, nSSHKeyID):

		arrParams = [
			nSSHKeyID,
		]

		self.rpc("user_ssh_key_delete", arrParams)


	def user_api_key_regenerate(self, strUserID):

		arrParams = [
			strUserID,
		]

		self.rpc("user_api_key_regenerate", arrParams)


	def user_password_recovery(self, strLoginEmail, strRedirectURL = None, strAESKey = None):

		arrParams = [
			strLoginEmail,
			strRedirectURL,
			strAESKey,
		]

		self.rpc("user_password_recovery", arrParams)


	def user_create_retry_mail(self, strLoginEmail, strRedirectURL = None, strAESKey = None):

		arrParams = [
			strLoginEmail,
			strRedirectURL,
			strAESKey,
		]

		self.rpc("user_create_retry_mail", arrParams)


	def user_update_email(self, strUserID, strNewLoginEmail, strRedirectURL = None, strAESKey = None):

		arrParams = [
			strUserID,
			strNewLoginEmail,
			strRedirectURL,
			strAESKey,
		]

		return self.rpc("user_update_email", arrParams)


	def user_update_language(self, strUserID, strLanguage):

		arrParams = [
			strUserID,
			strLanguage,
		]

		return Deserializer.deserialize(self.rpc("user_update_language", arrParams))

	def user_delegate_add(self, strUserID, strDelegateUserEmail, bCreateUserIfNotExists = False):

		arrParams = [
			strUserID,
			strDelegateUserEmail,
			bCreateUserIfNotExists,
		]

		self.rpc("user_delegate_add", arrParams)


	def user_delegate_remove(self, strUserID, strDelegateUserEmail):

		arrParams = [
			strUserID,
			strDelegateUserEmail,
		]

		self.rpc("user_delegate_remove", arrParams)


	def user_delegate_children(self, strUserID):

		arrParams = [
			strUserID,
		]

		objUser = self.rpc("user_delegate_children", arrParams)
		for strKeyUser in objUser:
			objUser[strKeyUser] = Deserializer.deserialize(objUser[strKeyUser])
		return objUser

	def user_delegate_parents(self, strUserID):

		arrParams = [
			strUserID,
		]

		objUser = self.rpc("user_delegate_parents", arrParams)
		for strKeyUser in objUser:
			objUser[strKeyUser] = Deserializer.deserialize(objUser[strKeyUser])
		return objUser

	def user_cookie_session(self, bFetchUserLoginSessionData = False):

		arrParams = [
			bFetchUserLoginSessionData,
		]

		return Deserializer.deserialize(self.rpc("user_cookie_session", arrParams))

	def user_logout(self):

		arrParams = [
		]

		return self.rpc("user_logout", arrParams)


	def user_gui_settings_save(self, strUserID, objGUIUserSettings, arrPropertyNames):

		objGUIUserSettings = Serializer.serialize(objGUIUserSettings)

		arrParams = [
			strUserID,
			objGUIUserSettings,
			arrPropertyNames,
		]

		self.rpc("user_gui_settings_save", arrParams)


	def throw_error(self, nErrorCode):

		arrParams = [
			nErrorCode,
		]

		self.rpc("throw_error", arrParams)


	def cluster_gui_settings_save(self, strClusterID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strClusterID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("cluster_gui_settings_save", arrParams)


	def event_counters(self, strInfrastructureID):

		arrParams = [
			strInfrastructureID,
		]

		return self.rpc("event_counters", arrParams)


	def infrastructure_get(self, strInfrastructureID):

		arrParams = [
			strInfrastructureID,
		]

		return Deserializer.deserialize(self.rpc("infrastructure_get", arrParams))

	def infrastructure_hang_until_touched(self, nInfrastructureID, strKnownValue):

		arrParams = [
			nInfrastructureID,
			strKnownValue,
		]

		return self.rpc("infrastructure_hang_until_touched", arrParams)


	def instance_interface_ips(self, nInstanceInterfaceID):

		arrParams = [
			nInstanceInterfaceID,
		]

		return self.rpc("instance_interface_ips", arrParams)


	def instance_get(self, strInstanceID):

		arrParams = [
			strInstanceID,
		]

		return Deserializer.deserialize(self.rpc("instance_get", arrParams))

	def instance_array_get(self, strInstanceArrayID):

		arrParams = [
			strInstanceArrayID,
		]

		return Deserializer.deserialize(self.rpc("instance_array_get", arrParams))

	def instance_array_gui_settings_save(self, strInstanceArrayID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strInstanceArrayID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("instance_array_gui_settings_save", arrParams)


	def subnet_get(self, strSubnetID):

		arrParams = [
			strSubnetID,
		]

		return Deserializer.deserialize(self.rpc("subnet_get", arrParams))

	def data_lake_gui_settings_save(self, strDataLakeID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strDataLakeID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("data_lake_gui_settings_save", arrParams)


	def monitoring_instance_measurement_value_get(self, nInstanceMeasurementID):

		arrParams = [
			nInstanceMeasurementID,
		]

		return self.rpc("monitoring_instance_measurement_value_get", arrParams)


	def monitoring_instance_measurements_get_for_instance(self, strInstanceID, bIgnoreVirtualEthernetInterfaces = False):

		arrParams = [
			strInstanceID,
			bIgnoreVirtualEthernetInterfaces,
		]

		return self.rpc("monitoring_instance_measurements_get_for_instance", arrParams)


	def monitoring_instance_measurements_rendering_get(self, strInstanceID, arrMeasurements, objRenderingOptions = [], bEncodeBase64 = True):

		objRenderingOptions = Serializer.serialize(objRenderingOptions)

		arrParams = [
			strInstanceID,
			arrMeasurements,
			objRenderingOptions,
			bEncodeBase64,
		]

		return self.rpc("monitoring_instance_measurements_rendering_get", arrParams)


	def monitoring_instance_interface_measurements_rendering_get(self, nInstanceInterfaceID, arrMeasurements, objRenderingOptions = [], bEncodeBase64 = True):

		objRenderingOptions = Serializer.serialize(objRenderingOptions)

		arrParams = [
			nInstanceInterfaceID,
			arrMeasurements,
			objRenderingOptions,
			bEncodeBase64,
		]

		return self.rpc("monitoring_instance_interface_measurements_rendering_get", arrParams)


	def monitoring_network_measurements_rendering_get(self, strNetworkID, strNetworkTrafficType, arrMeasurements, objRenderingOptions = [], bEncodeBase64 = True):

		objRenderingOptions = Serializer.serialize(objRenderingOptions)

		arrParams = [
			strNetworkID,
			strNetworkTrafficType,
			arrMeasurements,
			objRenderingOptions,
			bEncodeBase64,
		]

		return self.rpc("monitoring_network_measurements_rendering_get", arrParams)


	def network_get(self, strNetworkID):

		arrParams = [
			strNetworkID,
		]

		return Deserializer.deserialize(self.rpc("network_get", arrParams))

	def network_gui_settings_save(self, strNetworkID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strNetworkID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("network_gui_settings_save", arrParams)


	def server_type_get(self, strServerTypeID):

		arrParams = [
			strServerTypeID,
		]

		return Deserializer.deserialize(self.rpc("server_type_get", arrParams))

	def server_type_available_server_count(self, strUserIDOwner, strDatacenterName, strServerTypeID, nMaximumResults):

		arrParams = [
			strUserIDOwner,
			strDatacenterName,
			strServerTypeID,
			nMaximumResults,
		]

		return self.rpc("server_type_available_server_count", arrParams)


	def shared_drive_get(self, strSharedDriveID):

		arrParams = [
			strSharedDriveID,
		]

		return Deserializer.deserialize(self.rpc("shared_drive_get", arrParams))

	def shared_drive_gui_settings_save(self, strSharedDriveID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strSharedDriveID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("shared_drive_gui_settings_save", arrParams)


	def drive_get(self, strDriveID):

		arrParams = [
			strDriveID,
		]

		return Deserializer.deserialize(self.rpc("drive_get", arrParams))

	def drive_array_get(self, strDriveArrayID):

		arrParams = [
			strDriveArrayID,
		]

		return Deserializer.deserialize(self.rpc("drive_array_get", arrParams))

	def drive_array_gui_settings_save(self, strDriveArrayID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strDriveArrayID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("drive_array_gui_settings_save", arrParams)


	def volume_template_get(self, strVolumeTemplateID):

		arrParams = [
			strVolumeTemplateID,
		]

		return Deserializer.deserialize(self.rpc("volume_template_get", arrParams))

	def user_change_password_encrypted(self, strUserID, strAESCipherPassword, strRSACipherAESKey, strOldPassword = None):

		arrParams = [
			strUserID,
			strAESCipherPassword,
			strRSACipherAESKey,
			strOldPassword,
		]

		self.rpc("user_change_password_encrypted", arrParams)


	def user_authenticate_password_encrypted(self, strLoginEmail, strAESCipherPassword, strRSACipherAESKey, strOneTimePassword = None, bRememberLogin = False, bTestCredentials = False, bRenewKerberosTicket = False):

		arrParams = [
			strLoginEmail,
			strAESCipherPassword,
			strRSACipherAESKey,
			strOneTimePassword,
			bRememberLogin,
			bTestCredentials,
			bRenewKerberosTicket,
		]

		return self.rpc("user_authenticate_password_encrypted", arrParams)


	def transport_request_public_key(self, bGenerateNewIfNotFound = True):

		arrParams = [
			bGenerateNewIfNotFound,
		]

		return self.rpc("transport_request_public_key", arrParams)


	def user_email_to_user_id(self, strLoginEmail):

		arrParams = [
			strLoginEmail,
		]

		return self.rpc("user_email_to_user_id", arrParams)


	def instance_drives(self, strInstanceID):

		arrParams = [
			strInstanceID,
		]

		objDrive = self.rpc("instance_drives", arrParams)
		for strKeyDrive in objDrive:
			objDrive[strKeyDrive] = Deserializer.deserialize(objDrive[strKeyDrive])
		return objDrive

	def infrastructure_deploy_blockers(self, strInfrastructureID):

		arrParams = [
			strInfrastructureID,
		]

		arrInfrastructureDeployBlockers = self.rpc("infrastructure_deploy_blockers", arrParams)
		for index in range(len(arrInfrastructureDeployBlockers)):
			arrInfrastructureDeployBlockers[index] = Deserializer.deserialize(arrInfrastructureDeployBlockers[index])
		return arrInfrastructureDeployBlockers

	def cluster_suspend(self, strClusterID):

		arrParams = [
			strClusterID,
		]

		return Deserializer.deserialize(self.rpc("cluster_suspend", arrParams))

	def user_suspend_reasons(self, nUserID):

		arrParams = [
			nUserID,
		]

		arrUserSuspendReasons = self.rpc("user_suspend_reasons", arrParams)
		for index in range(len(arrUserSuspendReasons)):
			arrUserSuspendReasons[index] = Deserializer.deserialize(arrUserSuspendReasons[index])
		return arrUserSuspendReasons

	def volume_templates_private(self, strUserID, arrVolumeTemplateIDs = None):

		arrParams = [
			strUserID,
			arrVolumeTemplateIDs,
		]

		objVolumeTemplate = self.rpc("volume_templates_private", arrParams)
		for strKeyVolumeTemplate in objVolumeTemplate:
			objVolumeTemplate[strKeyVolumeTemplate] = Deserializer.deserialize(objVolumeTemplate[strKeyVolumeTemplate])
		return objVolumeTemplate

	def volume_templates(self, strUserID, arrVolumeTemplateIDs = None):

		arrParams = [
			strUserID,
			arrVolumeTemplateIDs,
		]

		objVolumeTemplate = self.rpc("volume_templates", arrParams)
		for strKeyVolumeTemplate in objVolumeTemplate:
			objVolumeTemplate[strKeyVolumeTemplate] = Deserializer.deserialize(objVolumeTemplate[strKeyVolumeTemplate])
		return objVolumeTemplate

	def container_array_create(self, strInfrastructureID, objContainerArray):

		objContainerArray = Serializer.serialize(objContainerArray)

		arrParams = [
			strInfrastructureID,
			objContainerArray,
		]

		return Deserializer.deserialize(self.rpc("container_array_create", arrParams))

	def container_array_get(self, strContainerArrayID):

		arrParams = [
			strContainerArrayID,
		]

		return Deserializer.deserialize(self.rpc("container_array_get", arrParams))

	def container_array_edit(self, strContainerArrayID, objContainerArrayOperation, bKeepDetachingDrives = None):

		objContainerArrayOperation = Serializer.serialize(objContainerArrayOperation)

		arrParams = [
			strContainerArrayID,
			objContainerArrayOperation,
			bKeepDetachingDrives,
		]

		return Deserializer.deserialize(self.rpc("container_array_edit", arrParams))

	def container_array_delete(self, strContainerArrayID):

		arrParams = [
			strContainerArrayID,
		]

		return Deserializer.deserialize(self.rpc("container_array_delete", arrParams))

	def container_array_stop(self, strContainerArrayID):

		arrParams = [
			strContainerArrayID,
		]

		return Deserializer.deserialize(self.rpc("container_array_stop", arrParams))

	def container_array_start(self, strContainerArrayID):

		arrParams = [
			strContainerArrayID,
		]

		return Deserializer.deserialize(self.rpc("container_array_start", arrParams))

	def container_arrays(self, strInfrastructureID, arrContainerArrayIDs = None):

		arrParams = [
			strInfrastructureID,
			arrContainerArrayIDs,
		]

		objContainerArray = self.rpc("container_arrays", arrParams)
		for strKeyContainerArray in objContainerArray:
			objContainerArray[strKeyContainerArray] = Deserializer.deserialize(objContainerArray[strKeyContainerArray])
		return objContainerArray

	def container_platform_create(self, strInfrastructureID, objContainerPlatform):

		objContainerPlatform = Serializer.serialize(objContainerPlatform)

		arrParams = [
			strInfrastructureID,
			objContainerPlatform,
		]

		return Deserializer.deserialize(self.rpc("container_platform_create", arrParams))

	def container_platform_get(self, strContainerPlatformID):

		arrParams = [
			strContainerPlatformID,
		]

		return Deserializer.deserialize(self.rpc("container_platform_get", arrParams))

	def container_platform_edit(self, strContainerPlatformID, objContainerPlatformOperation, objServerTypeMatches = None):

		objContainerPlatformOperation = Serializer.serialize(objContainerPlatformOperation)
		objServerTypeMatches = Serializer.serialize(objServerTypeMatches)

		arrParams = [
			strContainerPlatformID,
			objContainerPlatformOperation,
			objServerTypeMatches,
		]

		return Deserializer.deserialize(self.rpc("container_platform_edit", arrParams))

	def container_platform_stop(self, strContainerPlatformID):

		arrParams = [
			strContainerPlatformID,
		]

		return Deserializer.deserialize(self.rpc("container_platform_stop", arrParams))

	def container_platform_start(self, strContainerPlatformID):

		arrParams = [
			strContainerPlatformID,
		]

		return Deserializer.deserialize(self.rpc("container_platform_start", arrParams))

	def container_platform_delete(self, strContainerPlatformID):

		arrParams = [
			strContainerPlatformID,
		]

		return Deserializer.deserialize(self.rpc("container_platform_delete", arrParams))

	def container_platforms(self, strInfrastructureID, arrContainerPlatformIDs = None):

		arrParams = [
			strInfrastructureID,
			arrContainerPlatformIDs,
		]

		objContainerPlatform = self.rpc("container_platforms", arrParams)
		for strKeyContainerPlatform in objContainerPlatform:
			objContainerPlatform[strKeyContainerPlatform] = Deserializer.deserialize(objContainerPlatform[strKeyContainerPlatform])
		return objContainerPlatform

	def container_platform_suspend(self, strContainerPlatformID):

		arrParams = [
			strContainerPlatformID,
		]

		return Deserializer.deserialize(self.rpc("container_platform_suspend", arrParams))

	def container_array_gui_settings_save(self, strContainerArrayID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strContainerArrayID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("container_array_gui_settings_save", arrParams)


	def container_platform_gui_settings_save(self, strContainerPlatformID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strContainerPlatformID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("container_platform_gui_settings_save", arrParams)


	def container_platform_container_arrays(self, strContainerPlatformID, arrContainerArrayIDs = None):

		arrParams = [
			strContainerPlatformID,
			arrContainerArrayIDs,
		]

		objContainerArray = self.rpc("container_platform_container_arrays", arrParams)
		for strKeyContainerArray in objContainerArray:
			objContainerArray[strKeyContainerArray] = Deserializer.deserialize(objContainerArray[strKeyContainerArray])
		return objContainerArray

	def container_array_containers(self, strContainerArrayID):

		arrParams = [
			strContainerArrayID,
		]

		objContainer = self.rpc("container_array_containers", arrParams)
		for strKeyContainer in objContainer:
			objContainer[strKeyContainer] = Deserializer.deserialize(objContainer[strKeyContainer])
		return objContainer

	def cluster_password_change(self, strClusterID, strNewPassword):

		arrParams = [
			strClusterID,
			strNewPassword,
		]

		self.rpc("cluster_password_change", arrParams)


	def cluster_public_key_get(self, strClusterID):

		arrParams = [
			strClusterID,
		]

		return self.rpc("cluster_public_key_get", arrParams)


	def drive_snapshot_get(self, strSnapshotID):

		arrParams = [
			strSnapshotID,
		]

		return Deserializer.deserialize(self.rpc("drive_snapshot_get", arrParams))

	def instance_public_key_get(self, strInstanceID):

		arrParams = [
			strInstanceID,
		]

		return self.rpc("instance_public_key_get", arrParams)


	def client_ip(self):

		arrParams = [
		]

		return self.rpc("client_ip", arrParams)


	def query_parse(self, strSQL):

		arrParams = [
			strSQL,
		]

		return self.rpc("query_parse", arrParams)


	def query_structured(self, strUserID, strTableName, objQueryConditions, strCollapseType = "array_subrows"):

		objQueryConditions = Serializer.serialize(objQueryConditions)

		arrParams = [
			strUserID,
			strTableName,
			objQueryConditions,
			strCollapseType,
		]

		return self.rpc("query_structured", arrParams)


	def resource_utilization_summary_start_timestamp_default(self, strUserID):

		arrParams = [
			strUserID,
		]

		return self.rpc("resource_utilization_summary_start_timestamp_default", arrParams)


	def cluster_automatic_management_status_set(self, strClusterID, bStatus):

		arrParams = [
			strClusterID,
			bStatus,
		]

		self.rpc("cluster_automatic_management_status_set", arrParams)


	def infrastructure_design_lock_set(self, strInfrastructureID, bLockStatus):

		arrParams = [
			strInfrastructureID,
			bLockStatus,
		]

		self.rpc("infrastructure_design_lock_set", arrParams)


	def instance_server_type_reservation_create(self, strInstanceID, bRecurring, nReservationCycleMonths, nInstallmentCycleMonths):

		arrParams = [
			strInstanceID,
			bRecurring,
			nReservationCycleMonths,
			nInstallmentCycleMonths,
		]

		return Deserializer.deserialize(self.rpc("instance_server_type_reservation_create", arrParams))

	def prices(self):

		arrParams = [
		]

		return self.rpc("prices", arrParams)


	def server_types_match_hardware_configuration(self, strDatacenterName, objHardwareConfiguration):

		objHardwareConfiguration = Serializer.serialize(objHardwareConfiguration)

		arrParams = [
			strDatacenterName,
			objHardwareConfiguration,
		]

		objServerType = self.rpc("server_types_match_hardware_configuration", arrParams)
		for strKeyServerType in objServerType:
			objServerType[strKeyServerType] = Deserializer.deserialize(objServerType[strKeyServerType])
		return objServerType

	def infrastructure_public_designs(self):

		arrParams = [
		]

		return self.rpc("infrastructure_public_designs", arrParams)


	def server_type_available_server_count_batch(self, strUserIDOwner, strDatacenterName, arrServerTypeIDs, nMaximumResults, bIncludeReservedForUser = False, nInstanceArrayID = None):

		arrParams = [
			strUserIDOwner,
			strDatacenterName,
			arrServerTypeIDs,
			nMaximumResults,
			bIncludeReservedForUser,
			nInstanceArrayID,
		]

		return self.rpc("server_type_available_server_count_batch", arrParams)


	def user_server_type_reservations_unused(self, strUserID, strDatacenterName):

		arrParams = [
			strUserID,
			strDatacenterName,
		]

		return self.rpc("user_server_type_reservations_unused", arrParams)


	def shared_drive_container_arrays(self, strSharedDriveID):

		arrParams = [
			strSharedDriveID,
		]

		return self.rpc("shared_drive_container_arrays", arrParams)


	def user_franchise_get(self, strUserID):

		arrParams = [
			strUserID,
		]

		return self.rpc("user_franchise_get", arrParams)


	def subnet_create_from_owned_subnet_pool(self, strNetworkID, objSubnet):

		objSubnet = Serializer.serialize(objSubnet)

		arrParams = [
			strNetworkID,
			objSubnet,
		]

		return self.rpc("subnet_create_from_owned_subnet_pool", arrParams)


	def user_authenticator_has(self, strUserID):

		arrParams = [
			strUserID,
		]

		return self.rpc("user_authenticator_has", arrParams)


	def server_types_datacenter(self, strDatacenterName):

		arrParams = [
			strDatacenterName,
		]

		return self.rpc("server_types_datacenter", arrParams)


	def prices_history(self, bExcludeFuturePrices = False, bOnlyActivePrices = False):

		arrParams = [
			bExcludeFuturePrices,
			bOnlyActivePrices,
		]

		return self.rpc("prices_history", arrParams)


	def container_cluster_create(self, strInfrastructureID, objContainerCluster):

		objContainerCluster = Serializer.serialize(objContainerCluster)

		arrParams = [
			strInfrastructureID,
			objContainerCluster,
		]

		return Deserializer.deserialize(self.rpc("container_cluster_create", arrParams))

	def container_cluster_get(self, strContainerClusterID, bAccessSaaSAPI = True, nAccessSaaSAPITimeoutSeconds = 10):

		arrParams = [
			strContainerClusterID,
			bAccessSaaSAPI,
			nAccessSaaSAPITimeoutSeconds,
		]

		return Deserializer.deserialize(self.rpc("container_cluster_get", arrParams))

	def container_cluster_edit(self, strContainerClusterID, objContainerClusterOperation):

		objContainerClusterOperation = Serializer.serialize(objContainerClusterOperation)

		arrParams = [
			strContainerClusterID,
			objContainerClusterOperation,
		]

		return Deserializer.deserialize(self.rpc("container_cluster_edit", arrParams))

	def container_cluster_stop(self, strContainerClusterID):

		arrParams = [
			strContainerClusterID,
		]

		return Deserializer.deserialize(self.rpc("container_cluster_stop", arrParams))

	def container_cluster_start(self, strContainerClusterID):

		arrParams = [
			strContainerClusterID,
		]

		return Deserializer.deserialize(self.rpc("container_cluster_start", arrParams))

	def container_cluster_delete(self, strContainerClusterID):

		arrParams = [
			strContainerClusterID,
		]

		return Deserializer.deserialize(self.rpc("container_cluster_delete", arrParams))

	def container_clusters(self, strInfrastructureID, arrContainerClusterIDs = None):

		arrParams = [
			strInfrastructureID,
			arrContainerClusterIDs,
		]

		objContainerCluster = self.rpc("container_clusters", arrParams)
		for strKeyContainerCluster in objContainerCluster:
			objContainerCluster[strKeyContainerCluster] = Deserializer.deserialize(objContainerCluster[strKeyContainerCluster])
		return objContainerCluster

	def container_cluster_suspend(self, strContainerClusterID):

		arrParams = [
			strContainerClusterID,
		]

		return Deserializer.deserialize(self.rpc("container_cluster_suspend", arrParams))

	def container_cluster_automatic_management_status_set(self, strContainerClusterID, bStatus):

		arrParams = [
			strContainerClusterID,
			bStatus,
		]

		self.rpc("container_cluster_automatic_management_status_set", arrParams)


	def container_cluster_gui_settings_save(self, strContainerClusterID, objGUIProductSettings, arrPropertyNames):

		objGUIProductSettings = Serializer.serialize(objGUIProductSettings)

		arrParams = [
			strContainerClusterID,
			objGUIProductSettings,
			arrPropertyNames,
		]

		self.rpc("container_cluster_gui_settings_save", arrParams)


	def user_prices_history(self, strUserID, bExcludeFuturePrices = False, bOnlyActivePrices = False, bExpandWithPrivateDatacenters = True):

		arrParams = [
			strUserID,
			bExcludeFuturePrices,
			bOnlyActivePrices,
			bExpandWithPrivateDatacenters,
		]

		return self.rpc("user_prices_history", arrParams)


	def user_prices(self, strUserID):

		arrParams = [
			strUserID,
		]

		return self.rpc("user_prices", arrParams)


	def fs_create(self, strFSURL, strType, strPermission = None):

		arrParams = [
			strFSURL,
			strType,
			strPermission,
		]

		self.rpc("fs_create", arrParams)


	def fs_delete(self, strFSURL, bRecursive = False):

		arrParams = [
			strFSURL,
			bRecursive,
		]

		self.rpc("fs_delete", arrParams)


	def fs_info(self, strFSURL):

		arrParams = [
			strFSURL,
		]

		self.rpc("fs_info", arrParams)


	def fs_list(self, strFSURL):

		arrParams = [
			strFSURL,
		]

		self.rpc("fs_list", arrParams)


	def fs_move(self, strFSURL, strPathNew):

		arrParams = [
			strFSURL,
			strPathNew,
		]

		self.rpc("fs_move", arrParams)


	def fs_owner_set(self, strFSURL, strOwner):

		arrParams = [
			strFSURL,
			strOwner,
		]

		self.rpc("fs_owner_set", arrParams)


	def fs_read(self, strFSURL, strEncoding, nOffset, nLength):

		arrParams = [
			strFSURL,
			strEncoding,
			nOffset,
			nLength,
		]

		self.rpc("fs_read", arrParams)


	def fs_rename(self, strFSURL, strFilenameNew):

		arrParams = [
			strFSURL,
			strFilenameNew,
		]

		self.rpc("fs_rename", arrParams)


	def fs_truncate(self, strFSURL, nLengthNew = 0):

		arrParams = [
			strFSURL,
			nLengthNew,
		]

		self.rpc("fs_truncate", arrParams)


	def fs_write(self, strFSURL, strContents, strEncoding, nOffset = None, bTruncate = True):

		arrParams = [
			strFSURL,
			strContents,
			strEncoding,
			nOffset,
			bTruncate,
		]

		self.rpc("fs_write", arrParams)


	def fs_download_url(self, strFSURL):

		arrParams = [
			strFSURL,
		]

		self.rpc("fs_download_url", arrParams)


	def fs_upload_url(self, strFSURL):

		arrParams = [
			strFSURL,
		]

		return self.rpc("fs_upload_url", arrParams)


	def user_limits(self, strUserID):

		arrParams = [
			strUserID,
		]

		return Deserializer.deserialize(self.rpc("user_limits", arrParams))

	def instance_monitoring_data_get(self, nInstanceID, nGranularityMinutes = 1, strTimestampStart = None, strTimestampEnd = None):

		arrParams = [
			nInstanceID,
			nGranularityMinutes,
			strTimestampStart,
			strTimestampEnd,
		]

		return self.rpc("instance_monitoring_data_get", arrParams)


	def instance_array_monitoring_data_get(self, nInstanceArrayID, nGranularityMinutes = 1, strTimestampStart = None, strTimestampEnd = None):

		arrParams = [
			nInstanceArrayID,
			nGranularityMinutes,
			strTimestampStart,
			strTimestampEnd,
		]

		return self.rpc("instance_array_monitoring_data_get", arrParams)


	def container_platform_monitoring_data_get(self, nContainerPlatformID, nGranularityMinutes = 1, strTimestampStart = None, strTimestampEnd = None):

		arrParams = [
			nContainerPlatformID,
			nGranularityMinutes,
			strTimestampStart,
			strTimestampEnd,
		]

		return self.rpc("container_platform_monitoring_data_get", arrParams)


	def license_type_for_volume_template(self, strVolumeTemplateID):

		arrParams = [
			strVolumeTemplateID,
		]

		return self.rpc("license_type_for_volume_template", arrParams)


	def data_lake_core_site_conf_download_url(self, strUserID, nDataLakeID):

		arrParams = [
			strUserID,
			nDataLakeID,
		]

		return self.rpc("data_lake_core_site_conf_download_url", arrParams)


	def secure_gateway_authorize_resource(self, strResourceUrl):

		arrParams = [
			strResourceUrl,
		]

		self.rpc("secure_gateway_authorize_resource", arrParams)


	def container_get(self, strContainerID):

		arrParams = [
			strContainerID,
		]

		return Deserializer.deserialize(self.rpc("container_get", arrParams))

	def containers(self, strInfrastructureID):

		arrParams = [
			strInfrastructureID,
		]

		objContainer = self.rpc("containers", arrParams)
		for strKeyContainer in objContainer:
			objContainer[strKeyContainer] = Deserializer.deserialize(objContainer[strKeyContainer])
		return objContainer

	def container_logs(self, strContainerID, strSinceTimestamp = None, nLimitBytes = None):

		arrParams = [
			strContainerID,
			strSinceTimestamp,
			nLimitBytes,
		]

		return self.rpc("container_logs", arrParams)


	def container_drives(self, strContainerID):

		arrParams = [
			strContainerID,
		]

		objDrive = self.rpc("container_drives", arrParams)
		for strKeyDrive in objDrive:
			objDrive[strKeyDrive] = Deserializer.deserialize(objDrive[strKeyDrive])
		return objDrive

	def container_array_shared_drives(self, strContainerArrayID):

		arrParams = [
			strContainerArrayID,
		]

		return self.rpc("container_array_shared_drives", arrParams)


	def cluster_app(self, strClusterID, bAccessSaaSAPI = True, nAccessSaaSAPITimeoutSeconds = 10):

		arrParams = [
			strClusterID,
			bAccessSaaSAPI,
			nAccessSaaSAPITimeoutSeconds,
		]

		return Deserializer.deserialize(self.rpc("cluster_app", arrParams))

	def container_array_drive_arrays(self, strContainerArrayID):

		arrParams = [
			strContainerArrayID,
		]

		return self.rpc("container_array_drive_arrays", arrParams)


	def container_cluster_app(self, strContainerClusterID, bAccessSaaSAPI = True, nAccessSaaSAPITimeoutSeconds = 10):

		arrParams = [
			strContainerClusterID,
			bAccessSaaSAPI,
			nAccessSaaSAPITimeoutSeconds,
		]

		return Deserializer.deserialize(self.rpc("container_cluster_app", arrParams))
