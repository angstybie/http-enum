#!/usr/bin/python3


import http.client

"""
Setup HTTP Methods to test
"""

methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"]
print("Testing for: ", methods)
addmethod=input("Want to add a method? (Y/N)")
if(addmethod=='Y' or addmethod=='y'):
	method=str(input('Enter method to be added: '))
	methods.append(method)

"""
Setup Target
"""

host=input("\nEnter IP address of your target: ")
port=input("Enter port (default 80): ")
url=input("Enter URL (default: '/'): ")

if(port==""):
	port=80
if(url==""):
	url='/'


"""
Testing code
"""
	
for item in methods:
	try:
		print("\n******************************")
		print("[+] Trying for ",item)
		connection = http.client.HTTPConnection(host,port)
		connection.request(item, url)
		response=connection.getresponse()
		print("Headers: ", response.getheaders())
		print("Status: ", response.status)
		connection.close()
	except ConnectionRefusedError:
		print("Connection Failed")