import pyodbc

def get_connection():
    return pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=D:\UNIVERSITY\Python\Project\guesthouse\guesthouse.accdb;"
    )
