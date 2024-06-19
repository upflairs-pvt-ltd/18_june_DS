# string 
# var =
# a - z , A - Z , 0 -9 , _ 

# age = 10 
# Age = 15 
# AGE = 20 

# st@ = 10 
# print(st@) 

# string   data types 
# st = "UPFLAIRS PVT LTD JAIPUR RAJASTHAN"
# st = "upflairs"
# print(st) 
# print(type(st))
# print(st[17:23]) 
# print(st[7])
# print(st[:8])
# print(st[:]) 
# [start : ending : jump]
# print(st[::]) 
# print(st[::1])   # by default 1  


# st = "upflairs"
# print(st[::3])
# print(st[::-1])

# st = "upflairs pvt ltd jaipur rajasthan "
# st2 = "UPFLAIRS PVT LTD JAIPUR RAJASTHAN"
# print(len(st))  # count no. of charachter 
# print(st.upper())
# print(st2.lower())
#   
# print(st.count('z'))
# print(st.index("f"))
# print(st.replace("upflairs","flipkart"))  
# st.  


## <<<<<<<<<<<, LIST   >>>>>>>>>>>>

# ls = [10,20.25,410,10.2,'upflairs',True,500]
# print(ls)
# print(type(ls))
# student_name = ['mohit','rohit','kanak','ruchika']
# print(student_name[-1])


# ls = ['A','B','C','D','E','F','G','H']
# ST = "ABCDEFG"
# print(ls[-2:])

# ls[3] = "DON"
# ls.append("I") # last 
# ls.pop()  # item remove last 

# ls.insert(2,'UPFLAIRS')
# ls.remove('E')

# print(ls)

# ls = ['a sharma','b kumar','c khanna']

# ls.remove('b ') 
# del ls[1]
# print(ls)


ls1 = ['A','B','C','D','E']
ls2 = ['F','G','H']

# ls1.append(ls2)
ls1.extend(ls2)
print(ls1)

# assignment 
ls1.reverse() 
ls1.sort()
ls1.clear()
ls1.copy()

