nd=lambda x: x * 2
print(nd(10))
list_goc=(10,9,8,7,6,1,2,3,4,5)
list_moi=list(filter(lambda x: x%2==0, list_goc))
print(list_moi)
list1_goc=(10,9,8,7,6,1,2,3,4,5)
list1_moi=list(map(lambda x: x*2, list1_goc))
print(list1_moi)