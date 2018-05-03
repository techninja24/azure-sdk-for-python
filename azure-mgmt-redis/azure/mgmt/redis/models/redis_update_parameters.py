# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RedisUpdateParameters(Model):
    """Parameters supplied to the Update Redis operation.

    :param redis_configuration: All Redis Settings. Few possible keys:
     rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value
     etc.
    :type redis_configuration: dict[str, str]
    :param enable_non_ssl_port: Specifies whether the non-ssl Redis server
     port (6379) is enabled.
    :type enable_non_ssl_port: bool
    :param tenant_settings: A dictionary of tenant settings
    :type tenant_settings: dict[str, str]
    :param shard_count: The number of shards to be created on a Premium
     Cluster Cache.
    :type shard_count: int
    :param minimum_tls_version: Optional: requires clients to use a specified
     TLS version (or higher) to connect (e,g, '1.0', '1.1', '1.2'). Possible
     values include: '1.0', '1.1', '1.2'
    :type minimum_tls_version: str or ~azure.mgmt.redis.models.TlsVersion
    :param sku: The SKU of the Redis cache to deploy.
    :type sku: ~azure.mgmt.redis.models.Sku
    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'redis_configuration': {'key': 'properties.redisConfiguration', 'type': '{str}'},
        'enable_non_ssl_port': {'key': 'properties.enableNonSslPort', 'type': 'bool'},
        'tenant_settings': {'key': 'properties.tenantSettings', 'type': '{str}'},
        'shard_count': {'key': 'properties.shardCount', 'type': 'int'},
        'minimum_tls_version': {'key': 'properties.minimumTlsVersion', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, redis_configuration=None, enable_non_ssl_port=None, tenant_settings=None, shard_count=None, minimum_tls_version=None, sku=None, tags=None):
        super(RedisUpdateParameters, self).__init__()
        self.redis_configuration = redis_configuration
        self.enable_non_ssl_port = enable_non_ssl_port
        self.tenant_settings = tenant_settings
        self.shard_count = shard_count
        self.minimum_tls_version = minimum_tls_version
        self.sku = sku
        self.tags = tags
