#!/usr/bin/env python

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import argparse
import client
import helper

class C:
    pass

c = C()

def main():

    parser = argparse.ArgumentParser(
        prog=helper.utilName,
        description='通过GA协议获取数据，用于调试GA控件树。示例：' + helper.commonTip,
        usage=helper.commonTip
    )
    parser.add_argument('get', help='通过GA协议获取数据')
    parser.add_argument('cmd', type=int, help='协议CMD，300获取控件树名称和属性信息，103获取控件树的布局位置信息')
    parser.add_argument('--port', dest='port', type=int, help=helper.portTip)
    args = parser.parse_args(namespace=c)
    if args.get:
        if args.port:
             client.init_client(int(args.port), int(args.cmd))
        else:
            print('请先指定' + helper.portTip + '。示例：' + helper.commonTip)
    else: 
        print(helper.commonTip)        
if __name__ == '__main__':
    main()
