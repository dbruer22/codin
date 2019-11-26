answer = 0
endpoint = 1000
for iteration in range(1,endpoint + 1):
    answer += iteration ** iteration
print(str(answer)[len(str(answer)) - 10:len(str(answer))])


#string_answer = str(answer)
#number_of_char = len(string_answer)
#start_index = number_of_char - 10
#print(string_answer[start_index:number_of_char])
