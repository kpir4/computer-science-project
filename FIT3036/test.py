import mysql.connector

db = "enron"
table = "employeelist"

f = open('/home/osboxes/Desktop/FIT3036/password.txt', 'r')
p = f.read()
f.close()
cnx = mysql.connector.connect(user = 'root', password = 'fit3036', host = '127.0.0.1')

cnx.database = db

def get_table_names()