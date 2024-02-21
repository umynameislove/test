fi = open('/Users/quocbaotran/code practice/python/learning/dinamic programming/cho_thue_may/file.txt')

n = int(fi.readline())
c = []
s = []
v = []
for i in range(n):
    ci,si,vi = list(map(int,fi.readline().split()))
    c.append(ci)
    s.append(si)
    v.append(vi) 
c[:0] = [0]
s[:0] = [0]
v[:0] = [0]
# xep cuoc hop
c = sorted(c)
s = sorted(s)
v = sorted(v)
f = [0] * (n + 1)
t = [0] * (n + 1)
f[1] = [1]
  
for i in range(1 , n+ 1):
    f[i] = v[i]
    for j in range(1, i):
        if c[i] >= s[j] and f[i] < f[j] + v[i]:
            f[i] = f[j] + v[i]
            t[i] = j

print(f)
truyvet = []

csm = f.index(max(f))

while t[csm]:
    truyvet.append(s[csm])
    csm = t[csm]
truyvet.append(s[csm])
print(truyvet)

