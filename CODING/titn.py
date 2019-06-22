/*

sum_(k=1)^t (2^k - 1) (n + 1 - (k + 1) a) (n + 1 - (k + 1) b) = 1/6 (a (b (-2 t^3 + 3 (2^(t + 2) - 3) t^2 - 13 t + 24 (2^t - 1)) + 3 (n + 1) t (t - 2^(t + 2) + 3)) + 3 (n + 1) (b t^2 - t (b (2^(t + 2) - 3) + 2) + n (-2 t + 2^(t + 2) - 4) + 4 (2^t - 1)))

vertical and horizontal   : warasumm(1, 0, n, n-1, m)
cross                   : warasumm(1, 1, n, n-1, m)
other (gradient (a, b)) : 2*warasumm(a, b, n, floor(n/a)-1, m)

*/

warasum(a, b, n, t) = (a * (b * (-2 * t^3 + 3 * (2^(t + 2) - 3) * t^2 - 13 * t + 24 * (2^t - 1)) + 3 * (n + 1) * t * (t - 2^(t + 2) + 3)) + 3 * (n + 1) * (b * t^2 - t * (b * (2^(t + 2) - 3) + 2) + n * (-2 * t + 2^(t + 2) - 4) + 4 * (2^t - 1))) / 6

warasumm(a, b, n, t, m) = (a* (b* (-2* t^3 + 3* (Mod(2, m)^(t + 2) - 3)* t^2 - 13 *t + 24* (Mod(2, m)^t - 1)) + 3* (n + 1)* t* (t - Mod(2, m)^(t + 2) + 3)) + 3* (n + 1)* (b* t^2 - t *(b* (Mod(2, m)^(t + 2) - 3) + 2) + n *(-2* t + Mod(2, m)^(t + 2) - 4) + 4* (Mod(2, m)^t - 1)))/3

n = 111
m = 10^8

complement = 0

gaitou = 0

{
for(a=1, n, fact = factor(a);
  for(b=1, a, if (gcd(a, b)==1,
    if (a == b || a < b || a*2 > n, next;);
    t = floor(n/a)-1;
    complement += 2*warasumm(a, b, n, t, m);)));
}

/* vertical and horizontal */
complement += warasumm(1, 0, n, n-1, m) + warasumm(1, 1, n, n-1, m)

/* empty set and sets with size 1 */
complement += 1 + (n+1)^2

/* final result */
result = Mod(2, m)^((n+1)^2) - complement

print(result)

quit