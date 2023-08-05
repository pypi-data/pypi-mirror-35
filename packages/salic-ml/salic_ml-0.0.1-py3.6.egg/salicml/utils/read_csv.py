import pandas as pd
import os


FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.join(FILE_PATH, os.pardir, os.pardir)
DATA_FOLDER = '~/Desktop/unb/lappis/salic-ml/data/raw' #os.path.join(PROJECT_ROOT, 'data', 'raw')


def read_csv(csv_name):
    """Returns a DataFrame from a .csv file stored in /data/raw/"""
    csv_path = os.path.join(DATA_FOLDER, csv_name)
    print(csv_path)
    csv = pd.read_csv(csv_path, low_memory=False)
    return csv
