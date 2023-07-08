# merging two data sets
import csv
f1 = open("emp.csv",'r')
f2 = open("sal.csv",'r')
f3 = open("emp_sal",'w')

contents1 = f1.read()
contents2 = f2.read()

# nm=[]
sal=[]

lines1 = contents1.split('\n')
lines2 = contents2.split('\n')

for l1 in lines1:
    words1 = l1.split(',')
    
    for l2 in lines2:
        words2 = l2.split(',')
        if(words1[0]==words2[0]):
            l1 = words1[0] + "," +words1[1]+ "," +words2[2] +"\n"
            f3.write(l1)
            
            # nm.append(words1[1])
            sal.append(int(words2[2]))
            
f1.close()
f2.close()
f3.close()

# print(nm)
print(sal)

print("The highest salary is : ",max(sal))
print("Least salary is : ",min(sal))
print("Average salary is : ",sum(sal)/len(sal))