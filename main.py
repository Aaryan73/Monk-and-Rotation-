'''
Author: Aaryan Regmi
'''

def intlistelement(numlist):   # convert the string items of list into integer
  for j in range(len(numlist)):
    numlist[j] = int(numlist[j])
  return numlist

def rotate(intlist, k):    # bring the element from last of the list to first
    lastelement = 0
    for i in range(k):      # for rotating the elements k number of times 
        lastelement = intlist[len(intlist)-1]
        intlist.pop()
        intlist.insert(0, lastelement)
    return intlist
  
def output(intlist, n):   # formats the list for output
  stroutput = ""
  for o in intlist:
    stroutput += str(o)
    stroutput += " "
  return stroutput

t = int(input())
i = 1
while i <= t:                          # 
    n, k = input().split(" ")
    n, k = int(n), int(k)
    numlist = input().split(" ")
    intlist = intlistelement(numlist)     # list items gets converted into integer
    intlist = rotate(intlist, k)      # brings last elements to first
    intlist = output(intlist, n)     # formats the items of intlist for output
    print(intlist)
    i += 1
