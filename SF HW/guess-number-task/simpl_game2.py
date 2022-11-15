import numpy as np
number = 11

number_min = 1
number_max=101
count = 0

while True:
   count += 1
   midl_number = int((number_max+number_min)/2)
   if number == midl_number:
      break  # выход из цикла если угадали
    
   elif number > midl_number:
        number_min = midl_number
   else:
        
        number_max = midl_number
# print (midl_numbler)

while True:
   
    count += 1
    if midl_number==number==number_min:
        break
    predict_number = np.random.randint(number_min, midl_number)  # предполагаемое число
    if number == predict_number or number == predict_number==1 or number == predict_number==101 :
        break  # выход из цикла если угадали
    
    elif predict_number<number:
        number_min += 1
        if number_min == midl_number:
           break
print (count)
print (number)

       
 
       
        
        
    