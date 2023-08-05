#用户所需函数

import data0719,sys

def user_login():
    #登录账号密码
    username = input("请输入账号：")
    if username in data0719.users:
        password = input("请输入密码：")

        user = data0719.users[username]

        if password == user["password"]:
            #登陆成功
            #展示用户内容
            input("登陆成功，按任意键继续")
            return True

        else:
            mi_ma = input("密码错误，按任意键重新登录")
            return False
    else:
        print("账号错误或者不存在")
        zhang_hao = input("按R重新登录")
        if zhang_hao == "R":
            return user_login()
        else:
            input("没有这个选项，按任意键返回菜单")
            return user_login()




def user_register():
    #注册账号
    username = input("请输入您要注册的账号：")
    if username in data0719.users:
        input("此账号已存在，请按任意键重新输入")
        return False
    password = input("请输入您要注册的密码：")
    nicheng = input("请输入您要注册的昵称：")

    #创建一个新的字典
    user1 = { username, password, nicheng}
    #把新创建的字典添加到users
    data0719.users[username] = user1
    input("注册成功，请按任意键返回首页登录")
    return True


def exit_sysytem():
    #退出系统
    print("用户大大，臣退了")
    print("这一退，可能就是一个辈子")
    print("感谢您的使用，再会")
    sys.exit(1)



