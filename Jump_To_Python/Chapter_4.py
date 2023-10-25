# 4장 함수

# ex1)-----------------------------------------------
# def 함수_이름 (매개변수):
#     수행할 문장_1
#     수행할 문장_2
# ex2)-----------------------------------------------
# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result
#
# result = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)
# ex3)----------------------------------------------
# def add_mul(choice, *args):
#         if choice == "add":
#             result = 0
#             for i in args:
#                 result = result + i
#         elif choice == "mul":
#             result = 1
#             for i in args:
#                 result = result * i
#         return result
#
# result = add_mul('add', 1,2,3,4,5)
# print(result)
# result1 = add_mul('mul', 1,2,3,4,5)
# print(result1)
# ex4)----------------------------------------------
# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s 입니다." % nick)
# say_nick('바보')
# ex5)----------------------------------------------
# number = input("숫자를 입력하세요: ")
# print(number)
# ex6)----------------------------------------------
# f = open("C:/비둘기/새 파일.txt", "w")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
# ex7)----------------------------------------------
# f = open("C:/비둘기/새 파일.txt", 'a')
# for i in range(11, 20):
#     data = "%d번 째 줄입니다.\n" % i
#     f.write(data)
# f.close()


# 4장 되새김 문제
print("\n-----------------------")
print("\n Q1 홀수, 짝수 판별하기")

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

Ans1 = is_odd(3)
print(" Answer is : %s" % Ans1)
print("\n-----------------------")
print("\n Q2 모든 입력의 평균값 구하기")

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

Ans2 = avg_numbers(1, 2, 3, 4, 5)
print(" Answer is : %s" % Ans2)
print("\n-----------------------")
print("\n Q3 프로그램 오류 수정하기")
input1 = input(" 첫번째 숫자를 입력하세요: ")
input2 = input(" 두번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print(" Answer is : %d " % total)
print("\n-----------------------")
print("\n Q4 출력 결과가 다른 것은?")
print(" Answer is : 3번 띄어쓰기 가능 문구" )
print("\n - 결과 List 출력 - ")
print(' 1. print("you""need""python")')
print("    Ans: ""you""need""python")
print(' 2. print("you"+"need"+"python)')
print("    Ans: ""you"+"need"+"python")
print(' 3. print("you", "need", "python")')
print("    Ans: ""you", "need", "python")
print(' 4. print("".join(["you", "need", "python"]))')
print("    Ans:", "".join(["you", "need", "python"]))
print("\n-----------------------")
print("\n Q5 프로그램 오류 수정하기2")
f1 = open("test.txt", 'w')
f1.write(" Answer is : Life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
print("\n-----------------------")
print("\n Q6 사용자 입력 저장하기")
user_input = input("저장할 내용을 입력하세요: ")
f = open('C:/비둘기/test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close
print("\n-----------------------")
print("\n Q7 파일의 문자열 바꾸기")
f = open('test')