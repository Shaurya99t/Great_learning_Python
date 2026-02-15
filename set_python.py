# set is an unordered and unindexed collection of element enclosed with{}, duplicate are not allowed in set
s1={"shaurya","shaurya","pranjal",7,9,11,"new york",90}
print(s1)
print(type(s1))
s1.add("rajesh")
print(s1)
s1.update(["rydm",87,24,"yooo bois"])
print(s1)
s1.remove("rydm")
print(s1)
s1.remove(24)
print(s1)
s2={1,3,5,7,9,11,13}
print(s1.union(s2))
print(s1.intersection(s2))
