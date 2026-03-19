#string slicing program
s = "codegnan"
a = s[5:8:-1]
print(a)
b = s[-1:10:2]
print(b)
c = s[::-2]
print(c)
d = s[::2]
print(d)
e = s[1:100:3]
print(e)
f = s[-2:5:1]
print(f)
g = s[-2:-3:-1]
print(g)

#string concatenation
s1 = 'code'
s2 = 'gnan'
print(s1 + s2)
print(s1 + " " + s2)
print((s1 + " ") * 5)


n = 5
abscent = 0
present = 0
for i in range(1, n+1):
    val = int(input(f"Enter the roll no {i} attendance 0- absent 1 - present: "))


