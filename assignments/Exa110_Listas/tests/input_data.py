# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        [4, 1, 2, 3, 4],
        ["", "", "", "", "", "[1, 4, 27, 16]"],
        ["La salida no cumple con el caso de prueba\nVerifica los requerimientos"]
    ),
    # Test case 2
    (
        [5, 9, 8, 7, 6, 5],
        ["", "", "", "", "", "", "[729, 64, 343, 36, 125]"],
        ["La salida no cumple con el caso de prueba\nVerifica los requerimientos"]
    ),
    # Test case 3
    (
        [0],
        ["", "Error"],
        ["La salida no cumple con el caso de prueba\nVerifica cuando el numero de elementos es cero o menor que cero"]
    ),
    # Test case 4
    (
        [-5],
        ["", "Error"],
        ["La salida no cumple con el caso de prueba\nVerifica cuando el numero de elementos es cero o menor que cero"]
    ),
]
