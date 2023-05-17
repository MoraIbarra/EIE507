#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

print("Contnet-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - get CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body>")
print("</html>")
