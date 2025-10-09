"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    azara_coordinate = azara_record[1]
    rui_coordinate = ''.join(rui_record[1])
    return azara_coordinate == rui_coordinate


def create_record(azara_record, rui_record):
    
    azara_coordinate = azara_record[1]
    rui_coordinate_tuple = rui_record[1]
    rui_coordinate_str = ''.join(rui_coordinate_tuple)
    
    if azara_coordinate == rui_coordinate_str:
    
        return (azara_record[0], azara_coordinate, rui_record[0], rui_coordinate_tuple, rui_record[2])
    else:
        return "not a match"


def clean_up(combined_record_group):
    cleaned_records = []
    for record in combined_record_group:

        cleaned_record = (record[0], record[2], record[3], record[4])
        cleaned_records.append(cleaned_record)
    

    result = ""
    for record in cleaned_records:
        result += f"{record}\n"
    
    return result