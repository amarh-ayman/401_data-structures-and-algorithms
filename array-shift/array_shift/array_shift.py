def array_shift(a,new_num):
    if ( len(a)==0 ) or not(type(a)==type([])):
         return 'error' 


    j=len(a)
    i=j//2
    if(j%2!=0):
      i+=1

    main_value=new_num
    while i<=j:
      if i==j:
        a+=[main_value]
      else:  
        second_value=a[i]
        a[i]=main_value

      main_value=second_value
      i+=1
      
    return a