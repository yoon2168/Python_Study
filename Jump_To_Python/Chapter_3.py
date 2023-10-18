# 3장 프로그램 제어

# #Ex 1)
# money = 2000
# card = True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")
#
# #Ex 2)
# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if  treeHit == 10:
#         print("나무 넘어갑니다.")
#
# #Ex 3)
# prompt = """
# ... 1. Add
# ... 2. Del
# ... 3. List
# ... 4. Quit
# ...
# ... Enter number: """
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# 3장 되새김 문제
print("\n-----------------------")
print("\n Q1 조건문의 참과 거짓")
print("위에서 밑에서 순서를 세면 3번째 결과값만 출력된다. 하지만, 4번째 결과값도 True다. ")

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

print("\n-----------------------")
print("\n Q2 3의 배수의 합 구하기")

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

print("\n-----------------------")
print("\n Q3 별 표시하기")
i1 = 0
while True:
    i1 += 1
    if i1 > 5: break
    print("*" * i1)

print("\n-----------------------")
print("\n Q4 1부터 100까지 출력하기")
for i2 in range(1, 101):
    print(i2)

print("\n-----------------------")
print("\n Q5 평균 점수 구하기")
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score

average = total / len(A)
print(average)

print("\n-----------------------")
print("\n Q6 리스트 컴프리헨션 사용하기")
numbers = [1, 2, 3, 4, 5]
result2 = []
for n2 in numbers:
    if n2 % 2 == 1:
        result2.append(n2 * 2)

print("EX :", result2)

numbers1 = [1, 2, 3, 4, 5]
result3 = [n3 * 2 for n3 in numbers1 if n3 % 2 == 1]
print("Q6 :", result3)

