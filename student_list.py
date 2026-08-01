import json

def load_data():
    try:
        with open("student.json","r",encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return []
    
student_list = load_data()

def save_data(student_list):
    with open("student.json", "w", encoding="utf-8") as f:
        json.dump(student_list, f, ensure_ascii=False, indent=2)

def add_single_student(student_list):

    name = input("请输入学生姓名：")
    try:
        age = int(input("请输入学生年龄："))   
        score = int(input("请输入学生分数："))
        stu_dict = {"name": name, "age": age, "score": score}
        student_list.append(stu_dict)
        save_data(student_list)
    except ValueError:
        print("年龄分数请添加数字")


def search_student(student_list):
    name = input("请输入要查询的学生姓名：")
    found  = False
    for stu in student_list:
        if stu["name"] == name:
            print(f"姓名:{stu['name']},年龄:{stu['age']},分数:{stu['score']}")
            found = True
    if not found:
        print("未找到该学生")

def modify_student(student_list):
    name = input("请输入要修改的学生姓名：")
    found = False
    for stu in student_list:
        if stu["name"] == name:
            try:
                new_age = int(input("请输入新年龄："))
                new_score = int(input("请输入新分数："))
                stu["age"] = new_age
                stu["score"] = new_score
                print("修改成功！")
                found = True
                save_data(student_list)
            except ValueError:
                print("年龄分数请输入数字！")
    if not found:
        print("未找到该学生，修改失败")

def delete_student(student_list):
    name = input("请输入要删除的学生姓名：")
    for stu in student_list:
            if stu["name"] == name:
                student_list.remove(stu)
                print(f"学生{name}已删除！")
                save_data(student_list)
                return
            print("找不到这名学生！")

    
while True:
    print ("""====学生管理系统==== 
    1. 添加学生
    2. 查询学生
    3. 修改学生
    4. 删除学生
    0. 退出系统
    ===================
    请输入操作序号：""")
    try:
        num = int(input("请输入功能序号："))
        if num == 1:
            add_single_student(student_list)
        elif num == 2:
            search_student(student_list)
        elif num == 3:
            modify_student(student_list)
        elif num == 4:
            delete_student(student_list)
        elif num == 0:
            break
        else:
            print("请输入0~4")
    except ValueError:
        print("请输入数字")
