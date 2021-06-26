from stacks_and_queues.stacks_and_queues  import Queue

def DuckDuckGoose(list , k):
    en=Queue()
    count=1
    
    for item in list:
        en.enqueue(item)
    
    while en.front.next:
        if count < k:
            en.enqueue(en.front.value)
            en.dequeue()
            count+=1
        else:
            en.dequeue()
            count=1
            
    return en.front.value
        
    
            

list =['a','b','c','d','e']


print(DuckDuckGoose(list,3))
    
            
            
            
            