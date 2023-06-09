#!/usr/bin/python

import os
import time
import urllib3
import tldextract
from bs4 import BeautifulSoup

#create a pool to store sites
pool = urllib3.PoolManager(num_pools=5)

#main menu
def menu():
    print( f" {'Menu':^5}" )
    #Number of requests made
    print( f"Number of requests made: {len(pool.pools)} \n")
    uri = input('Enter target url > ')
    method = str(input('Enter Method Type(GET/POST)')).upper()
    uriextract = tldextract.extract(uri)
    uriname = uriextract.domain
    return method , uri , uriname


def connect(methodarg,uriarg):
    web = pool.request(methodarg, uriarg)
    return web

def storage(uriname,Hstore, Dstore):
    #check & create a root data dir in the program folder
    #root = '/home/mobly/Documents/Python/Pentesting'
    rootH = str(uriname + '_Header.txt')
    rootB = str(uriname + '_Body.xml')
    if not os.path.exists('Data_Files'):
        os.mkdir('Data_Files')
    #check & genrator file
    with open(os.path.join('Data_Files/',rootH), 'w') as Hwriter:
        Hwriter.write(Hstore)
            
    with open(os.path.join('Data_Files/',rootB), 'w') as Bwriter:
        Bwriter.write(Dstore)
            
def custom_search(Dstore, query):
    soup_doc = BeautifulSoup(Dstore, 'lxml')
    search_content = soup_doc.find_all(str(query))
    #Organise and store content
    for ele in search_content:
        store = f"{ele} \n"
        with open('Data_Files/data.txt', 'a') as tar_data:
            tar_data.write(store)
    print("Done")
            
        
        
    

def display(web):
    header = web.headers
    dom = str(web.data)
    #Formating headers
    Hstore = "Header \n"
    for head, val in header.items():
        print(f"{head} : {val}")
        Hstore += f"{head} , {val}"
    # pause 5 sec to view    
    time.sleep(1)
    os.system("clear")
    #Split the dom
    Seq = dom.split("\\n")
    # display and store the dom in a file
    Dstore = " Source Code \n"
    for Domele in Seq:
        Dstore += f"{Domele} \n"
       
    return Hstore, Dstore
            
    print(Dstore)     
    time.sleep(1)
    
    
while True:
    method, uri ,uriname = menu()
    web = connect(method, uri)
    Hstore, Dstore = display(web)
    storage(uriname, Hstore, Dstore)
    os.system("clear")
    search = input("search > ")
    custom_search(Dstore, search)
    time.sleep(10)
    exit = input("Do you wish to exit?(y/n)")
    if exit == 'y':
        continue
    else:
        web.close()
        break
    
    
    
    

