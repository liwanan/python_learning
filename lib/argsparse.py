#!/usr/bin/env python3
"""""""""""""""""""""""""""""""""
" 功能描述：解析命令行参数
" 作者：liwanan@aliyun.com
" 修改时间：2019/11/10 10:56:26
"""""""""""""""""""""""""""""""""
import argparse

parser = argparse.ArgumentParser(description="解析解析命令行参数")
#添加参数
parser.add_argument("-c", "--client", default="127.0.0.1", help="Client IP address")
parser.add_argument("-s", "--server", default="127.0.0.1", help="Server IP address")
args = parser.parse_args()
#获取参数值
client = args.client
server = args.server

if __name__ == '__main__':
	print(client)
	print(server)