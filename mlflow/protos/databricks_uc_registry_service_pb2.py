# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: databricks_uc_registry_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import databricks_pb2 as databricks__pb2
from . import databricks_uc_registry_messages_pb2 as databricks_uc_registry_messages_pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$databricks_uc_registry_service.proto\x12\x16mlflow.ucmodelregistry\x1a\x10\x64\x61tabricks.proto\x1a%databricks_uc_registry_messages.proto\x1a\x15scalapb/scalapb.proto2\x87\'\n\x16UcModelRegistryService\x12\xf2\x01\n\x15\x43reateRegisteredModel\x12\x34.mlflow.ucmodelregistry.CreateRegisteredModelRequest\x1a\x35.mlflow.ucmodelregistry.CreateRegisteredModelResponse\"l\xf2\x86\x19h\n<\n\x04POST\x12./mlflow/unity-catalog/registered-models/create\x1a\x04\x08\x02\x10\x00\x10\x03*&(Unity Catalog) Create RegisteredModel\x12\xf3\x01\n\x15UpdateRegisteredModel\x12\x34.mlflow.ucmodelregistry.UpdateRegisteredModelRequest\x1a\x35.mlflow.ucmodelregistry.UpdateRegisteredModelResponse\"m\xf2\x86\x19i\n=\n\x05PATCH\x12./mlflow/unity-catalog/registered-models/update\x1a\x04\x08\x02\x10\x00\x10\x03*&(Unity Catalog) Update RegisteredModel\x12\xf4\x01\n\x15\x44\x65leteRegisteredModel\x12\x34.mlflow.ucmodelregistry.DeleteRegisteredModelRequest\x1a\x35.mlflow.ucmodelregistry.DeleteRegisteredModelResponse\"n\xf2\x86\x19j\n>\n\x06\x44\x45LETE\x12./mlflow/unity-catalog/registered-models/delete\x1a\x04\x08\x02\x10\x00\x10\x03*&(Unity Catalog) Delete RegisteredModel\x12\xe2\x01\n\x12GetRegisteredModel\x12\x31.mlflow.ucmodelregistry.GetRegisteredModelRequest\x1a\x32.mlflow.ucmodelregistry.GetRegisteredModelResponse\"e\xf2\x86\x19\x61\n8\n\x03GET\x12+/mlflow/unity-catalog/registered-models/get\x1a\x04\x08\x02\x10\x00\x10\x03*#(Unity Catalog) Get RegisteredModel\x12\xf5\x01\n\x16SearchRegisteredModels\x12\x35.mlflow.ucmodelregistry.SearchRegisteredModelsRequest\x1a\x36.mlflow.ucmodelregistry.SearchRegisteredModelsResponse\"l\xf2\x86\x19h\n;\n\x03GET\x12./mlflow/unity-catalog/registered-models/search\x1a\x04\x08\x02\x10\x00\x10\x03*\'(Unity Catalog) Search RegisteredModels\x12\xe3\x01\n\x12\x43reateModelVersion\x12\x31.mlflow.ucmodelregistry.CreateModelVersionRequest\x1a\x32.mlflow.ucmodelregistry.CreateModelVersionResponse\"f\xf2\x86\x19\x62\n9\n\x04POST\x12+/mlflow/unity-catalog/model-versions/create\x1a\x04\x08\x02\x10\x00\x10\x03*#(Unity Catalog) Create ModelVersion\x12\xe4\x01\n\x12UpdateModelVersion\x12\x31.mlflow.ucmodelregistry.UpdateModelVersionRequest\x1a\x32.mlflow.ucmodelregistry.UpdateModelVersionResponse\"g\xf2\x86\x19\x63\n:\n\x05PATCH\x12+/mlflow/unity-catalog/model-versions/update\x1a\x04\x08\x02\x10\x00\x10\x03*#(Unity Catalog) Update ModelVersion\x12\xe5\x01\n\x12\x44\x65leteModelVersion\x12\x31.mlflow.ucmodelregistry.DeleteModelVersionRequest\x1a\x32.mlflow.ucmodelregistry.DeleteModelVersionResponse\"h\xf2\x86\x19\x64\n;\n\x06\x44\x45LETE\x12+/mlflow/unity-catalog/model-versions/delete\x1a\x04\x08\x02\x10\x00\x10\x03*#(Unity Catalog) Delete ModelVersion\x12\xd3\x01\n\x0fGetModelVersion\x12..mlflow.ucmodelregistry.GetModelVersionRequest\x1a/.mlflow.ucmodelregistry.GetModelVersionResponse\"_\xf2\x86\x19[\n5\n\x03GET\x12(/mlflow/unity-catalog/model-versions/get\x1a\x04\x08\x02\x10\x00\x10\x03* (Unity Catalog) Get ModelVersion\x12\xe6\x01\n\x13SearchModelVersions\x12\x32.mlflow.ucmodelregistry.SearchModelVersionsRequest\x1a\x33.mlflow.ucmodelregistry.SearchModelVersionsResponse\"f\xf2\x86\x19\x62\n8\n\x03GET\x12+/mlflow/unity-catalog/model-versions/search\x1a\x04\x08\x02\x10\x00\x10\x03*$(Unity Catalog) Search ModelVersions\x12\xd8\x02\n(GenerateTemporaryModelVersionCredentials\x12G.mlflow.ucmodelregistry.GenerateTemporaryModelVersionCredentialsRequest\x1aH.mlflow.ucmodelregistry.GenerateTemporaryModelVersionCredentialsResponse\"\x98\x01\xf2\x86\x19\x93\x01\nQ\n\x04POST\x12\x43/mlflow/unity-catalog/model-versions/generate-temporary-credentials\x1a\x04\x08\x02\x10\x00\x10\x03*<(Unity Catalog) Generate Temporary Model Version Credentials\x12\x9e\x02\n\x1aGetModelVersionDownloadUri\x12\x39.mlflow.ucmodelregistry.GetModelVersionDownloadUriRequest\x1a:.mlflow.ucmodelregistry.GetModelVersionDownloadUriResponse\"\x88\x01\xf2\x86\x19\x83\x01\nB\n\x03GET\x12\x35/mlflow/unity-catalog/model-versions/get-download-uri\x1a\x04\x08\x02\x10\x00\x10\x03*;(Unity Catalog) Get Download URI For ModelVersion Artifacts\x12\xee\x01\n\x14\x46inalizeModelVersion\x12\x33.mlflow.ucmodelregistry.FinalizeModelVersionRequest\x1a\x34.mlflow.ucmodelregistry.FinalizeModelVersionResponse\"k\xf2\x86\x19g\n;\n\x04POST\x12-/mlflow/unity-catalog/model-versions/finalize\x1a\x04\x08\x02\x10\x00\x10\x03*&(Unity Catalog) Finalize Model Version\x12\xfa\x01\n\x17SetRegisteredModelAlias\x12\x36.mlflow.ucmodelregistry.SetRegisteredModelAliasRequest\x1a\x37.mlflow.ucmodelregistry.SetRegisteredModelAliasResponse\"n\xf2\x86\x19j\n;\n\x04POST\x12-/mlflow/unity-catalog/registered-models/alias\x1a\x04\x08\x02\x10\x00\x10\x03*)(Unity Catalog) Set RegisteredModel Alias\x12\x88\x02\n\x1a\x44\x65leteRegisteredModelAlias\x12\x39.mlflow.ucmodelregistry.DeleteRegisteredModelAliasRequest\x1a:.mlflow.ucmodelregistry.DeleteRegisteredModelAliasResponse\"s\xf2\x86\x19o\n=\n\x06\x44\x45LETE\x12-/mlflow/unity-catalog/registered-models/alias\x1a\x04\x08\x02\x10\x00\x10\x03*,(Unity Catalog) Delete RegisteredModel Alias\x12\xf6\x01\n\x16GetModelVersionByAlias\x12\x35.mlflow.ucmodelregistry.GetModelVersionByAliasRequest\x1a\x36.mlflow.ucmodelregistry.GetModelVersionByAliasResponse\"m\xf2\x86\x19i\n:\n\x03GET\x12-/mlflow/unity-catalog/registered-models/alias\x1a\x04\x08\x02\x10\x00\x10\x03*)(Unity Catalog) Get ModelVersion By Alias\x12\xf1\x01\n\x15SetRegisteredModelTag\x12\x34.mlflow.ucmodelregistry.SetRegisteredModelTagRequest\x1a\x35.mlflow.ucmodelregistry.SetRegisteredModelTagResponse\"k\xf2\x86\x19g\n:\n\x04POST\x12,/mlflow/unity-catalog/registered-models/tags\x1a\x04\x08\x02\x10\x00\x10\x03*\'(Unity Catalog) Set RegisteredModel Tag\x12\xff\x01\n\x18\x44\x65leteRegisteredModelTag\x12\x37.mlflow.ucmodelregistry.DeleteRegisteredModelTagRequest\x1a\x38.mlflow.ucmodelregistry.DeleteRegisteredModelTagResponse\"p\xf2\x86\x19l\n<\n\x06\x44\x45LETE\x12,/mlflow/unity-catalog/registered-models/tags\x1a\x04\x08\x02\x10\x00\x10\x03**(Unity Catalog) Delete RegisteredModel Tag\x12\xe2\x01\n\x12SetModelVersionTag\x12\x31.mlflow.ucmodelregistry.SetModelVersionTagRequest\x1a\x32.mlflow.ucmodelregistry.SetModelVersionTagResponse\"e\xf2\x86\x19\x61\n7\n\x04POST\x12)/mlflow/unity-catalog/model-versions/tags\x1a\x04\x08\x02\x10\x00\x10\x03*$(Unity Catalog) Set ModelVersion Tag\x12\xf0\x01\n\x15\x44\x65leteModelVersionTag\x12\x34.mlflow.ucmodelregistry.DeleteModelVersionTagRequest\x1a\x35.mlflow.ucmodelregistry.DeleteModelVersionTagResponse\"j\xf2\x86\x19\x66\n9\n\x06\x44\x45LETE\x12)/mlflow/unity-catalog/model-versions/tags\x1a\x04\x08\x02\x10\x00\x10\x03*\'(Unity Catalog) Delete ModelVersion TagB5\n(com.databricks.api.proto.ucmodelregistry\x90\x01\x01\xa0\x01\x01\xe2?\x02\x10\x01')



_UCMODELREGISTRYSERVICE = DESCRIPTOR.services_by_name['UcModelRegistryService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.databricks.api.proto.ucmodelregistry\220\001\001\240\001\001\342?\002\020\001'
  _UCMODELREGISTRYSERVICE.methods_by_name['CreateRegisteredModel']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['CreateRegisteredModel']._serialized_options = b'\362\206\031h\n<\n\004POST\022./mlflow/unity-catalog/registered-models/create\032\004\010\002\020\000\020\003*&(Unity Catalog) Create RegisteredModel'
  _UCMODELREGISTRYSERVICE.methods_by_name['UpdateRegisteredModel']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['UpdateRegisteredModel']._serialized_options = b'\362\206\031i\n=\n\005PATCH\022./mlflow/unity-catalog/registered-models/update\032\004\010\002\020\000\020\003*&(Unity Catalog) Update RegisteredModel'
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteRegisteredModel']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteRegisteredModel']._serialized_options = b'\362\206\031j\n>\n\006DELETE\022./mlflow/unity-catalog/registered-models/delete\032\004\010\002\020\000\020\003*&(Unity Catalog) Delete RegisteredModel'
  _UCMODELREGISTRYSERVICE.methods_by_name['GetRegisteredModel']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['GetRegisteredModel']._serialized_options = b'\362\206\031a\n8\n\003GET\022+/mlflow/unity-catalog/registered-models/get\032\004\010\002\020\000\020\003*#(Unity Catalog) Get RegisteredModel'
  _UCMODELREGISTRYSERVICE.methods_by_name['SearchRegisteredModels']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['SearchRegisteredModels']._serialized_options = b'\362\206\031h\n;\n\003GET\022./mlflow/unity-catalog/registered-models/search\032\004\010\002\020\000\020\003*\'(Unity Catalog) Search RegisteredModels'
  _UCMODELREGISTRYSERVICE.methods_by_name['CreateModelVersion']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['CreateModelVersion']._serialized_options = b'\362\206\031b\n9\n\004POST\022+/mlflow/unity-catalog/model-versions/create\032\004\010\002\020\000\020\003*#(Unity Catalog) Create ModelVersion'
  _UCMODELREGISTRYSERVICE.methods_by_name['UpdateModelVersion']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['UpdateModelVersion']._serialized_options = b'\362\206\031c\n:\n\005PATCH\022+/mlflow/unity-catalog/model-versions/update\032\004\010\002\020\000\020\003*#(Unity Catalog) Update ModelVersion'
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteModelVersion']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteModelVersion']._serialized_options = b'\362\206\031d\n;\n\006DELETE\022+/mlflow/unity-catalog/model-versions/delete\032\004\010\002\020\000\020\003*#(Unity Catalog) Delete ModelVersion'
  _UCMODELREGISTRYSERVICE.methods_by_name['GetModelVersion']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['GetModelVersion']._serialized_options = b'\362\206\031[\n5\n\003GET\022(/mlflow/unity-catalog/model-versions/get\032\004\010\002\020\000\020\003* (Unity Catalog) Get ModelVersion'
  _UCMODELREGISTRYSERVICE.methods_by_name['SearchModelVersions']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['SearchModelVersions']._serialized_options = b'\362\206\031b\n8\n\003GET\022+/mlflow/unity-catalog/model-versions/search\032\004\010\002\020\000\020\003*$(Unity Catalog) Search ModelVersions'
  _UCMODELREGISTRYSERVICE.methods_by_name['GenerateTemporaryModelVersionCredentials']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['GenerateTemporaryModelVersionCredentials']._serialized_options = b'\362\206\031\223\001\nQ\n\004POST\022C/mlflow/unity-catalog/model-versions/generate-temporary-credentials\032\004\010\002\020\000\020\003*<(Unity Catalog) Generate Temporary Model Version Credentials'
  _UCMODELREGISTRYSERVICE.methods_by_name['GetModelVersionDownloadUri']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['GetModelVersionDownloadUri']._serialized_options = b'\362\206\031\203\001\nB\n\003GET\0225/mlflow/unity-catalog/model-versions/get-download-uri\032\004\010\002\020\000\020\003*;(Unity Catalog) Get Download URI For ModelVersion Artifacts'
  _UCMODELREGISTRYSERVICE.methods_by_name['FinalizeModelVersion']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['FinalizeModelVersion']._serialized_options = b'\362\206\031g\n;\n\004POST\022-/mlflow/unity-catalog/model-versions/finalize\032\004\010\002\020\000\020\003*&(Unity Catalog) Finalize Model Version'
  _UCMODELREGISTRYSERVICE.methods_by_name['SetRegisteredModelAlias']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['SetRegisteredModelAlias']._serialized_options = b'\362\206\031j\n;\n\004POST\022-/mlflow/unity-catalog/registered-models/alias\032\004\010\002\020\000\020\003*)(Unity Catalog) Set RegisteredModel Alias'
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteRegisteredModelAlias']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteRegisteredModelAlias']._serialized_options = b'\362\206\031o\n=\n\006DELETE\022-/mlflow/unity-catalog/registered-models/alias\032\004\010\002\020\000\020\003*,(Unity Catalog) Delete RegisteredModel Alias'
  _UCMODELREGISTRYSERVICE.methods_by_name['GetModelVersionByAlias']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['GetModelVersionByAlias']._serialized_options = b'\362\206\031i\n:\n\003GET\022-/mlflow/unity-catalog/registered-models/alias\032\004\010\002\020\000\020\003*)(Unity Catalog) Get ModelVersion By Alias'
  _UCMODELREGISTRYSERVICE.methods_by_name['SetRegisteredModelTag']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['SetRegisteredModelTag']._serialized_options = b'\362\206\031g\n:\n\004POST\022,/mlflow/unity-catalog/registered-models/tags\032\004\010\002\020\000\020\003*\'(Unity Catalog) Set RegisteredModel Tag'
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteRegisteredModelTag']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteRegisteredModelTag']._serialized_options = b'\362\206\031l\n<\n\006DELETE\022,/mlflow/unity-catalog/registered-models/tags\032\004\010\002\020\000\020\003**(Unity Catalog) Delete RegisteredModel Tag'
  _UCMODELREGISTRYSERVICE.methods_by_name['SetModelVersionTag']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['SetModelVersionTag']._serialized_options = b'\362\206\031a\n7\n\004POST\022)/mlflow/unity-catalog/model-versions/tags\032\004\010\002\020\000\020\003*$(Unity Catalog) Set ModelVersion Tag'
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteModelVersionTag']._options = None
  _UCMODELREGISTRYSERVICE.methods_by_name['DeleteModelVersionTag']._serialized_options = b'\362\206\031f\n9\n\006DELETE\022)/mlflow/unity-catalog/model-versions/tags\032\004\010\002\020\000\020\003*\'(Unity Catalog) Delete ModelVersion Tag'
  _UCMODELREGISTRYSERVICE._serialized_start=145
  _UCMODELREGISTRYSERVICE._serialized_end=5144
UcModelRegistryService = service_reflection.GeneratedServiceType('UcModelRegistryService', (_service.Service,), dict(
  DESCRIPTOR = _UCMODELREGISTRYSERVICE,
  __module__ = 'databricks_uc_registry_service_pb2'
  ))

UcModelRegistryService_Stub = service_reflection.GeneratedServiceStubType('UcModelRegistryService_Stub', (UcModelRegistryService,), dict(
  DESCRIPTOR = _UCMODELREGISTRYSERVICE,
  __module__ = 'databricks_uc_registry_service_pb2'
  ))


# @@protoc_insertion_point(module_scope)
