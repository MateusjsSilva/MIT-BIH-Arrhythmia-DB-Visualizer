import wfdb
import os

def load_record(record_path, record_name, channels=None):
    """
    Loads an ECG record using the WFDB library.

    Parameters:
        :param `record_path (str)`: Path to the directory where the files are located.
        :param `record_name (str)`: Record name (without extension).
        :param `channels (list or None)`: List of channel names to load. If None, all channels are loaded.
        
    Returns: 
        :return: WFDB record object.
    """
    record = wfdb.rdrecord(os.path.join(record_path, record_name), channel_names=channels)
    return record

def load_annotations(record_path, record_name):
    """
    Loads ECG notes using the WFDB library.

    Parameters:
        :param `record_path (str)`: Path to the directory where the files are located.
        :param `record_name (str)`: Record name (without extension).

    Returns:
        :return: WFDB notes object.
    """
    annotation = wfdb.rdann(os.path.join(record_path, record_name), 'atr')
    return annotation

def load_data_mit(record_path, record_name, channels=None):
    """
    Loads an ECG record and its associated notes using the WFDB library.

    Parameters:
        :param `record_path (str)`: Path to the directory where the files are located.
        :param `record_name (str)`: Record name (without extension).
        :param `channels (list or None)`: List of channel names to load. If None, all channels are loaded.

    Returns:
        :return: A tuple containing the WFDB record object and the WFDB annotations object.
    """
    record = load_record(record_path, record_name, channels)
    annotation = load_annotations(record_path, record_name)
    return record, annotation