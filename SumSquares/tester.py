import json
import requests


#Correct answer 8.77
url = "http://127.0.0.1:5000/highestnumbers"
jsonInput = """{"data": [5,4,6,1]}"""
headers = {'Content-Type': 'application/json'}

res = requests.post(url, data=jsonInput, headers=headers)
print(res.text)



#Correct answer 80.22
url = "http://127.0.0.1:5000/highestnumbers"
jsonInput = """{"data": [8,6,2,12,44,66]}"""
headers = {'Content-Type': 'application/json'}

res = requests.post(url, data=jsonInput, headers=headers)
print(res.text)



#Must return "Error: List must contain at least 3 numbers." 
url = "http://127.0.0.1:5000/highestnumbers"
jsonInput = """{"data": [5,4]}"""
headers = {'Content-Type': 'application/json'}

res = requests.post(url, data=jsonInput, headers=headers)
print(res.text)


#Must return "Error: List must contain only numbers." 
url = "http://127.0.0.1:5000/highestnumbers"
jsonInput = """{"data": [5, 4, "S"]}"""
headers = {'Content-Type': 'application/json'}

res = requests.post(url, data=jsonInput, headers=headers)
print(res.text)