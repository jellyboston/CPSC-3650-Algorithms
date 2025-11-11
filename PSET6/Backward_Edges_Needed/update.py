def update(e, reverse, b):
    """ Updates the given edge and the corresponding edge in the
        reverse direction to add the given amount of flow.

        e -- an edge in a flow graph represented as a HalfEdge
        reverse -- the edge that gies between the same vertices as e
                   but in the opposite direction
        b -- a positive number less than or equal to e.residual()
    """
    # note that this implementation assumes only one edge with positive capacity
    # as in the original statement of the problem
    if e.capacity() > 0:
       # e is a forward edge
       e.add_flow(b)
    else:
       # e is a backward edge (0 capacity),
       # so cancel flow in opposite direction
       reverse.add_flow(-b)

    # update residuals
    e.add_residual(-b)
    reverse.add_residual(b)


