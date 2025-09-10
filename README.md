# numrep


Float      overflow: 1.70141e+38    underflow: 1.4013e-45
Double     overflow: 8.98847e+307   underflow: 4.94066e-324
Integer    overflow: 2147483647     underflow: -2147483648
Unsigned   overflow: 4294967295     underflow: 0

In python, integers have arbitrary precision with automatic memory allocation. They are allowed to grow as large as the bits allow.

BESSEL FUNCTION:
The down method is more accurate. We can tell by only by inspecting the very
beginning of J_8(x) where we see the up method have some little oddity the
down doesn't have. This is probably because the up method starts with the smallest
value, which means the error accumulates. Since down begins with the largest
number, the error doesn't grow.

NUMERICAL DERIVATIVES:
According to our plots, $\varepsilon_{min,fd} \sim 10^{-8}$, with two exceptions being only an order of magnitude larger. Comparing with Landau, we see that the forward method should have a relative error around $10^{-8}$. Likewise, $\varepsilon_{min,cd} \sim 10^{-11}$, again with two exceptions an order of magnitude higher. This too is in agreement with Landau. Though he does not give an estimate for the extrapolation case, we found in both cos(x) and exp(x), t=0.1, 1 had $\varepsilon_{min,ed} \sim 10^{-13}$ and t=100 had $\varepsilon_{min,ed} \sim 10^{-12}$.
As for the slopes, Landau stated that the relationships were $\varepsilon_{rel,fd} \sim h$, $\varepsilon_{rel,cd} \sim h^2$, and $\varepsilon_{rel,fd} \sim h^4$. Since we are looking at a log plot, the slope is the power. Just by eye, we can see that this is correct: the forward method yielded a slope of 1, the central a slope of 2, and the extrapolation a higher slope, though we can guess it to be 3 or 4. 
Lastly, each relative error plot, regardless of parent function or method, takes the shape of a "v". The left side is where round-off error dominates, and the right is where algorithmic error dominates.
