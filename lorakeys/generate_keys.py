#!/usr/bin/env python
# Generates one AppEUI and list of AppKeys
# 1: number of AppKeys to generate
# 2: EUI prefix to use (default: 70b3d549)

DEFAULT_PREFIX= '70b3d549'
import secrets
import argparse


def gen_list(prefix, n):
    print("AppEUI: {}{}".format(prefix, secrets.token_hex(4)))
    print("AppKeys: ")  
    for i in range(0, n):
        print(secrets.token_hex(16))        

parser = argparse.ArgumentParser(description='Generate an App EUI and list of AppKeys')
parser.add_argument('number_of_keys', type=int, help='number of AppKeys to generate (default: 1)')
parser.add_argument('--prefix', type=str, default=DEFAULT_PREFIX, help='EUI prefix to use (default:' + DEFAULT_PREFIX+ ')')
args = parser.parse_args()

gen_list(args.prefix, args.number_of_keys)