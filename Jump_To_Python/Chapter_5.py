# # ex1)-----------------------------------------------
# result = 0
#
# def add(num):
#     global result
#     result += num
#     return result
#
# print(add(3))
# print(add(4))

# # ex2)-----------------------------------------------
# class Caculator:
#     def __init__(self):
#         self.result = 0
#
#     def add(self, num):
#         self.result += num
#         return self.result
#
# cal1 = Caculator()
# cal2 = Caculator()
#
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))


# # ex3)-----------------------------------------------
# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
#
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
#
# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
#
#
# # a = MoreFourCal(4, 2)
# # RT1 = a.pow()
# # print(RT1)
#
# a = SafeFourCal(4, 0)
# RT2 = a.div()
# print(RT2)

# 5장 되새김 문제
print("\n-----------------------")
print("\n Q1 [클래스 상속받고 메서드 추가하기 1]")
class Calculator1:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradCalculator1(Calculator1):

    def minus(self, val):
        self.value -= val

cal1 = UpgradCalculator1()

cal1.add(10)
cal1.minus(7)
print(" Answer is : %s" % cal1.value)

print("\n-----------------------")
print("\n Q2 [클래스 상속받고 메서드 추가하기 2]")

class Calculator2:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
class MaxLimitCalculator(Calculator2):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)
print(" Answer is : %s" % cal2.value)

print("\n-----------------------")
print("\n Q3 [참과 거짓 예측하기]")

print(' \n all([1, 2, abs(-3)-3])')
print(' Answer is : False가 나타난다. 0 때문에')
print(" chr(ord('a')) == 'a'")
print(' Answer is : True가 나타난다. "a"="a"이므로')

print("\n-----------------------")
print("\n Q4 [음수 제거하기]")

a = list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))
print(" Answer is :", a)

print("\n-----------------------")
print("\n Q5 [16진수를 10진수로 변경하기]")

Q51 = hex(234)
Q52 = int('0xea', 16)
print(" Answer is : %s" % Q51) 
print(" Answer is : %s" % Q52)

print("\n-----------------------")
print("\n Q6 [리스트 항목마다 3곱하여 리턴하기]")

Q61 = list(map(lambda x: x*3, [1, 2, 3, 4]))
print(" Answer is : %s" % Q61)

print("\n-----------------------")
print("\n Q7 [최댓값과 최솟값의 합]")

a = [-8, 2, 7, 5, -3, 5, 0, 1]
m1 = max(a)
m2 = min(a)
ms = m1 + m2
print(" Answer is : %s" % m1)
print(" Answer is : %s" % m2)
print(" Sum Value is : %s" % ms)

print("\n-----------------------")
print("\n Q8 [소수점 반올림하기]")

Q81 = 17 / 3
Q82 = round(Q81, 4)
print(" Answer is : %s" % Q81)
print(" Round Answer is : %s" % Q82)

print("\n-----------------------")
print("\n Q9 [디렉터리 이동하고 파일 목록 출력하기]")

print ("\n '작성되어 있는 Code 참조'")
# import os
# os.chdir("c:/doit")
# result = os.popen("dir")
# print(result.read())30

print("\n-----------------------")
print("\n Q10 [파일 확장자가 .py 인 파일만 찾기]")

print ("\n '작성되어 있는 Code 참조'")
# import glob
# glob.glob("c:/doit/*.py")
# ['c:/doit/doit01.py, 'c:/doit/test/py']

print("\n-----------------------")
print("\n Q11 [날짜 표시하기]")

import time
a = time.strftime("%Y/%m/%d %H:%M:%S")
print(" Present Time is :", a)

print("\n-----------------------")
print("\n Q12 [로또 번호 생성하기]")

import random

result11 = []
while len(result11) < 6:
    num = random.randint(1, 45)
    if num not in result11:
        result11.append(num)

print(" Answer is :", result11)

print("\n-----------------------")
print("\n Q13 [누나는 영철이보다 며칠 더 먼저 태어났을까?]")

import datetime
day1S = datetime.date(1995, 11, 20)
day2B = datetime.date(1998, 10, 6)
diff = day2B - day1S
print(" Answer is :", diff.days )

print("\n-----------------------")
print("\n Q14 [기록순으로 정렬하기]")

import operator
data = [('윤서현', 15.25),
        ('김예지', 13.31),
        ('박예원', 15.34),
        ('송순자', 15.57),
        ('김시우', 15.48),
        ('배숙자', 17.9),
        ('전정웅', 13.39),
        ('김혜진', 16.63),
        ('최보람', 17.14),
        ('한지영', 14.83),
        ('이성호', 17.7),
        ('김옥순', 16.71),
        ('황민지', 17.65),
        ('김영철', 16.7),
        ('주병철', 15.67),
        ('박상현', 14.16),
        ('김영순', 14.81),
        ('오지아', 15.13),
        ('윤지은', 16.93),
        ('문재호', 16.39)]

data = sorted(data, key=operator.itemgetter(1))
for d in data:
    print(d)

print("\n-----------------------")
print("\n Q15 [청소 당번 2명 뽑기]")

import itertools
students = ['나 지 혜', '성 성 민', '윤 지 현', '김 정 숙']
result15 = itertools.combinations(students, 2)
print(" Answer is :", list(result15))

print("\n-----------------------")
print("\n Q16 [문자열 나열하기]")

import itertools

a = "abcd"
result = itertools.permutations(a, 4)

for r in result:
    print(''.join(r))

print("\n-----------------------")
print("\n Q17 [5명에게 할 일 부여하기]")

import random
import itertools

people = ['김 승 현', '김 진 호', '강 춘 자', '이 예 준', '김 현 주']
duty = ['청 소', '빨 래', '설 거 지']

random.shuffle(people)
result = itertools.zip_longest(people, duty, fillvalue='휴 식')
for r in result:
    print(r)

print("\n-----------------------")
print("\n Q18 [벽에 타일 붙이기]")

import math

width = 200
height = 80

square_size = math.gcd(width, height)
print(" 타일한 선의 길이 : {}".format(square_size))
width_count = width/square_size
height_count = height/square_size
print(" 필요한 타일의 갯수 : {}".format(int(width_count * height_count)))

print("\n-----------------------")