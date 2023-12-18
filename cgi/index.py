#!/usr/local/bin/python3

import os

envs = os.environ

print("Content-Type: text/html")
print("Connection: close")
print() # empty line - end of headers
print(f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CHI</title>
  </head>
  <body>
    <h1>CGI works</h1>
    <ul>
        {"".join(f"<li>{k} = {v}</li>" for k, v in envs.items())}
    </ul>
  </body>
</html>''')