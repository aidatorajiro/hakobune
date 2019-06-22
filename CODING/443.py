import math

# PARI GP CODE: x=5;y=13;for(i=0,2000,t=(-x)%factor(y-x)[1,1];x+=t;y+=t;y+=gcd(x,y);x+=1;print(t))
# MORE POLITE (?): x=5;y=13;for(i=0,2000,t=vecmin(apply(m->(-x)%m, factor(y-x)[,1]));x+=t;y+=t;y+=gcd(x,y);x+=1;print(t))


"""
(x, y) = (172, 513). find least natural number k s.t. (x+k, y+k) is not coprime.

(y+k) - (x+k) = 513 - 172 = 341.

"(x+k, y+k) is not coprime" is equivalent to "(x + k, (y+k) - (x+k)) is not coprime"

"(172 + k, 341) is not coprime" occurs if and only if:

172 + k = ds
    and
341     = dt

where d, s, t are integers larger than 1.

The least d which satisfies equations above is d=11 (from 341 = 11*31).
Therefore if n is the least natural number which satisfies equations above, d = 11.

So, we can write
k = 11s - 172

Then s = 16 and
k = (-172)%11 = 4
"""


x = 5
y = 13

for i in range(0, 1000):
  print(x, y)
  t = (-x) % factor(y-x)[0] # factor(y-x)[0] represents the minimum prime factor of y-x.
  x += t
  y += t
  y += math.gcd(x, y)
  x += 1
