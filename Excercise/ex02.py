# a = input(": " )
# print(a)
# print(type(a))

# a = int(input())
# b = int(input())
# c = a + b*2
# print(a+b, c) 


# print("{}year {}month {}day".format(2021,3,10))
# a = "HeLLo".upper()
# b = "WORLD".lower()
# print(a , b )
# print("     This Is Python    ".strip())
# print("     This Is Python    ".lstrip())
# print("     This Is Python    ".rstrip())
# print("abcdef".find("c"))
# print("abcdefgc".rfind("c"))
# print("a" in "dad")

# output_a = "{:+d}".format(52)
# output_c = "{:+5d}".format(52)
# output_b = "{:+d}".format(-43)
# output_d = "{:+05d}".format(-43)
# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)

# #split()
# a = "adfacadfafadadfaca".split("a")
# print(a)

# 조건문
# print("tom" == "tom")

# number1 = int(input("정수입력: "))
# number2 = int(input("정수입력: "))
# if number1 > 0:
#     print(number1 , "양수입니다")
# if number2 <0:
#     print(number2, "음수입니다")

#date time

# import datetime
# now = datetime.datetime.now()
# now1 = datetime.datetime.now()

# print(now1)
# print(now.year,"년",now.month, "월",now.day, "일",
#       now.hour, "시",now.minute, "분",now.second, "초")
# print(now.microsecond,"마이크로새컨드")      
# print("{}년{}월{}일{}시{}분{}초".format(now.year,now.month,now.day,
#                                 now.hour,now.minute,now.second))

# if now.hour<12:
#     print("{}{}{}입니다".format("오전",now.hour,"시"))
#     # print("오전",now.hour,"시 입니다")
# if now.hour>12:
#     # print("오후",now.hour,"시 입니다")
#     print("{} {}{}".format("오후",now.hour-12,"시 입니다"))

# # 계절 구분
# if 3 <= now.month <6:
#     print("이번달은 {}로 봄입니다".format(now.month))
