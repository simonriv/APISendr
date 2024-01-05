import json
import os
import requests

def read_json(route):
    with open(route, 'r') as f:
        data = json.load(f)
    return data

def send_request(method,url,body,headers,authorization):
    if authorization != None:
        headers['Authorization'] = authorization 
    try:
        if method == 'get' or method == 'GET':
            if headers != None and body != None:
                r = requests.get(url,data=body,headers=headers)
            elif body != None and headers == None:
                r = requests.get(url,data=body)
            elif headers != None and body == None:
                r = requests.get(url,headers=headers)
            else:
                r = requests.get(url)
        elif method == 'post' or method == 'POST':
            if headers != None and body != None:
                r = requests.post(url,data=body,headers=headers)
            elif body != None and headers == None:
                r = requests.post(url,data=body)
            elif headers != None and body == None:
                r = requests.post(url,headers=headers)
            else:
                r = requests.post(url)
        elif method == 'put' or method == 'PUT':
            if headers != None and body != None:
                r = requests.put(url,data=body,headers=headers)
            elif body != None and headers == None:
                r = requests.put(url,data=body)
            elif headers != None and body == None:
                r = requests.put(url,headers=headers)
            else:
                r = requests.put(url)
        elif method == 'patch' or method == 'PATCH':
            if headers != None and body != None:
                r = requests.patch(url,data=body,headers=headers)
            elif body != None and headers == None:
                r = requests.patch(url,data=body)
            elif headers != None and body == None:
                r = requests.patch(url,headers=headers)
            else:
                r = requests.patch(url)
        elif method == 'delete' or method == 'DELETE':
            if headers != None and body != None:
                r = requests.delete(url,data=body,headers=headers)
            elif body != None and headers == None:
                r = requests.delete(url,data=body)
            elif headers != None and body == None:
                r = requests.delete(url,headers=headers)
            else:
                r = requests.delete(url)
        else:
            return 'ERR/(0x003): The Method is not recognized.'
    except requests.exceptions.HTTPError as errh:
        raise errh
    except requests.exceptions.ConnectionError as errc:
        raise errc
    except requests.exceptions.Timeout as errt:
        raise errt
    except requests.exceptions.RequestException as err:
        raise err
    return r

def extract_data(data):
    if data != []:
        if "method" in data and "url" in data:
            if "body" in data and "headers" in data and "authorization" in data:
                return data["method"],data["url"],data["body"],data["headers"],data["authorization"]
            elif not "headers" in data and "body" in data and "authorization" in data:
                return data["method"],data["url"],data["body"],None,data["authorization"]
            elif not "body" in data and "headers" in data and "authorization" in data:
                return data["method"],data["url"],None,data["headers"],data["authorization"]
            elif "body" in data and "headers" in data and not "authorization" in data:
                return data["method"],data["url"],data["body"],data["headers"],None
            elif not "headers" in data and "body" in data and not "authorization" in data:
                return data["method"],data["url"],data["body"],None,None
            elif not "body" in data and "headers" in data and not "authorization" in data:
                return data["method"],data["url"],None,data["headers"],None
            else:
                return data["method"],data["url"],None,None,None
        else:
            print('ERR/(0x002): Method and Url is required.')
            return False
    else:
        print('ERR/(0x002): For extract data the file is should not be empty')
        return False
