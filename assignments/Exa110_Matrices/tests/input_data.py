# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["4", "3", "4-5-6-7", "1-2-3-9", "3-2-8-10", "11-23-3-4", ],
        ["", "", "", "", "", "", "[[4, 5, 6, 7], [1, 2, 3, 9], [3, 2, 8, 10], [11, 23, 3, 4]]",
            "[[12, 15, 18, 21], [3, 6, 9, 27], [9, 6, 24, 30], [33, 69, 9, 12]]"],
        "Verifica los requerimientos que se solicitan"
    ),
    # Test case 2
    (
        ["2", "10", "3-4-5-7", "1-2-3-4"],
        ["", "", "", "", "[[3, 4, 5, 7], [1, 2, 3, 4]]",
            "[[30, 40, 50, 70], [10, 20, 30, 40]]"],
        "Verifica los requerimientos que se solicitan"
    ),
]
