amt=input()
amt_size=len(amt)
result=[]
#print(amt_size)
ones=['one','two','three','four','five','six','seven','eight','nine']
tens=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
elevens=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

#function pv(val,name):
 #if val   
#loop to declare every digit
for index in range(amt_size):
   digit=int(amt[index])
   if(index-amt_size) in (-2, -5):
        		if digit==1:
        		    result.append(elevens[digit-1])
        		else:
        		    if digit>0:
        		        result.append(tens[digit-1])
   else:
             # print(index-amt_size)
              if (index - amt_size) in (-3, -6):
                  if digit>0: 
                      result.append(ones[digit-1])
                  result.append("hundred")
              elif(index-amt_size)==-4:
                  if digit>0:
                      result.append(ones[digit-1])
                  result.append("thousand")
              else:
                  if digit>0:
                      result.append(ones[digit-1])
print(" ".join(result))
                  