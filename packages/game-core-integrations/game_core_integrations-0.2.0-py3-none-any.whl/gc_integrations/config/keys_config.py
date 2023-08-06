from pydantic import BaseSettings, Field
from dotenv import load_dotenv


class GCISecrets(BaseSettings):
    """A model to hold values of environment variables. Load .env file variables with load_env_secrets()."""

    IGDB_CLIENT_ID: str = Field(default=None)
    IGDB_CLIENT_SECRET: str = Field(default=None)


def load_env_secrets():
    """Helper function to optionally load the environment variables from a .env file
    @return GCISecrets: A model containing the environment variables.
    """

    load_dotenv()
    secrets = GCISecrets()
    return secrets
