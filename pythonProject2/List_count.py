list_one = ['1','w','e','5','d','8','5','5']
a = 0
max_str = 0
for i in list_one:
    if list_one.count(i)>a:
        a = list_one.count(i)
        max_str= i
print("出现次数最多的是"+str(max_str)+",次数为："+str(a))