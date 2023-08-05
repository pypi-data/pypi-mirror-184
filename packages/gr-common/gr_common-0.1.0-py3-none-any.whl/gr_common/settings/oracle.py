from pydantic import BaseSettings, SecretStr


class OracleSettings(BaseSettings):
    oracle_user: str
    oracle_password: SecretStr
    oracle_host: str
    oracle_db: str
    oracle_client_path: str | None

    @property
    def db_url(self) -> str:
        return (
            f"oracle+cx_oracle://{self.oracle_user.strip()}"
            f":{self.oracle_password.get_secret_value().strip()}"
            f"@{self.oracle_host.strip()}"
            f"/?service_name={self.oracle_db.strip()}"
        )
