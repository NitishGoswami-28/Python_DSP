sen = str(input("Enter a sentence: "))
s=0
for i in range(len(sen)):
   if sen[i] ==" " or i == len(sen)-1:
    if i == len(sen) - 1:
            print(sen[s:i+1][::-1], end=" ")
    else:
            print(sen[s:i][::-1], end=" ")
    s = i + 1