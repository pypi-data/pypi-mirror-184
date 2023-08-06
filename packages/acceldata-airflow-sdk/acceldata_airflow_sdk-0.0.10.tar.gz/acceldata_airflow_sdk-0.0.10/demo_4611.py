# from acceldata_sdk.torch_client import TorchClient
# import acceldata_sdk.constants as const
# from acceldata_sdk.models.tags import AssetLabel
# from acceldata_sdk.models.profile import ProfilingType
# from acceldata_sdk.models.assetType import AssetType
# from acceldata_sdk.models.profile import AutoProfileConfiguration, Profile, ProfileRequest, ProfilingType
import pprint
from semantic_version import Version, SimpleSpec


# from acceldata_sdk.torch_client import TorchClient
# from acceldata_sdk.models.pipeline import CreatePipeline, PipelineMetadata, PipelineRunResult, PipelineRunStatus
import pprint
from datetime import datetime
# from acceldata_sdk.models.job import CreateJob, JobMetadata, Node
# from acceldata_sdk.events.generic_event import GenericEvent
from acceldata_airflow_sdk.utils.torch_client import TorchDAGClient
pp = pprint.PrettyPrinter(indent=4)


torch_dag_client = TorchDAGClient()
pipelineRun = torch_dag_client.get_pipeline_run(pipeline_run_id=244)
pp.pprint('pipelineRun run id 244')
pp.pprint(pipelineRun)
pipeline = torch_dag_client.get_pipeline(42)
pipelineRun = torch_dag_client.get_pipeline_run(continuation_id='heterogeneous_test1', pipeline_id=42)
pp.pprint('pipeline')
pp.pprint(pipeline)
pp.pprint('pipelineRun cont id 244 pipeline id 42')
pp.pprint(pipelineRun)
exit()

# from acceldata_airflow_sdk.initialiser import torch_credentials
# torch_client = TorchClient(**torch_credentials())
#
# torch_credentials = {
#     'url':  'https://acceldata.dev.10.90.3.89.nip.io',
#     'access_key':  '21DK0CVJUAE0LET',
#     'secret_key':  '1PT5E06TLCHKGELZCOEC7LLOCPYHJO',
#     'do_version_check': False
# }
# torchClient = TorchClient(**torch_credentials)
# ds_id = torchClient.get_datasource('1', True)
# status = ds_id.get_crawler_status()
# # asset = torchClient.get_asset(4)
# # sample_data_asset = asset.sample_data()
#
# asset = torchClient.get_asset(4)
# start_profile_asset = asset.start_profile(ProfilingType.FULL)
# profile_status = start_profile_asset.get_status()
# if profile_status['profileRequest']['status'] == 'IN PROGRESS':
#     cancel_res = start_profile_asset.cancel()
#     assert cancel_res is not None
# exit()
# from acceldata_sdk.torch_client import TorchClient
#
# torchClient = TorchClient(url="https://winterfel.qetest.acceldata.dev", access_key="S58A3VBB7L3T5PZ",
#                           secret_key="51YPWKNLXOUZMI4QTTKIPRKYQBZX9W",do_version_check=False)
#
# torchClient = TorchClient(url="https://torchtenant.unified.acceldata.tech", access_key="TXU3N9MDGN7ZIZD",
#                                   secret_key="OGWX9ONR37CQFKL2EL7S4NBKPY433G", do_version_check=False)


torch_credentials = {
    'url': 'https://torch.acceldata.local:5443/torch',
    'access_key': 'P04IM8FNQRUCRTU',
    'secret_key': 'E6LL9YUPMG4BDTJHT2VZD75HW0B8E5',
    'do_version_check': 'False'
}
torch_client = TorchClient(**torch_credentials)
torch_dag_client = TorchDAGClient()
pp.pprint(torch_credentials)
pipelineRun = torch_dag_client.get_pipeline_run(pipeline_run_id=244)
pp.pprint('pipelineRun run id 244')
pp.pprint(pipelineRun)
pipeline = torch_dag_client.get_pipeline(42)
pipelineRun = torch_dag_client.get_pipeline_run(continuation_id='heterogeneous_test1', pipeline_id=42)
pp.pprint('pipeline')
pp.pprint(pipeline)
pp.pprint('pipelineRun cont id 244 pipeline id 42')
pp.pprint(pipelineRun)
exit()
# supported_versions = torch_client.get_supported_sdk_versions()
# pp.pprint('supported_versions')
# pp.pprint(supported_versions)
# torch_version = torch_client.get_torch_version()
# pp.pprint('torch_version')
# pp.pprint(torch_version)
#
# supported_versions = torch_client.get_supported_sdk_versions()
# torch_version: str = torch_client.get_torch_version()
# if torch_version.buildVersion is not None and torch_version.buildVersion != "":
#     actual_version = torch_version.buildVersion[:5]
# else:
#     actual_version = supported_versions.maxVersion
# ver_comparator = SimpleSpec(f'<={actual_version}')
# if Version('2.5.0') in ver_comparator:
#     print ("new call")
# else:
#     print ("old call")
# exit()
# meta = PipelineMetadata(owner='sdk/pipeline-user', team='TORCH', codeLocation='...')
#
# pipeline = CreatePipeline(
#     uid="test_backward.apipeline",
#     name="test_backward.apipeline",
#     description=f'The pipeline "test_backward.apipeline" has been created from torch-sdk',
#     meta=meta,
#     context={'pipeline_uid': "test_backward.apipeline", 'pipeline_name': "test_backward.apipeline"}
# )
# pipeline = torch_client.create_pipeline(pipeline)
# pipeline_run = pipeline.create_pipeline_run(continuation_id="test_aackward_compat7", context_data={'key1': 'value2', 'name': 'backend'})
# pipeline_run = pipeline.get_run(continuation_id="test_aackward_compat5")
# rootSpan = pipeline_run.get_root_span()

# inputs = [Node(job_uid='customers.data-generation')]
# outputs = [Node(asset_uid=f'S3-DS.s3_customers')]
# context_job = {'job': 'data_gene', 'time': str(datetime.now()), 'uid': 'customers.data-generation',
#                'operator': 'write_file_func'}
# metadata = JobMetadata('Jason', 'COKE', 'https://github.com/coke/reports/customers.kt')
# # pipeline = torch_client.get_pipeline(pipeline_uid)
# latest_run = pipeline.get_latest_pipeline_run()
# job_uid = "span_bound.test"
# job = CreateJob(
#     uid=job_uid,
#     name=f'{job_uid} Job',
#     pipeline_run_id=latest_run.id,
#     description=f'{job_uid} created using torch SDK',
#     inputs=inputs,
#     outputs=outputs,
#     meta=metadata,
#     context=context_job,
#     bounded_by_span=True,
#     span_uid="test_shubh"
# )
# job = pipeline.create_job(job)
#
# job_uid = "span_bound.test2"
# job = CreateJob(
#     uid=job_uid,
#     name=f'{job_uid} Job',
#     description=f'{job_uid} created using torch SDK',
#     inputs=inputs,
#     outputs=outputs,
#     meta=metadata,
#     context=context_job,
#     bounded_by_span=True,
#     span_uid="test_shubh"
# )
# job = latest_run.create_job(job)
# exit()
# torchClient = TorchClient(**torch_credentials)
# assemblyName = "COMPUTE_WH"
# torchClient.get_datasource(assemblyName,False)
# torchClient.get_datasource(const.AssetSourceType.SNOWFLAKE)
# exit()
# base_path = 's3a://demo-data-plane-one/execution_result'
# good_data_location = 's3a://demo-data-plane-one/execution_result/2022-09-29/segmented_cc/_1664445283208/successrecords'
# stage_path_suffix=good_data_location.lstrip(base_path)

#
# torch_client = TorchClient(url='https://dataplaneone.cp.torch.demo.acceldata.dev/torch', access_key='3557ZXXOEYVCCX0', secret_key='FH8YHP3GZPFHIAH5MWQOIZKSSK202C', do_version_check=False)
#
# recon_rule_id=132
# # import pdb;pdb.set_trace()
# sync_execution_result = torch_client.get_policy_execution_result(const.PolicyType.DATA_QUALITY, 30)
# import json
# persitence_paths = json.loads(sync_execution_result.execution.persistencePath)
# persitence_path_configs = persitence_paths['persistencePathConfigs']
# for path in persitence_path_configs:
#     if path['recordType'] == 'GOOD':
#         base_path = path['basePath']
# good_data_location = sync_execution_result.execution.resultPersistencePath['goodDataLocation']
# stage_path_suffix=good_data_location.lstrip(base_path)
# stage_name='@shubh_ext_stage2/'
# stage_load_data_path = stage_name + stage_path_suffix
# pp(stage_load_data_path)


# sync_execution_result = recon_rule2.get_result()

# pipeline_uid = "torch.airflow.demo.lambda"
# torch_credentials = {
#     'url': 'https://torchdemo.acceldata.tech/torch',
#     'access_key': 'V05DG18TV4MAF93',
#     'secret_key': 'VZF8O9Q5G6GUE08MQY5A8CA0TAE5KD'
# }
# torch_credentials = {
#     'url': 'https://torch.acceldata.local:5443/torch',
#     'access_key': 'P04IM8FNQRUCRTU',
#     'secret_key': 'E6LL9YUPMG4BDTJHT2VZD75HW0B8E5',
#     'do_version_check': 'True'
# }

# torch_credentials = {
#     'url':  'https://acceldata.dev.10.90.3.89.nip.io',
#     'access_key': '21DK0CVJUAE0LET',
#     'secret_key': '1PT5E06TLCHKGELZCOEC7LLOCPYHJO'
# }

# torch_credentials = {
#     'url': 'https://yubi.torch.acceldata.dev/torch',
#     'access_key': 'SAQ8XAOLSSLAD16',
#     'secret_key': 'KL5C4UA5XBQ2HBUMQPATJ3FB45HRH9'
# }


# recon_rule_id=1
# # import pdb;pdb.set_trace()
# torch_client = TorchClient(**torch_credentials)
#
# recon_rule2 = torch_client.execute_policy(const.PolicyType.DATA_QUALITY, recon_rule_id, sync=True, incremental=False, pipeline_run_id=401)
# sync_execution_result = recon_rule2.get_result()
# exit(0)

######## suman 2.3.0 test
# torch_credentials = {
#     'url': 'https://torchtenant.unified.acceldata.tech',
#     'access_key': 'TXU3N9MDGN7ZIZD',
#     'secret_key': 'OGWX9ONR37CQFKL2EL7S4NBKPY433G'
# }
# torch_credentials = {
#     'url': 'https://jeevan.verisk.demo.acceldata.tech/torch',
#     'access_key': 'HVN976UDHFQUJ52',
#     'secret_key': '57RBZ3693XA3DC92UN3A4XS42JXV6X'
# }

#    TORCH_CATALOG_URL: "https://jeevan.verisk.demo.acceldata.tech/torch"
#    TORCH_ACCESS_KEY: "HVN976UDHFQUJ52"
#    TORCH_SECRET_KEY: "57RBZ3693XA3DC92UN3A4XS42JXV6X"
# torch_client = TorchClient(**torch_credentials)
# supported_versions = torch_client.get_supported_sdk_versions()
# pp.pprint('supported_versions')
# pp.pprint(supported_versions)


# asset = torch_client.get_asset(95775)
# jeevan verisk torch enterprise
# asset = torch_client.get_asset(4)
#
# pp.pprint('asset')
# pp.pprint(asset)
# metadata_asset = asset.get_metadata()
# pp.pprint('metadata_asset')
# pp.pprint(metadata_asset)
# sample_asset = asset.sample_data()
# pp.pprint('sample_asset')
# pp.pprint(sample_asset)

# asset.add_labels(labels=[AssetLabel('test1', 'shubh1'), AssetLabel('test2', 'shubh3')])
# labels_asset = asset.get_labels()
# pp.pprint('labels_asset')
# pp.pprint(labels_asset)
# exit()
###############

#### pipelines ###
torch_client = TorchClient(**torch_credentials)
# supported_versions = torch_client.get_supported_sdk_versions()
# pp.pprint('supported_versions')
# pp.pprint(supported_versions)

pipelineRun = torch_client.get_pipeline_run(pipeline_run_id=244)
pp.pprint('pipelineRun run id 244')
pp.pprint(pipelineRun)
# exit()
pipeline = torch_client.get_pipeline(42)
pipelineRun = torch_client.get_pipeline_run(continuation_id='heterogeneous_test1', pipeline_id=42)

pp.pprint('pipeline')
pp.pprint(pipeline)
pp.pprint('pipelineRun cont id 244 pipeline id 42')
pp.pprint(pipelineRun)
exit()
# runs = pipeline.get_runs()
# pp.pprint('runs')
# pp.pprint(runs)
# pipeline_uid = torch_client.get_pipeline('torch.airflow.demo.lambda')
# pp.pprint('pipeline_uid')
# pp.pprint(pipeline_uid)
# pipelines = torch_client.get_pipelines()
# pp.pprint('pipelines')
# pp.pprint(pipelines)
# pipelineRun = torch_client.get_pipeline_run(244)
# pp.pprint('pipelineRun')
# pp.pprint(pipelineRun)
# pipeline_details = pipelineRun.get_details()
# pp.pprint('pipeline_details')
# pp.pprint(pipeline_details)
# pipeline_spans = pipelineRun.get_spans()
# pp.pprint('pipeline_spans')
# pp.pprint(pipeline_spans)
# pipeline = torch_client.get_pipeline(33)
# delete_response = pipeline.delete()
#### pipelines ###
# import pdb;pdb.set_trace()
# async_executor = torch_client.execute_policy(const.PolicyType.DATA_QUALITY, 3, sync=True)
# xcom_key = f'{const.PolicyType.DATA_QUALITY.name}_{3}_execution_id'
# pp.pprint(xcom_key)
# if async_executor.errorMessage is not None:
#     async_execution_result = async_executor.get_result()

###suman test###



torch_credentials = {
    'url': 'https://torch.acceldata.local:5443/torch',
    'access_key': 'P04IM8FNQRUCRTU',
    'secret_key': 'E6LL9YUPMG4BDTJHT2VZD75HW0B8E5'
}
torchclient = TorchClient(**torch_credentials)
# print(torchclient.get_datasource(assemblyName, True))
print(torchclient.get_datasource(1, True))

print(torchclient.get_datasource('sf_ds', True))
print(torchclient.get_datasources(const.AssetSourceType.SNOWFLAKE))
torch_credentials = {
    'url': "https://testtorchswetha.qetest.acceldata.dev",
    'access_key': '95UZMC25GGPU2HD',
    'secret_key': 'ZHRK78X34GH5JBNU4TXYHU2E2AOBCY'
}
torchclient = TorchClient(**torch_credentials)
# print(torchclient.get_datasource(assemblyName, True))
print(torchclient.get_datasource(1, True))

print(torchclient.get_datasource('sf_ds', False))
print(torchclient.get_datasources(const.AssetSourceType.SNOWFLAKE))
exit()
#####

#
# torch_credentials = {
#     'url': 'https://test.torch1001.acceldata.dev/torch',
#     'access_key': 'WKZW28UJGPHVJZJ',
#     'secret_key': '5XP4HKAK0PBP00UQOUF89FEWDO7ZB6'
# }


'''dss = torch_client.get_datasources()
pp.pprint('datasources')
pp.pprint(dss)
dss = torch_client.get_datasources(const.AssetSourceType.SNOWFLAKE)
pp.pprint('datasources snowflake')
pp.pprint(dss)

ds = torch_client.get_datasource(1, True)
pp.pprint('datasource with properties')
pp.pprint(ds)
asset = ds.get_asset(251)
pp.pprint('asset')
pp.pprint(asset)
response_start_crawler = ds.start_crawler()
pp.pprint('response_start_crawler')
pp.pprint(response_start_crawler)
response_status_crawler = ds.get_crawler_status()
pp.pprint('response_status_crawler')
pp.pprint(response_status_crawler)'''

# asset = torch_client.get_asset(251)
# pp.pprint('asset')
# pp.pprint(asset)
'''metadata_asset = asset.get_metadata()
pp.pprint('metadata_asset')
pp.pprint(metadata_asset)
sample_asset = asset.sample_data()
pp.pprint('sample_asset')
pp.pprint(sample_asset)

asset.add_labels(labels=[AssetLabel('test1', 'shubh1'), AssetLabel('test2', 'shubh3')])
labels_asset = asset.get_labels()
pp.pprint('labels_asset')
pp.pprint(labels_asset)
asset.add_custom_metadata(custom_metadata=[CustomAssetMetadata('testcm1', 'shubhcm1'), CustomAssetMetadata('testcm2', 'shubhcm2')])
latest_profile_status_asset = asset.get_latest_profile_status()
pp.pprint('latest_profile_status_asset')
pp.pprint(latest_profile_status_asset)'''
start_profile_asset = asset.start_profile(ProfilingType.FULL)
pp.pprint('start_profile_asset')
pp.pprint(start_profile_asset)
profile_status = start_profile_asset.get_status()
pp.pprint('profile_status')
pp.pprint(profile_status)
cancel_res = profile_status = start_profile_asset.cancel()
pp.pprint('cancel_res')
pp.pprint(cancel_res)



# asset2 = ds.get_asset(1558)
# dq_rule = torch_client.get_policy(const.PolicyType.RECONCILIATION, "auth001_reconciliation")
from acceldata_sdk.models.ruleExecutionResult import RuleType, PolicyFilter, ExecutionPeriod
# filter = PolicyFilter(policyType=RuleType.RECONCILIATION, enable=True)
dq_rule_execution = torch_client.get_all_rule_execution(RuleType.DATA_QUALITY)
pp.pprint(dq_rule_execution)
filter = PolicyFilter(policyType=RuleType.DATA_QUALITY, enable=True)
dq_rules = torch_client.list_all_policies(filter=filter)
pp.pprint(dq_rules)
# asset = ds.get_asset(1207)
# # asset.add_labels(labels=[AssetLabel('test1', 'shubh1'), AssetLabel('test2', 'shubh3')])
# asset.add_custom_metadata(custom_metadata=[CustomAssetMetadata('testcm1', 'shubhcm1'), CustomAssetMetadata('testcm2', 'shubhcm2')])

# pipeline_uid = "5321.airflow.coke.precreate13594"

# torch_client = TorchClient(**torch_credentials)
# pipeline = torch_client.get_pipeline(pipeline_uid)
# pipeline_run = pipeline.get_latest_pipeline_run()
# span_context = pipeline_run.get_root_span()

# async_executor = torch_client.execute_policy(const.DATA_QUALITY, 46, sync=False)
# async_execution_result = async_executor.get_result()
# import pdb;pdb.set_trace()
# execution_current_status = async_executor.get_status()
# pp.pprint("async_execution_result")
# pp.pprint(async_execution_result)
# #
# sync_executor_result = torch_client.execute_policy(const.DATA_QUALITY, 46, sync=True)
# import pdb;pdb.set_trace()
# #pp.pprint(sync_executor_result)
#
# execution_status = sync_executor_result.get_status(execution_details.id)
# sync_execution_result = sync_executor_result.get_result()
# pp.pprint("sync_execution_result")
# pp.pprint(sync_execution_result)

# torch_client = TorchClient(url='https://demo.acceldata.app', access_key='IV7QOLGIPBUH4M9', secret_key='2FYBOHEU0GDPCFOYIJVE7XK6FWF4IJ')
#
# recon_rule_id=132
# import pdb;pdb.set_trace()
# recon_rule2 = torch_client.execute_policy(const.RECONCILIATION, recon_rule_id, sync=True, incremental=False)
# sync_execution_result = recon_rule2.get_result()

