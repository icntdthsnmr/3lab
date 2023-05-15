def z1():
    n = int(input('Введите N: '))
    res = ''
    for i in range(n):
        s = input()
        res = res + s + ' '
    print(res)

def z2():
    a = input()
    res = ''
    while a.lower() != 'stop':
        a = input()
        res = res + a + ' '
    print(res)

def z3():
    word = input()
    if 'ф' in word:
        print('Ого! Это редкое слово!')
    else:
        print('Это не очень редкое слово')

def z4():
    from random import randint
    m = 0
    r = 0
    while m < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        res = int(input(str(a) + '+' + str(b) + '='))
        if res != a + b:
            print('Ответ неверный!')
            m += 1
        else:
            print('Правильно!')
            r += 1
    print('Игра окончена. Правильных ответов:', r)
z1()
z2()
z3()
z4()