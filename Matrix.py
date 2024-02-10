# The creators are:
# Carmel Dor - 316015882
# Segev Chen - 322433400
# Gad Hasson - 207898123
# Artiom Bondar - 332692730


def print_matrix(_list):  # A function to print a matrix
    for row in _list:
        print(row, end='\n')


def build_squared_matrix():
    # create and empty list of lists
    _list = []

    # size of the matrix (since the matrix is squared we don't need to get the columns
    size = int(input("Enter the size of the matrix: "))

    # iterating the elements to the list

    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(int(input("Enter the elements of the matrix: ")))
        _list.append(row)

    return _list


def sum_of_matrix(_list1, _list2):  # function that calculate the sum of two matrices
    if len(_list1) != len(_list2):  # Check
        print("Invalid")
        return None

    _temp_matrix = []
    for i in range(len(_list1)):  # Loop on the rows
        _row = []
        for j in range(len(_list1)):  # Loop on the columns
            _row.append(_list1[i][j]+_list2[i][j])
        _temp_matrix.append(_row)

    return _temp_matrix


def mult_of_matrix(_list1, _list2):
    if len(_list1) != len(_list2):  # since the matrices are squared then the num rows is equal to the num of columns
        print("Invalid the size needs to be the equal since the matrices are squared")

    _size = len(_list1)  # temp parameter to save the size of the rows and columns (the matrix is squared)
    # print(f"the size is--> {_size}")  # for checking purposes

    _result_matrix = [[] for _ in range(_size)]  # creating a list that contains _size amount of lists

    for row in range(_size):  # iterate on rows
        for column in range(_size):  # iterate on columns
            _value = 0  # temporary parameter to save the value of the mult calculation for each element in the matrix
            for k in range(_size):
                _value += _list1[row][k]*_list2[k][column]  # the calculation for the element
            _result_matrix[row].append(_value)

    return _result_matrix


if __name__ == '__main__':
    print("Make sure you're entering the same size for both matrices because mult and sum needs the size to be equal\n")
    print("MATRIX 1\n")
    _mat1 = build_squared_matrix()
    print("MATRIX 2\n")
    _mat2 = build_squared_matrix()

    print("The matrices are:\n")
    print("MATRIX 1\n")
    print_matrix(_mat1)
    print("\n\n")
    print("MATRIX 2\n")
    print_matrix(_mat2)

    print("\n\n")
    print("The sum of the matrices is:\n")
    print_matrix(sum_of_matrix(_mat1, _mat2))
    print("the multiplication of the matrices is:\n")
    print_matrix(mult_of_matrix(_mat1, _mat2))
