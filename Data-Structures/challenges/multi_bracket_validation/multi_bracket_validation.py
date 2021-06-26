import re
import pysnooper

dictinary={ 
    '{':'}',
    '(':')',
    '[':']'
}

@pysnooper.snoop()
def check(input):
  value= re.findall(r'[{}()\[\]]',input)
  array_check=[]

  if len(value)%2==1:
    return False
  for item in value:    
      try : 
              if len(array_check)>0 and item==dictinary[array_check[-1]]:
                  array_check.pop()
              else :    
                array_check.append(item)
      except:
              return False

  if len(array_check)>0:
    return False 
  
            
  return True            
               

print(check('()[[Extra Characters]]'))
print(check('()}})'))
print(check('{)'))
print(check('{}'))
print(check('{}(){}'))