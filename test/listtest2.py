studengts = []
count = 3
for i in range(count):
     id = input(f'请输入第{i+1}个学生的学号:')
     name = input(f'请输入第{i+1}个学生的姓名:')
     score =input(f'请输入第{i+1}个学生的分数:')
     stu_list = [id,name,score]
     studengts.append(stu_list)
for stu in studengts:
    for v in stu:
        print(v,end =' ')
    print()