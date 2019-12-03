answer = 0
#base that become the answer
endpoint = 500
#the point where the sequence ends

for iteration in range(1,endpoint + 1):
    #starts a sequence and counts up from 1 to 1000
    answer += iteration + iteration
    # answer = answer + iteration ** iteration
    # adding anser to the iteration squared to consolodate in one spot the answerprint(str(answer)[len(str(answer)) - 10:len(str(answer))])
string_answer = str(answer)
print string_answer
    #changes answer into a string
#number_of_char = len(string_answer)
    #counts how many chararcters are in the string_answer
#start_index = number_of_char - 10
    #where the start of counting the last 10 digits starts
#print(string_answer[start_index:number_of_char])
    #prints the last 10 digits of a numbwer


#for when you want to look cool
    #print(str(answer)[len(str(answer)) - 10:len(str(answer))])
