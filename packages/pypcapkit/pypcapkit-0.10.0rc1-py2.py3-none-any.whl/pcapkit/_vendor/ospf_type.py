# -*- coding: utf-8 -*-

import csv
import os
import re

import requests


ROOT = os.path.dirname(os.path.abspath(__file__))

page = requests.get('https://www.iana.org/assignments/ospfv2-parameters/ospfv2-parameters-3.csv')
data = page.text.strip().split('\r\n')

reader = csv.reader(data)
header = next(reader)

oper = list()
for item in reader:
    name = item[1]
    rfcs = item[2]
    temp = list()
    for rfc in filter(None, re.split(r'\[|\]', rfcs)):
        if 'RFC' in rfc:
            temp.append(f'[{rfc[:3]} {rfc[3:]}]')
        else:
            temp.append(f'[{rfc}]')
    desc = f"# {''.join(temp)}" if rfcs else ''
    try:
        code = int(item[0])
        oper.append(f"{code:>5} : '{name}',".ljust(50) + desc)
        # print(code, name, ''.join(temp))
    except ValueError:
        start, stop = map(int, item[0].split('-'))
        for code in range(start, stop+1):
            oper.append(f"{code:>5} : '{name} ({code})',".ljust(50) + desc)
            # print(code, name, ''.join(temp))

with open(os.path.join(ROOT, '../_common/ospf_type.py'), 'w') as file:
    file.write('# -*- coding: utf-8 -*-\n\n')
    file.write('# OSPF Packet Types\n')
    file.write('OPER = {\n')
    file.write('\n'.join(oper))
    file.write('\n}\n')
