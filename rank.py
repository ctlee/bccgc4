import operator
import csv
f=open("CatS_score_compounds_D3R_GC4_answers.csv","r")

lines=f.readlines()

s=[]
for i in lines[1:]:
    entry=i.split(" ")
    s.append(entry)
print(s)


dict={}

for k in s:
    for h in k:
        print(h)
        h=h.split(",")
        print(h[0])
        dict[h[0]]=float(h[2])

sorted_dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)

print(sorted_dict)

count=1
All=[]
#for a in sorted_dict:
#    line=[]
#    line.append(a[0])
#    line.append(count)
#    line.append(float(a[1]))
#    for a,b in zip(sorted_dict[1:],sorted_dict):
#        print (a[1],b[1])
#
#        if a[1]!=b[1]:
#    
#            count=count+1
#    All.append(line)
#print(All)

#for a in sorted_dict:
#    line=[]
#    line.append(a[0])
#    line.append(count)
#    line.append(float(a[1]))
for a,b in zip(sorted_dict[1:],sorted_dict):
    print (a[1],b[1])
    line=[]
    line.append(b[0])
    line.append(count)
    line.append(float(b[1]))

    if a[1]!=b[1]:
#    
        count=count+1
    All.append(line)
print(All)

with open("Answers.csv","w") as g:
    writer=csv.writer(g,dialect="excel")
    writer.writerows(All)
