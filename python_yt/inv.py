# (C) Copyright 2023 Hewlett Packard Enterprise Development LP
import asyncio
import time
from datetime import datetime, timezone
from typing import cast
from enigma.application_services.job_context import JobContext
from enigma.application_services.job_definitions import (
    common_utils,
    inventory_utils,
    ov_common_utils,
    ov_request_utils,
    storage_configuration_utils,
)
from enigma.application_services.job_exceptions import (
    JobErrorException,
    JobException,
    JobRetryException,
    JobRetryWithContinueException,
    JobRetryWithErrorException,
    JobRetryWithStallException,
)
from enigma.application_services.job_node import JobNode
from enigma.application_services.job_polling_step import JobPollingStep
from enigma.application_services.job_step import JobStep
from enigma.application_services.job_tree import JobTree
from enigma.application_services.jobs.request_message import RequestMessage
from enigma.core.config import RAS_REQUESTS_TOPIC
from enigma.core.constants import (
    APPLIANCE_URI,
    BODY,
    CHASSIS,
    CHASSIS_INVENTORY,
    COBALT_FETCH_TIME,
    COLLECTED,
    COLLECTED_STALE,
    COLLECTION_STATE,
    COLLECTION_STATE_CAMELCASE,
    CURRENT_STEP,
    DATA_KEY,
    DEFAULT_FORM_FACTOR,
    DEFAULT_RESOURCE_TAGS,
    DESCRIPTION,
    DEVICE_CONTEXT,
    DEVICE_ID,
    DEVICE_INVENTORY,
    ERROR_MESSAGE,
    EXPAND_ALL_PREFIX,
    FILTER_RESOURCE_NAME,
    FIRMWARE_INVENTORY,
    FORM_FACTOR,
    FW_INVENTORY,
    HPE,
    INITIAL_POWER_STATE,
    INVENTORY,
    INVENTORY_CATEGORY,
    IS_ACTIVITY_MESSAGE_NEEDED,
    IS_ONEVIEW_SERVER,
    IS_REPORTS_CALL,
    LAST_COLLECTED_POWER_STATE,
    LAST_COLLECTION_TIME,
    LOCAL_STORAGE_TEMPORARY,
    LOCAL_STORAGE_V2_TEMPORARY,
    MEMORY_INVENTORY,
    MESSAGE,
    MESSAGES,
    NAME,
    NETWORK_INVENTORY,
    NOT_APPLICABLE,
    OEM,
    OV_DEVICES,
    OV_FIRMWARE_INVENTORY,
    OV_LOCAL_STORAGE,
    OV_LOCAL_STORAGE_V2,
    OV_MEMORY,
    OV_NETWORK_ADAPTERS,
    OV_POWER_SUPPLIES,
    OV_PROCESSORS,
    OV_SERVER_HARDWARE_REQUEST_URI_PREFIX,
    OV_SERVER_HARDWARE_TYPE,
    OV_SOFTWARE_INVENTORY,
    OV_THERMAL,
    PAYLOAD,
    PCI_DEVICES,
    POWER_ON_REQUEST,
    POWER_STATE_DURING_INV_COLLECTION,
    POWER_SUPPLY_INVENTORY,
    PROCESS_RESPONSE_START_TIME,
    PROCESSOR_INVENTORY,
    PRODUCT_ID,
    RAS_DEVICES,
    RAS_FIRMWARE_INVENTORY,
    RAS_LOCAL_STORAGE,
    RAS_LOCAL_STORAGE_V2,
    RAS_MEMORY,
    RAS_NETWORK_ADAPTERS,
    RAS_POWER_SUPPLIES,
    RAS_PROCESSOR,
    RAS_SOFTWARE_INVENTORY,
    RAS_THERMAL,
    REDFISH_RESOURCES,
    REPORT_ID,
    SERIAL,
    SERVER_UUID,
    SMART_STORAGE_INVENTORY,
    SOFTWARE_INVENTORY,
    START_TIME,
    STATUS_LOWERCASE,
    STORAGE_INVENTORY,
    SUBRESOURCES,
    SUBRESOURCES_COUNT,
    SUCCESS,
    SUCCESS_CACHED,
    SW_INVENTORY,
    TASK_CRITICAL,
    TASK_EXCEPTION,
    TASK_MONITOR,
    TASK_STATE,
    TASK_STATUS,
    THERMAL_INVENTORY,
    VAR_ADAPTERS,
    VAR_CHASSIS,
    VAR_FIRMWARE,
    VAR_LOCAL_STORAGE,
    VAR_LOCAL_STORAGE_V2,
    VAR_MEMORY,
    VAR_PCI_DEVICES,
    VAR_POWER_SUPPLIES,
    VAR_PROCESSOR,
    VAR_SOFTWARE,
    VAR_THERMAL,
    VERSION,
)
from enigma.core.exceptions import DependentResourceNotFoundException
from enigma.core.feature_flags import FeatureFlags
from enigma.core.http_error_enum import ErrorEnum
from enigma.core.interfaces.ilo_resource_api import IloResourceApi
from enigma.core.interfaces.job_messaging_client import JobMessagingClient
from enigma.core.interfaces.jobs_resource_api import JobResourceApi
from enigma.core.interfaces.reports_client import ReportsClient
from enigma.core.models.server import (
    FirmwareInventoryItem,
    Inventory,
    NewInventory,
    PowerState,
    RawInventory,
    Server,
    SoftwareInventoryItem,
)
class Helper:
    @staticmethod
    def is_last_jobstep_failed(context: JobContext):
        return (
            "FAILURE_REASON" in context.results
            and context.results["FAILURE_REASON"]
            and ERROR_MESSAGE in context.data
            and context.data[ERROR_MESSAGE]
        )
    @staticmethod
    def is_last_jobstep_success(context: JobContext):
        return not Helper.is_last_jobstep_failed(context)
    @staticmethod
    def is_oneview_server(context: JobContext):
        return (
            IS_ONEVIEW_SERVER in context.data
            and context.data.get(IS_ONEVIEW_SERVER) is True
        )
    @staticmethod
    def is_oneview_server_and_jobstep_success(context: JobContext):
        return Helper.is_last_jobstep_success(context) and Helper.is_oneview_server(
            context
        )
    @staticmethod
    def is_not_oneview_server(context: JobContext):
        return (
            IS_ONEVIEW_SERVER in context.data
            and context.data.get(IS_ONEVIEW_SERVER) is False
        )
    @staticmethod
    def is_not_oneview_server_and_jobstep_success(context: JobContext):
        return Helper.is_last_jobstep_success(context) and Helper.is_not_oneview_server(
            context
        )
# This jobstep will do validate the provided data payload
class ValidatePayload(JobStep):
    def __init__(
        self,
    ):
        super().__init__()
    async def logic(self, context: JobContext):
        self.logger.info(
            "Validating the input parameters for server %s with job %s",
            context.associated_resource_uri,
            context.job_id,
        )
        is_reports_call = context.data.get(IS_REPORTS_CALL)
        # If the LD is enabled, then we need to check if the is_activity_message_needed is provided
        # in the request. Only if the request specifically asks to create the activity, we will create
        # the activity. Else, by default, we will not create it.
        context.results[IS_ACTIVITY_MESSAGE_NEEDED] = (
            FeatureFlags.T_20240314_28296_RESTRICT_INVENTORY_ACTIVITY_CREATION_BOOL()
            and IS_ACTIVITY_MESSAGE_NEEDED in context.data
            and context.data.get(IS_ACTIVITY_MESSAGE_NEEDED) is True
        )
        # is_reports_call is not mandatory. But, if it is provided in the request,
        # validate if it has a valid boolean value.
        if is_reports_call is not None and not isinstance(is_reports_call, bool):
            raise JobException("is_reports_call is provided with a non-boolean value.")
        filters = context.data.get(FILTER_RESOURCE_NAME)
        invalid_filters = self.find_invalid_filters(filters)
        self.logger.info(
            "filters : %s, Invalid filters (if any) : %s", filters, invalid_filters
        )
        # filters array is also not mandatory. But if it is provided, and if the correspnding
        # LD is enabled, then we need to complain if the invalid filters are provided. If LD
        # is disabled, "filters" arrays is not considered anywhere. Entire list of subresources
        # defined in DEFAULT_RESOURCE_TAGS will be considered.
        if FeatureFlags.T_20230927_17800_FILTERED_INVENTORY() and invalid_filters:
            raise JobException(
                f"Few of the filters provided are invalid. Invalid filters : {invalid_filters} . Valid filters are : {DEFAULT_RESOURCE_TAGS}"
            )
    # All filter attributes which are NOT in DEFAULT_RESOURCE_TAGS will be invalid ones. We
    # only support filter attributes defined in DEFAULT_RESOURCE_TAGS
    def find_invalid_filters(self, filters):
        invalid_filters = []
        if filters:
            invalid_filters = list(set(filters).difference(DEFAULT_RESOURCE_TAGS))
        return invalid_filters
# This JobStep will fetch the server details from Devices table of Cobalt.
# We first fetch the row for this server from Devices table to check if the
# server is a DirectConnect server or OneView connected server based on the
# availability of appliance_uri attribute.
class GetServerFromCobalt(JobStep):
    def __init__(
        self,
        ilo_resource_api: IloResourceApi,
    ):
        super().__init__()
        self.ilo_resource_api = ilo_resource_api
    async def logic(self, context: JobContext):
        context.data[CURRENT_STEP] = 1
        start_time = time.time()
        self.logger.info(
            "Getting server data from Cobalt for server %s with job %s",
            context.associated_resource_uri,
            context.job_id,
        )
        # Fetch the data for the ID from the devices table and check if this has
        # an appliance_uri. If yes, that means its an OneView server, else, Direct
        # Connect server.
        ilo = await self.ilo_resource_api.get_ilo(
            cast(Server, context.associated_resource).id
        )
        if ilo is None:
            raise DependentResourceNotFoundException(
                f"No iLO found with ID: {context.associated_resource_uri}",
                ErrorEnum.HPE_GL_COMPUTE_OPS_0300131,
            )
        isOneViewServer = True if ilo.oneview and ilo.oneview.appliance_uri else False
        # Store necessary details in the context. These are needed in further steps
        # to determine the course of action.
        context.data[IS_ONEVIEW_SERVER] = isOneViewServer
        if ilo.hardware is None:
            context.results["FAILURE_REASON"] = "NO_ASSOCIATED_HARDWARE"
            raise JobErrorException("ilo.hardware is None")
        context.data[SERVER_UUID] = ilo.hardware.uuid
        context.data[INITIAL_POWER_STATE] = ilo.hardware.power_state
        context.data[POWER_STATE_DURING_INV_COLLECTION] = ilo.hardware.power_state
        # If this is a OneView server, then we will store the appliance_uri additionally
        # in the job context.
        if isOneViewServer and ilo.oneview:
            context.data[APPLIANCE_URI] = ilo.oneview.appliance_uri
        context.data[COBALT_FETCH_TIME] = time.time() - start_time
        self.logger.info(
            "Set the boolean for isOneViewServer in context. isOneViewServer : %s, server : %s. GetServerFromCobalt completed in : %s seconds",
            isOneViewServer,
            context.associated_resource_uri,
            context.data[COBALT_FETCH_TIME],
        )
class PowerOnServerIfNeeded(JobPollingStep):
    def __init__(
        self,
        job_messaging_client: JobMessagingClient,
        job_resource_api: JobResourceApi,
        ilo_resource_api: IloResourceApi,
    ):
        super().__init__()
        self.job_messaging_client = job_messaging_client
        self.job_resource_api = job_resource_api
        self.RETRIES = 10
        self.ilo_resource_api = ilo_resource_api
        self.logger.debug("Starting job step : PowerOnServerIfNeeded")
    async def logic(self, context: JobContext):
        if inventory_utils.is_power_on_needed_during_inventory(context):
            context.status = "Powering on and waiting for discovery to complete"
            context.data[CURRENT_STEP] += 1
            # PLEASE dont change the text "Starting full inventory collection" in below log. This is used for inventory dashboard
            self.logger.info(
                "Starting powering ON for server %s with job %s via RAS",
                context.associated_resource_uri,
                context.job_id,
            )
            self.logger.info("Power On Request : %s", POWER_ON_REQUEST)
            await self.job_messaging_client.add_request_message_to_job_context(
                context, RequestMessage(RAS_REQUESTS_TOPIC, POWER_ON_REQUEST)
            )
            await common_utils.post_job_in_progress_message(
                context,
                self.job_messaging_client,
                "POWER_ON_MESSAGE",
                None,
                inventory_utils.get_results_data_for_inventory(context),
            )
            self.logger.info(
                "Submitted the Power ON request to RAS for the server %s with job : %s",
                context.associated_resource_uri,
                context.job_id,
            )
        else:
            self.logger.info(
                "One of the conditions is not matching. So not trying to power on the server : %s as part of the inventory",
                context.associated_resource_uri,
            )
    async def process_response(self, context: JobContext):
        self.logger.info(
            "In PowerOnServerIfNeeded.process_response for server : %s. isOneViewServer : %s. with job : %s.",
            context.associated_resource_uri,
            context.data[IS_ONEVIEW_SERVER],
            context.job_id,
        )
        # Ignore any message which is not a RAS returned one. All RAS returned response
        # will have taskStatus in its message body. So to avoid unnecessary processing,
        # we are ignoring the message amd initiate the retry immediately. Also, we will not
        # update the retry count in such cases because, here we really didnt do any try to
        # process the response.
        # Ideally, we should not end up with this condition, but if there are any issue with
        # the requestId, we may start processing the responses in which case, we dont want
        # to process such responses which are not returned by RAS.
        if (
            not context.response_data.data
            or TASK_STATUS not in context.response_data.data
        ):
            self.logger.info(
                "Not a RAS response. Hence ignoring. context.step_retries = %s, server : %s",
                context.step_retries,
                context.associated_resource_uri,
            )
            raise JobRetryWithStallException()
        task_state = context.response_data.data[TASK_STATE]
        task_status = context.response_data.data[TASK_STATUS]
        ras_task = context.response_data.data[TASK_MONITOR]
        context.data[TASK_MONITOR] = ras_task
        response_status = await common_utils.get_response_status_from_ras_message(
            context.response_data
        )
        self.logger.info(
            "RAS PowerON Task = %s, TaskStatus = %s, TaskState = %s, status : %s for the server : %s",
            ras_task,
            task_status,
            task_state,
            response_status,
            context.associated_resource_uri,
        )
        if task_state == "Running":
            self.logger.debug(
                "Power on and wait for discovery is still running on the server : %s",
                context.associated_resource_uri,
            )
            raise JobRetryWithContinueException()
        else:
            if response_status == 200:
                message = context.response_data
                # Adding some basic validations for the returned data
                if (
                    not message
                    or not message.data
                    or not message.data.get(PAYLOAD)
                    or not message.data.get(PAYLOAD).get(BODY)
                    or not message.data.get(PAYLOAD).get(BODY).get(REDFISH_RESOURCES)
                ):
                    self.logger.error(
                        "Recieved data from PowerOn task is incomplete. Hence marking the inventory job as error for the server : %s. RAS response : %s",
                        context.associated_resource_uri,
                        message,
                    )
                    error_msg = "Marking the inventory job as error. Recieved RAS Kafka message is either empty or have no data."
                    context.results["FAILURE_REASON"] = "EMPTY_RESPONSE"
                    context.data[ERROR_MESSAGE] = error_msg
                    return
                self.logger.info(
                    "Power on and wait for discovery completed on the server : %s",
                    context.associated_resource_uri,
                )
                context.data[POWER_STATE_DURING_INV_COLLECTION] = PowerState.On
            else:
                # If retries are exhausted, or if the inventory task was a failure, then we dont want to update the
                # inventory, but we will mark the job as failure. We wont even persist the partial inventory
                if task_status == TASK_CRITICAL or task_state == TASK_EXCEPTION:
                    error_msg = f"Marking the inventory job as error for job:{context.job_id}. An unexpected or failed response was received during get server inventory. Response status: {response_status}"
                    context.results["FAILURE_REASON"] = "INTERNAL_ERROR"
                    context.data[ERROR_MESSAGE] = error_msg
                    context.data[
                        common_utils.STATE_REASON_MESSAGE
                    ] = await common_utils.get_job_state_reason_message(
                        "INV_COLLECTION_POWER_ON_FAILED"
                    context.data[common_utils.STATE_REASON_MESSAGE] = (
                        await common_utils.get_job_state_reason_message(
                            "INV_COLLECTION_POWER_ON_FAILED"
                        )
                    )
                elif context.step_retries >= self.RETRIES:
                    error_msg = f"Marking the inventory job as error for job :{context.job_id}  because it timed out waiting for RAS PowerOn task {context.data[TASK_MONITOR]} to complete."
                    context.results["FAILURE_REASON"] = "RETRIES_EXHAUSTED"
                    context.data[ERROR_MESSAGE] = error_msg
                    context.data[
                        common_utils.STATE_REASON_MESSAGE
                    ] = await common_utils.get_job_state_reason_message(
                        "INV_COLLECTION_POWER_ON_RETRIES_EXHAUSTED"
                    context.data[common_utils.STATE_REASON_MESSAGE] = (
                        await common_utils.get_job_state_reason_message(
                            "INV_COLLECTION_POWER_ON_RETRIES_EXHAUSTED"
                        )
                    )
                    raise JobRetryWithContinueException(error_msg)
                else:
                    # If taskStatus or taskState are not failed terminal, then we dont mark the job as error,
                    # but we simply wait for next message processing.
                    context.data[
                        common_utils.STATE_REASON_MESSAGE
                    ] = await common_utils.get_job_state_reason_message(
                        "INV_COLLECTION_POWER_ON_FAILED"
                    context.data[common_utils.STATE_REASON_MESSAGE] = (
                        await common_utils.get_job_state_reason_message(
                            "INV_COLLECTION_POWER_ON_FAILED"
                        )
                    )
                    raise JobRetryWithContinueException()

    async def retry(self, context: JobContext):
        # We dont want to retry the power ON logic. We just need to retry fetching
        # the response from the next incoming message.
        self.logger.debug(
            "PowerOnServerIfNeeded: context.step_retries count : %s, self.RETRIES : %s, server : %s",
            context.step_retries,
            self.RETRIES,
            context.associated_resource_uri,
        )
        # If there are any other error already, dont retry the logic.
        if Helper.is_last_jobstep_failed(context):
            context.step_retries = self.RETRIES
        if context.step_retries >= self.RETRIES:
            # If there are other errors already, dont overwrite the error.
            # Add error_message and failure_reason only if last step was success.
            if Helper.is_last_jobstep_success(context):
                error_msg = (
                    f"Unable to power on server after {context.step_retries} attempts."
                )
                context.results["FAILURE_REASON"] = "RETRIES_EXHAUSTED"
                context.data[ERROR_MESSAGE] = error_msg
            context.data[
                common_utils.STATE_REASON_MESSAGE
            ] = await common_utils.get_job_state_reason_message(
                "INV_COLLECTION_POWER_ON_RETRIES_EXHAUSTED"
            context.data[common_utils.STATE_REASON_MESSAGE] = (
                await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_POWER_ON_RETRIES_EXHAUSTED"
                )
            )
            await common_utils.ahs_download_job(
                self.logger, context, self.job_resource_api
            )
# If the server is Direct Connect server, this JobStep will fetch the inventory
# by making RAS call.
class GetFullInventoryForDirectConnectServers(JobPollingStep):
    def __init__(
        self,
        job_messaging_client: JobMessagingClient,
        job_resource_api: JobResourceApi,
        ilo_resource_api: IloResourceApi,
    ):
        super().__init__()
        self.job_messaging_client = job_messaging_client
        self.RETRIES = 5
        self.ilo_resource_api = ilo_resource_api
        self.job_resource_api = job_resource_api
        self.logger.debug("Starting job step : GetFullInventoryForDirectConnectServers")
    async def logic(self, context: JobContext):
        context.data[START_TIME] = time.time()
        context.status = "Collecting the inventory"
        await common_utils.post_job_in_progress_message(
            context,
            self.job_messaging_client,
            "COLLECT_INV_AFTER_POWER_ON_MESSAGE"
            if inventory_utils.is_power_on_needed_during_inventory(context)
            else "COLLECT_INV_MESSAGE",
            (
                "COLLECT_INV_AFTER_POWER_ON_MESSAGE"
                if inventory_utils.is_power_on_needed_during_inventory(context)
                else "COLLECT_INV_MESSAGE"
            ),
            None,
            inventory_utils.get_results_data_for_inventory(context),
        )
        # PLEASE dont change the text "Starting full inventory collection" in below log. This is used for inventory dashboard
        self.logger.info(
            "Starting full inventory collection for server %s with job %s via RAS",
            context.associated_resource_uri,
            context.job_id,
        )
        # If Filtered inventory LD is enabled, then consider the provided filters.
        # Else, inventory will be fetched for all resources mentioned in DEFAULT_RESOURCE_TAGS
        resource_tags = (
            context.data.get(FILTER_RESOURCE_NAME)
            if context.data.get(FILTER_RESOURCE_NAME)
            and FeatureFlags.T_20230927_17800_FILTERED_INVENTORY()
            else DEFAULT_RESOURCE_TAGS
        )
        request = {
            "verb": "getInventory",
            FILTER_RESOURCE_NAME: {"resourceTags": resource_tags},
        }
        self.logger.info("Inventory Request : %s", request)
        # Initialize the subresources count and step count to update progress status
        context.data[SUBRESOURCES_COUNT] = len(resource_tags)
        context.data[CURRENT_STEP] += 1
        await self.job_messaging_client.add_request_message_to_job_context(
            context, RequestMessage(RAS_REQUESTS_TOPIC, request)
        )
        self.logger.info(
            "Submitted the inventory request to RAS for the server %s with job : %s",
            context.associated_resource_uri,
            context.job_id,
        )
    async def process_response(self, context: JobContext):
        process_response_start = time.time()
        context.data[PROCESS_RESPONSE_START_TIME] = process_response_start
        self.logger.info(
            "In process_response for server : %s. isOneViewServer : %s. with job : %s. Inventory fetched in : %s seconds",
            context.associated_resource_uri,
            context.data[IS_ONEVIEW_SERVER],
            context.job_id,
            process_response_start - context.data[START_TIME],
        )
        is_inventory_collection_complete = False
        total_steps = context.data[SUBRESOURCES_COUNT]
        current_step = context.data[CURRENT_STEP]
        # Ignore any message which is not a RAS returned one. All RAS returned response
        # will have taskStatus in its message body. So to avoid unnecessary processing,
        # we are ignoring the message amd initiate the retry immediately. Also, we will not
        # update the retry count in such cases because, here we really didnt do any try to
        # process the response.
        # Ideally, we should not end up with this condition, but if there are any issue with
        # the requestId, we may start processing the responses in which case, we dont want
        # to process such responses which are not returned by RAS.
        if (
            not context.response_data.data
            or TASK_STATUS not in context.response_data.data
        ):
            self.logger.info(
                "Not a RAS response. Hence ignoring. context.step_retries = %s",
                context.step_retries,
            )
            context.step_retries = context.step_retries - 1
            raise JobRetryWithContinueException()
        task_state = context.response_data.data[TASK_STATE]
        task_status = context.response_data.data[TASK_STATUS]
        ras_task = context.response_data.data[TASK_MONITOR]
        context.data[TASK_MONITOR] = ras_task
        response_status = await common_utils.get_response_status_from_ras_message(
            context.response_data
        )
        self.logger.info(
            "RAS Task = %s, TaskStatus = %s, TaskState = %s, status : %s for the server : %s",
            ras_task,
            task_status,
            task_state,
            response_status,
            context.associated_resource_uri,
        )
        # Process the response with task state Running to update the inventory collection progress
        if task_state is not None and task_state == "Running":
            self.logger.debug("Update the inventory collection progress")
            self._update_inventory_collection_progress(
                context, current_step, total_steps
            )
            # Send wait signal till the inventory collection is completed
            await self.set_step_waiting(context, not is_inventory_collection_complete)
            return is_inventory_collection_complete
        if response_status == 200:
            message = context.response_data
            # Adding some basic validations for the returned data
            if not message or not message.data:
                self.logger.error(
                    "message or message.data is null. Hence skipping save data to cobalt"
                )
                error_msg = "Marking the inventory job as error. Recieved RAS Kafka message is either empty or have no data."
                context.results["FAILURE_REASON"] = "EMPTY_RESPONSE"
                context.data[ERROR_MESSAGE] = error_msg
                return
            payload = message.data.get(PAYLOAD)
            if not payload or not payload.get(BODY):
                self.logger.error(
                    "payload or payload.body is null. Hence skipping save data to cobalt"
                )
                error_msg = "Marking the inventory job as error. Recieved RAS Kafka message has empty payload or no inventory data."
                context.results["FAILURE_REASON"] = "EMPTY_PAYLOAD"
                context.data[ERROR_MESSAGE] = error_msg
                return
            redfish_resources = payload.get(BODY).get(REDFISH_RESOURCES)
            if not redfish_resources:
                self.logger.error(
                    "RedfishResources in kafka message payload is null. Hence skipping save data to cobalt"
                )
                error_msg = "Marking the inventory job as error. Recieved RAS Kafka message has no redfish resource data."
                context.results["FAILURE_REASON"] = "EMPTY_REDFISH_SUBRESOURCE"
                context.data[ERROR_MESSAGE] = error_msg
                return
            # Only on successful data retrieval from RAS, we need to post the data to cobalt. Hence,
            # on success, we will store the inventory in job context for further processing.
            context.data[INVENTORY] = redfish_resources
            self.logger.debug(
                "Saving the inventory to context. Inventory : %s", redfish_resources
            )
            # Inventory collection is successful. Send signal to stop waiting.
            is_inventory_collection_complete = True
            await self.set_step_waiting(context, not is_inventory_collection_complete)
            return is_inventory_collection_complete
        else:
            # If retries are exhausted, or if the inventory task was a failure, then we dont want to update the
            # inventory, but we will mark the job as failure. We wont even persist the partial inventory
            if context.step_retries >= self.RETRIES:
                error_msg = f"Marking the inventory job as error for job :{context.job_id}  because it timed out waiting for RAS task {context.data[TASK_MONITOR]} to complete."
                context.results["FAILURE_REASON"] = "RETRIES_EXHAUSTED"
                context.data[ERROR_MESSAGE] = error_msg
                context.data[
                    common_utils.STATE_REASON_MESSAGE
                ] = await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_RETRIES_EXHAUSTED"
                context.data[common_utils.STATE_REASON_MESSAGE] = (
                    await common_utils.get_job_state_reason_message(
                        "INV_COLLECTION_RETRIES_EXHAUSTED"
                    )
                )

            elif task_status == TASK_CRITICAL or task_state == TASK_EXCEPTION:
                error_msg = f"Marking the inventory job as error for job:{context.job_id}. An unexpected or failed response was received during get server inventory. Response status: {response_status}"
                context.results["FAILURE_REASON"] = "INTERNAL_ERROR"
                context.data[ERROR_MESSAGE] = error_msg
                context.data[
                    common_utils.STATE_REASON_MESSAGE
                ] = await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_INTERNAL_ERROR"
                context.data[common_utils.STATE_REASON_MESSAGE] = (
                    await common_utils.get_job_state_reason_message(
                        "INV_COLLECTION_INTERNAL_ERROR"
                    )
                )

            else:
                # If taskStatus or taskState are not failed terminal, then we dont mark the job as error,
                # but we simply wait for next message processing.
                context.data[
                    common_utils.STATE_REASON_MESSAGE
                ] = await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_INTERNAL_ERROR"
                context.data[common_utils.STATE_REASON_MESSAGE] = (
                    await common_utils.get_job_state_reason_message(
                        "INV_COLLECTION_INTERNAL_ERROR"
                    )
                )
                raise JobRetryWithErrorException()

    async def retry(self, context: JobContext):
        # We dont want to retry any inventory fetch logic. We just need to retry fetching
        # the response from the next incoming message.
        self.logger.debug(
            "context.step_retries count : %s, self.RETRIES : %s",
            context.step_retries,
            self.RETRIES,
        )
        # If there are any other error already, dont retry the logic.
        if Helper.is_last_jobstep_failed(context):
            context.step_retries = self.RETRIES
        if context.step_retries >= self.RETRIES:
            # If there are other errors already, dont overwrite the error.
            # Add error_message and failure_reason only if last step was success.
            if Helper.is_last_jobstep_success(context):
                error_msg = f"Unable to collect inventory for server after {context.step_retries} attempts."
                context.results["FAILURE_REASON"] = "RETRIES_EXHAUSTED"
                context.data[ERROR_MESSAGE] = error_msg
            context.data[
                common_utils.STATE_REASON_MESSAGE
            ] = await common_utils.get_job_state_reason_message(
                "INV_COLLECTION_INTERNAL_ERROR"
            context.data[common_utils.STATE_REASON_MESSAGE] = (
                await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_INTERNAL_ERROR"
                )
            )
            await common_utils.ahs_download_job(
                self.logger, context, self.job_resource_api
            )
    def _update_inventory_collection_progress(
        self, context: JobContext, current_step, total_steps
    ):
        response = context.response_data
        if (
            response
            and response.data
            and response.data.get(MESSAGES)
            and len(response.data.get(MESSAGES)) > 0
            and "Collecting" in response.data.get(MESSAGES)[-1][MESSAGE]
        ):
            prefix = f"Step {current_step} of {total_steps} - "
            context.status = prefix + response.data.get(MESSAGES)[-1][MESSAGE]
            context.data[CURRENT_STEP] += 1
        else:
            self.logger.debug(
                "The interim response does not have inventory collection status. Hence skipping the update"
            )
# If the server is OneView Connected server, this JobStep will fetch the inventory
# by making OV call.
class GetFullInventoryForOneViewServer(JobStep):
    def __init__(
        self,
        job_messaging_client: JobMessagingClient,
        ilo_resource_api: IloResourceApi,
    ):
        super().__init__()
        self.job_messaging_client = job_messaging_client
        self.RETRIES = 5
        self.ilo_resource_api = ilo_resource_api
        self.logger.debug("Starting job step : GetFullInventoryForOneViewServer")
    async def logic(self, context: JobContext):
        # PLEASE dont change the text "Starting full inventory collection" in below log. This is used for inventory dashboard
        self.logger.info(
            "Starting full inventory collection for OneView server %s with job %s",
            context.associated_resource_uri,
            context.job_id,
        )
        context.status = "Collecting the inventory"
        appliance_url = context.data.get(APPLIANCE_URI)
        serverUuid = context.data[SERVER_UUID]
        self.logger.debug(
            "isOneview = %s, appliance_uri = %s, serverUuid : %s, server : %s",
            context.data.get(IS_ONEVIEW_SERVER),
            appliance_url,
            serverUuid,
            context.associated_resource_uri,
        )
        # If this is a OneView server, then we MUST have a valid server UUID. Because we use
        # the serverUUID to build the OneView API call. If ServerUUID is not available, then
        # we cant proceed with the inventory collection. Hence error out the job.
        if not serverUuid:
            raise DependentResourceNotFoundException(
                f"No iLO found with ID: {context.associated_resource_uri}",
                ErrorEnum.HPE_GL_COMPUTE_OPS_0300132,
            )
        context.data[DEVICE_ID] = "oneview+" + appliance_url.rsplit("/", 1)[1]
        # We will make the OV API call with expand query to get complete inventory information.
        request_uri = (
            OV_SERVER_HARDWARE_REQUEST_URI_PREFIX + serverUuid + EXPAND_ALL_PREFIX
        )
        self.logger.debug(
            "request uri %s",
            request_uri,
        )
        inventory_request = ov_request_utils.get_server_inventory_request(request_uri)
        context.data[INVENTORY_CATEGORY] = OV_SERVER_HARDWARE_TYPE
        context.data[START_TIME] = time.time()
        await self.job_messaging_client.add_request_message_to_job_context(
            context,
            inventory_request,
        )
        self.logger.info(
            "Submitted the inventory request from OneView for %s with job : %s",
            request_uri,
            context.job_id,
        )
    async def process_response(self, context: JobContext):
        process_response_start = time.time()
        context.data[PROCESS_RESPONSE_START_TIME] = process_response_start
        self.logger.info(
            "In process_response for server : %s. isOneViewServer : %s. with job : %s, Inventory fetched in : %s seconds",
            context.associated_resource_uri,
            context.data[IS_ONEVIEW_SERVER],
            context.job_id,
            process_response_start - context.data[START_TIME],
        )
        response_status = await common_utils.get_response_status_from_redfish_message(
            context.response_data
        )
        response_body = await common_utils.get_response_body_from_redfish_message(
            context.response_data
        )
        self.logger.debug(
            "Oneview Response status : %s, response data : %s",
            response_status,
            response_body,
        )
        if response_status == 200:
            subresources = (
                response_body.get(SUBRESOURCES)
                if response_body.get(SUBRESOURCES)
                else None
            )
            if not subresources:
                self.logger.error(
                    "subresources is null. Hence skipping save data to cobalt"
                )
                error_msg = f"Marking the inventory job as error for the job:{context.job_id}. Recieved Oneview Redfish message dont have subresources."
                context.results["FAILURE_REASON"] = "EMPTY_REDFISH_SUBRESOURCE"
                context.data[ERROR_MESSAGE] = error_msg
            context.data[INVENTORY] = subresources
        else:
            if context.step_retries >= self.RETRIES:
                error_msg = f"Marking the inventory job as error for the job:{context.job_id}. An unexpected response was received during get server inventory. Response status: {response_status}"
                context.data[
                    common_utils.STATE_REASON_MESSAGE
                ] = await common_utils.get_job_state_reason_message(
                    ov_common_utils.GetOneViewServerInventoryErrorCodes.GET_SERVER_HW_INVENTORY_FAIL
                context.data[common_utils.STATE_REASON_MESSAGE] = (
                    await common_utils.get_job_state_reason_message(
                        ov_common_utils.GetOneViewServerInventoryErrorCodes.GET_SERVER_HW_INVENTORY_FAIL
                    )
                )
                context.results["FAILURE_REASON"] = "INTERNAL_ERROR"
                context.data[ERROR_MESSAGE] = error_msg
            else:
                context.data[
                    common_utils.STATE_REASON_MESSAGE
                ] = await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_INTERNAL_ERROR"
                context.data[common_utils.STATE_REASON_MESSAGE] = (
                    await common_utils.get_job_state_reason_message(
                        "INV_COLLECTION_INTERNAL_ERROR"
                    )
                )
                raise JobRetryWithErrorException()

    async def retry(self, context: JobContext):
        if context.step_retries > self.RETRIES:
            error_msg = f"Unable to get server inventory after {context.step_retries + 1} attempts."
            context.results["FAILURE_REASON"] = "RETRIES_EXHAUSTED"
            context.data[ERROR_MESSAGE] = error_msg
            context.data[
                common_utils.STATE_REASON_MESSAGE
            ] = await common_utils.get_job_state_reason_message(
                "INV_COLLECTION_RETRIES_EXHAUSTED"
            context.data[common_utils.STATE_REASON_MESSAGE] = (
                await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_RETRIES_EXHAUSTED"
                )
            )
            raise JobErrorException(error_msg)
        self.logger.debug(
            "retry: %s",
            context.step_retries,
        )
# Save the inventory stored in JobContext to raw_inventory table of Cobalt with this JobStep
class SaveInventoryToCobalt(JobStep):
    def __init__(
        self,
        ilo_resource_api: IloResourceApi,
        roundup_client: ReportsClient,
    ):
        super().__init__()
        self.ilo_resource_api = ilo_resource_api
        self.roundup_client = roundup_client
        self.logger.debug("Starting job step : SaveInventoryToCobalt")
    async def logic(self, context: JobContext):
        self.logger.info(
            "Saving inventory to Cobalt for server %s with job %s",
            context.associated_resource_uri,
            context.job_id,
        )
        inventory = context.data[INVENTORY]
        server_id = cast(Server, context.associated_resource).id
        product_id, serial = server_id.rsplit("+", 1)
        self.logger.debug(
            "Retrieved inventory for server_id: %s, serial : %s, product_id : %s, inventory : %s",
            server_id,
            serial,
            product_id,
            inventory,
        )
        # If Filtered inventory LD is enabled, then consider the provided filters.
        # Else, inventory will be processed for all resources mentioned in DEFAULT_RESOURCE_TAGS.
        # For Direct connect servers, this will not be an issue as we would have sent filters to
        # RAS while fetching the inventory. But for OV connected servers, we make the full server
        # call and then based on provided filters, we extract specific subresources only from the response.
        resource_tags = (
            context.data.get(FILTER_RESOURCE_NAME)
            if context.data.get(FILTER_RESOURCE_NAME)
            and FeatureFlags.T_20230927_17800_FILTERED_INVENTORY()
            else DEFAULT_RESOURCE_TAGS
        )
        # This will have all the inventory variables which holds the actual inventory
        variables = {SERIAL: serial, PRODUCT_ID: product_id}
        # OneView server inventory has different subresource names which are returned via
        # OneView call unlike the DirectConnect servers. In case of direct connect servers,
        # the subresource names directly map to the RAS subresource name. But with OV, the
        # subresource names are little different. Also, in case of filtered inventory call,
        # we need to extract only those subresources from the OV response which are provided
        # in "filters" of the request. These "filters" will be considered only if the
        # corresponding LD is enabled, else, we consider all subresources that OV returns.
        if context.data[IS_ONEVIEW_SERVER]:
            variables[VAR_FIRMWARE] = self.extract_data_from_response(
                OV_FIRMWARE_INVENTORY, inventory, resource_tags, RAS_FIRMWARE_INVENTORY
            )
            variables[VAR_SOFTWARE] = self.extract_data_from_response(
                OV_SOFTWARE_INVENTORY, inventory, resource_tags, RAS_SOFTWARE_INVENTORY
            )
            variables[VAR_CHASSIS] = self.extract_data_from_response(
                CHASSIS, inventory, resource_tags, CHASSIS
            )
            variables[VAR_PROCESSOR] = self.extract_data_from_response(
                OV_PROCESSORS, inventory, resource_tags, RAS_PROCESSOR
            )
            variables[VAR_MEMORY] = self.extract_data_from_response(
                OV_MEMORY, inventory, resource_tags, RAS_MEMORY
            )
            variables[VAR_ADAPTERS] = self.extract_data_from_response(
                OV_NETWORK_ADAPTERS, inventory, resource_tags, RAS_NETWORK_ADAPTERS
            )
            variables[VAR_POWER_SUPPLIES] = self.extract_data_from_response(
                OV_POWER_SUPPLIES, inventory, resource_tags, RAS_POWER_SUPPLIES
            )
            variables[VAR_THERMAL] = self.extract_data_from_response(
                OV_THERMAL, inventory, resource_tags, RAS_THERMAL
            )
            variables[VAR_PCI_DEVICES] = self.extract_data_from_response(
                OV_DEVICES, inventory, resource_tags, RAS_DEVICES
            )
            variables[VAR_LOCAL_STORAGE] = self.extract_data_from_response(
                OV_LOCAL_STORAGE, inventory, resource_tags, RAS_LOCAL_STORAGE
            )
            variables[VAR_LOCAL_STORAGE_V2] = self.extract_data_from_response(
                OV_LOCAL_STORAGE_V2, inventory, resource_tags, RAS_LOCAL_STORAGE_V2
            )
        else:
            variables[VAR_FIRMWARE] = self.extract_data_from_response(
                RAS_FIRMWARE_INVENTORY, inventory, resource_tags, RAS_FIRMWARE_INVENTORY
            )
            variables[VAR_SOFTWARE] = self.extract_data_from_response(
                RAS_SOFTWARE_INVENTORY, inventory, resource_tags, RAS_SOFTWARE_INVENTORY
            )
            variables[VAR_CHASSIS] = self.extract_data_from_response(
                CHASSIS, inventory, resource_tags, CHASSIS
            )
            variables[VAR_PROCESSOR] = self.extract_data_from_response(
                RAS_PROCESSOR, inventory, resource_tags, RAS_PROCESSOR
            )
            variables[VAR_MEMORY] = self.extract_data_from_response(
                RAS_MEMORY, inventory, resource_tags, RAS_MEMORY
            )
            variables[VAR_ADAPTERS] = self.extract_data_from_response(
                RAS_NETWORK_ADAPTERS, inventory, resource_tags, RAS_NETWORK_ADAPTERS
            )
            variables[VAR_POWER_SUPPLIES] = self.extract_data_from_response(
                RAS_POWER_SUPPLIES, inventory, resource_tags, RAS_POWER_SUPPLIES
            )
            variables[VAR_THERMAL] = self.extract_data_from_response(
                RAS_THERMAL, inventory, resource_tags, RAS_THERMAL
            )
            variables[VAR_PCI_DEVICES] = self.extract_data_from_response(
                RAS_DEVICES, inventory, resource_tags, RAS_DEVICES
            )
            variables[VAR_LOCAL_STORAGE] = self.extract_data_from_response(
                RAS_LOCAL_STORAGE, inventory, resource_tags, RAS_LOCAL_STORAGE
            )
            variables[VAR_LOCAL_STORAGE_V2] = self.extract_data_from_response(
                RAS_LOCAL_STORAGE_V2, inventory, resource_tags, RAS_LOCAL_STORAGE_V2
            )
        try:
            if FeatureFlags.T_20230901_13831_UPDATED_INVENTORY_DATA():
                self.logger.info(
                    "Since T_20230901_13831_UPDATED_INVENTORY_DATA LD flag is enabled, using NewInventory Object"
                )
                await self.selective_inventory_update(variables, server_id, context)
            else:
                self.logger.info(
                    "Since T_20230901_13831_UPDATED_INVENTORY_DATA LD flag is disabled, using legacy Inventory Object"
                )
                await self.normal_inventory_update(variables, server_id, context)
        except asyncio.TimeoutError:
            self.logger.info("TimeoutError while updating inventory")
            raise JobRetryException()
        except Exception:
            self.logger.exception(
                "Exception while processing the inventory for server_id %s.",
                server_id,
            )
            error_msg = f"Marking the inventory job as error for the job:{context.job_id}. An unexpected error occured while parsing the retrieved inventory for server {server_id}."
            context.results["FAILURE_REASON"] = "INTERNAL_ERROR"
            context.data[ERROR_MESSAGE] = error_msg
            context.data[
                common_utils.STATE_REASON_MESSAGE
            ] = await common_utils.get_job_state_reason_message(
                "INV_COLLECTION_INTERNAL_ERROR"
            context.data[common_utils.STATE_REASON_MESSAGE] = (
                await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_INTERNAL_ERROR"
                )
            )
            return

        # If this is a reports call, the job context or the job payload will be populated with an
        # additional 'data' attribute 'is_reports_call' as true. So, when we find this attribute
        # is populated with a True value, then we need to build a reports payload and make a roundup
        # POST call to populate data in the roundup. Sample payload for the job is:
        #    {
        #        "jobTemplateUri": "/compute-ops/v1beta2/job-templates/d6595f1b-84e6-4587-ade5-656e2a5ea20d",
        #        "resourceUri": "/compute-ops/v1beta2/servers/994179-G04+8899994179104843",
        #        "data": {
        #            "is_reports_call": true
        #        }
        #    }
        is_reports_call = context.data.get(IS_REPORTS_CALL)
        if (
            isinstance(is_reports_call, bool)
            and is_reports_call
            and REPORT_ID in context.data
            and context.data.get(REPORT_ID)
            and Helper.is_last_jobstep_success(context)
        ):
            self.logger.info(
                "Saving inventory data in roundup for server %s with job %s",
                context.associated_resource_uri,
                context.job_id,
            )
            ilo = await self.ilo_resource_api.get_ilo(
                cast(Server, context.associated_resource).id
            )
            if ilo is None:
                raise DependentResourceNotFoundException(
                    f"No iLO found with ID: {context.associated_resource_uri}",
                    ErrorEnum.ILO_DEVICE_NOT_FOUND,
                )
            raw_inventory_obj = await self.ilo_resource_api.get_ilo_raw_inventory(
                ilo.id
            )
            if raw_inventory_obj is None:
                raise DependentResourceNotFoundException(
                    f"No raw inventory data found for ID: {context.associated_resource_uri}",
                    ErrorEnum.RAW_INVENTORY_MISSING,
                )
            if ilo.hardware is None:
                context.results["FAILURE_REASON"] = "NO_ASSOCIATED_HARDWARE"
                raise JobErrorException("ilo.hardware is None")
            payload = {
                "@odata.id": "/redfish",
                "InventoryDetail": {
                    "name": ilo.display_name,
                    "serverGeneration": ilo.server_generation,
                    "powerState": (
                        ilo.hardware.power_state.value
                        if ilo.hardware.power_state
                        else PowerState.Unknown.value
                    ),
                    "bmc": {
                        "manager": self.get_ilo_type_from_generation(
                            ilo.server_generation
                        )
                    },
                    "hardware": {
                        "serialNumber": serial,
                        "productId": product_id,
                        "model": ilo.hardware.model,
                        "processorVendor": ilo.processorvendor,
                    },
                    "processor": {DATA_KEY: raw_inventory_obj.processor_inventory},
                    "memory": {DATA_KEY: raw_inventory_obj.memory_inventory},
                    "smartStorage": {
                        DATA_KEY: (
                            raw_inventory_obj.storage_inventory.get(OV_LOCAL_STORAGE)
                            if raw_inventory_obj.storage_inventory
                            else []
                        )
                    },
                    "storage": {
                        DATA_KEY: (
                            raw_inventory_obj.storage_inventory.get(OV_LOCAL_STORAGE_V2)
                            if raw_inventory_obj.storage_inventory
                            else []
                        )
                    },
                    "device": {DATA_KEY: raw_inventory_obj.pci_devices},
                    "thermal": {DATA_KEY: raw_inventory_obj.thermal_inventory},
                    "powerSupply": {DATA_KEY: raw_inventory_obj.power_supply_inventory},
                    "chassis": {
                        DATA_KEY: [
                            {
                                FORM_FACTOR: self.get_form_factor_from_chassis(
                                    raw_inventory_obj.chassis_inventory
                                )
                            }
                        ]
                    },
                },
            }
            self.logger.debug("Roundup payload = %s", payload)
            acid = context.application_customer_id
            await self.roundup_client.store_metric_data_log(
                context.associated_resource,
                acid,
                payload,
                {"report_id": context.data.get(REPORT_ID)},
                report_type=context.data.get("report_type"),
            )
        else:
            self.logger.info(
                "This is not a reports call or there are errors. Hence ignoring the roundup data population. is_reports_call : %s, reportId : %s",
                is_reports_call,
                context.data.get(REPORT_ID) if REPORT_ID in context.data else None,
            )
        # PLEASE dont change the text - "Server inventory collection is successful with job_id" in below log. This is used for drawing the inventory dashboard.
        self.logger.info(
            "Server inventory collection is successful with job_id %s and server %s. DB inventory fetch took : %s sec, Inventory collection took : %s sec. Processing inventory and saving took : %s sec",
            context.job_id,
            context.associated_resource_uri,
            context.data[COBALT_FETCH_TIME],
            context.data[PROCESS_RESPONSE_START_TIME] - context.data[START_TIME],
            time.time() - context.data[PROCESS_RESPONSE_START_TIME],
        )
    # Retrieve the Form Factor from the Chassis Inventory
    def get_form_factor_from_chassis(self, chassis_inventory):
        form_factor = DEFAULT_FORM_FACTOR
        try:
            if (
                chassis_inventory
                and chassis_inventory[0]
                and chassis_inventory[0].get(OEM)
                and chassis_inventory[0].get(OEM).get(HPE)
                and chassis_inventory[0].get(OEM).get(HPE).get(FORM_FACTOR)
            ):
                form_factor = chassis_inventory[0].get(OEM).get(HPE).get(FORM_FACTOR)
        except Exception:
            self.logger.exception(
                "Exception while fetching form factor from chassis. Ignoring this and defaulting the form factor to 1U. Exception : %s",
            )
        return form_factor
    # Raw inventory for storage will have both LocalStorage and LocalStorageV2 in its response.
    # We need to set them only upon identifying if any of these is updated.
    def check_and_update_storage_raw_inv_payload(
        self,
        localstorage,
        localstoragev2,
        inventory_object: NewInventory,
        modified_inventory,
    ) -> None:
        self.check_and_update_payload(
            LOCAL_STORAGE_V2_TEMPORARY,
            localstoragev2,
            inventory_object.storage_inventory if inventory_object else None,
            modified_inventory,
            False,
        )
        self.check_and_update_payload(
            LOCAL_STORAGE_TEMPORARY,
            localstorage,
            inventory_object.smart_storage_inventory if inventory_object else None,
            modified_inventory,
            False,
        )
        # If either of LocalStorage or LocalStorageV2 are changed, we need to populate raw
        # inventory table with appropriate data as raw inventory stoes both LS and LSv2
        # inventory in a same column.
        storageinventory = {
            OV_LOCAL_STORAGE: (
                modified_inventory.get(LOCAL_STORAGE_TEMPORARY)
                if modified_inventory.get(LOCAL_STORAGE_TEMPORARY)
                else (
                    localstorage.get(DATA_KEY)
                    if localstorage and localstorage.get(DATA_KEY)
                    else []
                )
            ),
            OV_LOCAL_STORAGE_V2: (
                modified_inventory.get(LOCAL_STORAGE_V2_TEMPORARY)
                if modified_inventory.get(LOCAL_STORAGE_V2_TEMPORARY)
                else (
                    localstoragev2.get(DATA_KEY)
                    if localstoragev2 and localstoragev2.get(DATA_KEY)
                    else []
                )
            ),
        }
        # If either of the inventory is updated, then add it to the modified inventory
        # so that it can be persisited.
        if modified_inventory.get(LOCAL_STORAGE_TEMPORARY) or modified_inventory.get(
            LOCAL_STORAGE_V2_TEMPORARY
        ):
            modified_inventory[STORAGE_INVENTORY] = storageinventory
            self.logger.info(
                "Setting storage inventory in payload. data : %s",
                modified_inventory[STORAGE_INVENTORY],
            )
        else:
            self.logger.info("Not setting the storage inventory in the payload")
    # Add the subresource to the inventory payload based on certain conditions.
    def check_and_update_payload(
        self,
        subresource_name,
        new_subresource,
        existing_subresource,
        modified_inventory,
        is_inventory_call,
    ) -> None:
        new_col_state = new_subresource.get(COLLECTION_STATE)
        existing_col_state = (
            existing_subresource.get(COLLECTION_STATE)
            if existing_subresource and existing_subresource.get(COLLECTION_STATE)
            else None
        )
        new_subres = new_subresource.get(DATA_KEY)
        existing_subres = (
            existing_subresource.get(DATA_KEY)
            if existing_subresource and existing_subresource.get(DATA_KEY)
            else None
        )
        # If the new inventory is latest, then only save it to DB.
        if self.should_patch(
            new_col_state, existing_col_state, new_subres, existing_subres
        ):
            self.logger.info(
                "Adding subresource: %s to payload. new_subresource : %s",
                subresource_name,
                new_subresource,
            )
            modified_inventory[subresource_name] = (
                self.format_to_inventory(new_subresource)
                if is_inventory_call
                else new_subresource.get(DATA_KEY)
            )
        else:
            self.logger.info("NOT adding subresource: %s to payload", subresource_name)
    # This method will have the main logic of deciding if the subresource should be replaced or not.
    # TODO This should be revisited and further conditions should be added
    def should_patch(
        self, new_col_state, existing_col_state, new_subres, existing_subres
    ) -> bool:
        # If new sub resource has "Success" or "Collected" state and have data, always replace the inventory
        if (new_col_state == SUCCESS or new_col_state == COLLECTED) and (new_subres):
            return True
        # If new sub resource has "SuccessCached" or "CollectedStale" state, always replace the inventory
        if (
            new_col_state == SUCCESS_CACHED or new_col_state == COLLECTED_STALE
        ) and new_subres:
            return True
        # If new sub resource has data and DB dont have data currently, always replace the inventory
        if new_subres and not existing_subres:
            return True
        return False
    # Update the devices table based on updated attributes
    async def update_device_table(self, devices_payload, server_id) -> None:
        if (
            FeatureFlags.T_20240220_28779_POWER_ON_SERVER_SUPPORT_BEFORE_INVENTORY_BOOL()
        ):
            inventory_update_details_from_db = (
                await self.ilo_resource_api.get_last_inventory_update_details(server_id)
            )
            self.logger.info(
                "inventory_update_details_from_db : %s",
                inventory_update_details_from_db,
            )
            if inventory_update_details_from_db:
                if (
                    LAST_COLLECTION_TIME in inventory_update_details_from_db
                    and inventory_update_details_from_db[LAST_COLLECTION_TIME]
                ):
                    devices_payload[
                        LAST_COLLECTION_TIME
                    ] = inventory_update_details_from_db[LAST_COLLECTION_TIME]
                    devices_payload[LAST_COLLECTION_TIME] = (
                        inventory_update_details_from_db[LAST_COLLECTION_TIME]
                    )
                if (
                    LAST_COLLECTED_POWER_STATE in inventory_update_details_from_db
                    and inventory_update_details_from_db[LAST_COLLECTED_POWER_STATE]
                ):
                    devices_payload[
                        LAST_COLLECTED_POWER_STATE
                    ] = inventory_update_details_from_db[LAST_COLLECTED_POWER_STATE]
                    devices_payload[LAST_COLLECTED_POWER_STATE] = (
                        inventory_update_details_from_db[LAST_COLLECTED_POWER_STATE]
                    )
            else:
                self.logger.info(
                    "T_20240220_28779_POWER_ON_SERVER_SUPPORT_BEFORE_INVENTORY_BOOL is not enabled. Hence skipping the update of last collection time and power state for server : %s",
                    server_id,
                )
        if len(devices_payload) > 1:
            self.logger.info("Updating the devices with payload : %s", devices_payload)
            # Update the server (devices table) with the formatted inventory items
            updated_ilo: Server = Server(**devices_payload)
            self.logger.info("Data to be patched to devices table : %s", updated_ilo)
            # All exception handling are performed in the caller.
            await self.ilo_resource_api.patch_ilo(server_id, updated_ilo)
        else:
            self.logger.info(
                "NOT updating the devices as the Firmware/Software/Storage didnt change as part of this call for server : %s",
                server_id,
            )
    # This function is for updating the cobalt tables selectively. Based on saved and new collection
    # state, we decide which all sub resources can be updated to DB.
    async def selective_inventory_update(self, variables, server_id, context) -> None:
        inventory_from_db: NewInventory = (
            await self.ilo_resource_api.get_ilo_inventory_v1beta2(server_id)
        inventory_from_db: NewInventory = await self.ilo_resource_api.get_ilo_inventory(
            server_id
        )
        self.logger.debug(
            "Inventory from DB for server : %s is : %s", server_id, inventory_from_db
        )
        # Update the firmware, software and storage inventory in devices_payload
        # We are not updating the devices table here because, we also need couple
        # of attributes last collection time and power state which will be available only
        # upon saving them to inventory DB. So, once inventory DB is updated, then we will
        # fetch these two attributes from DB and then copy it to devices and save it.
        devices_payload = await self.get_devices_table_payload(
            context,
            inventory_from_db,
            variables[VAR_FIRMWARE],
            variables[VAR_SOFTWARE],
            variables[VAR_LOCAL_STORAGE],
            variables[VAR_LOCAL_STORAGE_V2],
        )
        # Create and update the json modified_raw_inventory with necessary payload
        # attributes after comparing it with the existing inventory from DB. At the
        # end of these checks, modified_raw_inventory will have attributes which
        # needs to be PATCHed in raw inventory.
        modified_raw_inventory = {
            SERIAL: variables[SERIAL],
            PRODUCT_ID: variables[PRODUCT_ID],
        }
        self.check_and_update_payload(
            FW_INVENTORY,
            variables[VAR_FIRMWARE],
            inventory_from_db.fw_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        self.check_and_update_payload(
            SW_INVENTORY,
            variables[VAR_SOFTWARE],
            inventory_from_db.sw_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        self.check_and_update_payload(
            PCI_DEVICES,
            variables[VAR_PCI_DEVICES],
            inventory_from_db.device_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        self.check_and_update_payload(
            CHASSIS_INVENTORY,
            variables[VAR_CHASSIS],
            inventory_from_db.chassis_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        self.check_and_update_payload(
            MEMORY_INVENTORY,
            variables[VAR_MEMORY],
            inventory_from_db.memory_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        self.check_and_update_payload(
            NETWORK_INVENTORY,
            variables[VAR_ADAPTERS],
            inventory_from_db.network_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        self.check_and_update_payload(
            PROCESSOR_INVENTORY,
            variables[VAR_PROCESSOR],
            inventory_from_db.processor_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        self.check_and_update_payload(
            POWER_SUPPLY_INVENTORY,
            variables[VAR_POWER_SUPPLIES],
            inventory_from_db.power_supply_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        self.check_and_update_payload(
            THERMAL_INVENTORY,
            variables[VAR_THERMAL],
            inventory_from_db.thermal_inventory if inventory_from_db else None,
            modified_raw_inventory,
            False,
        )
        # storage inventory is special in raw inventory in a sense where we need to
        # combine LS and LSv2 together. Hence we are handling it seperately.
        self.check_and_update_storage_raw_inv_payload(
            variables[VAR_LOCAL_STORAGE],
            variables[VAR_LOCAL_STORAGE_V2],
            inventory_from_db,
            modified_raw_inventory,
        )
        self.logger.debug("modified_raw_inventory after : %s", modified_raw_inventory)
        # If the modified_raw_inventory has any other attributes other than serial
        # and product_id, we need to update the raw inventory.
        if len(modified_raw_inventory) > 2:
            self.logger.debug("Saving the raw inventory for server : %s", server_id)
            raw_inventory_obj = RawInventory(**modified_raw_inventory)
            await self.ilo_resource_api.update_ilo_raw_inventory(
                server_id, raw_inventory_obj
            )
        else:
            self.logger.info("Not saving the raw inventory for server : %s", server_id)
        self.logger.info("Updating inventory table for server : %s", server_id)
        modified_inventory = {
            SERIAL: variables[SERIAL],
            PRODUCT_ID: variables[PRODUCT_ID],
        }
        if (
            FeatureFlags.T_20240220_28779_POWER_ON_SERVER_SUPPORT_BEFORE_INVENTORY_BOOL()
        ):
            self.update_collection_time_and_powerstate(
                modified_inventory, server_id, context
            )
        else:
            self.logger.info(
                "T_20240220_28779_POWER_ON_SERVER_SUPPORT_BEFORE_INVENTORY_BOOL is not enabled. Hence skipping the update of last collection time and power state for server : %s",
                server_id,
            )
        # Similar to raw inventory, we need to check if the sub resource changed for
        # inventory. We need to this explicitely (cant combine with the raw_inventory
        # logic) because, here the attribute (column) names are completely different
        # for inventory and raw_inventory. We will see how these can be combined in
        # future reviews. At the end of these blocks, modified_inventory will have
        # attributes that should be PATCHed in the inventory table.
        self.check_and_update_payload(
            FW_INVENTORY,
            variables[VAR_FIRMWARE],
            inventory_from_db.fw_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            SW_INVENTORY,
            variables[VAR_SOFTWARE],
            inventory_from_db.sw_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            STORAGE_INVENTORY,
            variables[VAR_LOCAL_STORAGE_V2],
            inventory_from_db.storage_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            SMART_STORAGE_INVENTORY,
            variables[VAR_LOCAL_STORAGE],
            (inventory_from_db.smart_storage_inventory if inventory_from_db else None),
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            DEVICE_INVENTORY,
            variables[VAR_PCI_DEVICES],
            inventory_from_db.device_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            CHASSIS_INVENTORY,
            variables[VAR_CHASSIS],
            inventory_from_db.chassis_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            MEMORY_INVENTORY,
            variables[VAR_MEMORY],
            inventory_from_db.memory_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            NETWORK_INVENTORY,
            variables[VAR_ADAPTERS],
            inventory_from_db.network_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            PROCESSOR_INVENTORY,
            variables[VAR_PROCESSOR],
            inventory_from_db.processor_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            POWER_SUPPLY_INVENTORY,
            variables[VAR_POWER_SUPPLIES],
            inventory_from_db.power_supply_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.check_and_update_payload(
            THERMAL_INVENTORY,
            variables[VAR_THERMAL],
            inventory_from_db.thermal_inventory if inventory_from_db else None,
            modified_inventory,
            True,
        )
        self.logger.debug("modified_inventory after : %s", modified_inventory)
        # If the modified_inventory has any other attributes other than serial and product_id,
        # that means we have an updated inventory which should be saved.
        if len(modified_inventory) > 2:
            inventory_object = NewInventory(**modified_inventory)
            self.logger.debug("Inventory Object to PATCH: %s", inventory_object)
            await self.ilo_resource_api.update_ilo_inventory(
                server_id, inventory_object
            )
        else:
            self.logger.info(
                "Not updating inventory table for server : %s since the inventory didnt change",
                server_id,
            )
        await self.update_device_table(devices_payload, server_id)
    # Only for full inventory collection (if fitered inventory is empty in request or if all subresources are provided in the filtered inventory),
    # we will update the last_collection_time and last_collected_power_state in the inventory DB
    def update_collection_time_and_powerstate(
        self, modified_inventory, server_id, context
    ):
        power_state = context.data[POWER_STATE_DURING_INV_COLLECTION]
        filtered_resources = context.data.get(FILTER_RESOURCE_NAME)
        if (not filtered_resources) or (
            FeatureFlags.T_20230927_17800_FILTERED_INVENTORY()
            and filtered_resources
            and set(filtered_resources) == set(DEFAULT_RESOURCE_TAGS)
        ):
            now = datetime.now(timezone.utc)
            self.logger.info(
                "Its a full inventory call. Hence updating last power state : %s and last collection time : %s in inventory DB for server : %s",
                power_state,
                now,
                server_id,
            )
            modified_inventory[LAST_COLLECTED_POWER_STATE] = power_state
            modified_inventory[LAST_COLLECTION_TIME] = now
        else:
            self.logger.info(
                "Its NOT a full inventory call. Hence NOT updating last power state and last collection time in inventory DB for server : %s",
                server_id,
            )
    # This function will handle the full inventory update path irrespective of the collection state.
    # This blindly update all the inventory RAS fetched into cobalt table
    async def normal_inventory_update(self, variables, server_id, context):
        storage_inventory = {
            OV_LOCAL_STORAGE: variables[VAR_LOCAL_STORAGE],
            OV_LOCAL_STORAGE_V2: variables[VAR_LOCAL_STORAGE_V2],
        }
        # Update the firmware, software and storage inventory in devices table
        devices_payload = await self.get_devices_table_payload(
            context,
            None,
            variables[VAR_FIRMWARE],
            variables[VAR_SOFTWARE],
            variables[VAR_LOCAL_STORAGE],
            variables[VAR_LOCAL_STORAGE_V2],
        )
        # TODO check the collectionState of each subresources and only if the
        # collectionState is SUCCESS or SUCCESS_CACHED, write it to cobalt.
        raw_inventory_obj = RawInventory(
            fw_inventory=variables[VAR_FIRMWARE],
            sw_inventory=variables[VAR_SOFTWARE],
            storage_inventory=storage_inventory,
            pci_devices=variables[VAR_PCI_DEVICES],
            chassis_inventory=variables[VAR_CHASSIS],
            memory_inventory=variables[VAR_MEMORY],
            network_inventory=variables[VAR_ADAPTERS],
            processor_inventory=variables[VAR_PROCESSOR],
            power_supply_inventory=variables[VAR_POWER_SUPPLIES],
            thermal_inventory=variables[VAR_THERMAL],
            serial=variables[SERIAL],
            product_id=variables[PRODUCT_ID],
        )
        await self.ilo_resource_api.update_ilo_raw_inventory(
            server_id, raw_inventory_obj
        )
        self.logger.info("Updating inventory table for server : %s", server_id)
        inventory_object = Inventory(
            fw_inventory=self.format_to_inventory(variables[VAR_FIRMWARE]),
            sw_inventory=self.format_to_inventory(variables[VAR_SOFTWARE]),
            storage_inventory=self.format_to_inventory(variables[VAR_LOCAL_STORAGE_V2]),
            smart_storage_inventory=self.format_to_inventory(
                variables[VAR_LOCAL_STORAGE]
            ),
            device_inventory=self.format_to_inventory(variables[VAR_PCI_DEVICES]),
            chassis_inventory=self.format_to_inventory(variables[VAR_CHASSIS]),
            memory_inventory=self.format_to_inventory(variables[VAR_MEMORY]),
            network_inventory=self.format_to_inventory(variables[VAR_ADAPTERS]),
            processor_inventory=self.format_to_inventory(variables[VAR_PROCESSOR]),
            power_supply_inventory=self.format_to_inventory(
                variables[VAR_POWER_SUPPLIES]
            ),
            thermal_inventory=self.format_to_inventory(variables[VAR_THERMAL]),
            serial=variables[SERIAL],
            product_id=variables[PRODUCT_ID],
        )
        self.logger.debug("Inventory Object to PATCH: %s", inventory_object)
        await self.ilo_resource_api.update_ilo_inventory(server_id, inventory_object)
        await self.update_device_table(devices_payload, server_id)
    # Return the ILO type based on provided generation
    def get_ilo_type_from_generation(self, generation):
        ilo_type = None
        if "10" in generation:
            ilo_type = "iLO 5"
        elif "11" in generation:
            ilo_type = "iLO 6"
        else:
            ilo_type = "Unknown"
        return ilo_type
    # As part of the inventory call, update the fw, sw and storage inventory in device table
    async def get_devices_table_payload(
        self,
        context,
        inventory_from_db: NewInventory,
        firmware,
        software,
        local_storage,
        local_storage_v2,
    ):
        ALL_STORAGE_IDS = []
        ilo_id = cast(Server, context.associated_resource).id
        # For a selective inventory update, we will have this "inventory_from_db" object. Else, not.
        server_payload = {"id": ilo_id}
        self.check_and_update_payload(
            FIRMWARE_INVENTORY,
            firmware,
            inventory_from_db.fw_inventory if inventory_from_db else None,
            server_payload,
            False,
        )
        self.check_and_update_payload(
            SOFTWARE_INVENTORY,
            software,
            inventory_from_db.sw_inventory if inventory_from_db else None,
            server_payload,
            False,
        )
        self.check_and_update_payload(
            STORAGE_INVENTORY,
            local_storage_v2,
            inventory_from_db.storage_inventory if inventory_from_db else None,
            server_payload,
            False,
        )
        if server_payload.get(FIRMWARE_INVENTORY):
            server_payload[FIRMWARE_INVENTORY] = self.format_fw_inventory(
                firmware.get(DATA_KEY)
            )
        if server_payload.get(SOFTWARE_INVENTORY):
            server_payload[SOFTWARE_INVENTORY] = self.format_sw_inventory(
                software.get(DATA_KEY)
            )
        if server_payload.get(STORAGE_INVENTORY):
            # Storage inventory in devices table is stored in a different format than
            # other inventory. For keeping the structure intact, we are reusung the
            # util methods which already exists to get the unique storage IDs from
            # the available storage inventory.When we checked existing code, we are
            # only consuming /Storage endpoint calls which is equivalent to local_Storage_v2.
            # Hence using LSv2 for computing this.
            (
                ALL_STORAGE_IDS,
                not_ready,
            ) = await storage_configuration_utils.get_all_storage_ids_from_members(
                local_storage_v2.get(DATA_KEY)
            )
            self.logger.debug("ALL_STORAGE_IDS : %s", ALL_STORAGE_IDS)
            # Format the inventory in the format {'STORAGE_ID1' : {},'STORAGE_ID2' : {}}
            formatted_storage_inventory = await storage_configuration_utils.get_formatted_storage_inventory_for_inventory_list(
                local_storage_v2.get(DATA_KEY),
                ALL_STORAGE_IDS,
                context.associated_resource,
                self.logger,
            )
            self.logger.debug(
                "Formatted storage inventory : %s", formatted_storage_inventory
            )
            server_payload[STORAGE_INVENTORY] = formatted_storage_inventory
        return server_payload
    # Devices table in Cobalt have a minimal version of complete firmware inventory.
    # Hence, we need to format the current full firmware inventory to a minimal one
    # before saving to devices table in cobalt.
    def format_fw_inventory(self, members):
        fw_inv = []
        self.logger.debug("Firmware inventory retrieved : %s", members)
        if members:
            for member in members if type(members) is list else members.get(DATA_KEY):
                fw_inv_item = FirmwareInventoryItem(
                    name=member[NAME],
                    version=member[VERSION] if member[VERSION] else NOT_APPLICABLE,
                    device_context=member[OEM][HPE][DEVICE_CONTEXT],
                )
                fw_inv.append(fw_inv_item)
        self.logger.debug("Formatted Firmware Inventory : %s", fw_inv)
        return fw_inv
    # Devices table in Cobalt have a minimal version of complete Software inventory.
    # Hence, we need to format the current full software inventory to a minimal one
    # before saving to devices table in cobalt.
    def format_sw_inventory(self, members):
        sw_inv = []
        self.logger.debug("Software inventory retrieved : %s", members)
        if members:
            for member in members if type(members) is list else members.get(DATA_KEY):
                self.logger.debug("Software member : %s", member)
                hpe = member[OEM][HPE]
                device_context = hpe.get(DEVICE_CONTEXT, None)
                sw_inv_item = SoftwareInventoryItem(
                    name=member[NAME],
                    version=member[VERSION] if member[VERSION] else NOT_APPLICABLE,
                    device_context=(
                        device_context if device_context else member[DESCRIPTION]
                    ),
                )
                sw_inv.append(sw_inv_item)
        self.logger.debug("Formatted Software Inventory : %s", sw_inv)
        return sw_inv
    # Extract subresources from the inventory response
    def extract_data_from_response(
        self, subresource_name, redfish_resources, filter_array, filter_name
    ):
        resource_data = {}
        if filter_name not in filter_array:
            self.logger.debug(
                "Inventory for : %s is not requested via filters. Hence not extracting it from response.",
                subresource_name,
            )
            return (
                resource_data
                if FeatureFlags.T_20230901_13831_UPDATED_INVENTORY_DATA()
                else []
            )
        self.logger.debug("Extracting data for subresource : %s", subresource_name)
        subresource_data = redfish_resources.get(subresource_name)
        if FeatureFlags.T_20230901_13831_UPDATED_INVENTORY_DATA():
            if subresource_data:
                resource_data = {
                    DATA_KEY: self.add_only_non_null_members(
                        subresource_data.get(DATA_KEY)
                    ),
                    COLLECTION_STATE: (
                        subresource_data.get(STATUS_LOWERCASE)
                        if subresource_data.get(STATUS_LOWERCASE)
                        else subresource_data.get(COLLECTION_STATE_CAMELCASE)
                    ),
                }
            return resource_data
        else:
            return (
                self.add_only_non_null_members(subresource_data.get(DATA_KEY))
                if subresource_data
                else []
            )
    """
    Raw-Inventory table expects an array with all non-none data.
    Hence, this util method will filter out any possible None member
    from data array.
    """
    def add_only_non_null_members(self, data):
        if data and type(data) is list:
            filtered_members = [member for member in data if member is not None]
            return filtered_members
        else:
            return data
    """
    Inventory table expects data to be in the format:
    subresourceName: {
        "data" : actual_data_json_array
    }
    Hence, this util method will convert data to this format and
    return to the caller.
    """
    def format_to_inventory(self, inventory):
        subresource_data = {DATA_KEY: inventory}
        self.logger.debug("data : %s", subresource_data)
        return subresource_data
class PowerOffServerIfNeeded(JobPollingStep):
    def __init__(
        self,
        job_messaging_client: JobMessagingClient,
        job_resource_api: JobResourceApi,
        ilo_resource_api: IloResourceApi,
    ):
        super().__init__()
        self.job_messaging_client = job_messaging_client
        self.job_resource_api = job_resource_api
        self.RETRIES = 5
        self.ilo_resource_api = ilo_resource_api
        self.logger.debug("Starting job step : PowerOffServerIfNeeded")
    async def logic(self, context: JobContext):
        if inventory_utils.is_power_on_needed_during_inventory(context):
            context.data[CURRENT_STEP] += 1
            context.status = "Powering off the server"
            # PLEASE dont change the text "Starting full inventory collection" in below log. This is used for inventory dashboard
            self.logger.info(
                "Starting powering OFF for server %s with job %s via RAS",
                context.associated_resource_uri,
                context.job_id,
            )
            request = {
                "verb": "performAction",
                "actions": [{"action": "ForcePowerOffServer"}],
            }
            self.logger.info("Power Off Request : %s", request)
            await self.job_messaging_client.add_request_message_to_job_context(
                context, RequestMessage(RAS_REQUESTS_TOPIC, request)
            )
            self.logger.info(
                "Submitted the Power OFF request to RAS for the server %s with job : %s",
                context.associated_resource_uri,
                context.job_id,
            )
        else:
            self.logger.info(
                "Server didnt powered ON as part of this inventory. So not trying to power off server : %s",
                context.associated_resource_uri,
            )
            # If there are any exceptions in the earlier steps, throw it here and mark the job as failed.
            if Helper.is_last_jobstep_failed(context):
                self.logger.error(
                    "There is an error in the inventory collection. Error : %s",
                    context.data[ERROR_MESSAGE],
                )
                raise JobErrorException(context.data[ERROR_MESSAGE])
            else:
                self.logger.info(
                    "Server inventory collection is successful for the server %s",
                    context.associated_resource_uri,
                )
    async def process_response(self, context: JobContext):
        self.logger.info(
            "In PowerOffServerIfNeeded.process_response PowerOffServerIfNeeded for server : %s. isOneViewServer : %s. with job : %s.",
            context.associated_resource_uri,
            context.data[IS_ONEVIEW_SERVER],
            context.job_id,
        )
        # Ignore any message which is not a RAS returned one. All RAS returned response
        # will have taskStatus in its message body. So to avoid unnecessary processing,
        # we are ignoring the message amd initiate the retry immediately. Also, we will not
        # update the retry count in such cases because, here we really didnt do any try to
        # process the response.
        # Ideally, we should not end up with this condition, but if there are any issue with
        # the requestId, we may start processing the responses in which case, we dont want
        # to process such responses which are not returned by RAS.
        if (
            not context.response_data.data
            or TASK_STATUS not in context.response_data.data
        ):
            self.logger.info(
                "Not a RAS response. Hence ignoring. context.step_retries = %s, server : %s",
                context.step_retries,
                context.associated_resource_uri,
            )
            raise JobRetryWithErrorException()
        task_state = context.response_data.data[TASK_STATE]
        task_status = context.response_data.data[TASK_STATUS]
        ras_task = context.response_data.data[TASK_MONITOR]
        context.data[TASK_MONITOR] = ras_task
        response_status = await common_utils.get_response_status_from_ras_message(
            context.response_data
        )
        self.logger.info(
            "RAS ForcePowerOff Task = %s, TaskStatus = %s, TaskState = %s, status : %s for the server : %s",
            ras_task,
            task_status,
            task_state,
            response_status,
            context.associated_resource_uri,
        )
        if task_state == "Running":
            self.logger.debug(
                "Power OFF RAS task is still running on server : %s",
                context.associated_resource_uri,
            )
            raise JobRetryWithErrorException()
        else:
            if response_status == 200:
                message = context.response_data
                # Adding some basic validations for the returned data
                if (
                    not message
                    or not message.data
                    or not message.data.get(PAYLOAD)
                    or not message.data.get(PAYLOAD).get(BODY)
                    or not message.data.get(PAYLOAD).get(BODY).get(REDFISH_RESOURCES)
                ):
                    self.logger.error(
                        "Recieved data from PowerOff task is incomplete. Hence marking the inventory job as error for the server : %s. RAS response : %s",
                        context.associated_resource_uri,
                        message,
                    )
                    error_msg = "Marking the inventory job as error. Recieved RAS Kafka message for PowerOFF is either empty or have no data."
                    context.results["FAILURE_REASON"] = "EMPTY_RESPONSE"
                    raise JobErrorException(error_msg)
                self.logger.info(
                    "Power off completed for server : %s",
                    context.associated_resource_uri,
                )
                # If there are any exceptions in the earlier steps, throw it here and mark the job as failed.
                if Helper.is_last_jobstep_failed(context):
                    self.logger.error(context.data[ERROR_MESSAGE])
                    raise JobErrorException(context.data[ERROR_MESSAGE])
                self.logger.info(
                    "Server inventory collection is successful for the server %s",
                    context.associated_resource_uri,
                )
            else:
                # If retries are exhausted, or if the inventory task was a failure, then we dont want to update the
                # inventory, but we will mark the job as failure. We wont even persist the partial inventory
                context.data[
                    common_utils.STATE_REASON_MESSAGE
                ] = await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_INTERNAL_ERROR"
                context.data[common_utils.STATE_REASON_MESSAGE] = (
                    await common_utils.get_job_state_reason_message(
                        "INV_COLLECTION_INTERNAL_ERROR"
                    )
                )
                if task_status == TASK_CRITICAL or task_state == TASK_EXCEPTION:
                    error_msg = f"Marking the inventory job as error for job:{context.job_id}. An unexpected or failed response was received during get server inventory. Response status: {response_status}"
                    context.results["FAILURE_REASON"] = "INTERNAL_ERROR"
                    raise JobErrorException(error_msg)
                elif context.step_retries >= self.RETRIES:
                    error_msg = f"Marking the inventory job as error for job :{context.job_id}  because it timed out waiting for RAS task {context.data[TASK_MONITOR]} to complete."
                    context.results["FAILURE_REASON"] = "RETRIES_EXHAUSTED"
                    raise JobErrorException(error_msg)
                else:
                    # If taskStatus or taskState are not failed terminal, then we dont mark the job as error,
                    # but we simply wait for next message processing.
                    raise JobRetryWithErrorException()
    async def retry(self, context: JobContext):
        # We dont want to retry any inventory fetch logic. We just need to retry fetching
        # the response from the next incoming message.
        self.logger.debug(
            "PowerOffServerIfNeeded: context.step_retries count : %s, self.RETRIES : %s, server : %s",
            context.step_retries,
            self.RETRIES,
            context.associated_resource_uri,
        )
        if context.step_retries >= self.RETRIES:
            error_msg = (
                f"Unable to power off server after {context.step_retries} attempts."
            )
            context.results["FAILURE_REASON"] = "RETRIES_EXHAUSTED"
            context.data[
                common_utils.STATE_REASON_MESSAGE
            ] = await common_utils.get_job_state_reason_message(
                "INV_COLLECTION_INTERNAL_ERROR"
            context.data[common_utils.STATE_REASON_MESSAGE] = (
                await common_utils.get_job_state_reason_message(
                    "INV_COLLECTION_INTERNAL_ERROR"
                )
            )
            await common_utils.ahs_download_job(
                self.logger, context, self.job_resource_api
            )
            raise JobErrorException(error_msg)
"""
These are the steps that gets executed as part of this job.
"""
# Step1: Validate the data payload
root = JobNode(ValidatePayload)
# Step2: Create root node with GetServerFromCobalt
getServerFromCobaltNode = root.add_node(JobNode(GetServerFromCobalt))
terminateJobNode = JobNode(PowerOffServerIfNeeded, when=Helper.is_last_jobstep_failed)
# Step3: Power on the server if needed
powerOnServerNode = getServerFromCobaltNode.add_node(JobNode(PowerOnServerIfNeeded))
# Step 4: If is_oneview_server is True, then we need to call GetFullInventoryForOneViewServer. Else,
# we need to call GetFullInventoryForDirectConnectServers
getFullInventoryForOneViewServer = JobNode(
    GetFullInventoryForOneViewServer,
    when=Helper.is_oneview_server_and_jobstep_success,
)
getFullInventoryForDirectConnectServers = JobNode(
    GetFullInventoryForDirectConnectServers,
    when=Helper.is_not_oneview_server_and_jobstep_success,
)
dcFullInventoryNode = powerOnServerNode.add_node(
    getFullInventoryForDirectConnectServers
)
ovcFullInventoryNode = powerOnServerNode.add_node(getFullInventoryForOneViewServer)
powerOnServerNode.add_node(terminateJobNode)
# Step 5: After collecting inventory by either of the nodes, we need to then save the data to Cobalt
# by calling SaveInventoryToCobalt
saveInventoryToCobaltNode = JobNode(
    SaveInventoryToCobalt,
    when=Helper.is_last_jobstep_success,
)
dcFullInventoryNode.add_node(saveInventoryToCobaltNode)
dcFullInventoryNode.add_node(terminateJobNode)
ovcFullInventoryNode.add_node(saveInventoryToCobaltNode)
ovcFullInventoryNode.add_node(terminateJobNode)
# Step 6: Power off the server if needed
powerOffServerNode = saveInventoryToCobaltNode.add_node(JobNode(PowerOffServerIfNeeded))
job_tree = JobTree(root)
"""
 Get Server Inventory Job tree flow:
  ┌──────Step 1──────────────┐
  │                          │
  │ ┌──────▼──────────────┐  │
  │ |  ValidatePayload    |  ├
  │ └─────────────────────┘  │
  └──────────────────────────┘
            │
            ▼
  ┌──────Step 2──────────────┐
  │                          │
  │ ┌──────▼──────────────┐  │
  │ │GetServerFromCobalt  |  │
  │ └─────────────────────┘  │
  └──────────────────────────┘
            │
            ▼
  ┌──────Step 3─────────────────┐
  │                             │
  │ ┌──────▼─────────────────┐  │                         Is there a failure?
  │ | PowerOnServerIfNeeded  |  ├──┼──────────────┐
  │ └────────────────────────┘  │                 │
  └─────────────────────────────┘                 ▼
                                            Is there a failure? ─────────────────────────────────────────────────────┐
                                                  │                                                                  │
                                                  │ No                                                               │
                                                  │                                                                  │
                                                  ▼                                                                  │
                                            Is OneView Server ?                                                      │
                                                  │                                                                  │
┌────────────────Step 4───────────────────┐       │       ┌────────────────────Step 4───────────────────────┐        │
│ ┌────────────────────────────────────┐  │   Yes │ No    │  ┌───────────────────────────────────────────┐  │ Error? │
│ │  getFullInventoryForOneViewServer  │  │◄──────┴──────►│  │  getFullInventoryForDirectConnectServers  │  |────────│
│ └────────────────────────────────────┘  │               │  └───────────────────────────────────────────┘  │        │
└───────────────┬─────────────────────────┘               └──────────────────────┬──────────────────────────┘        │
                │                                                                │                                   │
                │              ┌──────────────Step 5────────────────┐            │                                   │
                │              │      ┌────────────────────────┐    │            │                                   │
                └─────────────►│      │ SaveInventoryToCobalt  │    │◄───────────┘                                   │
                               │      └────────────────────────┘    │                                                │
                               └────────────────────────────────────┘                                                │
                                                 │                                                                   │
                                                 ▼                                                                   │
                                    ┌──────Step 6─────────────────┐                                                  │
                                    │                             │                                                  |
                                    │ ┌──────▼─────────────────┐  │                                                  |
                                    │ | PowerOffServerIfNeeded |  ├◄─────────────────────────────────────────────────┘
                                    │ └────────────────────────┘  │
                                    └─────────────────────────────┘
"""
  1 change: 1 addition & 0 deletions1  
enigma/core/feature_flags.py
Viewed
Original file line number	Diff line number	Diff line change
@@ -75,3 +75,4 @@ class FeatureFlags(CommonFeatureFlags):
    T_20240718_45992_BLOCKILO_160_BOOL = FeatureFlag(False)
    T_20240731_32913_ENHANCED_ONEVIEW_APPLIANCE_AUTH_SETTINGS_BOOL = FeatureFlag(False)
    T_20240522_CCSPM2809_INSIGHTS_BOOL = FeatureFlag(False)
    T_20240717_35495_STABLE_SERVERS_API_BOOL = FeatureFlag(False)
  2 changes: 1 addition & 1 deletion2  
enigma/core/interfaces/ilo_resource_api.py
Viewed
Original file line number	Diff line number	Diff line change
@@ -117,7 +117,7 @@ async def get_ilos_for_acid(self, acid: str) -> Optional[List[Server]]:
        """
        raise NotImplementedError

    async def get_ilo_inventory_v1beta2(self, id: str):
    async def get_ilo_inventory(self, id: str):
        """
        Gets the inventory data for the provided iLO. This data is fetched from cobalt
        inventory table
  9 changes: 5 additions & 4 deletions9  
enigma/infrastructure/clients/cobalt_ilo_resource_api.py
Viewed
Original file line number	Diff line number	Diff line change
@@ -68,6 +68,7 @@ def get_query_params(devices: List[str]):
class CobaltIloResourceApi(IloResourceApi):
    COBALT_API_URL = config.COBALT_API_URL
    ILO_RESOURCE_URI = "/compute/v1/servers/"
    STABLE_ILO_RESOURCE_URI = "/compute-ops-mgmt/v1/servers/"
    APPLIANCE_URI = "/compute/v1/appliances/"
    APPLIANCE_SERVER = "/servers"
    # Need at least v1beta1 for pagination.
@@ -249,7 +250,7 @@ async def update_ilo_raw_inventory(
    async def get_ilo_raw_inventory(self, id: str) -> Optional[RawInventory]:
        async with ClientSession() as session:
            async with session.get(
                f"{self.COBALT_API_URL}{self.ILO_RESOURCE_URI}{id}{self.ILO_RAW_INVENTORY_RESOURCE_URI}",
                f"{self.COBALT_API_URL}{self.STABLE_ILO_RESOURCE_URI if FeatureFlags.T_20240717_35495_STABLE_SERVERS_API_BOOL() else self.ILO_RESOURCE_URI}{id}{self.ILO_RAW_INVENTORY_RESOURCE_URI}",
                timeout=self.TIMEOUT_IN_SECONDS,
                retry_options=RETRY_OPTIONS,
            ) as resp:
@@ -306,7 +307,7 @@ async def __send_post_for_inventory_with_payload(self, json_data, id, methodname
        params["format"] = "json"
        async with ClientSession() as session:
            async with session.post(
                f"{self.COBALT_API_URL}{self.SERVER_URI}{id}{self.ILO_INVENTORY_RESOURCE_URI}",
                f"{self.COBALT_API_URL}{self.STABLE_ILO_RESOURCE_URI if FeatureFlags.T_20240717_35495_STABLE_SERVERS_API_BOOL() else self.SERVER_URI}{id}{self.ILO_INVENTORY_RESOURCE_URI}",
                json=json_data,
                params=params,
                timeout=config.TIMEOUT_IN_SECONDS,
@@ -663,10 +664,10 @@ async def get_ilos_for_acid(self, acid) -> Optional[List[Server]]:
            )
        return flatten_nested_batches(servers)

    async def get_ilo_inventory_v1beta2(self, id: str):
    async def get_ilo_inventory(self, id: str):
        async with ClientSession() as session:
            async with session.get(
                f"{self.COBALT_API_URL}{self.ILO_RESOURCE_V1BETA2_SERVERS}/{id}{self.ILO_INVENTORY_RESOURCE_URI}",
                f"{self.COBALT_API_URL}{self.STABLE_ILO_RESOURCE_URI if FeatureFlags.T_20240717_35495_STABLE_SERVERS_API_BOOL() else self.ILO_RESOURCE_V1BETA2_SERVERS}/{id}{self.ILO_INVENTORY_RESOURCE_URI}",
                timeout=self.TIMEOUT_IN_SECONDS,
                retry_options=RETRY_OPTIONS,
            ) as resp: