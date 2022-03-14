#{1: 10, 2: 60, 3: 30, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60} 
for i in dic1 :
    for j in dic2:
        if i==j:
            dic3[i]=dic1[i]+dic2[j]
        else:
            dic3[i]=dic1[i]
            dic3[i]=dic2[j]
print(dic3)
print((len(dic1)))



# Sum list of dictionaries with the same key?

dic = [{'a':5, 'b':10, 'c':90},{'a':45, 'b':78}, {'a':90, 'c':10}]
d={}
for i in dic:
    for j in i.keys():
        d[j]=d.get(j,0)+i[j]
print(d)

