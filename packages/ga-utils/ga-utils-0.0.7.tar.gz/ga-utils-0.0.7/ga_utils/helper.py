import json
import xmltodict
import struct
import os
import time
from typing import Union

portTip = 'GA服务的本机tcp端口';
commonTip = 'ga-utils get 300 --port 2004';
utilName = 'ga-utils';

def xmltojson(xmlstr: str) -> str:
    xmlparse = xmltodict.parse(xmlstr, force_list=('GameObject', 'UWidget'))
    jsonstr = json.dumps(xmlparse,indent=1)
    return jsonstr

def deepLoop(data, child: str, callback):
    callback(data)
    if child in data:
        for item in data[child]:
            deepLoop(item, child, callback)

def getIds(data, child: str, attr: str) -> list[Union[int, str]]: 
    ids = [];
    def cb(node):
        if attr in node:
            ids.append(node[attr])
        else:
            ids.append(None)
    deepLoop(data, child, cb)
    return ids;

def handleIds(ids: list[Union[int, str]], isNumber: bool) -> list[Union[int, str]]:
    result = []
    origin = ids[1: ];
    if isNumber:
        for item in origin:
            result.append(int(item))
        return result
    else:
        return origin
def get_buffer(body: str):
    body_buffer = body.encode('UTF-8')
    head_buffer = struct.pack('<i', len(body_buffer))
    return body_buffer, head_buffer

def time_to_date(format_string="%Y-%m-%d %H:%M:%S"):
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date
 
def log(body):
    msg = body.decode('UTF-8')
    name = utilName + '.' + time_to_date(format_string="%Y-%m-%d") + '.log'
    file = os.getcwd() + '/' + name
    with open(file, 'a', encoding='UTF-8') as f:
        f.write(time_to_date(format_string="%Y-%m-%d %H:%M:%S"))
        f.write(': ')
        f.write(msg)
        f.write('\n')


