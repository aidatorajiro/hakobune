/*

sum_(k=1)^t (2^k - 1) (n + 1 - (k + 1) a) (n + 1 - (k + 1) b) = 1/6 (a (b (-2 t^3 + 3 (2^(t + 2) - 3) t^2 - 13 t + 24 (2^t - 1)) + 3 (n + 1) t (t - 2^(t + 2) + 3)) + 3 (n + 1) (b t^2 - t (b (2^(t + 2) - 3) + 2) + n (-2 t + 2^(t + 2) - 4) + 4 (2^t - 1)))

vertical and horizontal   : warasumm(1, 0, n, n-1, p)
cross                   : warasumm(1, 1, n, n-1, p)
other (gradient (a, b)) : 2*warasumm(a, b, n, floor(n/a)-1, p)

*/

warasum(a, b, n, t) = (a * (b * (-2 * t^3 + 3 * (2^(t + 2) - 3) * t^2 - 13 * t + 24 * (2^t - 1)) + 3 * (n + 1) * t * (t - 2^(t + 2) + 3)) + 3 * (n + 1) * (b * t^2 - t * (b * (2^(t + 2) - 3) + 2) + n * (-2 * t + 2^(t + 2) - 4) + 4 * (2^t - 1))) / 6

warasumm(a, b, n, t, p) = (a* (b* (-2* t^3 + 3* (Mod(2, p)^(t + 2) - 3)* t^2 - 13 *t + 24* (Mod(2, p)^t - 1)) + 3* (n + 1)* t* (t - Mod(2, p)^(t + 2) + 3)) + 3* (n + 1)* (b* t^2 - t *(b* (Mod(2, p)^(t + 2) - 3) + 2) + n *(-2* t + Mod(2, p)^(t + 2) - 4) + 4* (Mod(2, p)^t - 1)))/3

/* unit a, unit b, n, iteration, modulo       sympy: Sum((n+1-m*a)*(n+1-m*b)*(2**(m-1)-1), (m, 2, s)).doit()*2 */
/* ratsum(a, b, n, s, p) = -(-6*Mod(2, p)^s*a*b*s^2 + 12*Mod(2, p)^s*a*b*s - 18*Mod(2, p)^s*a*b + 6*Mod(2, p)^s*a*n*s - 6*Mod(2, p)^s*a*n + 6*Mod(2, p)^s*a*s - 6*Mod(2, p)^s*a + 6*Mod(2, p)^s*b*n*s - 6*Mod(2, p)^s*b*n + 6*Mod(2, p)^s*b*s - 6*Mod(2, p)^s*b - 6*Mod(2, p)^s*n^2 - 12*Mod(2, p)^s*n - 6*Mod(2, p)^s + 2*a*b*s^3 + 3*a*b*s^2 + a*b*s + 18*a*b - 3*a*n*s^2 - 3*a*n*s + 6*a*n - 3*a*s^2 - 3*a*s + 6*a - 3*b*n*s^2 - 3*b*n*s + 6*b*n - 3*b*s^2 - 3*b*s + 6*b + 6*n^2*s + 6*n^2 + 12*n*s + 12*n + 6*s + 6)/3 */

/* rat(a, b, n, m, p) = (Mod(2, p)^(m - 1) - 1)*(n + 1 - m*a)*(n + 1 - m*b) */

/* Sum((n+1-m*a)*(n+1-m*b)*(2**(m-1)-1), (b, 1, s)).doit()*4 */
karasum(a, n, m, s, p) = s*(Mod(2, p)^m*a*m^2*(s + 1) - Mod(2, p)^m*m*n*(s + 1) - Mod(2, p)^m*m*(s + 1) - Mod(2, p)^(m + 1)*a*m*n - Mod(2, p)^(m + 1)*a*m + Mod(2, p)^(m + 1)*n^2 + Mod(2, p)^(m + 1) + Mod(2, p)^(m + 2)*n - 2*a*m^2*(s + 1) + 4*a*m*n + 4*a*m + 2*m*n*(s + 1) + 2*m*(s + 1) - 4*n^2 - 8*n - 4)

n = 111
p = 10^8

complement = 0

{
for(a=2, n, fact = factor(a);
  fact = factor(a)[,1];
  apply(x->complement += rat(), fact)
  print(fact)
);
}

/* vertical and horizontal */
complement += warasumm(1, 0, n, n-1, p) + warasumm(1, 1, n, n-1, p)

/* empty set and sets with size 1 */
complement += 1 + (n+1)^2

/* final result */
result = Mod(2, p)^((n+1)^2) - complement

print(result)