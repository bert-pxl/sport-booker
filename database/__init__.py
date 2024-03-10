from logs import LOGGER
import pathlib
import json

LOGGER.info('Loading database configuration')


def load_config(file_name: str = '../database/database-config.json'):
    try:
        script_dir = pathlib.Path(__file__).resolve().parent
        config_file = script_dir / file_name

        with config_file.open(mode='r') as f_in:
            config = json.load(f_in)
            if 'mysql' in config:
                mysql_config = config['mysql']
                if all(key in mysql_config for key in ['host', 'user', 'passwd', 'db']):
                    return (f'mysql://{mysql_config["user"]}:{mysql_config["passwd"]}@{mysql_config["host"]}/'
                            f'{mysql_config["db"]}')
                else:
                    LOGGER.error("Incomplete MySQL configuration. Required fields: host, user, passwd, db")
            elif 'sqlite' in config:
                sqlite_config = config['sqlite']
                if 'file' in sqlite_config:
                    return f'sqlite:///{sqlite_config["file"]}'
                else:
                    LOGGER.error("SQLITE configuration not found in the provided configuration file.")
            else:
                LOGGER.error("MySQL configuration not found in the provided configuration file.")

    except FileNotFoundError:
        LOGGER.error(f"The file '{file_name}' was not found in the same directory as the script.")
        return None


CONNECTION_STRING = load_config()
