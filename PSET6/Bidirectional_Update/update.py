def update(e, reverse, b):
    """ Updates the given edge and the corresponding edge in the
        reverse direction to add the given amount of flow.

        e -- an edge in a flow graph represented as a HalfEdge
        reverse -- the edge that gies between the same vertices as e
                   but in the opposite direction
        b -- a positive number less than or equal to e.residual()
    """   
    '''
    PSET 6
    - both edges can be in the og graph BUT not residual graph
    - total flow u <-> v is only one direction at a time
    Idea:
    - only one of f(u,v) and f(v,u) may be positive at any time
    - push from v->u means erase from u->v (up to amount sending)
      -> if there's still more, then increase f(v,u)

   Logic:
   1. Always cancel opposite-direction flow first (not allowed to have both >0 directions)
   2. If flow is 0, we simply cancel 0 and add b
   3. Compute c = min(b, reveres.flow())

   EX: 
      (u,v): c=5, f=5
      (v,u): c=4, f=2
      b=4
    '''
   # note that this implementation assumes only one edge with positive capacity
    # as in the original statement of the problem

    # cancel flow in opposite-direction first
    c = min(b, reverse.flow())
    if c > 0:
       # decrease reverse flow
       reverse.add_flow(-c)
       # incr reverse and decrease forward residuals
       reverse.add_residual(c)
       e.add_residual(-c)

    # add the remainder to the intended direction
    r = b - c
    if r > 0:
       # ensure we don't increase more than capacity
       safe_add = min(r, e.residual())
       if safe_add > 0:
          # increase forward flow
          e.add_flow(safe_add)
          # decr forward residual and incr reverse residual
          e.add_residual(-safe_add)
          reverse.add_residual(safe_add)


