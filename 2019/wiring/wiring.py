PATH1 = ['R8','U5','L5','D3']
PATH2 = ['U7','R6','D4','L4']

WIRE_PATH = [
    'R75',
    'D30',
    'R83',
    'U83',
    'L12',
    'D49',
    'R71',
    'U7',
    'L72',
]

def decode_edge(edge: str) -> (int, int):
    """takes an edge in the form R75 and returns an int,int vector"""

    direction = edge[0]
    magnitude = int(edge[1:])

    if direction == 'L':
        return (magnitude * -1, 0)
    elif direction == 'D':
        return (0, magnitude * -1)
    elif direction == 'U':
        return (0, magnitude)
    elif direction == 'R':
        return (magnitude, 0)
    else:
        raise ValueError(f'Invalid direction {direction}')


def vector_to_coord_series(
        vector: (int, int),
        origin: (int, int)=(0, 0),
        include_origin=False):
    """Assumes only movement in cardinal directions"""

    if include_origin:
        series = [origin]
    else:
        series = []

    for i, component in enumerate(vector):

        if component == 0:
            continue

        coord = list(origin)  # need mutable object

        if component > 0:
            for j in range(1, component + 1):
                coord[i] = origin[i] + j
                series.append(tuple(coord))

        else:  # component < 0
            for j in range(1, component * -1 + 1):
                coord[i] = origin[i] - j
                series.append(tuple(coord))

    return series


def wire_path_to_map(wire_path: [str]) -> [(int, int)]:

    origin = (0, 0)
    wire_map = [origin]

    for edge in wire_path:
        vector = decode_edge(edge)
        coords = vector_to_coord_series(vector, origin)
        wire_map += coords
        origin = coords[-1]
        
    return wire_map


def overlaps(path1: [str], path2: [str], exclude_origin=True) -> [(int, int)]:

    map1 = set(wire_path_to_map(path1))
    map2 = set(wire_path_to_map(path2))

    intersection = map1 & map2

    if exclude_origin:
        intersection = intersection - set( [(0,0)] )

    return list(intersection)


def nearest_overlap(overlaps: [(int, int)]) -> ((int, int), int):
    nearest_so_far = None
    nearest_address_so_far = None

    for overlap in overlaps: 
        x_distance = abs(overlap[0])
        y_distance = abs(overlap[1])
        manhattan_distance = x_distance + y_distance

        if nearest_so_far is None or nearest_so_far > manhattan_distance:
            nearest_so_far = manhattan_distance
            nearest_address_so_far = overlap

    return (nearest_address_so_far, nearest_so_far)
