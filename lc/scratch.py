from multiprocessing import Pool
def f(x):
    return x*x
if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(f, [10])    # evaluate "f(10)" asynchronously
    print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"
exit(0)

import os, multiprocessing
def init(env):
    os.environ = env




def myfunc():
    print os.environ['FOO']

if __name__ == "__main__":
    child_env = os.environ.copy()
    child_env['FOO'] = "foo"
    pool = multiprocessing.Pool()
    pool.apply(myfunc,())
    pool.close()
    pool.join()
exit(0)

import re
print re.split('(https)', 'Join us!https://t.co/Fe0oTahdom')



exit(0)
candy = []
with open('demo.txt', 'r') as f:
    for line in f:
        line = line.strip()
if len(line) > 0:
    candy.append(map(int, line.split(',')))
print(candy)

parsedList=[]
with open("demo.txt","r") as f:
    lst=f.read().splitlines()
    for i in lst:
        parsedList.append(i.split())
with open("days.txt","r") as f:
    param = int(f.readline().split("=")[1])

for innerList in parsedList:
    for element in innerList:
        if element.isdigit():
            if int(element)>=param:
                print " "
            else:
                print "$"
        else:
            print "?"
    print








exit(0)



myDict = {'R':'AG', 'Y':'CT', 'M':'CA', 'G':'G', 'D':'ATG', 'A':'A'}
myString = "ARD"

results = []

def recu(str, pos):
    for w in myDict[myString[pos]]:
        if len(myString) - 1 == pos:
            results.append(str + w)
        else:
            recus(str + w, pos + 1)

recu('', 0)
print results

exit(0)

unknown = ['X', 9, 2, 1, 8, 'X', 8]

new = [[x, 9, 2, 1, 8, x, 8, 7, 0, 8, 8, 0, 5, 0, 8, 9] for x in xrange(10)]

print new

exit(0)

import csv
with open('timesheet.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    print your_list
    for x in your_list:
        print x
        current_date = x[0][:10]
        print current_date

exit(0)

from collections import OrderedDict

a = OrderedDict()
a[1] = 2
a[2] = 3
del a[1]
a[1] = 3
print a.popitem()
print a.popitem()

exit(0)

import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

a = Trie()
a.insert("abc")
a.insert("ab")
a.search("c")

exit(0)


def fib(r,a,b):
    return [a] + fib(r-1,b,a+b) if r>0 else []

print fib(5,1,10)

exit(0)



from copy import deepcopy

def aa(l):
    l[0], l[1] = (2,3)

l1 = [1,2,3]
aa(l1)
print l1


exit(0)

d = {1:2, 3:4, 5:6}
l = sorted(d.keys())
for i in range(0, len(d)):
    l.insert(i+1, d[l[i]])
    l.append(d[l[-1]])


exit(0)

import numpy
assignment = numpy.zeros((12,10),dtype=int)
for i in range(0,12,3):
    for j in range(10):
        assignment[i:i+3,j] = numpy.random.permutation(3)


print assignment


exit(0)
import csv
from time import strptime
print "Please fill out the following information:"
with open('userinfo.csv', 'a') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)

    name = raw_input("Your name:")
    def get_date():
        while True:
            date = raw_input("Please enter a date in MM/DD/YY format:")
            try:
                parsed = strptime(date, "%m/%d/%Y")
            except ValueError as e:
                print "Could not parse date: {0}".format(e)
            else:
                return parsed[:3], date
    (year, month, day), date = get_date()
    print date
    employeeid =raw_input("EmployeeID:")
    w.writerow([name,date,employeeid])

exit(0)

class a(object):
    def __init__(self, id):
        self.id = id


a1 = a(1)
a2 = a(2)

A = [a1,a2]
B = [1]

print A
print [x.id for x in A]




exit()




s = "bcba"
result = ""
#if len(s) == 0:
    #return result
s1 = s + s[::-1]
pre = [0] * len(s1)
for i in range(1, len(s1)):
    j = pre[i-1]
    while j > 0 and s1[i] != s1[j]:
        j = pre[j-1]
    if s1[i] == s1[j]:
        pre[i] = j + 1
    else:
        pre[i] = 0
print pre