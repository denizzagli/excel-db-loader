import utils
import db_connection
import pandas as pd

def main():
    files = utils.get_excel_files()
    engine = db_connection.get_db_engine()

    for file in files:
        df = pd.read_excel(file)
        df.to_sql(file.split("\\")[-1].split(".")[0], engine, if_exists="replace", index=False)

if __name__ == "__main__":
    main()