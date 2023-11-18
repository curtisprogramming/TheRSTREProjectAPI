from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Class to manage application settings.

    Attributes:
        database_hostname (str): The hostname of the database.
        database_port (str): The port number of the database.
        database_password (str): The password for the database.
        database_name (str): The name of the database.
        database_username (str): The username for the database.
        secret_key (str): The secret key for authentication.
        algorithm (str): The algorithm used for authentication.
        access_token_expire_minutes (int): The expiration time for access tokens in minutes.

    Note:
        The settings are loaded from the environment file specified in the Config class.
    """
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = "app/.env"

# Create an instance of the Settings class to access the settings
settings = Settings()
