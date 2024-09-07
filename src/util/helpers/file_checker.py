import os
from config import Config

def check_files_exist_mit(record_name, record_path):
    """
    Checks whether files for a specific record exist in the directory.

    Parameters:
        :param `record_name (str)`: Record name (without extension).
        :param `record_path (str)`: Path to the directory where the files are located.
    
    Returns:
        :return: (bool) True if all files exist, False otherwise.
    """
    extensions = ['atr', 'dat', 'hea']
    for ext in extensions:
        file_path = os.path.join(record_path, f'{record_name}.{ext}')
        if not os.path.isfile(file_path):
            return False
        
    return True

def check_all_files_exist_mit(record_path):
    """
    Verifies that all necessary files for all records are present.

    Parameters:
        :param `record_path (str)`: Path to the directory where the files are located.

    Returns:
        :return: (bool) True if all files exist, False otherwise.
    """
    for record_name in Config.all_records:
        if not check_files_exist_mit(record_name, record_path):
            return False
        
    return True