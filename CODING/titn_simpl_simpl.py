warasumm(a, b, n, t, p) = (a* (b* (-2* t^3 + 3* (Mod(2, p)^(t + 2) - 3)* t^2 - 13 *t + 24* (Mod(2, p)^t - 1)) + 3* (n + 1)* t* (t - Mod(2, p)^(t + 2) + 3)) + 3* (n + 1)* (b* t^2 - t *(b* (Mod(2, p)^(t + 2) - 3) + 2) + n *(-2* t + Mod(2, p)^(t + 2) - 4) + 4* (Mod(2, p)^t - 1)))/3

rat(a, b, n, m, p) = (Mod(2, p)^(m - 1) - 1)*(n + 1 - a)*(n + 1 - b)

n = 111
p = 10^8

complement = 0

{
for(a=1, n,
  for(b=0, a,
    if (b==0 || a==b, complement += 2*rat(a, b, n, gcd(a, b), p), complement += 4*rat(a, b, n, gcd(a, b), p))
  );
);
}

/* empty set and sets with size 1 */
complement += 1 + (n+1)^2

/* final result */
result = Mod(2, p)^((n+1)^2) - complement

print(result)