def intlistelement(numlist):
  for j in range(len(numlist)):
    numlist[j] = int(numlist[j])
  return numlist

def rotate(intlist, k):
    lastelement = 0
    for i in range(k):    
        lastelement = intlist[len(intlist)-1]
        intlist.pop()
        intlist.insert(0, lastelement)
    return intlist
  
def output(intlist, n):
  stroutput = ""
  for o in intlist:
    stroutput += str(o)
    stroutput += " "
  return stroutput

t = int(input())
i = 1
while i <= t:
    n, k = input().split(" ")
    n, k = int(n), int(k)
    numlist = input().split(" ")
    intlist = intlistelement(numlist)
    intlist = rotate(intlist, k)    
    intlist = output(intlist, n)
    print(intlist)
    i += 1
