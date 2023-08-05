import data,sys

username = data.users

#空间主界面

def show_info():
    print("\t欢迎来到私人素描的空间")
    print("*!~"*20)
    print("\t1. 帐号登录")
    print("\t2. 帐号注册")
    print("\t3. 退出系统")
    print("*!~"*20)
    choice = input("请输入你的选项：")
    if choice == "1":
        #帐号登录
        return login()
        #登陆成功，商城主页
        pass

    elif choice == "2":
        #帐号注册
        return register()

    elif choice == "3":
        #退出系统
        return sys_exit()

    else:
        input("输入有误，请重新输入，按任意键继续")
        show_info()


#帐号登录
def login():
    res = False
    username = input("请输入你的账号<输入exit返回>：")
    if username == "exit":
        show_info()
    elif username in data.users:
        userpass = input("请输入你的密码：")
        if userpass == data.users[username]["password"]:
        # if userpass == data.username["password"]:
            global user
            user = data.users[username]
            input("登陆成功，按任意键继续")
            return home_page()

        else:
            return login()




#查看个人信息
# def my_info(**kwargs):
#     print(**kwargs)
# my_info(user)
def my_info():
    my = user
    print(user)
    print("*!~"*20)
    choice = input("按A键返回空间主页,按R键返回登录界面,按其他键继续查看个人信息")
    if choice == "A":
        return home_page()
    elif choice == "R":
        return login()
    else :
        return my_info()




#空间主页
def home_page():
    print("\t欢迎来到私人素描的空间")
    print("*!~"*20)
    print("\t1. 购买商品")
    print("\t2. 休闲小游戏")
    print("\t3. 查看个人信息")
    print("\t4. 返回登录界面")
    print("*!~"*20)
    choice = input("请输入你的选项：")
    if choice == "1":
        #购买商品
        pass

    elif choice == "2":
        #休闲小游戏
        pass
    elif choice == "3":
        #查看个人信息
        my_info()

    elif choice == "4":
        #返回登陆界面
        return show_info()

    else :
        input("输入有误，按任意键重新输入")
        return home_page()


#帐号注册
def register():
    username = input("请输入你想要的账号：")
    if username in data.users:
        input("帐号已存在，请重新注册，按任意键继续")
        return register()
    else:
        password = input("请输入你的密码：")
        nickname = input("请输入你的昵称：")
        #创建一个用户字典
        u3 = {"username":username,
              "password":password,
              "nicename":nickname
              }
        #将新建的用户字典添加到data中的用户字典中
        data.users[username] = u3
        choice = input("帐号注册成功，按R键进入登录系统，其他键返回空间主界面")
        if choice == "R":
            login()
        else :
            show_info()



#退出系统
def sys_exit():
    sys.exit(1)



