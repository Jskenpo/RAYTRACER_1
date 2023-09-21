def elementwise_subtract(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud para la resta elemento por elemento.")

    result = [v1 - v2 for v1, v2 in zip(vector1, vector2)]
    return result


def vector_addition(vector1, scalar, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud para la suma.")

    result = [v1 + scalar * v2 for v1, v2 in zip(vector1, vector2)]
    return result

