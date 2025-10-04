import sys
import itertools as it

from graph import Graph
import hyperloop


def read_graphs():
    # read and check number of vertices
    n = int(sys.stdin.readline())
    if n <= 0:
        raise ValueError(f"Invalid number of vertices: {n}")
    car = Graph(n)
    loop = Graph(n)

    # read source and destination
    line = sys.stdin.readline()
    endpoints = line.split()
    if len(endpoints) != 2:
        raise ValueError(f"Invalid endpoints: {line}")
    source = int(endpoints[0])
    dest = int(endpoints[1])
    if source < 0 or source >= n:
        raise ValueError(f"Invalid vertex index: {source}")
    if dest < 0 or dest >= n:
        raise ValueError(f"Invalid vertex index: {dest}")
        
    
    # read one edge per line
    for line in sys.stdin:
        edge = line.split()
        if len(edge) != 4:
            raise ValueError(f"Invalid edges: {line}")
        u = int(edge[0])
        v = int(edge[1])
        w_car = float(edge[2])
        w_loop = float(edge[3])
        if u < 0 or u >= n:
            raise ValueError(f"Invalid vertex index: {u}")
        if v < 0 or v >= n:
            raise ValueError(f"Invalid vertex index: {v}")
        if w_car < 0.0:
            raise ValueError(f"Times must be non-negative: {w_car}")
        if w_loop < 0.0:
            raise ValueError(f"Times must be non-negative: {w_loop}")
        car.add_edge(u, v, w_car)
        loop.add_edge(u, v, w_loop)
    return car, loop, source, dest


def check_route(car, loop, source, dest, route):
    """ Checks that the given list of (u, v, mode) triples represents a valid
        path in the graphs and returns the weight.

        car -- an undirected, weighted graph with non negative-weight edges
        loop -- an undirected, weighted graph with the same edges as car and corresponding weights no greater
        source -- the index of a vertex in the graphs
        dest -- the index of a vertex in the graphs reachable from and not equal to source
        route -- a list of (u, v, mode) triples
    """
    # check that route is non-empty
    if len(route) == 0:
        raise ValueError("Empty route")

    # check that endpoints match
    if route[0][0] != source:
        raise ValueError(f"Route must start at source {source}, not {route[0][0]}")
    if route[-1][1] != dest:
        raise ValueError(f"Route must end at destination {dest}, not {route[-1][1]}")

    # check individual edges and add up weights and mode counts
    weight = 0
    car_count = 0
    loop_count = 0
    last = None
    for edge in route:
        if edge[2] == "car":
            car_count += 1
            g = car
        elif edge[2] == "hyperloop":
            loop_count += 1
            g = loop
        else:
            raise ValueError(f"Invalid mode {edge[2]}")

        # check that edge starts where last one ended
        if last is not None and edge[0] != last:
            raise(ValueError(f"Non-adjacent edges; {edge} should start at {last}"))
                  
        # check that edge exists, add in weight and remember last endpoint
        w = g.weight(edge[0], edge[1])
        if w is None:
            raise ValueError(f"Edge does not exist {edge}")
        weight += w
        last = edge[1]
        
    # check at most one Hyperloop
    if loop_count > 1:
        raise ValueError(f"Too many Hyperloop edges ({loop_count})")

    return weight
        
    

def run(verbose=False):
    # runs the Python implementation
    car, loop, source, dest = read_graphs()
    
    # find best route
    route = hyperloop.find_route(car, loop, source, dest)
    if verbose:
        print(route)

    # check that route is valid and output weight for external testing framework to check
    try:
        weight = check_route(car, loop, source, dest, route)
        print("Valid route")
        print(weight)
    except ValueError as ex:
        print(ex)
        print(route)


def validate():
    # for validating output of C/C++ program
    # 1st line is route, then graph size, source/dest, edges

    # read path and convert to list of triples
    line = sys.stdin.readline().split()
    route = []
    if len(line) == 0 or len(line) % 3 != 0:
        raise ValueError(f"Invalid path: {line}")
    for i in range(0, len(line), 3):
        route.append((int(line[i]), int(line[i + 1]), line[i + 2]))

    # read graphs and source/destination
    car, loop, source, dest = read_graphs()

    # check route and output weight for Ed to check
    try:
        weight = check_route(car, loop, source, dest, route)
        print("Valid route")
        print(weight)
    except ValueError as ex:
        print(ex)
        print(route)
                     


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--validate":
        validate()
    elif len(sys.argv) > 1 and sys.argv[1] == "--print":
        run(True)
    else:
        run()
