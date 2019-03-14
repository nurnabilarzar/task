# **Internship  Progress Report**

# Contents
  - [Read Me](#read-me)
  - [Accomplishments and Work Performed](#accomplishments-and-work-performed)
  - [Notes](#notes)
  
# Read Me
- This is a progress report on what have been done during internship period.
- All codes were compiled and run using **Visual** Code studio.
- The operating system use is **Ubuntu** operating system.
  
# Accomplishments and Work Performed

## **Python and Linux**
First week is to learn and explore python3 and linux. Create directory using *mkdir* command, show list of file using *ls* command and change to another directory using *cd* command. Another commands are to create file using *touch* or *cat* command, to remove directory using *rmdir* command and any other commands.

## **Git and GitHub**
An introduction using [Git](https://git-scm.com/) and [GitHub](https://github.com/). GitHub is web-based hosting service for version control. Issue the command of installing the git ```sudo apt install git-all``` in terminal window. To add file into the project, issue the command ```git add progressIntern.md``` and check the file by issuing ```git status``` command.

To commit all changes that have been made in a file, issue the command ```git commit -m "message"``` where message is your message about the changes. Branch is to separate development work without affecting other branches. Create new branch ```git checkout -b EXPERIMENT``` where **EXPERIMENT** is the name of new branch. To push project into GitHub repository ```git push -u origin master ```.

## **Task 1**
Task 1 is to retrieve the McDonald's stores data from [McDonald's wesite](https://www.mcdonalds.com.my/locate-us).

### **Import library**
First task is to store data of [McDonald's](https://www.mcdonalds.com.my/locate-us) into sqlite3 database. Three library need to be imported which are *requests*, *json* and *sqlite3*

```python
import requests
import json
import sqlite3
```
### **POST requests**
Allows to send data to the request by passing **dictionary** to the **data**.
```python
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
```
The **data** contains the important keys and values that are needed for getting the JSON data.

### **Encoding**
The code below set the encoding of the content to be **'utf-8-sig'**. Without setting the encoding to be **'utf-8-sig'** will raise an error when accessing **resp.text**.
```python
resp.encoding = 'utf-8-sig'
```

### **Defining the api-endpoint**
```python
endpoint = 'https://www.mcdonalds.com.my/storefinder/index.php'
```
The **headers** is passed to the **headers** parameter in a request as shown in below.

```python
resp = requests.post(endpoint, data=data, headers=headers)
```
Now, it has a sending **post** request and object called **resp**. We can get all the information we need from this object. Use *requests.post()* method since it sends a **POST** request.

### **JSON data to a Python object**
For **json string**, use *json.loads()* method to parse it. Result will be in **Python dictionary**.
```python
stores = json.loads(resp.text)
```

### **Create database SQLite for storing data**
Create database to store data of McDonald's and open a connection to a database.
```python
conn=sqlite3.connect("mcdonalds.db")
c=conn.cursor()
```
After that, create a table **stores** for storing *McDonald's store* information. **CREATE TABLE** statement is used by calling **execute()** statement of a cursor.
```python
c.execute("""CREATE TABLE IF NOT EXISTS stores (storeName TEXT, address TEXT, telephone TEXT, email TEXT, website TEXT, fax TEXT, desc TEXT, lat REAL, long REAL, cat TEXT)""")
```
To store information to **SQLite** database, **INSERT** statement is executed by calling **execute()** statement of the cursor. **For** loop is used to insert each information into database.

```python
for s in stores ["stores"]:
    list = []
    for cat in s["cat"]:
         list.append(cat["cat_name"])
       # print(cat["cat_name"])
    p = json.dumps(list)
    #print(p) 

    c.execute("INSERT OR IGNORE INTO stores VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (s["name"],s["address"],s["telephone"],s["email"],s["website"],s["fax"], s["description"], s["lat"], s["lng"], p))
```

# **Notes**
Linux commands and Python are difficult since I never learned or experienced it before. The first week is hard because I still cannot remember the commands and all. For SQLite, some of the syntax are familiar and some I need to learn it. Overall, this is a new things that I learn and right now I am working with django.
  