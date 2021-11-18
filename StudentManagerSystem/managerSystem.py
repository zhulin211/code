# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
from student import *


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()

        while True:
            self.show_menu()

            menu_num = int(input('请输入您需要的功能序号：'))
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    #2.1 显示功能菜单 ---打印序号的功能对应关系 --静态
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1: 添加学员')
        print('2: 删除学员')
        print('3: 修改学员')
        print('4: 查询学员')
        print('5: 显示所有学员')
        print('6: 保存')
        print('7: 退出系统')
    #2.2 添加学员
    def add_student(self):
        # 1. 输入姓名性别手机号
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的电话：')
        # 2. 创建学员对象 -----类在student文件里面
        student = Student(name, gender, tel)
        # 3. 将该对象添加到学员列表
        self.student_list.append(student)
        print(self.student_list)    # cesh
        print(student)              # desh
    #2.3 删除学员
    def del_student(self):
        # print('删除学员')
        # 1. 用户输入目标学员姓名
        del_name = input('请输入要删除需要的姓名：')
        #2. 如果用户输入的学员存在则删除，否则提示学员不存在
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print('查无此人')
        #验证
        print(self.student_list)
    #2.4 修改学员信息
    def modify_student(self):
        modify_name = input('请输入要修改的学员的姓名：')
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入学员姓名：')
                i.gender = input('请输入学员性别：')
                i.tel = input('请输入学员电话：')
                print(f'修改改学员信息成功，姓名{i.name}, 性别{i.gender}, 电话{i.tel}')
                break
        else:
            print('查无此人')
    #2.5 查询学员信息
    def  search_student(self):
        # print('查询学员')
        search_name = input('请输入要查询学员的姓名：')
        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名{i.name}, 性别{i.gender}, 电话{i.tel}')
                break
        else:
            print('查无此人')
    #2.6 显示所有学员信息
    def show_student(self):
        # print('显示学员')
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')
    #2.7 保存学员信息
    def save_student(self):
        # print('保存')
        f = open('student.data', 'w')
        #写入：写入的不能是对象的内存地址，需要先把学员数据转换成列表字典
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        f.write(str(new_list))
        f.close()
    #2.8 加载学员信息
    def load_student(self):
        # print('加载学员数据')
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            new_list = eval(data)
            self.student.list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()








if __name__ == '__main__':
    pass
