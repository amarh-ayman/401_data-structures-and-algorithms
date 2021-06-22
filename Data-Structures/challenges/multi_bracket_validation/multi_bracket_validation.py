import re
dictinary={ 
    '{':'}',
    '(':')',
    '[':']'
}

class multi_bracket_validation:
  def __init__(self) :
    self.value=None 
    self.array_check=[]

  def check(self,input):
    r_string = re.sub(r'[\w\s]', '', input )
    self.value=''.join(r_string)
    
    if len(self.value)%2==1:
      return False

    for item in self.value:    
        try : 
                if len(self.array_check)>0 and item==dictinary[self.array_check[-1]]:
                    self.array_check.pop()
                else :    
                  self.array_check.append(item)
        except:
                return False

    if len(self.array_check)>0:
      return False            
    return True            
               

item=multi_bracket_validation()
# print(item.check('()[[Extra Characters]]'))
# print(item.check('()}})'))
# print(item.check('{)'))
assert item.check('{}')==True
print(item.check('{}(){}'))