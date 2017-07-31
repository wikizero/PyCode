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