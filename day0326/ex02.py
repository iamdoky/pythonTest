import json
str = '[{"name":"홍길동","age":"20"},{"name":"강감찬","age":"30"}]'
list = json.loads(str)

print(str)
print(type(str))
print(str[0])
print(list)
print(type(list))
print(list[0])

