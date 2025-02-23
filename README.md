# Excel to PostgreSQL Importer

This project is designed to **automatically import Excel files into a PostgreSQL database**.

## Project Structure
**project-directory**  
├── **tables/** → Folder containing Excel files  
├── **config.py** → PostgreSQL connection settings  
├── **db_connection.py** → Database connection setup  
├── **utils.py** → Utility functions  
├── **main.py** → Main process file  
├── **README.md** → Project documentation  
└── **requirements.txt** → Required dependencies  

## Project Steps
### Install Required Packages
```pip install -r requirements.txt```

### Configure PostgreSQL Connection
Open config.py and update the following database settings:
```
DB_HOST = "-----"
DB_PORT = "-----"
DB_NAME = "-----"
DB_USER = "-----"
DB_PASS = "-----"
FOLDER_NAME = "-----"
```

### Add Excel Files
Place all .xlsx, .xls, .xlsm files inside the tables/ directory.

### Running the Main Process
To start the import process, run the following command:
```python main.py```
