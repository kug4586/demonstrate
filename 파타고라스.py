import os, keyboard
def clear():
    os.system('cls')

'''
피타고라스의 수 검색
1. 직각삼각형에서 C^2 = A^2 + B^2
2. 이때 반드시 A<B<C (연산 회수를 줄이는 방법)
'''
def find_pita():
    cnt = 0
    pita_nums = []
    c = 3
    print('*종료하려면 [space bar]를 누르시오....')
    while(1):
        for b in range(2, c):
            found = False
            for a in range(1, b):
                if (keyboard.is_pressed('space')):
                    print('\n\n반복을 종료합니다.\n')
                    return pita_nums, cnt
                if c**2 == a**2 + b**2:
                    pita_nums.append((a,b,c))
                    print(' > 찾은 피타고라스의 수의 개수: %d' % len(pita_nums), end='\r')
                    found = True
                    break
                cnt += 1
            if found:
                break
        c += 1

pitagoras = []
while(1):
    clear()
    print('='*30 + '\n피타고라스의 수를 찾아보자!\n' + '='*30)
    choice = input('\n종료 [0]  |  검색 시작 [1]  |  결과 출력 [2] >> ')

    if '0' in choice:
        print('\n프로그램을 종료합니다....\n')
        exit()

    elif '1' in choice:
        print('\n***검색을 시작합니다***\n')
        pitagoras, calculated = find_pita()
        print('\n***검색 결과***')
        print('찾은 피타고라스의 수: %d  |  검색 횟수: %d' % (len(pitagoras), calculated))
        print('(계속하려면 [space bar]를 누르세요....)')
        keyboard.wait('space')

    elif '2' in choice:
        if len(pitagoras) == 0:
            print('먼저 검색을 해주세요...\n')
            print('(계속하려면 [space bar]를 누르시오....)')
            keyboard.wait('space')

        else:
            print('\n***출력 방식***')
            while(1):
                mathod = input('전체 출력 [0]  |  선택 검색 [1]  |  같은 비율 제거 [2] >> ')

                if '0' in mathod:
                    print(pitagoras)
                    print('(계속하려면 [space bar]를 누르세요....)')
                    keyboard.wait('space')
                    break

                elif '1' in mathod:
                    while(1):
                        idx = int(input('몇 번째 결과를 불러올까요? (총 %d개): ' % len(pitagoras)))
                        if idx <= len(pitagoras):
                            print(pitagoras[idx-1])
                            print('\n(계속하려면 [space bar]를 누르시오....)')
                            keyboard.wait('space')
                            break
                        else:
                            print('갯수 내에서 골라주세요....')
                            print('\n(계속하려면 [space bar]를 누르시오....)')
                            keyboard.wait('space')
                    break


                elif '2' in mathod:
                    print('(계속하려면 [space bar]를 누르시오....)')
                    keyboard.wait('space')
                    break

                else:
                    print('입력방식에 맞춰서 입력해주세요...\n')
                    print('(계속하려면 [space bar]를 누르시오....)')
                    keyboard.wait('space')
    
    else:
        print('입력방식에 맞춰서 입력해주세요...\n')
        print('(계속하려면 [space bar]를 누르시오....)')
        keyboard.wait('space')