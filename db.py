import mysql.connector
import os

from PIL import Image
from dotenv import load_dotenv
from data_parse import Parse

# Load env and set up CONSTs
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_NAME =  os.getenv("DB_SCEMA")
DB_TABLE = os.getenv("DB_TABLE")
DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")

class DbClass:
    
    # Get connector
    def DbConnect(usr, pwd, host, db):
        try:
            connector = mysql.connector.connect(user=usr, password=pwd,
                                        host=host, database=db)
            print("Connected!")
            return connector
        except mysql.connector.Error as er:
            print(er)
            return None
        
    def InsertPhotoRecord(con, data):
        # Data must be in tuple form
        # TODO: Check the data for the right formatting
        # Required vars
        add_photo = """INSERT INTO machine_pics (machine_name, created_date, picture) VALUES (%s, %s, %s)"""
        
        # Insert record
        try:
            cursor = con.cursor()
            cursor.execute(add_photo, data)
            con.commit()
            cursor.close()
            con.close()
            print("Record Added")
        except mysql.connector.Error as er:
            print(er)