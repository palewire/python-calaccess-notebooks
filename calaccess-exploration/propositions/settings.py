import os
import pandas as pd

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

db_settings = dict(
    NAME="calaccess_website_processed_data",
    USER="",
    PASSWORD="",
    HOST="",
    PORT="5432"
)

db_connection = 'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(
    **db_settings
)

def open_csv(path, **kwargs):
    return pd.read_csv(
        os.path.join(data_dir, path),
        **kwargs
    )