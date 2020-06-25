def main():

    while True:

        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        print("Your choice: ", end="")
        choice = input()

        if choice == "0":

            break

        elif choice == "1":

            print("Enter size of first matrix: ", end="")
            rows1, columns1 = [int(x) for x in input().split()]

            matrix1 = initialize(rows1)

            print("Enter size of second matrix: ", end="")
            rows2, columns2 = [int(x) for x in input().split()]

            matrix2 = initialize(rows2)

            if rows1 == rows1 and columns1 == columns2:

                print("The result is:")
                print_matrix(matrix_sum(matrix1, matrix2))
                print()

            else:

                print("The operation cannot be performed.")
                print()

        elif choice == "2":

            print("Enter size of matrix: ", end="")
            rows, columns = [int(x) for x in input().split()]

            print("Enter matrix:")
            matrix = initialize(rows)

            print("Enter constant: ", end="")
            scalar = float(input())

            print("The result is:")
            print_matrix(scalar_mult(matrix, scalar))

            print()

        elif choice == "3":

            print("Enter size of first matrix: ", end="")
            rows1, columns1 = (int(x) for x in input().split())

            print("Enter first matrix:")
            matrix1 = initialize(rows1)

            print("Enter size of second matrix: ", end="")
            rows2, columns2 = (int(x) for x in input().split())

            print("Enter second matrix:")
            matrix2 = initialize(rows2)

            if columns1 == rows2:

                print_matrix(mult(matrix1, matrix2))
                print()

            else:

                print("The operation cannot be performed.")
                print()

        elif choice == "4":

            print()
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")

            print("You choice: ", end="")
            option = input()

            if option in (str(x) for x in range(1, 5)):

                print("Enter matrix size: ", end="")
                rows, columns = [int(x) for x in input().split()]

                print("Enter matrix:")
                matrix = initialize(rows)

                print("Your result is:")
                print_matrix(transpose(matrix, option=option))
                print()

            else:

                print("Invalid option")

        elif choice == "5":

            print("Enter matrix size: ", end="")
            rows, columns = (int(x) for x in input().split())

            matrix = initialize(rows)

            print(f"The result is:\n{determinant(matrix)}")

        elif choice == "6":

            print("Enter matrix size: ", end="")
            rows, columns = (int(x) for x in input().split())

            matrix = initialize(rows)
            det = determinant(matrix)

            if det:

                print("The result is:")
                print_matrix(scalar_mult(transpose(c_t(matrix), option="1"), 1 / det))

            else:

                print("This matrix doesn't have an inverse.\n")

        else:

            print("Invalid option")


def transpose(matrix, option="1"):

    trans = []

    if option == "1":

        for i in range(len(matrix[0])):

            trans.append([])
            for j in range(len(matrix)):

                trans[i].append(matrix[j][i])

    elif option == "2":

        counter = 0
        for i in range(len(matrix[0]) - 1, -1, -1):

            trans.append([])
            for j in range(len(matrix) - 1, -1, -1):

                trans[counter].append(matrix[j][i])

            counter += 1

    elif option == "3":

        for i in range(len(matrix)):

            trans.append([])
            for j in range(len(matrix[0]) - 1, -1, -1):

                trans[i].append(matrix[i][j])

    elif option == "4":

        counter = 0
        for i in range(len(matrix) - 1, -1, -1):

            trans.append([])
            for j in range(len(matrix[0])):

                trans[counter].append(matrix[i][j])

            counter += 1

    return trans


def scalar_mult(matrix, scalar):

    multiplied = [[scalar * item for item in line] for line in matrix]

    return multiplied


def matrix_sum(matrix1, matrix2):

    sum_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    return sum_matrix


def initialize(rows):

    matrix = []

    for i in range(rows):

        row = input()

        row = [float(x) for x in row.split()]

        matrix.append(row)

    return matrix


def print_matrix(matrix):

    for i in matrix:

        counter = 0
        for j in i:

            #print(str(j) + " " if counter < len(matrix[0]) - 1 else str(j), end="")
            print("%.2g" % j + " " if counter < len(matrix[0]) - 1 else "%.2g" % j, end="")
            counter += 1

        print()


def mult(matrix1, matrix2):

    matrix = []

    for i in range(len(matrix1)):

        matrix.append([])
        for x in range(len(matrix2[0])):

            result = 0
            for j in range(len(matrix2)):

                result += matrix2[j][x] * matrix1[i][j]

            matrix[i].append(result)

    return matrix


def minor(matrix, i, j):

    new_matrix = []
    counter = 0

    for row in range(len(matrix)):

        if row == i:

            continue

        new_matrix.append([])
        for column in range(len(matrix[0])):

            if column == j:

                continue

            new_matrix[counter].append(matrix[row][column])
        counter += 1

    return new_matrix


def cofactor(i, j):

    return (-1)**(i + j)


def determinant(matrix):

    if len(matrix[0]) == 2:

        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    elif len(matrix[0]) == 1:

        return matrix[0][0]

    det = 0

    for j in range(len(matrix[0])):

        det += matrix[0][j] * cofactor(1, j + 1) * determinant(minor(matrix, 0, j))

    return det


def c_t(matrix):

    new_matrix = []
    counter = 0

    for row in range(len(matrix)):

        new_matrix.append([])
        for column in range(len(matrix[0])):

            new_matrix[counter].append(cofactor(row + 1, column + 1)
                                       * determinant(minor(matrix, row, column)))

        counter += 1

    return new_matrix





main()
