import json

str = '{"name":"홍길동","age":"32"}'
print(str)
print(type(str))

str2 = {"name":"홍길동","age":"32"}
print(str2)
print(type(str2))

r = json.loads(str)
print(r)
print(type(r))