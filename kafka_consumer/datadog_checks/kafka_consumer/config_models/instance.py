# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class SaslOauthTokenProvider(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    url: Optional[str] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    close_admin_client: Optional[bool] = None
    consumer_groups: Optional[MappingProxyType[str, Any]] = None
    consumer_groups_regex: Optional[MappingProxyType[str, Any]] = None
    consumer_queued_max_messages_kbytes: Optional[int] = None
    data_streams_enabled: Optional[bool] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    kafka_client_api_version: Optional[str] = None
    kafka_connect_str: Union[str, tuple[str, ...]]
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    monitor_all_broker_highwatermarks: Optional[bool] = None
    monitor_unlisted_consumer_groups: Optional[bool] = None
    sasl_kerberos_domain_name: Optional[str] = None
    sasl_kerberos_keytab: Optional[str] = None
    sasl_kerberos_principal: Optional[str] = None
    sasl_kerberos_service_name: Optional[str] = None
    sasl_mechanism: Optional[str] = None
    sasl_oauth_token_provider: Optional[SaslOauthTokenProvider] = None
    sasl_plain_password: Optional[str] = None
    sasl_plain_username: Optional[str] = None
    security_protocol: Optional[str] = None
    service: Optional[str] = None
    tags: Optional[tuple[str, ...]] = None
    tls_ca_cert: Optional[str] = None
    tls_cert: Optional[str] = None
    tls_ciphers: Optional[tuple[str, ...]] = None
    tls_crlfile: Optional[str] = None
    tls_private_key: Optional[str] = None
    tls_private_key_password: Optional[str] = None
    tls_validate_hostname: Optional[bool] = None
    tls_verify: Optional[bool] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
