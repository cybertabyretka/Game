def convert_to_int(coordinates, delimiter=';'):
    return tuple(map(int, coordinates.split(delimiter)))


def convert_to_string(coordinates, delimiter=';'):
    return f'{coordinates[0]}{delimiter}{coordinates[1]}'