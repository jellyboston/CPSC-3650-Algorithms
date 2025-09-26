## 2.3
#### Proof
WTS: The greedy strategy always produces a solution with the minimum number of fence segments.

**Thm - Greedy Stays Ahead**

 For every i, gi >= oi. By the i-th fence post, greedy has always reached as far at least as the optimal. If this is true, then greedy never falls behind optimal. Thus, the greedy
cannot require more fence posts than optimal, and it uses the minimum as possible.

Proof. Suppose a set G representing Greedy's fence posts for G = {g1, g2, ..., gk}. Let set O represent one optimal solution's fence posts for O = {o1, o2, ..., om}. We want to show that every greedy fence post i always reaches as far as the optimal solution: gi >= oi for all i. 

Proceed by contradiction. Let j denote an arbitrary index. Suppose:
g1 >= o1
...
gj >= oj
gj+1 < oj+1 

If gj+1 < oj+1, then a greater length was chosen by O under the valid constraint L. However, by definition, greedy would have selected this greater length. By contradiction, gi >= oi

---
#### Proof
WTS: The greedy strategy always produces a solution with the minimum number of fence segments.

**Thm – Greedy Stays Ahead.**  
For every i, gi ≥ oi. By the i-th fence post, greedy has always reached at least as far as the optimal solution. If this holds, then greedy never falls behind optimal. Thus, greedy cannot require more fence posts than optimal, and it uses the minimum possible.

**Proof.** Suppose G = {g1, g2, ..., gk} are the greedy fence posts and O = {o1, o2, ..., om} are the fence posts of some optimal solution. We want to show that gi ≥ oi for all i.

Proceed by contradiction. Let j be the first index where greedy falls behind, i.e.,
g1 ≥ o1, g2 ≥ o2, ..., gj ≥ oj, but gj+1 < oj+1.  
This means the optimal solution places its (j+1)-th post farther along the perimeter than greedy does.

However, by construction, greedy always chooses the farthest tree reachable within distance L from gj. Since oj+1 is also reachable from oj (and gj ≥ oj), it must also be reachable from gj. Therefore greedy would have chosen oj+1 or a point even farther, contradicting gj+1 < oj+1.

Hence no such index j exists, and gi ≥ oi for all i.

Next, we prove `k = m` such that the number of fence posts placed by the greedy solution is equivalent to optimal. Proceed by contradiction.

By exhaustion, consider Case #1 where k > m. If the number of fence posts placed by greedy is greater than optimal (k > m),then this contradicts greedy by definition. Under the same perimeter and constraint L, this would mean that for some G1, ..., Gk the fence post length was not greedy. Thus, k <= m. 

Lastly, consider Case #2 where k < m. This means G required fewer fence posts than the optimal. However, by definition, this contradicts the optimal set and cannot be true. Thus, k = m and the number of fence posts placed by greedy is equivalent to optimal.

The proof shows that for every i, i, gi ≥ oi and k = m. Thus, greedy uses the minimum fence posts possible.
