# list_of_list = [[1,2,3],[4,5,6,7],[8,9]]
# for a in list_of_list:
#     # print(a)
#     for b in a:
#         print(b)


# excercise 05
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[  (number-1)%3  ].append(number)

print(output)

