# -*- coding: utf-8 -*-

import os
import re

import requests


ROOT = os.path.dirname(os.path.abspath(__file__))

page = requests.get('http://www.tcpdump.org/linktypes.html')
table = re.split(r'\<[/]*table.*\>', page.text)[1]
contents = re.split(r'\<tr valign=top\>', table)[1:]

linktype = list()
for content in contents:
    item = content.strip().split('<td>')
    name = item[1].strip('</td>')[9:]
    desc = item[3].strip('</td>')
    try:
        code = int(item[2].strip('</td>'))
        linktype.append(f"{code:>5} : '{name}',".ljust(50) + f"# {desc}")
        # print(code, name, desc)
    except ValueError:
        start, stop = map(int, item[2].strip('</td>').split('-'))
        for code in range(start, stop+1):
            linktype.append(f"{code:>5} : 'USER{code-start}',".ljust(50) + f"# DLT_USER{code-start}")
            # print(code, f'USER{code-start}', f'DLT_USER{code-start}')

with open(os.path.join(ROOT, '../_common/linktype.py'), 'w') as file:
    file.write('# -*- coding: utf-8 -*-\n\n')
    file.write('# Link-Layer Header Type Values\n')
    file.write('LINKTYPE = {\n')
    file.write('\n'.join(linktype))
    file.write('\n}\n')
