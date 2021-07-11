
def insertionSort(listTOBeSorting):
  for index ,item in enumerate(listTOBeSorting):
    j=index-1

    while j>=0 and item < listTOBeSorting[j]:
      listTOBeSorting[j+1]=listTOBeSorting[j]
      j-=1
    listTOBeSorting[j+1]=item  
    




# listN=[9,5,2,4,1]
# insertionSort(listN)
# print(listN)


