from pydantic import BaseSettings, Field


class AerospikeSettings(BaseSettings):
    aerospike_port: int = Field(default=3000)
    aerospike_hosts: str
    aerospike_namespace: str = Field(default="greco")

    @property
    def aerospike_client_config(self) -> dict:
        return {"hosts": [(item, self.aerospike_port) for item in self.aerospike_hosts.split(",")]}
