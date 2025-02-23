import os
import config

def get_excel_files():
    folder_path = os.path.join(os.path.dirname(__file__), config.FOLDER_NAME)

    excel_files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.endswith((config.XLS_FILE_EXTENSION, config.XLSX_FILE_EXTENSION, config.XLSM_FILE_EXTENSION))
    ]

    return excel_files