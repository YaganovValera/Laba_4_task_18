import random
import time
import colorama
from colorama import Fore, Back, Style

# Функция для вывода матрицы
def matrix_output(row_length, matrix):
    for row in range(row_length):
        for column in range(row_length):
            print("{:4}".format(matrix[row][column]), end=' ')
        print()

# Функция для произведения матрицы на аргумент
def multiplication_matrix_and_argument(row_length, matrix, argument):
    for row_matrix in range(row_length):
        for column_matrix_A in range(row_length):
            matrix[row_matrix][column_matrix_A] = argument * matrix[row_matrix][column_matrix_A]

# Получаем пользовательский ввод:
while True:
    N = input("Введите длину матрицы (положительное, целое число, больше 6): ")
    N = N.strip()
    if N.isdigit():
        N = int(N)
        if N >= 6:
            break
        else:
            print("Ошибка. Вы ввели число меньше 6.")
    else:
        print("Неверный ввод данных.")
while True:
    flag_minus = False
    K = input("Введите число K (целое число): ")
    K = K.strip()
    # Проверка на ввод знака
    if K[0] == '-' or K[0] == '+':
        if K[0] == '-':
            flag_minus = True
            K = K.replace('-', '')
    else:
        K = K.replace('+', '')
    if K.isdigit():
        K = int(K)
        if flag_minus:
            K = - int(K)
        break
    else:
        print("Неверный ввод.")

# Запуск таймера
start = time.monotonic()
try:
    # Флаг поднимается, если выполненяется условие (кол-во чисел, которые > K, в третьей четверти > произведения чисел во второй четверти)
    flag_swap_matrix_B_1_3 = False
    # Флаг поднимается, если условие не выполняется
    flag_swap_matrix_E_and_C = False

    # Создаем матрицу А
    print(" Матрица А: ")
    A = []
    for row in range(N):
        subMatrix = []
        for column in range(N):
            subMatrix.append(random.randint(-10, 10))
            if (N % 2 == 0) or (N % 2 != 0 and row != N//2):
                if row < N//2 and column < N//2:
                    print(Back.GREEN + '{:4}'.format(subMatrix[column]), end='')
                elif row < N//2 and column > N//2 - int(N % 2 == 0):
                    print(Back.RED + '{:4}'.format(subMatrix[column]), end='')
                elif row > N//2 - int(N % 2 == 0) and column < N//2:
                    print(Back.YELLOW + '{:4}'.format(subMatrix[column]), end='')
                elif row > N//2 - int(N % 2 == 0) and column > N//2 - int(N % 2 == 0):
                    print(Back.BLUE + '{:4}'.format(subMatrix[column]), end='')
                else:
                    print(Style.RESET_ALL + '{:4}'.format(subMatrix[column]), end='')
            else:
                print('{:4}'.format(subMatrix[column]), end='')
        print(Style.RESET_ALL)
        A.append(subMatrix)
    print(Style.RESET_ALL)

    # Создание подматриц B, C, D и E
    submatrix_length = N // 2  # Длина подматрицы

    sub_matrix_B = [A[row][0:submatrix_length] for row in range(submatrix_length + 1)]
    sub_matrix_C = [A[row][submatrix_length + N % 2: N] for row in range(submatrix_length + 1)]
    sub_matrix_D = [A[row][0: submatrix_length] for row in range(submatrix_length + N % 2, N)]
    sub_matrix_E = [A[row][submatrix_length + N % 2: N] for row in range(submatrix_length + N % 2, N)]

                                                                                        # Формирование матрицы F
    main_diagonal = 1  # 1 - если главная диагональ не входит в диапазон; 0 - если входит

    # Подсчет чисел, которые стоят в нечетных столбцах(отсчет столбцов начинается с первого столбца подматрицы С) области 3 подматрицы С и больше К
    counter_numbers_greater_than_K = 0                                                                      # Количество подходящих чисел
    for row_submatrix_C in range(submatrix_length // 2 + submatrix_length % 2):
        column_submatrix_C = submatrix_length - 1
        while column_submatrix_C > submatrix_length - 1 - row_submatrix_C - 1 + main_diagonal:
            if (column_submatrix_C + 1) % 2 != 0:
                if sub_matrix_C[row_submatrix_C][column_submatrix_C] > K:
                    counter_numbers_greater_than_K += 1
                if sub_matrix_C[submatrix_length - 1 - row_submatrix_C][column_submatrix_C] > K:
                    if submatrix_length - 1 - row_submatrix_C != row_submatrix_C:
                        counter_numbers_greater_than_K += 1
            else:
                column_submatrix_C += 1
            column_submatrix_C -= 2
    #Вывод чисел, которые считает программа
    print("3 область в подматрице С (выделена красным):")
    max_column = submatrix_length
    max_row = submatrix_length
    for row in range(submatrix_length):
        for column in range(submatrix_length):
            if (column > max_column - 1 - row - 1 + main_diagonal) and row < max_row // 2:
                print(Back.RED + "{:4}".format(sub_matrix_C[row][column]), end='')
                print(Style.RESET_ALL, end='')
            elif (column > max_column//2 - max_row//2 + row - 1 + main_diagonal) and row >= max_row // 2:
                print(Back.RED + "{:4}".format(sub_matrix_C[row][column]), end='')
                print(Style.RESET_ALL, end='')
            else:
                print("{:4}".format(sub_matrix_C[row][column]), end='')
        print('')
    print("\nЧисла, которые считает программа. Т.е они больше К и стоят в нечетных столбцах(Выделены так же красным).)")
    for row in range(submatrix_length):
        for column in range(submatrix_length):
            if (column > max_column - 1 - row - 1 + main_diagonal) and row < max_row // 2:
                if (column + 1) % 2 != 0 and sub_matrix_C[row][column] > K:
                    print(Back.RED + "{:4}".format(sub_matrix_C[row][column]), end='')
                    print(Style.RESET_ALL, end='')
                else:
                    print("{:4}".format(sub_matrix_C[row][column]), end='')
            elif (column > max_column // 2 - max_row // 2 + row - 1 + main_diagonal) and row >= max_row // 2:
                if (column + 1) % 2 != 0 and sub_matrix_C[row][column] > K:
                    print(Back.RED + "{:4}".format(sub_matrix_C[row][column]), end='')
                    print(Style.RESET_ALL, end='')
                else:
                    print("{:4}".format(sub_matrix_C[row][column]), end='')
            else:
                print("{:4}".format(sub_matrix_C[row][column]), end='')
        print('')

    # Произведение чисел в области 2, которые стоят в нечетных столбцах матрицы С
    multiplication_of_numbers = 1  # произведение подходящих чисел
    start_left_column_C = main_diagonal
    start_right_column_C = submatrix_length - 1 - main_diagonal
    for row_submatrix_C in range(0, submatrix_length // 2 + submatrix_length % 2 - main_diagonal + 1, 2):
        current_left_column_C = start_left_column_C
        current_right_column_C = start_right_column_C
        while current_left_column_C <= submatrix_length // 2 - int(submatrix_length % 2 == 0):
            if abs(multiplication_of_numbers) > counter_numbers_greater_than_K:
                if sub_matrix_C[row_submatrix_C][current_left_column_C] < 0:
                    multiplication_of_numbers *= (-1)
                elif sub_matrix_C[row_submatrix_C][current_left_column_C] == 0:
                    multiplication_of_numbers = 0
                    break
            else:
                multiplication_of_numbers *= sub_matrix_C[row_submatrix_C][current_left_column_C]
            if current_left_column_C != current_right_column_C:
                if abs(multiplication_of_numbers) > counter_numbers_greater_than_K:
                    if sub_matrix_C[row_submatrix_C][current_right_column_C] < 0:
                        multiplication_of_numbers *= (-1)
                    elif sub_matrix_C[row_submatrix_C][current_right_column_C] == 0:
                        multiplication_of_numbers *= 0
                        break
                else:
                    multiplication_of_numbers *= sub_matrix_C[row_submatrix_C][current_right_column_C]
            current_left_column_C += 1
            current_right_column_C -= 1
        if multiplication_of_numbers == 0:
            break
        start_left_column_C += 2
        start_right_column_C -= 2

    # 2 Область в подматрице С (выделена зеленым):
    print("\n2 Область в подматрице С (выделена зеленым): ")
    right_column = submatrix_length - 1
    left_column = 0
    max_row = submatrix_length
    for row in range(submatrix_length):
        for column in range(submatrix_length):
            if row < max_row // 2 - int(max_row % 2 == 0) + 1 - main_diagonal \
                    and column > left_column - 1 + main_diagonal + row and column < right_column + 1 - main_diagonal - row:
                print(Back.GREEN + "{:4}".format(sub_matrix_C[row][column]), end='')
                print(Style.RESET_ALL, end='')
            else:
                print("{:4}".format(sub_matrix_C[row][column]), end='')
        print('')

    # Числа, которые считает программа. Т.е они стоят в нечетных строках(Выделены так же зеленым)
    print("\nЧисла, которые считает программа. Т.е они стоят в нечетных строках(Выделены так же зеленым).)")
    right_column = submatrix_length - 1
    left_column = 0
    max_row = submatrix_length
    for row in range(submatrix_length):
        for column in range(submatrix_length):
            if (row + 1)% 2 != 0 and row < max_row // 2 - int(max_row % 2 == 0) + 1 - main_diagonal and \
                    column > left_column - 1 + main_diagonal + row and column < right_column + 1 - main_diagonal - row:
                print(Back.GREEN + "{:4}".format(sub_matrix_C[row][column]), end='')
                print(Style.RESET_ALL, end='')
            else:
                print("{:4}".format(sub_matrix_C[row][column]), end='')
        print('')

    print("\nКоличество подходящих чисел в третьей четверти:", counter_numbers_greater_than_K)
    print("Сокращенное прозведение чисел во 2 четверти:", multiplication_of_numbers)

    # Замена в подматрице B первой и третьей четверти: (если выполняется первое условие)
    if counter_numbers_greater_than_K > multiplication_of_numbers:
        flag_swap_matrix_B_1_3 = True
        for row_submatrix_B in range(submatrix_length // 2 + submatrix_length % 2):
            right_column_submatrix_B = submatrix_length - 1
            left_column_submatrix_B = 0
            while right_column_submatrix_B > submatrix_length - 1 - row_submatrix_B - 1 + main_diagonal:
                sub_matrix_B[row_submatrix_B][left_column_submatrix_B], sub_matrix_B[row_submatrix_B][
                    right_column_submatrix_B] \
                    = sub_matrix_B[row_submatrix_B][right_column_submatrix_B], sub_matrix_B[row_submatrix_B][
                    left_column_submatrix_B]
                if submatrix_length - 1 - row_submatrix_B != row_submatrix_B:
                    sub_matrix_B[submatrix_length - 1 - row_submatrix_B][left_column_submatrix_B], \
                    sub_matrix_B[submatrix_length - 1 - row_submatrix_B][right_column_submatrix_B] \
                        = sub_matrix_B[submatrix_length - 1 - row_submatrix_B][right_column_submatrix_B], \
                          sub_matrix_B[submatrix_length - 1 - row_submatrix_B][left_column_submatrix_B]
                right_column_submatrix_B -= 1
                left_column_submatrix_B += 1
        print("\nОтредактированная матрица B: ")
        matrix_output(submatrix_length, sub_matrix_B)
    # Замена подматрицы C и E: (если не выполняется первое условие)
    else:
        flag_swap_matrix_E_and_C = True
        sub_matrix_C, sub_matrix_E = sub_matrix_E, sub_matrix_C
        print("\nОтредактированная матриица C: ")
        matrix_output(submatrix_length, sub_matrix_C)
        print("\nОтредактированная матриица E: ")
        matrix_output(submatrix_length, sub_matrix_E)

    # Создание матрицы F:
    matrix_F = [A[row][0:N] for row in range(N)]
    for row_matrix_F in range(submatrix_length):
        left_column_matrix_F = 0
        right_column_matrix_F = submatrix_length + N % 2
        while left_column_matrix_F < submatrix_length:
            if flag_swap_matrix_B_1_3:  # если выполнилось первое условие
                matrix_F[row_matrix_F][left_column_matrix_F] = sub_matrix_B[row_matrix_F][left_column_matrix_F]
            if flag_swap_matrix_E_and_C:  # если выполнилось второе условие
                matrix_F[row_matrix_F][right_column_matrix_F] = sub_matrix_C[row_matrix_F][left_column_matrix_F]
                matrix_F[submatrix_length + N % 2 + row_matrix_F][right_column_matrix_F] = sub_matrix_E[row_matrix_F][
                    left_column_matrix_F]
            left_column_matrix_F += 1
            right_column_matrix_F += 1
    print("\n Матрица F: ")
    matrix_output(N, matrix_F)

    # Вычисляем выражение:
    # произведение матрцы А на К
    multiplication_matrix_and_argument(N, A, K)
    print("\nПроизведение матрицы А и аргумента К:")
    matrix_output(N, A)

    # произведение матриц A и F
    multiplication_A_and_F = [A[row][0:N] for row in range(N)]
    for row_matrix_A in range(N):
        number_column_matrix_A = 0
        while number_column_matrix_A < N:
            multiplication_of_numbers = 0
            for column_matrix_A in range(N):
                multiplication_of_numbers += (
                            A[row_matrix_A][column_matrix_A] * matrix_F[column_matrix_A][number_column_matrix_A])
            multiplication_A_and_F[row_matrix_A][number_column_matrix_A] = multiplication_of_numbers
            number_column_matrix_A += 1
    print("\nПроизведение матриц A и F: ")
    matrix_output(N, multiplication_A_and_F)

    # транспонирование матрицы F
    start_column_matrix_F = 1
    for row_matrix_F in range(N):
        for current_column_matrix_F in range(start_column_matrix_F, N):
            matrix_F[row_matrix_F][current_column_matrix_F], matrix_F[current_column_matrix_F][row_matrix_F] \
                = matrix_F[current_column_matrix_F][row_matrix_F], matrix_F[row_matrix_F][current_column_matrix_F]
        start_column_matrix_F += 1
    print("\nТранспонированная матрица F: ")
    matrix_output(N, matrix_F)

    # Произведение матрицы F и K
    print("\nПроизведение матрицы F на K: ")
    multiplication_matrix_and_argument(N, matrix_F, K)
    matrix_output(N, matrix_F)

    # Находим выражение
    for row in range(N):
        for column in range(N):
            multiplication_A_and_F[row][column] += matrix_F[row][column]
    print("\nВыражение ((К*A)*F + K* F^T) равно: ")
    matrix_output(N, multiplication_A_and_F)
except Exception as mistake:
    print("Извините. Произошел сбой программы. Ошибка:", mistake)
finish = time.monotonic()
print("\nВремя работы программы:", finish - start, "sec.")
