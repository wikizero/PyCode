# coding:utf-8
from functools import partial


def longest_common_prefix(lst):

	if not lst:
		return ''

	for i in zip(*lst):
		if len(set(i)) > 1:
			return lst[0][:i]

	return min(lst)

lst = ['aad', 'aad', 'aad', 'aad']
print longest_common_prefix(lst)


def valid_parentheses(s):
	temp = []
	dct = {')': '(', ']': '[', '}': '{'}
	for char in s:
		if char in dct.values():
			temp.append(char)
		elif char in dct.keys():
			if temp == [] or dct[char] != temp.pop():
				return False
	return temp == []

print valid_parentheses('(asd)asd[asd]sa{asd}')


# (1) xrange代替range

# (2) izip 代替 zip

# (3) print sorted(colors, key=len) colors是个list 按元素长度排序

# (4) 调用一个函数直到遇到标记值
blocks = []
for block in iter(partial(f.read, 32), ''):
	blocks.append(block)

# (5) 用字典计数
d = {}
for color in colors:
 d[color] = d.get(color, 0) + 1
# 稍微潮点的方法，但有些坑需要注意，适合熟练的老手。
d = defaultdict(int)
for color in colors:
 d[color] += 1


# (6) 用字典分组 -- 第I部分和第II部分
names = ['raymond', 'rachel', 'matthew', 'roger',
 'betty', 'melissa', 'judith', 'charlie']
# 在这个例子，我们按name的长度分组
d = defaultdict(list)
for name in names:
 key = len(name)
 d[key].append(name)

# (7)
字典的popitem()是原子的吗？
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
while d:
 key, value = d.popitem()
 print key, '-->', value
popitem是原子的，所以多线程的时候没必要用锁包着它。

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s

for digit, group in itertools.groupby('111221'):
    print digit, group
    print list(group)

print re.findall(r'((.)\2*)', ss)
http://www.jb51.net/tools/zhengze.html

# 字典合并方法
dct1 = {'reverse0': [(609L, 4.585), (615L, 4.285), (966L, 3.585)]}
dct2 = {'reverse1': [(619L, 3.185), (625L, 4.655), (936L, 1.585)]}

print zip(**{'a':'A', 'b':'B'})

print dict(dct1.items() + dct2.items())

print dict(dct1, **dct2)

temp = dct1.copy()
temp.update(dct2)
print temp

如果希望从网络读取文件进行处理，但是又不希望保存文件到硬盘，可以使用cStringIO模块进行处理
res = urllib2.urlopen(pic,timeout=10)
f = cStringIO.StringIO(res.read())
f 是一个文件对象，
它和：f = open('c:/1.jpg','rw')  打开的文件一样
可以向操作本地文件一样对内存文件进行读写

m, s = divmod(round(230962/1000.0), 60)
print ("%02d:%02d" % (m, s))

正则
http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
 regex： www.cnblogs.com/animalize/p/4949219.html
