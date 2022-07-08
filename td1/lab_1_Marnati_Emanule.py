

## README ##

# I run this program on linux in a cmd with inputs as follows:


#      python3   file.py  http://www.w3c.org:80  METHOD_NAME(like "GET") ("body message when needed in quotes!")


# I added some extra prints to follow along and debug
# I used requests API just to have a way to get the response_code
# I used requests API to redirect if I get a 300 response code

#!/usr/bin/env python3

import socket
import sys
import urllib.parse
import requests


def client_request():

 
 HOST = ''
 PORT = 80

 try:
        name, uri, met, message_body = sys.argv
        if met not in ['POST', 'PUT', 'PATCH']:  
          message_body = ' '
          print('You entered body message but for this method is unsupported!! It will be cancelled')

 except:

         name, uri, met = sys.argv
         if met in ['POST', 'PUT', 'PATCH']:
             message_body = input("Please type the message_body (end with ctrl-D): ")
             print("You entered: " + message_body + " as body message \n\n")
         else:
          message_body = ' '


 if(uri[0:7] == "http://"):
    uri = uri[7:]
    print('uri :' + uri)
    if ':' in uri:
      pos = 0
      for i in uri:
        pos += 1
        if i == ':':
          HOST = uri[0:pos - 1]
          POST = int(uri[pos:])

          print('host :' + HOST)
          print('port :' + str(PORT))
    else:
      HOST = uri[7:]

 elif(uri[0:3] == 'www'):
    uri = "http://" + uri
    print('uri di controllo  ' + uri)
    uri = uri[7:]
    print('uri :' + uri)
    if ':' in uri:
      pos = 0
      for i in uri:
        pos += 1
        if i == ':':
          HOST = uri[0:pos - 1]
          POST = int(uri[pos:])

          print('host :' + HOST)
          print('port :' + str(PORT))
    else:
      HOST = uri[7:]


 else:
    raise TypeError("miss http:// reference")

 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #  informative error message
    try:
           s.connect((HOST, PORT))
    except OSError as err:
           print("OS error: {0}".format(err))

    met_en = met.encode()
    print('The method is: ' + met + '\n\n')
    s.sendall( met_en + b' /index.html HTTP/1.1\r\nHost: '+ HOST.encode("utf-8") + b'\r\n\r\n' + message_body.encode("utf-8") + b'\r\n')
    response = s.recv(1024)
   

    print('recived', repr(response), '   \n\n ')

    
    resp = requests.request(method=met, url="http://" + str(HOST), allow_redirects=False)

    for i in range(400, 599):
      if str(resp) == '<Response [' + str(i)+ ']>' :
       raise TypeError("error message!!  method unsupported!!")

    for i in range(100, 299):
      if str(resp) == '<Response [' + str(i)+ ']>' :
        print('<response message check: '  +  str(resp))

    for i in range(300, 399):
      if str(resp) == '<Response [' + str(i)+ ']>' :
       print('<response message check: ' +   str(resp))
       resp = requests.request(method=met, url="http://" + str(HOST))
       print('I\'ll redirect to the following url:  ' + resp.url + '\n\n')
       uri = resp.url
       parsed_url = urllib.parse.urlparse(uri)
       HOST = parsed_url.netloc
       
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #  informative error message
        try:
              s.connect((HOST, PORT))
        except OSError as err:
               print("OS error: {0}".format(err))

        met_en = met.encode()
        print(met)
        s.sendall( met_en + b' /index.html HTTP/1.1\r\nHost: '+ HOST.encode("utf-8") + b'\r\n\r\n' + message_body.encode("utf-8") + b'\r\n')
        response = s.recv(1024)
   

        print('recived', repr(response), '   \n\n ')



client_request()