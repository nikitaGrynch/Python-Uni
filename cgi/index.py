#!/usr/local/bin/python3

import os
import mysql.connector
import sys
sys.path.append( '../' )
import db_ini


# сформувати з змінних перелік <ul> name = value
# envs = os.environ  # змінні оточення -- dict{ name: value }
# envs = f"<ul>{
#     "".join([f"<li>{k} = {v}</li>"
#                        if k in ["REQUEST_URI", "QUERY_STRING", "REQUEST_METHOD", "REMOTE_ADDR", "REQUEST_SCHEME"]
#                        else "" 
#                        for k,v in os.environ.items()])}</ul>"

# envs = {k: v for k, v in os.environ.items() if k in ["REQUEST_URI", "QUERY_STRING", "REQUEST_METHOD", "REMOTE_ADDR", "REQUEST_SCHEME"]}
# envs_html = f"<ul>{ "".join([f"<li>{k} = {v}</li>" for k,v in envs.items()]) }"
# envs_html += "</ul>"
# if envs["QUERY_STRING"]:
#     envs_html += f"<p>QUERY_STRING: {f"<ul>{ "".join([f"<li>{k} = {v}</li>" for k,v in {k: v for k, v in (pair.split('=') for pair in envs["QUERY_STRING"].split('&'))}.items()]) }"}</p>"

# print( "Content-Type: text/html; charset=cp1251" )
# print( "Connection: close" )
# print()   # порожній рядок - кінець заголовків
# print(envs_html)
# with open( 'home.html' ) as file :
#     print( file.read() )


#HW SHOW_DATABASES to HTML
db = mysql.connector.connect( **db_ini.connection_params )
sql = "SHOW DATABASES"
try :
    with db.cursor() as cursor :
        cursor.execute( sql )
        html_table = "<table border='1'><tr><th>Database Name</th></tr>"
        for row in cursor:
            html_table += "<tr>"
            html_table += f"<td>{row[0]}</td>"
            html_table += "</tr>"
        html_table += "</table>"
except mysql.connector.Error as err :
    print( err )
else :
    print( "Content-Type: text/html; charset=cp1251" )
    print( "Connection: close" )
    print()
    print(html_table)


"""
Д.З. CGI: забезпечити відображення лише наступних змінних оточення
REQUEST_URI, QUERY_STRING, REQUEST_METHOD, REMOTE_ADDR, REQUEST_SCHEME 
Розібрати рядок QUERY_STRING у словник 
 x=10&y=20  --> {x: 10, y: 20}
"""