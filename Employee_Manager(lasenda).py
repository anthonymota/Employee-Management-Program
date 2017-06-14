#this program will allow user to input information on employee

employee=input("Name: ")
norma = {
    "name": "Norma",
    "social security": "869-45-3456",
    "birthday": "4/6/89",
    "email": "norma@yahoo.com"
}
bentley = {
    "name": "Bentley",
    "social security": "869-45-3456",
    "birthday": "4/6/89",
    "email": "bentley@yahoo.com"
}
lety = {
    "name": "Lety",
    "social security": "869-45-3456",
    "birthday": "4/6/89",
    "email": "lety@yahoo.com"
}

employees=[norma,bentley,lety]

for item in employees:
    print (item["name"])
    print (item["social security"])
    print (item["birthday"])
    print (item["email"])
    print ("")
