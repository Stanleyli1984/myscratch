from collections import OrderedDict
import json, pickle, yaml, marshal

x = OrderedDict([('z', 3), ('x', 2), ('y', 1), ('xx', 5), ('xz', 4)])
print('json:', json.loads(json.dumps(x)))
print('pickle:', pickle.loads(pickle.dumps(x)))
print('YAML:', yaml.load(yaml.dump(x)))
print('marshal:', marshal.loads(marshal.dumps(x)))
