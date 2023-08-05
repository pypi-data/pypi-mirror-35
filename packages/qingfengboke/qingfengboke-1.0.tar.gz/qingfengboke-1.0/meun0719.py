#用户所需函数

import data0719,tools0719,sys

#登陆界面函数
def show_login():
    print("*"*30)
    print("*\t\t博客网站")
    print("*\t\t1、用户登录")
    print("*\t\t2、用户注册")
    print("*\t\t3、退出系统")
    print("*" * 30)

    a = input("请输入您的选项：")

    if a == "1":
        #登陆界面
        re = tools0719.user_login()
        if re == True:
            #展示首页界面
            pass
        else:
            #返回登录首面
            return show_login()

    elif a == "2":
        #注册界面
        re = tools0719.user_register()
        if re == True:
            #返回登录首页
            return show_login()
        else:
            #重新输入
            return tools0719.user_register()

    elif a == "3":
        #退出系统
        return tools0719.exit_sysytem()

    else:
        #没有这个选项
        input("没有这个选项，按任意键返回菜单")
        return show_login()

def show_index():
    # 展示登陆成功后的页面
    print("*" * 30)
    print("*\t\t博客网站")
    print("*\t\t1、查看用户信息")
    print("*\t\t2、修改登录密码")
    print("*\t\t3、完善个人资料")
    print("*\t\t4、发表文章")
    print("*\t\t5、查看文章")
    print("*\t\t6、删除文章")
    print("*\t\t7、返回上一级菜单")
    print("*\t\t8、退出系统")
    print("*" * 30)

    b = input("请输入您的选项：")

    if b == "1":
        #查看用户信息
        pass

    elif b == "2":
        #修改登录密码
        pass

    elif b == "3":
        #完善个人资料
        pass

    elif b == "4":
        #发表文章
        pass

    elif b == "5":
        #查看文章
        pass

    elif b == "6":
        #删除文章
        pass

    elif b == "7":
        #返回上一级菜单
        return show_login()

    elif b == "8":
        #退出系统
        return tools0719.exit_sysytem()

    else:
        input("没有这个选项，请按任意键返回首页菜单")
        return show_index()

