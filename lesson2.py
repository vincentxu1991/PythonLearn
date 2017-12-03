print('-----my first game by python------')
temp = input("guess the number in my heart? ")
guess = int(temp)

if guess == 8:
    print("guess well")
else:
    print("guess wrong")

print("game over")


#homework
#获取Python的BIF(内置函数)
help(input)
hello = input("what`s your name ?")
name = str(hello)
print("hello " + name)