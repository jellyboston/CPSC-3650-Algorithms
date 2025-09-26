## 2.2
#### Proof
WTS: The `MAKE_CHANGE()` algorithm produces an optimal solution using the fewest coins for all n when D = {1, 5, 10, 20, 50}.

Proceed by strong induction. Let P(n) be the statement: greedy is optimal for all amounts less than n. This will serve as the induction hypothesis (IH).

Case #1: Suppose 20 <= n <= 49. Then greedy chooses d = 20. We prove by contradiction that any optimal solution O must contain a 20.

Assume 20 ∉ O. Then O must consist only of {1, 5, 10}, so there exist nonnegative integers a, b, c with a + 5b + 10c = n.

Under this structure, one possible situation is a >= 5, where more than 5 pennies can be used. However a swap can be made with five 1 cent coins which can be replaced by a single 5 cent coin, reducing the number of coins. This contradicts optimality. 

Next consider b ≥ 2. The two 5¢ coins can be replaced by one 10¢ coin, which contradicts the assumption again.

c >= 2 is also possible, where more than two dimes can be used. Again, a contradiction in optimality can be seen by swapping with one d = 20. 

Lastly, let us consider c >= 1 and b >= 2. Again, a swap with one d = 20 can be made for a lower change amount, contradicting optimality.

Therefore, if none of these swaps are possible, then a < 5, b < 2, and c < 2. In that case, the maximum total value is 4 + 5 + 10 = 19 < 20, which contradicts the assumption that n ≥ 20. Hence O must contain a 20, exactly the greedy choice. By the IH, the remaining amount n−20 is solved optimally by greedy, and by optimal substructure the entire solution is optimal.

Case #2: Suppose n >= 50. Then greedy chooses d = 50. We prove by contradiction that any optimal solution O must contain a 50.

Assume 50 ∉ O. Then O must consist of {1, 5, 10, 20}, so there exist nonnegative integers a, b, c, e with a + 5b + 10c + 20e = n.

If b ≥ 10, then ten 5¢ coins can be replaced by one 50¢ coin, reducing the total number of coins. Contradiction.

If c ≥ 5, then five 10¢ coins can be replaced by one 50¢ coin. Contradiction.

If e ≥ 2 and c ≥ 1, then two 20¢ coins and one 10¢ coin sum to 50¢, which can be replaced by a single 50¢ coin. Likewise, if e = 1 and c ≥ 3, then one 20¢ and three 10¢ coins sum to 50¢ and can be replaced by one 50¢ coin. Contradiction.

Lastly, if b ≥ 4, c ≥ 1, and e ≥ 1, then four 5¢ coins, one 10¢ coin, and one 20¢ coin sum to 50¢ and can be replaced by one 50¢ coin. Contradiction.

Therefore, if none of these swaps are possible, then b < 10, c < 5, and e < 2. 
In that case, the maximum total value achievable is     a + 5·9 + 10·4 + 20·1 = a + 95.
But with a < 5 (otherwise we could swap pennies for nickels), the maximum value is at most 99. 
This contradicts the assumption that n ≥ 50 can be made *without* using a 50¢ coin, since larger n (e.g. 100) cannot be reached. 
Hence O must contain a 50¢ coin, exactly the greedy choice. By the IH, the remaining amount n−50 is solved optimally by greedy, and by optimal substructure the entire solution is optimal

Therefore, in both cases the greedy choice d is forced into any optimal solution. Combining this with the induction hypothesis that greedy is optimal for all smaller amounts, we conclude greedy is optimal for all n ≥ 0. □