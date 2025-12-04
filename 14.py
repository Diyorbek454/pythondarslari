#1 - masala

#A = int(input('A = :'))
#B = int(input('B = :'))
# 
#while A >= B :
#    A = A - B
#print(A)
#

#2 - masala

#A = int(input('A = :'))
#B = int(input('B = :'))
# 
#while A >= B :
#    A = A - B
#print(A)
##A = int(input('A = :'))
#B = int(input('B = :'))
#count = 0
#while A >= B :
#    A = A - B
#    count = count + 1  
#print(A)
#
#3 - masala
while true :
    yosh = int(input('Yoshingizni kiriting : '))
    if yosh <= 7 :
        narx = 2000
    elif yosh <= 18:
        narx = 3000
    elif yosh <= 65:
        narx = 10000
    else :
        narx = 0
    print(f"sizga chipta narxi {narx} som")
    javop = input("Yana davom etasizmi ? Dasturni tugatish uchun, 'exit' , yoki 'quit' ni yuborin" )
    if (javop.lower() == 'quit' or javop.lower() == 'exit'):
        break 