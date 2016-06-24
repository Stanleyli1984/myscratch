import json, pickle, yaml, marshal

from collections import OrderedDict
import json, pickle, yaml, marshal
import timeit

with open (r"origin.yaml") as fp:
    data = yaml.load(fp)

run = '''{unit}.dumps(data{method})'''
run_1 = '''{unit}.dump(data{method})'''

init = '''import {unit}
from __main__ import data'''

cmds = []
cmds.append((run.format(unit='json', method=''), init.format(unit='json', ext='json'), 'json'))
cmds.append((run_1.format(unit='yaml', method=''), init.format(unit='yaml', ext='yaml'), 'yaml'))
cmds.append((run.format(unit='pickle', method=',protocol=0'), init.format(unit='pickle', ext='pickle_v0'), 'pickle v0'))
cmds.append((run.format(unit='pickle', method=',protocol=1'), init.format(unit='pickle', ext='pickle_v1'), 'pickle v1'))
cmds.append((run.format(unit='pickle', method=',protocol=2'), init.format(unit='pickle', ext='pickle_v2'), 'pickle v2'))
cmds.append((run.format(unit='pickle', method=',protocol=3'), init.format(unit='pickle', ext='pickle_v3'), 'pickle v3'))
cmds.append((run.format(unit='pickle', method=',protocol=4'), init.format(unit='pickle', ext='pickle_v4'), 'pickle v4'))
cmds.append((run.format(unit='marshal', method=',0'), init.format(unit='marshal', ext='marshal_v0'), 'marshal v0'))
cmds.append((run.format(unit='marshal', method=',1'), init.format(unit='marshal', ext='marshal_v1'), 'marshal v1'))
cmds.append((run.format(unit='marshal', method=',2'), init.format(unit='marshal', ext='marshal_v2'), 'marshal v2'))
cmds.append((run.format(unit='marshal', method=',3'), init.format(unit='marshal', ext='marshal_v3'), 'marshal v3'))
cmds.append((run.format(unit='marshal', method=',4'), init.format(unit='marshal', ext='marshal_v4'), 'marshal v4'))


for run_cmd, init_cmd, title in cmds:
    print('LOAD {}: '.format(title.upper()), min(timeit.Timer(stmt=run_cmd, setup=init_cmd).repeat(repeat=5, number=1)))



