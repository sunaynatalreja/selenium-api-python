import openpyxl
import configparser


def get_excel_data(file_name,sheet_name):
    wb=openpyxl.load_workbook(file_name)
    sheet=wb[sheet_name]
    data=[]
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(dict(zip(headers,row)))
    return data

def get_property(file_name,property_name):
    config=get_all_properties(file_name)
    return config["DEFAULT"][property_name]

def get_all_properties(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)
    return config
