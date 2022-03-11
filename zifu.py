fp = open('/opt/test/a.txt', 'r', encoding='utf-8')
content = fp.read()
print(content)
li, li2, li3, li4 = [], [], [], []
for j in range(97, 123):
    li.append(j)
for v in li:
    li2.append(chr(v))
for j in range(65, 91):
    li3.append(j)
for v in li3:
    li4.append(chr(v))


def my_count(fun):
    def inner(con, s):
        n = content.count(s)
        fun(li, s)
        return n

    return inner


@my_count
def count(li, s):
    pass


print('各个字母出现的次数: ')
for v in li2:
    print(v, count(content, v), end='| ')
print()
# for v in li4:
#     print(v, count(content, v), end='| ')
# print()
