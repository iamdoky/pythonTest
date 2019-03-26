json_obj = {"name":"홍길동",
            "age":"32",
            "where":"역삼동",
            "phone":"010-6631-5135",
            "friends":[
                {'name':'슬기','age':'26'},
                {'name':'이솜','age':'23'}
            ]
            }
print(json_obj['name'])
print(json_obj['phone'])
friends = json_obj['friends']
for friend in friends:
    print(friend['name'])