# # ex1)-----------------------------------------------
# def gugu(n):
#     result1 = []
#     i = 1
#
#     while i < 10:
#         result1.append(i * 2)
#         i = i + 1
#
#     return result1
#
# print(gugu(2))

# # ex2)-----------------------------------------------
#
# def comnum(n):
#     result2 = 0
#     i = 1
#     while i < n:
#         if i % 3 == 0 or i % 5 == 0:
#             result2 += i
#         i = i + 1
#
#     return result2
#
# print(comnum(1000))

# # ex3)-----------------------------------------------
def pageappear(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(pageappear(5, 10))
print(pageappear(15, 10))
print(pageappear(25, 10))
print(pageappear(30, 10))