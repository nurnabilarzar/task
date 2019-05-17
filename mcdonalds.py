import requests
import json
import sqlite3

conn=sqlite3.connect("mcdonalds.db")
c=conn.cursor()


endpoint = 'https://www.mcdonalds.com.my/storefinder/index.php'

headers = {
    'user-agent':
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

data = {
    'ajax': '1',
    'action': 'get_nearby_stores',
    'distance': '100',
    'lat': '4.210484',
    'lng': '101.975',
    'state': '',
    'products': '',
    'address': '',
    'issuggestion': '0',
    'islocateus': '0'
}

resp = requests.post(endpoint, data=data, headers=headers)
resp.encoding = 'utf-8-sig'
if resp.status_code != 200:
    print('expected 200, got {code}'.format(code=resp.status_code))

stores = json.loads(resp.text)

#PRINT ANY DATA YOU WANT BY INSERTING INDEX
#print(stores['stores'][0])

c.execute("""CREATE TABLE IF NOT EXISTS stores (storeName TEXT, address TEXT, telephone TEXT, email TEXT, website TEXT, fax TEXT, desc TEXT, lat REAL, long REAL, cat TEXT)""")
        
for s in stores ["stores"]:
    list = []
    for cat in s["cat"]:
        list.append(cat["cat_name"])
       # print(cat["cat_name"])
    p = json.dumps(list)
    #print(p) 

    c.execute("INSERT OR IGNORE INTO stores VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (s["name"],s["address"],s["telephone"],s["email"],s["website"],s["fax"], s["description"], s["lat"], s["lng"], p))

conn.commit()
 
conn.close()