n = int(input())
name =[]
for x in range(n):
    a,b = map(str,input().split())
    name.append(a)
    name.append(b)
c = "Yes"
for y in range(n):
    a = name.pop(0)
    b = name.pop(0)
    if a in name:
        if b in name:
            c ="No"
            break
            
        else:
            name.append(a)
    elif b in name:
        name.append(b)

print(c)
