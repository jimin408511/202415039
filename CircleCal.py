import math

radius= float(input("원의 반지름 입력해라"))

circumference = 2 * math.pi * radius
area = math.pi * radius**2

print("원의 둘레", circumference)
print("원의 넓이", area)
