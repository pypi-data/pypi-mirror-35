import json
from urllib.parse import urlparse
import sys
import requests


responseSchema = {"headers": "", "statusCode": "", "statusMessage": "", "body": ""}
methodList=["get","post","put","delete","patch"]

class YappesLibrary:
    def __init__(self, token):
        self.xyappeskey = token
    #call Method (get,post,put,delete,patch)
    def call(self, apiUrl, parameters):
        if "method" not in parameters:
            return "Method not Available in parameters"
        if parameters["method"].isupper():
            parameters["method"]=parameters["method"].lower()
        try:        
            if parameters["method"] in methodList:
                urlParts = urlparse(apiUrl)
                options = {
                    "host": urlParts.hostname,
                    "path": urlParts.path,
                    "port": urlParts.port,
                    "method": parameters["method"],
                    "headers": parameters["headers"],
                }
                options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
                if options["port"] is None:
                    options["port"] = 443
                conn = requests.request(options["method"],
                    apiUrl, data=json.dumps(parameters["payload"]), params=parameters["queryparams"],headers=options["headers"]
                )
                responseSchema["headers"] = conn.headers
                responseSchema["statusCode"] = conn.status_code
                responseSchema["statusMessage"] = conn.reason
                responseSchema["body"] = conn.text
                return responseSchema
            else:
                return "Error 405 Unsupported Method/Method Not Allowed. Please refer read me section"
        except:
            print(sys.exc_info())

    # get operation
    def get(self, apiUrl, parameters):
        try:
            urlParts = urlparse(apiUrl)
            options = {
                "host": urlParts.hostname,
                "path": urlParts.path,
                "port": urlParts.port,
                "method": "get",
                "headers": parameters["headers"],
            }
            options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
            if options["port"] is None:
                options["port"] = 443
            conn = requests.get(apiUrl, data=json.dumps(parameters["payload"]),params=parameters["queryparams"],
                headers=options["headers"]
            )
            responseSchema["headers"] = conn.headers
            responseSchema["statusCode"] = conn.status_code
            responseSchema["statusMessage"] = conn.reason
            responseSchema["body"] = conn.text
            return responseSchema
        except:
            print(sys.exc_info())

    # post operation
    def post(self, apiUrl, parameters):
        try:
            urlParts = urlparse(apiUrl)
            options = {
                "host": urlParts.hostname,
                "path": urlParts.path,
                "port": urlParts.port,
                "method": "POST",
                "headers": parameters["headers"],
            }
            options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
            if options["port"] is None:
                options["port"] = 443
            conn = requests.post(
                apiUrl, data=json.dumps(parameters["payload"]), params=parameters["queryparams"],headers=options["headers"]
            )
            responseSchema["headers"] = conn.headers
            responseSchema["statusCode"] = conn.status_code
            responseSchema["statusMessage"] = conn.reason
            responseSchema["body"] = conn.text
            return responseSchema
        except:
            print(sys.exc_info())
    # put operation
    def put(self, apiUrl, parameters):
        try:
            urlParts = urlparse(apiUrl)
            options = {
                "host": urlParts.hostname,
                "path": urlParts.path,
                "port": urlParts.port,
                "method": "PUT",
                "headers": parameters["headers"],
            }
            options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
            if options["port"] is None:
                options["port"] = 443
            conn = requests.put(
                apiUrl, data=json.dumps(parameters["payload"]),params=parameters["queryparams"], headers=options["headers"]
            )
            responseSchema["headers"] = conn.headers
            responseSchema["statusCode"] = conn.status_code
            responseSchema["statusMessage"] = conn.reason
            responseSchema["body"] = conn.text
            return responseSchema
        except:
            print(sys.exc_info())
    #delete operation
    def delete(self, apiUrl, parameters):
        try:
            urlParts = urlparse(apiUrl)
            options = {
                "host": urlParts.hostname,
                "path": urlParts.path,
                "port": urlParts.port,
                "method": "DELETE",
                "headers": parameters["headers"],
            }
            options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
            if options["port"] is None:
                options["port"] = 443
            conn = requests.delete(
                apiUrl, data=json.dumps(parameters["payload"]), params=parameters["queryparams"],headers=options["headers"]
            )
            responseSchema["headers"] = conn.headers
            responseSchema["statusCode"] = conn.status_code
            responseSchema["statusMessage"] = conn.reason
            responseSchema["body"] = conn.text
            return responseSchema
        except:
            print(sys.exc_info())
    #patch operation        
    def patch(self, apiUrl, parameters):
        try:
            urlParts = urlparse(apiUrl)
            options = {
                "host": urlParts.hostname,
                "path": urlParts.path,
                "port": urlParts.port,
                "method": "PATCH",
                "headers": parameters["headers"],
            }
            options["headers"]["X-YAPPES-KEY"] = self.xyappeskey
            if options["port"] is None:
                options["port"] = 443
            conn = requests.patch(
                apiUrl, data=json.dumps(parameters["payload"]), params=parameters["queryparams"],headers=options["headers"]
            )
            responseSchema["headers"] = conn.headers
            responseSchema["statusCode"] = conn.status_code
            responseSchema["statusMessage"] = conn.reason
            responseSchema["body"] = conn.text
            return responseSchema
        except:
            print(sys.exc_info())
                    

