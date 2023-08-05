# ypconnector-python

ypconnector-python is a Python SDK used for integrating the Yappes Published APIs with your application. SDK is installed via npm. 

ypconnector-python provides individual action methods and a common method for making API requests.Currently it supports GET,POST,POST,DELETE and PATCH.


Install:
```
pip install ypconnector
```
Usage:
```
from yplib.ypconnector import YappesLibrary

//Yappes-Token obtained from yappes portal
yappesToken = "YOUR X-YAPPES-KEY";
ypObj = YappesLibrary(token)

//Data needed to call the library methods - individual Actions(GET/POST/PUT)
url = "http://localhost:8081/getdata";
data = {
 "headers": {
  "Content-Type":"application/json"
 },
 "queryparams": {
  "queryParam1" : "value1"
 },
 "payload": {
  "key":"value"
 }
}

//GET Request with empty payload: {}
responseData = ypObj.get(url, data)
print(responseData["body"])

//POST Request
responseData = ypObj.post(url, data)
print(responseData["body"])

//PUT Request
responseData = ypObj.put(url, data)
print(responseData["body"])

//Common Method
//Data needed to call the library methods - common action (call)
url = "http://localhost:8081/getdata";
data = {
 "method":"get"
 "headers": {
  "Content-Type":"application/json"
 },
 "queryparams": {
  "queryParam1" : "value1"
 },
 "payload": {
  "key":"value"
 }
}

responseData = ypObj.call(url, data)
print(responseData["body"])

```