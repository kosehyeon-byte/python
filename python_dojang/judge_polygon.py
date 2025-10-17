import turtle as t

n=int(input())
l=int(input())
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.fd(l)
    t.rt((360/n)*2)
    t.fd(l)
    t.lt(360/n)
