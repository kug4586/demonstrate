import os, random, keyboard
def clear():
    os.system('cls')

'''
자연수를 입력하는 방식
'''
def M1(n:int):
    print('소수 찾는 중.....', end='\r')
    arr_P = prime(n)

    print('약수 찾는 중.....', end='\r')
    arr_A = aliquot(n)
    print('# {}의 약수: {}     '.format(n, arr_A))

    print('서로소 찾는 중.....', end='\r')
    arr_R, count = relative_prime(arr_P, arr_A)

    report(arr_A, arr_R)

    print('='*50)
    print('입력한 수: {}'.format(n))
    print('모든 서로소의 개수: {}'.format(count))

'''
검증 방식
'''
def M2(cnt:int, n:int):
    k = 0

    for i in range(cnt):
        # 1~n 중 하나의 수
        rand = random.randint(1, n)
        print('\n입력된 수: {}'.format(rand))

        print('소수 찾는 중.....', end='\r')
        arr_P = prime(rand)

        print('약수 찾는 중.....    ', end='\r')
        arr_A = aliquot(rand)
        print('# {}의 약수: {}'.format(rand, arr_A))

        print('서로소 찾는 중.....', end='\r')
        arr_R, count = relative_prime(arr_P, arr_A)
        print('# 각 수의 서로소 개수: {}'.format([len(arr) for arr in arr_R]))
        print('>> 서로소의 총 개수: {}\n'.format(count))

        if (count==rand):
            k += 1
    
    print('='*50)
    print('<<최종 결과>>\n 입력값과 결과값이 같은 경우: {} / {}'.format(cnt, k))

'''
주어진 범위 내에서 소수 찾기
'''
def prime(n:int):
    prime_nums = []
    no = []
    for i in range(2, n+1):
        if (i not in prime_nums) and (i not in no):
            prime_nums.append(i)
            for j in range(i, n+1, i):
                if j not in no:
                    no.append(j)
    return prime_nums

'''
어떤 수의 약수 찾기
'''
def aliquot(n:int):
    aliquot_nums = []
    for i in range(1,n+1):
        if n%i == 0:
            aliquot_nums.append(i)

    return aliquot_nums

'''
각 약수들의 서로소 찾기
'''
def relative_prime(prime_nums:list, aliquot_nums:list):
    research = []
    result = 0
    for aliq in aliquot_nums:
        arr = []
        for i in range(1,aliq+1):
            is_deviced = False
            cnt = 0
            if (len(prime_nums) != 0):
                while (prime_nums[cnt] <= i):
                    if (aliq%prime_nums[cnt] == 0) and (i%prime_nums[cnt] == 0):
                        is_deviced = True
                        break
                    else:
                        cnt += 1
                    if (cnt >= len(prime_nums)):
                        break
            if (not is_deviced) or (i==1):
                arr.append(i)
                result += 1
        research.append(arr)

    return research, result

'''
찾은 서로소 출력
'''
def report(aliquot_nums:list, research:list):
    lens = [len(research[i]) for i in range(len(research))]
    for i in range(len(research)):
        s1 = '({})'.format(len(research[i]))
        print(
            str(aliquot_nums[i]).rjust(len(str(data))),
            ' ' * 2,
            s1,
            ' ' * (len(str(max(lens))) - len(str(len(research[i])))),
            end = '  '
        )
        if (len(research[i]) > 40):
            s2 = ''
            for j in range(38):
                s2 += str(research[i][j]) + ', '
            print('[' + s2 + '...' + str(max(research[i])) + ']')
        else:
            print(str(research[i]) + '   ')

while(True):
    clear()
    print('\n' + '='*30 + '\n서로소의 기묘한 이야기\n' + '='*30)
    print('\n데이터 입력 방식을 선택하세요.')
    mathod = int(input('직접 입력 [1]  |  검증 [2]  |  종료 [0]  >> '))
    print('\n' + '='*30 + '\n')

    data = None
    if (mathod==0):
        print('프로그램을 종료합니다...')
        print('입력 방식에 맞춰서 입력해 주세요....\n')
        print('(계속하려면 [space bar]를 누르세요....)')
        keyboard.wait('space')
        exit()

    elif (mathod==1):
        while (True):
            data = int(input('자연수를 입력하세요: '))
            if (data > 0):
                print('\n' + '='*50)
                M1(data)
                print('\n(계속하려면 [space bar]를 누르세요....)')
                keyboard.wait('space')
                break
            else:
                print('입력 방식에 맞춰서 입력해 주세요....\n')
                print('(계속하려면 [space bar]를 누르세요....)')
                keyboard.wait('space')

    elif (mathod==2):
        count = -1
        while (count <= 0):
            count = int(input('반복 횟수를 입력하세요: '))
            if(count > 0):
                break
            else:
                print('입력 방식에 맞춰서 입력해 주세요....\n')
        while (True):
            data = int(input('숫자를 무작위로 고르기 위해 범위의 최댓값을 입력하세요: '))
            if(data > 0):
                print('\n' + '='*50)
                M2(count, data)
                print('\n(계속하려면 [space bar]를 누르세요....)')
                keyboard.wait('space')
                break
            else:
                print('입력 방식에 맞춰서 입력해 주세요....\n')
                print('(계속하려면 [space bar]를 누르세요....)')
                keyboard.wait('space')

    else:
        print('지정되지 않은 입력입니다....')
        print('(계속하려면 [space bar]를 누르세요....)')
        keyboard.wait('space')