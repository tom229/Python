# list_of_list = [[1,2,3],[4,5,6,7],[8,9]]
# for a in list_of_list:
#     # print(a)
#     for b in a:
#         print(b)


### excercise 05
# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]

# for number in numbers:
#     output[  (number-1)%3  ].append(number)

# print(output)


##연습문제3 p158
# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# for number in numbers:
#     if number % 2==0:
#         print("{} 는 짝수입니다.".format(number))
#     else:
#         print("{} 는 홀수입니다.".format(number))
# print()
# print()
# for number in numbers:
#     print("{} 는 {} 자릿수입니다".format(number,len(str(number))))


##4

# list_oflist = [[1, 2, 3],[4, 5, 6, 7],[8, 9],]

# for list in list_oflist:
# #   print(list)
#     for b in list:
#         print(b)



##예제
# dictionary = {"name":"tom","age":15, "birth":92}

# value = dictionary.get("year")
# print(value)
# print()

# value1 = dictionary.get("name")
# print(value1)
# for key in dictionary:
#     print(key)
#     print(dictionary[key])


## 연습문제 3 p172

# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] +=1
#     else :
#         counter[number] = 1 

# print(counter)

## range  반드시 정수를 입력해야 한다

# a = range(3,6)   # 3 분터 5까지 범위를 만든다
# b = range(5)     # 0 부터 4까지 범위를 만든다
# print(a)
# print(b)
# c = range(1,7,2) # 1 분터 7까지 범위를 만들되 앞뒤의 숫자가 2만큼 차이를 가진다
# print(c)

# print(list(a))
# print(list(b))
# print(list(c))

array = [273, 32, 103, 57, 52]
for element in range(len(array)) :
    print("{} 번째: {}".format(element,array[element]))


