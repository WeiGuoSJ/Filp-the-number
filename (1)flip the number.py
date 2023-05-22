#Question:给变量"number"赋值123，使用取整和取模的方法将数字翻转为321，并将翻转结果赋值给"result"输出。



number = 123
a = number//40
b = number//60
c = number//120
result = a*100+b*10+c
print(result)
