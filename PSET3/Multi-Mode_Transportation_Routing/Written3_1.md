### Problem 3.1
WTS: optimal substructure of the min maximum problem

#### Draft 0
We want to show that u, x1,...,xj, wk, v is a path with minimum maximum weight given u, w1, ..., wk, v and u, x1,...,xj,wk are each respectively min max-weight (abbrv. MMW) as well. For the purpose of contradiction, suppose the hypothesis is false. If the path u, x1, ..., xj, wk, v was not MMW from u to v, then there must be some other path that achieves the MMW instead. 

#### Draft 1
Definitions
We need to define cost, optimality criteria, and paths. Define the weight cost as w(P(x,y)) = max w(x,y) for x,y in P for the maximum weight of the path. Define the optimality criteria as w(P(x,y)) = min w(P(x,y)) for the minimum max weight of all paths connecting two nodes. Lastly, let us define a path P(s,t) = s, ..., u, ..., v, ...., t. Define a subpath P(u,v) = u, ..., v. 

We want to show that if substructuve P(u,v) of P(s,t) is optimal, then P(s,t) itself is an optimal path with min-max weight. For the purpose of contradiction, suppose there exists P'(u,v) with a smaller maximum-weight than P(u,v). The minimum on subpath P'(u,v) has to be the new global minimum of the entire path P(s,t). Updating the subpath P'(u,v) would contradict that P(s,t) was originally optimal as the resulting path P'(s,t) would be optimal instead. Thus, by contradiction, P(s,t) can't be optimal if there's a smaller cost variant and we show optimal substructure for the minimum maximum-weight problem. 

#### Draft 2
Outline
- Define cost, optimality criteria, and paths
- State WTS and hypothesis
- Proceed with contradiction

We start by defining cost, optimality criteria, and paths. Let w(x,y) denote the weight of edge (x,y). 
Define the path cost as w_max(P) = max_{(x,y) ∈ P} w(x,y) which represents the largest edge weight on path P.
Define the optimality criterion as follows: a path P(a,b) is optimal if w_max(P(a,b)) = min_{P'} w_max(P'), 
where P' ranges over all paths connecting a to b. Lastly, let us write P(s,t) = (s, …, u, …, v, …, t), and define the subpath P(u,v) = (u, …, v). 

We want to show that the problem exhibits *optimal substructure*, that is if P(s,t) is an optimal path from s to t, then every subpath P(u,v) of P(s,t) is also optimal between its endpoints.

For the sake of contradiction, suppose there is a subpath P(u,v) of P(s,t) that is not pptimal. Then there exists a P'(u,v) from u to v where w_max(P'(u,v)) < w_max(P(u,v)). Construct a new path P'(s,t) by substituting P(u,v) in P(s,t) with P'(u,v). Then: 
            w_max(P'(s,t)) = max(w_max(P(s,u)), w_max(P'(u,v)), w_max(P(v,t))) 
                    < max(w_max(P(s,u)), w_max(P(u,v)), w_max(P(v,t))) 
                    = w_max(P(s,t)).
Thus P'(s,t) has strictly smaller maximum-edge weight than P(s,t), contradicting the assumption that P(s,t) was optimal.  Therefore, our assumption is false and we show that every subpath of an optimal path must itself be optimal, proving the problem has optimal substructure.



