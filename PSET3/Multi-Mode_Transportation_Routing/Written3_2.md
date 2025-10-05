#### Light Edge Theorem (a.k.a. Cut Property): 
Let 𝐺 = ( 𝑉 , 𝐸 , 𝑤 ) G=(V,E,w) be a connected, undirected, weighted graph. Let 𝑆 ⊂ 𝑉 S⊂V be any subset of vertices, and let 𝑉 − 𝑆 V−S be its complement. Consider all edges that cross the cut ( 𝑆 , 𝑉 − 𝑆 ) (S,V−S) — i.e., edges ( 𝑢 , 𝑣 ) (u,v) with 𝑢 ∈ 𝑆 , 𝑣 ∈ 𝑉 − 𝑆 u∈S,v∈V−S. If ( 𝑢 , 𝑣 ) (u,v) is a minimum-weight edge across that cut, then there exists some MST of 𝐺 G that includes ( 𝑢 , 𝑣 ) (u,v).

Let $T$ be a minimum spanning tree (MST) of $G$.
By the \emph{Light Edge Theorem}, if $(u,v)$ is the minimum-weight edge across some cut $(S, V-S)$, 
then there exists an MST that contains $(u,v)$.  \\ 

We want to show that for any two vertices $A$ and $B$, the unique simple path $P_T(A,B)$ between $A$ and $B$ in $T$ 
minimizes the maximum edge weight among all paths connecting $A$ and $B$ in $G$.  \\ 

Proceed by contradiction.  Suppose there exists another path $P'(A,B)$ in $G$ such that 
$$
\max_{(x,y)\in P'(A,B)} w(x,y) < \max_{(x,y)\in P_T(A,B)} w(x,y).
$$
Let $(u,v)$ be the edge on $P_T(A,B)$ with weight equal to $\max_{(x,y)\in P_T(A,B)} w(x,y)$.
Removing $(u,v)$ from $T$ splits the tree into two components, say $S$ and $V-S$, with $u\in S$ and $v\in V-S$. 

Because $P'(A,B)$ connects $A$ and $B$, it must contain some edge $(x,y)$ crossing this same cut.
By our assumption, $w(x,y) < w(u,v)$.
Replacing $(u,v)$ in $T$ with $(x,y)$ would form a new spanning tree with smaller total weight than $T$, 
contradicting the minimality of $T$.

Therefore, no such $P'(A,B)$ can exist, and the path $P_T(A,B)$ in the MST indeed minimizes the maximum edge weight 
among all paths between $A$ and $B$.

### Draft 1
