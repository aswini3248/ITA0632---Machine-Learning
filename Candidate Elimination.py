import csv
a = []
with open("C:/Users/aswin/Documents/ML/enjoysport.csv",'r') as dataset:
    Reader = csv.reader(dataset)
    for row in Reader:
        a.append(row)
        print(row)
num_attributes = len(a[0]) - 1
s = ['0'] * num_attributes
g = ['?'] * num_attributes

print("Most Specific hypothesis S0 : " + str(s))
print("Most General hypothesis G0 : " + str(g))
version_space = []
for i in range(0,len(a)):
    if(a[i][num_attributes] == 'yes'):
        print("Instance " + str(i+1) + " +ve ")
        for j in range(0,num_attributes):
            if (s[j] == '0' or s[j] == a[i][j]):
                s[j] = a[i][j]
            else:
                s[j] = '?'
        for j in range(0,num_attributes):
            for k in range(1,len(version_space)):
                if(version_space[k][j] != '?' and version_space[k][j]!=s[j]):
                    del version_space[k]
        print("S" + str(i+1) , s)
        print("G" + str(i+1) , version_space)
    if(a[i][num_attributes] == 'no'):
        print("Instance " + str(i+1) + " -ve ")
        print("S" + str(i+1),s)
        print("G" + str(i+1))
        for j in range(0,num_attributes):
            if(s[j]!=a[i][j] and s[j] !='?'):
                g[j] = s[j]
                version_space.append(g)
                g = ['?']*num_attributes
        print(version_space)
    print()
version_space.append(s)
print()
print("Final Version Space : " , version_space)
