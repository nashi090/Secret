from telethon.sync import TelegramClient
from telethon import utils
import csv
from csv import reader
import configparser






done = False
with open('phone.csv', 'r') as f:
    str_list = [row[0] for row in csv.reader(f)]

    
    po = 0
    for pphone in str_list:
        
        
        phone = utils.parse_phone(pphone)
        po += 1
        with open('api.csv', 'r') as api_obj_id:
    # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(api_obj_id)
    # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
    
            row_number = int(po)
            col_number = 1
            deltaop = list_of_rows[row_number - 1][col_number - 1]
    
        with open('api.csv', 'r') as hash_obj:
   
            csv_reader = csv.reader(hash_obj)
    # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
    
            row_number = int(po)
            col_number = 2
            deltaxd = list_of_rows[row_number - 1][col_number - 1]
    
        api_id = int(deltaop)
        api_hash = str(deltaxd)
       
        
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
        client.start(phone)
        

        client.disconnect()
        print()
    done = True

input("Done!" if done else "Error!")
