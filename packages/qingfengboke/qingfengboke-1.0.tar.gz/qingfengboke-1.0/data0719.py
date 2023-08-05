#创建一个字典，用来存一个用户的信息
u1 = {
    "username": "admin",
    "password": "123",
    "nicheng": "白王爷"
      }

u2 = {
    "username": "manage",
    "password": "123",
    "nicheng": "黑王爷"
}

#创建一个词典，用来存 所有用户的信息
users = {"admin": u1,
         "manage":u2}

#声明一个全局变量
login = None

