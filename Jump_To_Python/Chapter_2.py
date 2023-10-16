# 2장 되새김 문제


print("-----------------------")
print("#Q1 평균점수 구하기")
a = 80 #국어
b = 75 #영어
c = 55 #수학

avg = (a+b+c)/3
print(avg)

print("\n-----------------------")
print("#Q2 홀수, 짝수 판별하기")
d = 13 #자연수
e = d % 2

if e == 0:
    print("짝수")
elif e == 1:
    print("홀수")

print("\n-----------------------")
print("#Q3 주민등록번호 나누기")

pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

print("\n-----------------------")
print("#Q4 주민번호 인덱싱")

pin = "881120-1068234"
f = pin[7]

if f == "1":
    print("남자")
elif f == "2":
    print("여자")

print("\n-----------------------")
print("#Q5 문자열 바꾸기")

g = "a:b:c:b"
h = g.replace(":","#")
print(h)

print("\n-----------------------")
print("#Q6 리스트 역순 정렬하기")

I = [1, 3, 5, 4, 2]
I.sort()
I.reverse()
print(I)

print("\n-----------------------")
print("#Q7 리스트 문자열로 만들기")

J = ['Life', 'is', 'too', 'short']
result = J[0] + J[1] + J[2] +J[3]
print(result)

result1 = " ".join(J)
print(result1)

print("\n-----------------------")
print("#Q8 듀플 더하기")

K = (1, 2, 3)
K = K + (4,)
print(K)

print("\n-----------------------")
print("#Q9 딕셔너리의 키")
L = dict()
print('L[[1]] = "Python"')
print('이유는 L[1]값의 []을 사용하였기 때문에')

print("\n-----------------------")
print("#Q10 딕셔너리의 POP")
M = {'A':90, 'B':80, 'C':70}
result = M.pop('B')
print(M)
print(result)

print("\n-----------------------")
print("#11 리스트에서 중복 제거하기")
N = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
Nset = set(N)
O = list(Nset)
print(O)

print("\n-----------------------")
print("#12 파이썬 변수")
Q = R = [1, 2, 3]
Q[1] = 4
print(Q)
print(R)
print("a와 b는 복사된 list 주소를 가지고 있기 때문에 동일한 값을 가질 수 있다")

