from typing import Any

import aerospike
from aerospike import Client
from aerospike import client as aerospike_client

from gr_common.data.interfaces import NoSqlInterface
from gr_common.exceptions.data_exceptions import ValueNotFoundException
from gr_common.settings.aerospike import AerospikeSettings


class AerospikeClient(NoSqlInterface):
    def __init__(self, settings: AerospikeSettings):
        self.settings: AerospikeSettings = settings
        self._namespace: str = self.settings.aerospike_namespace
        self._config: dict = self.settings.aerospike_client_config
        self._client: Client = self._init_client()

    def _init_client(self) -> Client:
        return aerospike_client(self._config).connect()

    @staticmethod
    def _get_table_name(**kwargs: Any) -> str:
        if table_name := kwargs.get("table_name"):
            return table_name
        raise AttributeError("No argument table_name")

    def get(self, key: str, *args: Any, **kwargs: Any) -> dict:
        table_name = self._get_table_name(**kwargs)
        aerospike_key = (self._namespace, table_name, key)
        try:
            (response_key, meta, bins) = self._client.get(aerospike_key)
            return bins
        except aerospike.exception.RecordNotFound:
            raise ValueNotFoundException(key)

    def put(self, key: str, data: dict, *args: Any, **kwargs: Any) -> None:
        table_name = self._get_table_name(**kwargs)
        meta = kwargs.get("meta")
        if meta is not None and isinstance(meta, dict) is False:
            raise AttributeError("Argument meta must be type dict")
        aerospike_key = (self._namespace, table_name, key)
        self._client.put(aerospike_key, data, meta)

    def get_many(self, *args: Any, **kwargs: Any) -> list[tuple[tuple, dict, dict]]:
        table_name = self._get_table_name(**kwargs)
        return self._client.scan(self._namespace, table_name).results()

    def remove(self, key: str, *args: Any, **kwargs: Any) -> None:
        table_name = self._get_table_name(**kwargs)
        aerospike_key = (self._namespace, table_name, key)
        try:
            self._client.remove(aerospike_key)
        except aerospike.exception.RecordNotFound:
            raise ValueNotFoundException(key)
