n = 2

fib = [0, 1]
for i in xrange(n):
    fib = [fib[1], fib[0] + fib[1]]
print fib[1]

exit(0)

import os, multiprocessing

def init(env):
    os.environ = env
    os.environ['FOO'] = "foo_1"

def myfunc():
    print os.environ['FOO']

if __name__ == "__main__":
    child_env = os.environ.copy()
    child_env['FOO'] = "foo_2"
    pool = multiprocessing.Pool(initializer=init, initargs=(child_env,))
    child_env['FOO'] = "foo_3"
    for i in xrange(3):
        print i
        pool.apply_async(myfunc,())
    pool.close()
    pool.join()