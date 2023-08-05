'''菜单引擎'''

import models
import tools
class Engine:

    def __init__(self):
        self.manager_service = models.ManagerService()
        self.member_service = models.MemberService()
        self.data = models.DataService()
        self.service = models.Service()

    def show_index(self):
        print("\t个人博客")
        print("^~"*20)
        print("\t\t1.用户登录")
        print("\t\t2.注册一个会员")
        print("\t\t3.注册一个管理员")
        print("\t\t4.退出系统")
        print("^~"*20)

        choice = input("请选择：")

        if choice == "1":
            res = self.service.login()
            if res == 1:
                return self.manager_index()
            elif res == 2:
                return self.member_index()
            else:
                return self.show_index()
        elif choice == "2":
            self.member_service.record_member()
            return self.show_index()
        elif choice == "3":
            self.manager_service.record_manager()
            return self.show_index()
        elif choice == "4":
            tools.exit()
        else:
            input("没有该选项，按任意键继续！")
            return self.show_index()


    def manager_index(self):
        '''
        管理员[查看所有会员、查看单个会员、查看所有文章、查看单篇文章、删除会员]
        :return:
        '''
        print("您的身份是：管理员")
        print("_-"*20)
        print("\t\t1.查看所有会员")
        print("\t\t2.查看单个会员")
        print("\t\t3.查看所有文章")
        print("\t\t4.查看单篇文章")
        print("\t\t5.删除会员")
        print("\t\t6.返回登陆界面")
        print("\t\t7.退出系统")
        print("_-"*20)

        choice = input("请选择：")

        if choice == "1":
            #查看所有会员
            self.members = list()
            member = self.manager_service.find_all_member()
            self.members.extend(member)
            self.show_users_info(self.members)
            return self.manager_index()
        elif choice == "2":
            #查看单个会员
            self.show_member_single()
            self.show_users_info(self.member)
            return self.manager_index()
        elif choice == "3":
            #查看所有文章 TODO
            titles = self.manager_service.find_all_title()
            self.show_all_title(titles)
            return self.manager_index()
        elif choice == "4":
            #查看单篇文章 TODO
            title = self.show_single_title()
            if title == False:
                return self.manager_index()
            else:
                self.show_title(title)
                return self.manager_index()
        elif choice == "5":
            #删除会员 TODO
            pass
        elif choice == "6":
            return self.show_index()
        elif choice == "7":
            return tools.exit()
        else:
            input("没有该选项，按任意键继续")
            return self.manager_index()

    def member_index(self):
        '''会员界面'''
        '''
        会员[查看个人资料、修改登录密码、发表文章，查看所有文章，查看个人文章(删除/修改文章)]

        '''
        # 初始化登陆用户
        self.user_login = None
        self.user_login = self.service.user_login

        print("尊敬的会员：%s"%self.user_login.username)
        print("_-" * 20)
        print("\t\t1.查看个人资料")
        print("\t\t2.修改登陆密码")
        print("\t\t3.发表文章")
        print("\t\t4.查看所有文章")
        print("\t\t5.查看个人文章")
        print("\t\t6.返回登陆界面")
        print("\t\t7.退出系统")
        print("_-" * 20)

        choice = input("请选择：")

        if choice == "1":
            #查看个人资料
            self.user_info = list()
            self.user_info.append(self.user_login)
            self.show_users_info(self.user_info)
            return self.member_index()
        elif choice == "2":
            #修改登录密码
            res = self.member_service.change_password(self.user_login)
            if res == True:
                return self.show_index()
            else:
                return self.member_service.change_password(self.user_login)
        elif choice == "3":
            #发表文章 TODO
            title = self.member_service.public_title(self.user_login)
            self.show_title(title)
            return self.member_index()
        elif choice == "4":
            #查看所有文章 TODO
            titles = self.member_service.find_all_title()
            self.show_all_title(titles)
            return self.member_index()
        elif choice == "5":
            #查看个人文章 TODO
            title = self.show_single_title()
            if title == False:
                return self.member_index()
            else:
                self.show_title(title)
                return self.member_index()
        elif choice == "6":
            return self.show_index()
        elif choice == "7":
            return tools.exit()
        else:
            input("没有该选项，按任意键继续")
            return self.member_index()


    def show_users_info(self,show_object):
        print("用户管理系统----信息展示")
        print("=="*20)
        print("账号\t\t昵称\t\t性别\t\t年龄\t\t邮箱\t\t电话\t\t地址\t\t个人介绍\t\t状态")
        for user in show_object:
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s"%(user.username,
                                                                        user.nickname,
                                                                        user.gender,
                                                                        user.age,
                                                                        user.email,
                                                                        user.phone,
                                                                        user.address,
                                                                        user.info,
                                                                        user.status))
        print("==" * 20)
        input("按任意键继续")
        # return self.manager_index()


    def show_member_single(self):
        '''展示单个会员信息'''
        self.members = list()
        self.member = list()
        member = self.manager_service.find_all_member()
        self.members.extend(member)
        print("会员名称列表：")
        for member in self.members:
            print("会员名称：%s"%member.nickname)
        name = input("请输入会员名称:")
        member = self.manager_service.find_single_member(name)
        if member == False:
            input("没有该会员，按任意键继续！")
            return self.manager_index()
        else:
            self.member.append(member)
            return self.member


    def show_title(self,title):
        '''展示文章信息'''
        print("--"*20)
        print("文章信息如下:")
        print("文章标题：%s"%title.title_name)
        print("=================================================")
        print("内容：%s"%title.content)
        print("=================================================")
        print("作者：%s"%title.author.username)
        print("--"*20)
        input("按任意键返回")
        #return self.member_index()

    def show_all_title(self,titles):
        '''展示所有文章信息'''
        for title in titles:
            print("文章标题：%s"%title.title_name)
            print("作者：%s"%title.author.username)
            print("===========================")

        input("按任意键继续!")

    def show_single_title(self):
        '''展示单个文章信息'''
        self.titles = list()
        #self.title = list()
        title = self.manager_service.find_all_title()
        self.titles.extend(title)
        print("文章列表：")
        for title in self.titles:
            print("文章名称：%s" % title.title_name)
        title_name = input("请输入文章名称:")
        title = self.manager_service.find_single_title(title_name)
        if title == False:
            input("没有该文章，按任意键继续！")
            return self.manager_index()
        else:
            #self.title.append(title )
            return title







