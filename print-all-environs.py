#!/usr/bin/python3
import sys
import os
import cgitb

# print detailed error messages in case of failure
#cgitb.enable()

print("Content-type: text/html")

print("<html>")


print("<h2>Here are all the environment variables:</h2>")
#keys = os.environ.keys()
#keys.sort()
#for item in keys:
#    print(item, ":  ", os.environ[item], "<br>")
print("</html>" )