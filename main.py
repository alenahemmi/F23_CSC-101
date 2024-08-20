#introduction to python program 
#A) goal is to ask question that requires numeric count (scale, count)
#B) loop to accept additional answers to same ? until stop code is given
#C) compute a meaningful summary of responses and exit

#grab library and wait for use somewhere in code
import statistics

#setup data storage for user answers in a list
#start with an empty list by
answers = []
#store dummy response to control while
number_answer = 0

#loop over following until stop code given
while number_answer != -9:
  print("How many pets do you have?")
  print("(Or enter -9 to show summary and end)")
  
  user_answer = input()
  print("You entered: ", end='')
  print(user_answer)
  
  #convert string from user into integer for numeric processing
  #use cast funtion int()
  number_answer = int(user_answer)
  #only store answers that aren't our stop code
  if number_answer != -9:
    answers.append(number_answer)

#lines below are "outside" of while loop and only run
#when while condition is false
#display the contents of our list
print("List contents:")
print(answers)
avg_response = statistics.mean(answers)
print("The average answer is: ", end='')
print(avg_response)