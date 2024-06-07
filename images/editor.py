print(6%5)
from collections import defaultdict
d=defaultdict(lambda: "Not Present")
d["a"]=1
d["b"]=2
print(d.__missing__("a"))
print(d.__missing__("b"))
d["a"]=55
print(d["a"])
print(d.__missing__("a"))
print(d["a"])
country={'india':'0091','australia':'0025','nepal':'00977'}
print(country.get('india','not found'))
print(country.get('japan','not found'))
test={"Rajat":4,"is":7,"best":8,"for":6,"python":0}
print("the original dictionary is:"+str(test))
res=0
for va in  test.values():
    res=res+va
res=res/len(test)
print("the name of :"+str(test))
