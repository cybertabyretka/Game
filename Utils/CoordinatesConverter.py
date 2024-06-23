def convert_to_int(coordinates: str, delimiter: str = ';') -> tuple[int, ...]:
    return tuple(map(int, coordinates.split(delimiter)))


def convert_to_string(coordinates: tuple[int, int], delimiter: str = ';') -> str:
    return f'{coordinates[0]}{delimiter}{coordinates[1]}'
