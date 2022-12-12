from pathlib import Path

from pydantic import BaseModel

from urlx import Url


class DbConfig(BaseModel):
    HOST: str = 's'
    PORT: int = 5432
    USERNAME: str = 'root'
    PASSWORD: str = 'root'
    DB_NAME: str = 'movies_db'
    SCHEMA_NAME: str = 'movies_scheme'

    def build_url(self) -> Url:
        return Url(
            protocol='postgresql+asyncpg',
            host=self.HOST,
            username=self.USERNAME,
            password=self.PASSWORD,
            port=self.PORT,
            path=Path(self.DB_NAME),
        )


class Config(BaseModel):

    HOST: str = 'localhost'
    PORT: int = 8000
    RELOAD: bool = True

    POSTGRES_DB: DbConfig = DbConfig()
