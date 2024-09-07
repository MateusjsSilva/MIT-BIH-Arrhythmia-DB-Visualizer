class Config:
    """
    Configuration settings for processing the MIT-BIH Arrhythmia Database.

    - `input_path`: Path to the input data folder.
    - `all_records`: List of all available records.
    """
    
    # path to the input data
    input_path = './data/mit-bih-arrhythmia-database'

    # list of all available records
    all_records = [
        '100', '101', '102', '103', '104', '105', '106', '107', '108', '109',
        '111', '112', '113', '114', '115', '116', '117', '118', '119', '121',
        '122', '123', '124', '200', '201', '202', '203', '205', '207', '208',
        '209', '210', '212', '213', '214', '215', '217', '219', '220', '221',
        '222', '223', '228', '230', '231', '232', '233', '234'
    ]