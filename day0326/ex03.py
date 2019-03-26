import json
s= '{"name":"김경","age":"20"}'
obj = json.loads(s)

print(obj)
print(type(obj))

j = json.dumps(obj)
print(j)
print(type(j))


r = str(obj)
print(r)
print(type(r))