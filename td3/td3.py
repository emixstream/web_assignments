#!/usr/bin/python

# Ho eseguito il codice con Mozilla Firefox sotto Linux e pyhton 2.7 (MX-19.4_x64 patito feo)

# Per eseguire il programma: http://localhost/cgi-bin/td3.py?n=1234567890 o http://localhost/cgi-bin/td3.py


import cgi
import cgitb
import math
 
cgitb.enable()

dizionario = {}

lista=[]

def primeFactorsDiz(n):
    dizionario = {}
    dizionario["n"] = n
    dizionario["prime_factors"] = []

    m = n
    for i in range(2,int(math.sqrt(n))+1):
        if m % i == 0:
            support = {"prime": i, "power": 0}
            while m % i == 0:
                support["power"] += 1
                m /= i
            dizionario["prime_factors"].append(support)
    if m > 1:
        dizionario["prime_factors"].append({"prime": m, "power": 1})

    print '<p id="decomposition">' + str(dizionario["n"]) + " = " + " &times; ".join([str(x["prime"]) + "<sup>" + str(x["power"]) + "</sup>" for x in dizionario["prime_factors"]]) + '</p><br />'

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head><title>Factor Decomposition</title></head>'
print ' <script src="td3.js"></script> '
print '<body>'
print '<h1>Factor Decomposition</h1>'

form = cgi.FieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    print '<h2>Buongiorno, ha inserito il seguente numero: ' + name + '!</h2><br />'
    primeFactorsDiz(float(name))


arguments = cgi.FieldStorage()
for i in arguments.keys():
    name = arguments[i].value
   # print '<h2>Numero di cui fare decomposizione: ' + name + '; il numero viene scomposto: </h2><br />'
   # primeFactorsDiz(float(name))



if 'name' in globals():

    if isinstance(name, int):
        n = int(name)
        primeFactorsDiz(n)



print '<h3>Compili il seguente form per ottenere un ulteriore scomposizione:  </h3><br />'
print '<form method="get" onsubmit="return sendAjaxRequest(this);">'
print '<p>Number: </p><input type="text" name="name"/>'
print '</form>'

print '</body>'
print '</html>'
