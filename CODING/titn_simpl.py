/* Sum((2**(m - 1) - 1)*(n + 1 - m*a)*(n + 1 - m*b), (m, 2, s)).doit()*2 */
wholesum(a, b, n, s, p) = -2*Mod(2, p)^s*a*n*(s - 1) - 2*Mod(2, p)^s*a*(s - 1) - 2*Mod(2, p)^s*b*n*(s - 1) - 2*Mod(2, p)^s*b*(s - 1) + 2*Mod(2, p)^s - a*b*(2*s^3 + 3*s^2 + s - 6)/3 + 2*a*b*(Mod(2, p)^s*s^2 + 3*Mod(2, p)^s - Mod(2, p)^(s + 1)*s - 4) + a*n*(s^2 + s - 2) + a*(s^2 + s - 2) + b*n*(s^2 + s - 2) + b*(s^2 + s - 2) + 2*n^2*(Mod(2, p)^s - 2) + 2*n^2*(-s + 1) + 4*n*(Mod(2, p)^s - 2) - 4*n*(s - 1) - 2*s - 2

rat(a, b, n, m, p) = (Mod(2, p)^(m - 1) - 1)*(n + 1 - a)*(n + 1 - b)

n = 111
p = 10^8

complement = 0

{
for(a=4, n,
  for(b=1, a-1,
    complement += 4*rat(a, b, n, gcd(a, b), p)
  );
);
}

/* vertical and horizontal and cross */
complement += wholesum(1, 0, n, n, p) + wholesum(1, 1, n, n, p)

/* empty set and sets with size 1 */
complement += 1 + (n+1)^2

/* final result */
result = Mod(2, p)^((n+1)^2) - complement

print(result)