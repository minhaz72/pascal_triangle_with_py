def Pascal(num) : 
    arr= [1]
    tem=[]
    print(f'  the pascal triangle has  {num} number row  ')
    for i in  range(num): 
        print(f" rows = {i+1} " ,  end=' ' )
        for j in range  ( len(arr)) : 
            print(arr[j] ,  end=' ')
        print()
        tem.append(1)
        for j in range(len(arr)-1): 
            tem.append(arr[j]+  arr[j+1])
        tem.append(1)
        arr= tem 
        tem= []
n=  int(input('enter a num : '))
Pascal(n)
