# -*- coding:utf-8 -*-
import requests
import json

class HttpEngine():
    def getData(s, url, data, header, method):
        re = object
        isexcept = False
        if method == "post":
            try:
                re = s.post(url, headers=header, data=data)
            except requests.exceptions.ConnectionError as e:
                re = e
                isexcept = True

        if method == "get":
            try:
                re = s.get(url, headers=header, data=data)
            except requests.exceptions.ConnectionError as e:
                re = e
                isexcept = True

        if method == "delete":
            try:
                re = s.delete(url + "/" + data)
            except requests.exceptions.ConnectionError as e:
                re = e
                isexcept = True

        if method == "put":
            try:
                re = s.put(url)
            except requests.exceptions.ConnectionError as e:
                re = e
                isexcept = True

        return re, isexcept


