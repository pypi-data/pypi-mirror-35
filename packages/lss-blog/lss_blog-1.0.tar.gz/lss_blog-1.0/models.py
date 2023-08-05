'''
个人博客
    用户[管理员、会员]
        管理员[查看所有会员、查看单个会员、查看所有文章、查看单篇文章、删除会员]
        会员[查看个人资料、修改登录密码、发表文章，查看所有文章，查看个人文章(删除/修改文章)]
'''
import pickle
class User:

    def __init__(self,username,password,nickname,gender,age,email,phone):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.gender = gender
        self.age = age
        self.email = email
        self.phone = phone


class Manager(User):

    def __init__(self,username,password,nickname,gender,age,email,phone):
        super(Manager,self).__init__(username,password,nickname,gender,age,email,phone)
        self.status = "管理员"


class Member(User):

    def __init__(self,username,password,nickname,gender,age,email,phone,address,info):
        super(Member, self).__init__(username, password, nickname,gender,age,email,phone)
        self.address = address
        self.info = info
        self.status = "会员"


class Title:

    def __init__(self,title_name,content,author):
        self.title_name = title_name
        self.content = content
        self.author = author
        self.status = "文章"


class DataService:
    '''数据服务类型'''

    def __init__(self):
        #初始化一个文件夹名称
        self.project_file = "user.dat"
        self.title_file = "article.dat"
        # self.data_users = list()
        # self.data_titles = list()
        #初始化数据
        self.get_data()
        self.get_title_data()

    def get_data(self):
        self.data_users = pickle.load(open(self.project_file,"rb"))

    def save_data(self):
        pickle.dump(self.data_users,open(self.project_file,"wb"))

    def get_users(self):
        return self.data_users

    def set_users(self,username):
        self.data_users = username

    def add_user(self,user):
        self.data_users.append(user)


    def get_title_data(self):
        self.data_titles = pickle.load(open(self.title_file,"rb"))

    def save_title_data(self):
        pickle.dump(self.data_titles,open(self.title_file,"wb"))

    def get_titles(self):
        return self.data_titles

    # def set_titles(self,username):
    #     self.data_titles = username

    def add_title(self,title):
        self.data_titles.append(title)


# sd = DataService()
# sd.save_data()
# sd.save_title_data()

class ManagerService:
    '''管理员服务'''
    def __init__(self):
        self.data = DataService()

    def record_manager(self):
        username = input("请输入管理员账号：")
        password = input("请输入管理员密码：")
        nickname = input("请输入管理员昵称：")
        gender = input("请输入管理员性别：")
        age = input("请输入管理员年龄：")
        email = input("请输入管理员邮箱：")
        phone = input("请输入管理员电话：")


        #创建对象
        manager = Manager(username,password,nickname,gender,age,email,phone)
        #保存对象
        self.data.add_user(manager)
        #同步数据
        self.data.save_data()


    def find_all_member(self):
        '''查看所有会员'''
        members = list()
        users = self.data.get_users()

        for user in users:
            if user.status == "会员":
                members.append(user)
        return members


    def find_single_member(self,name):
        '''查看单个会员'''
        members = self.find_all_member()
        for m in members:
            if name == m.username:
                return m
        else:
            return False


    def find_all_title(self):
        '''查看所有文章'''
        titles = list()
        title_data = self.data.get_titles()
        for title in title_data:
            if title.status == "文章":
                titles.append(title)
        return titles


    def find_single_title(self,name):
        '''查看单个文章'''
        titles = self.find_all_title()
        for title in titles:
            if name == title.title_name:
                return title


class MemberService:
    '''会员服务类型'''
    def __init__(self):
        self.data = DataService()

    def record_member(self):

        username = input("请输入会员账号：")
        password = input("请输入会员密码：")
        nickname = input("请输入会员昵称：")
        age = input("请输入会员年龄：")
        gender = input("请输入会员性别：")
        email = input("请输入会员邮箱：")
        address = input("请输入会员邮箱：")
        phone = input("请输入会员电话：")
        info = input("请输入会员介绍：")

        #创建对象
        member = Member(username,password,nickname,gender,age,email,phone,address,info)
        #添加对象
        self.data.add_user(member)
        #保存对象
        self.data.save_data()


    def change_password(self,user_login):
        '''修改登录密码'''
        password = input("请输入原密码：")
        if password == user_login.password:
            new_password = input("请输入新密码:")
            new2_password = input("请再次输入新密码:")
            if new_password == new2_password:
                user_login.password = new_password
                input("密码修改成功，按任意键继续！")
                self.data.save_data()
                return True
        else:
            c = input("您输入的密码有误，按[Y]重新输入，任意键返回")
            if c.upper() == "Y":
                return False
            else:
                return True


    def public_title(self,author):
        '''发表文章'''
        title_name = input("请输入文章标题：")
        content = input("请输入文章内容：")
        title = Title(title_name,content,author)
        #添加文章
        self.data.add_title(title)
        #保存文章
        self.data.save_title_data()
        print("发表文章成功·········")
        return title


    def find_all_title(self):
        '''查看所有文章'''
        titles = list()
        title_data = self.data.get_titles()
        for title in title_data:
            if title.status == "文章":
                titles.append(title)
        return titles


    def find_single_title(self,name):
        '''查看单个文章'''
        titles = self.find_all_title()
        for title in titles:
            if name == title.title_name:
                return title


class Service:

    def __init__(self):
        self.service = DataService()

    def login(self):
        '''用户登录'''
        print("\t用户登陆界面")
        users = self.service.get_users()
        username = input("请输入账号：")
        password = input("请输入密码：")
        for user in users:
            if user.username == username:
                if user.password == password:
                    print("登陆成功！")
                    if user.status == "管理员":
                        return 1
                    else:
                        self.user_login = user
                        return 2
        else:
            input("您的账号或密码有误，请重新输入！")
            return False










