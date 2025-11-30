from src.api.helpers import read_from_file
from src.api.constants import constants

def get_create_data():
    workbook_name=read_from_file.get_property(constants.PROPERTY_FILE,"workbook")
    sheetname=read_from_file.get_property(constants.PROPERTY_FILE,"sheet_create")
    data=read_from_file.get_excel_data(constants.ROOT_DIR+"/data/" +workbook_name,sheetname)
    return data

def get_delete_data():
    workbook_name=read_from_file.get_property(constants.PROPERTY_FILE,"workbook")
    sheetname=read_from_file.get_property(constants.PROPERTY_FILE,"sheet_delete_user")
    data=read_from_file.get_excel_data(constants.ROOT_DIR+"/data/" +workbook_name,sheetname)
    return data
    