#1、50以内逢7避过
i=1
while i<51:
    if i%7==0 or '7'in str(i):
        print('过')
    else:
        print(i)
    i=i+1



