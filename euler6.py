answer_sum_square = 0
adding = 0
endpoint = 100
#the point where the sequence ends

for iteration in range(1,endpoint + 1):
    #starts a sequence and counts up from 1 to 1000
    answer_sum_square += (iteration ** 2)
    # answer = answer + iteration ** iteration
for iteration in range(1,endpoint + 1):
    adding += ((iteration))

answer_square_sum = adding ** 2

#print(answer_square_sum)
    #was a test to make sure was squaring the right number

answer = (answer_square_sum - answer_sum_square)
string_answer = str(answer)
    #changes answer into a string
print(string_answer)
