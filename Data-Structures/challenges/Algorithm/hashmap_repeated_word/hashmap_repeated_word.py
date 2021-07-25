import re

def hashmap_repeated_word(sentence):
    sntnc=re.sub('[^\w\d ]','',sentence).split()
    d={}
    t=True
    maxi=[1,'']
    for word in sntnc :
        try :
            if d[word.lower()] :
                d[word]+=1
                if maxi[0]< d[word] and t :
                    t=False
                    maxi=[d[word],word]
        except :
            d[word.lower()]=1
    
    if t==True :
        return 'there is no repeating'
    else :
        return [maxi ,d]

 

# a="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs,and I didnt know what I was doing in New York "

# # b="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."    
    


# print(hashmap_repeated_word(a)) 