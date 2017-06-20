##x,y=4,5
##small = x if x < y else y

##assert 3 > 4
##assert 4 > 3

##while 条件：循环体
##for 循环  ：  语法   for 目标 in 表达式：
##                        循环体
##favourite="fishC"
##for i in favourite:
##    print(i,end=" ")

##member = ["小甲鱼","黑夜","答复"]
##for i in member:
##    print(i,len(i))

##range(0,5,2) 

##break 跳出循环体
##continue 终止本轮，开始下一轮

##bingo = "陈永康"
##answer = input("请输入：")
##while True:
##    if answer == bingo:
##        break
##    answer = input("错了,重输入：")
##print("对了")

##for i in range(10):
##    if i%2 !=0:
##        print(i)
##        continue
##    i +=2
##    print(i)

##member = ["小甲鱼","黑夜","答复"]
##member.append("陈永康")
##member.extend(["我的","纷"])
##member.insert(0,"牡丹")
##member.remove("陈永康")
##del member[1]
##member.pop()
##member.pop(1)
##member[1:2]
