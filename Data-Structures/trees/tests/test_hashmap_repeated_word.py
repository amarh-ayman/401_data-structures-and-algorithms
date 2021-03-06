from Code_Challenges.ALgorithm.hashmap_repeated_word import *

def test_1():
  s1="Once upon a time, there was a brave princess who..."
  hashmap=hashmap_repeated_word(s1)
  assert hashmap[0][1]=='a'
  assert hashmap[1][hashmap[0][1]]==2

def test_2():
  s2="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

  hashmap=hashmap_repeated_word(s2)
  assert hashmap[0][1]=='it'
  assert hashmap[1][hashmap[0][1]]==10


def test_3():
  s3="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

  hashmap=hashmap_repeated_word(s3)
  assert hashmap[0][1]=="summer"
  assert hashmap[1][hashmap[0][1]]==2
