import wfdb
import os

def download_record(record_name, target_path):
    """
    Function to download a specific record from the MIT-BIH Arrhythmia database.
    
    Parameters:
        :param `record_name (str)`: Record name (without extension).
        :param `target_path (str)`: Path to save the downloaded record.

    Returns:
        :return: None
    """
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    wfdb.dl_database('mitdb', target_path, records=[record_name])

def download_all_records(target_path):
    """
    Function to download all records from the MIT-BIH Arrhythmia database.
    
    Parameters:
        :param `target_path (str)`: Path to save downloaded records.

    Returns:
        :return: None
    """
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    wfdb.dl_database('mitdb', target_path, records='all')