score=input("请输入您的分数：")
score=int(score)
if score>=90 and score<=100:
    print("优秀！")
elif score>=80 and score<90:
    print("良好！")
elif score>=70 and score<80:
    print("一般般！")
elif score>=60 and score<70:
    print("刚刚及格！")
elif score<60 and score>0:
    print("不及格！")
else:
    print("输入的成绩有误，请重新输入！")