Set1 = {10, 20, 30, 40, 50}
Set2 = {40, 50, 60, 70, 80}

print(Set1.difference(Set2))
print(Set1-Set2)
for el in Set1:
    if el not in Set2:
        print(el, end=" ")






# str="the quick brown fox jumps"
# def mysplit(str):
     
#     bag=""
#     output=[]
#     for i in range(len(str)):
         
#         if str[i]!=" ":
#                 bag=bag+str[i]
#         else:
#             if(bag!=""): 
#                 output.append(bag)
#             bag="";	
#     print(output)


# mysplit(str)
