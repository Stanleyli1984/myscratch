from collections import OrderedDict
import json, pickle, yaml, marshal
import timeit

#with open (r"test.marshal_v4", 'wb') as fp, open (r"origin.yaml") as fp1:
#    marshal.dump(yaml.load(fp1), fp, 4)

#exit()

run = '''{unit}.load(fp)'''

init = '''import {unit}
fp = open(r"test.{ext}", '{method}')'''

cmds = []
cmds.append((run.format(unit='json'), init.format(unit='json', ext='json', method='r'), 'json'))
cmds.append((run.format(unit='yaml'), init.format(unit='yaml', ext='yaml', method='r'), 'yaml'))
cmds.append((run.format(unit='pickle'), init.format(unit='pickle', ext='pickle_v0', method='rb'), 'pickle v0'))
cmds.append((run.format(unit='pickle'), init.format(unit='pickle', ext='pickle_v1', method='rb'), 'pickle v1'))
cmds.append((run.format(unit='pickle'), init.format(unit='pickle', ext='pickle_v2', method='rb'), 'pickle v2'))
cmds.append((run.format(unit='pickle'), init.format(unit='pickle', ext='pickle_v3', method='rb'), 'pickle v3'))
cmds.append((run.format(unit='pickle'), init.format(unit='pickle', ext='pickle_v4', method='rb'), 'pickle v4'))
cmds.append((run.format(unit='marshal'), init.format(unit='marshal', ext='marshal_v0', method='rb'), 'marshal v0'))
cmds.append((run.format(unit='marshal'), init.format(unit='marshal', ext='marshal_v1', method='rb'), 'marshal v1'))
cmds.append((run.format(unit='marshal'), init.format(unit='marshal', ext='marshal_v2', method='rb'), 'marshal v2'))
cmds.append((run.format(unit='marshal'), init.format(unit='marshal', ext='marshal_v3', method='rb'), 'marshal v3'))
cmds.append((run.format(unit='marshal'), init.format(unit='marshal', ext='marshal_v4', method='rb'), 'marshal v4'))


for run_cmd, init_cmd, title in cmds:
    print('LOAD {}: '.format(title.upper()), min(timeit.Timer(stmt=run_cmd, setup=init_cmd).repeat(repeat=5, number=1)))



