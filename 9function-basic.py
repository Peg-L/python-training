from tkinter import N


def add(n1, n2):
    result = n1 + n2
    print(result)


add(5, 6)
add(1, 2)


def say(msg):
    print(msg)
    return  # None


value = say("Hello Peggy")
print(value)

# 函式回傳字串 Hello


def add(n1, n2):
    result = n1 + n2
    return "Hello"


# 呼叫函式，取得回傳值
value = add(3, 4)
print(value)  # 印出Hello


# 回傳結果值 result


def add(n1, n2):
    result = n1 + n2
    return result


value = add(3, 4)
print(value)


# 定義函式
def multiply(n1, n2):
    print(n1*n2)
    return n1*n2


# 呼叫函式
multiply(5, 5)
multiply(6, 8)
value = multiply(3, 4)
print(value)


#函式可用來做程式的包裝: 同樣的邏輯可以重複利用
def calculate(n):
    sum = 0
    for n in range(1, n+1):
        sum += n
    print(sum)


calculate(10)
calculate(20)
