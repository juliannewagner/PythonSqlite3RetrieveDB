# downloaded sqllitebrowser and used db browser for sqllite
# downloaded week10.db and explored the database,
# 1 -24 lines in week10 table each with an associated text, interesting

# import all three
import sqlite3
import base64
import webbrowser

# user input for a record number between 1 and 24, other values ignored
# user is prompted (input) again and charater q quits program
# this needs to be in a loop
# writes and executes an SQLLite3 query to extract Link field associtated
# with the record (*SQLLite3 module*)
conn = sqlite3.connect("week10.db")  # open database week10.db
cur = conn.cursor()

inputRecord = input("Please enter a value to record between ID(1 and 24): ")

extractUserInput = cur.execute(
    "select * from lab10 where id = " + (inputRecord))
for row in extractUserInput.fetchall():
    idLink = ("ID =", row[0])
    link = ("LINK =", row[1])
    # this decodes the base64 encoded value of the URL.
    decode = str(base64.b64decode(row[1]))
    # need index for url to be from 3(2) line to second last(-1) to just get url
    decode = (decode[2:-1])
    # web browser model to open decoded string(*WebBrowser Module*)
    webbrowser.open_new(decode)
    q = quit
    if inputRecord == 'q':  # to reloop
        reloop = input(inputRecord)
# for the specific record, user input for name of city,
# and country and updates the record (*sqlite3 module*)

newId = input("Please enter the name you want to update: ")
city = input("Please enter the name of a city you want to update: ")
country = input("Please enter the name of the country you want to update: ")

extractUserInput = "UPDATE lab10 SET city ='" + city + "', country = '" + country + "', student ='" + newId + "'WHERE id =" + inputRecord + ""  # this updates the database
cur.execute(extractUserInput)
conn.commit()
conn.close()

# Bonus: try to find out who in the class lives in that city and update the associated student field.
