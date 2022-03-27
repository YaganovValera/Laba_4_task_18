import random
import time

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
    A = []
    for row in range(N):                                      # Заполняем матрицу А случайными числами от -10 до 10 (включительно)
        subMatrix = []
        for column in range(N):
            subMatrix.append(random.randint(-10, 10))
        A.append(subMatrix)
    print(" Матрица А: ")
    matrix_output(N, A)

    # Создание подматриц B, C, D и E
    submatrix_length = N//2                                                                             #Длина подматрицы

    sub_matrix_B = [A[row][0:submatrix_length] for row in range(submatrix_length + 1)]                  # Создание подматрицы В
    sub_matrix_C = [A[row][submatrix_length + N % 2: N] for row in range(submatrix_length + 1)]         # Создание подматрицы С
    sub_matrix_D = [A[row][0: submatrix_length] for row in range(submatrix_length + N % 2, N)]          # Создание подматрицы D
    sub_matrix_E = [A[row][submatrix_length + N % 2: N] for row in range(submatrix_length + N % 2, N)]  # Создание подматрицы E
    print("\n Матрица B: ")
    matrix_output(submatrix_length, sub_matrix_B)
    print("\n Матрица C: ")
    matrix_output(submatrix_length, sub_matrix_C)
    print("\n Матрица D: ")
    matrix_output(submatrix_length, sub_matrix_D)
    print("\n Матрица E: ")
    matrix_output(submatrix_length, sub_matrix_E)

                                                # Формирование матрицы F
    main_diagonal = 1                                                                          # 1 - если главная диагональ не входит в диапазон; 0 - если входит
    # Подсчет чисел, которые стоят в нечетных столбцах матрицы С и больше К, в области 3
    counter_numbers_greater_than_K = 0                                                         # Количество подходящих чисел
    for row_submatrix_C in range(submatrix_length//2 + submatrix_length % 2):                 # Цикл перебора строк до середины
        column_submatrix_C = submatrix_length - 1                                             # индекс последнего столбца (начало третий четверти)
        while column_submatrix_C > submatrix_length - 1 - row_submatrix_C - 1 + main_diagonal:# Перебираем числа в строке, до главной диагонали
            if (column_submatrix_C+1) % 2 != 0:                                               # проверка на четность столбца
                if sub_matrix_C[row_submatrix_C][column_submatrix_C] > K:                     # прверка подходящих чисел в верхних строках
                    counter_numbers_greater_than_K += 1
                if sub_matrix_C[submatrix_length - 1 - row_submatrix_C][column_submatrix_C] > K:    # проверка подходящих чисел в нижних строках (зеркальны верхним)
                    if submatrix_length - 1 - row_submatrix_C != row_submatrix_C:                   # отбрасываем скрещивающие строки
                        counter_numbers_greater_than_K += 1
            else:                                                                             # переход на нечетные столбцы, чтобы пропускать четные
                column_submatrix_C += 1
            column_submatrix_C -= 2

    # Произведение чисел в области 2, которые стоят в нечетных столбцах матрицы С
    multiplication_of_numbers = 1                                                                                  # произведение подходящих чисел
    start_left_column_C = main_diagonal                                                                            # столбцы слева
    start_right_column_C = submatrix_length - 1 - main_diagonal                                                    # столбцы справа
    for row_submatrix_C in range(0, submatrix_length // 2 + submatrix_length % 2 - main_diagonal + 1, 2):          # Цикл прохода по четным строкам до середины (т.к нужна 2 четверть)
        current_left_column_C = start_left_column_C
        current_right_column_C = start_right_column_C
        while current_left_column_C <= submatrix_length // 2 - int(submatrix_length % 2 == 0):                     # Цикл для прохода чисел с двух концов строки (начиная с главной диагонали) для ускорения программы
            if abs(multiplication_of_numbers) > counter_numbers_greater_than_K:                                    # прекращаем домножать на реальные числа матрицы, если их произведение уже превысило сумму чисел из 3 четверти
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

    print("\nКоличество подходящих чисел в третьей четверти:", counter_numbers_greater_than_K)
    print("Прозведение чисел во 2 четверти:", multiplication_of_numbers)

    # Замена в подматрице B первой и третьей четверти: (если выполняется первое условие)
    if counter_numbers_greater_than_K > multiplication_of_numbers:
        flag_swap_matrix_B_1_3 = True
        for row_submatrix_B in range(submatrix_length // 2 + submatrix_length % 2):                         # перебор строк
            right_column_submatrix_B = submatrix_length - 1                                                 # начало 3 четверти
            left_column_submatrix_B = 0                                                                     # начало 1 четверти
            while right_column_submatrix_B > submatrix_length - 1 - row_submatrix_B - 1 + main_diagonal:    # перебор чисел в строке до главной диагонали
                sub_matrix_B[row_submatrix_B][left_column_submatrix_B], sub_matrix_B[row_submatrix_B][right_column_submatrix_B] \
                    = sub_matrix_B[row_submatrix_B][right_column_submatrix_B], sub_matrix_B[row_submatrix_B][left_column_submatrix_B]       # Симметричная замена 1 и 3 четверти
                if submatrix_length - 1 - row_submatrix_B != row_submatrix_B:
                    sub_matrix_B[submatrix_length - 1 - row_submatrix_B][left_column_submatrix_B], sub_matrix_B[submatrix_length - 1 - row_submatrix_B][right_column_submatrix_B] \
                        = sub_matrix_B[submatrix_length - 1 - row_submatrix_B][right_column_submatrix_B], sub_matrix_B[submatrix_length - 1 - row_submatrix_B][left_column_submatrix_B]
                right_column_submatrix_B -= 1
                left_column_submatrix_B += 1
        print("\nОтредактированная матрица B: ")
        matrix_output(submatrix_length, sub_matrix_B)
    # Замена подматрицы C и E: (если выполняется второе условие)
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
            if flag_swap_matrix_B_1_3:                                                          # если выполнилось первое условие
                matrix_F[row_matrix_F][left_column_matrix_F] = sub_matrix_B[row_matrix_F][left_column_matrix_F]
            if flag_swap_matrix_E_and_C:                                                        # если выполнилось второе условие
                matrix_F[row_matrix_F][right_column_matrix_F] = sub_matrix_C[row_matrix_F][left_column_matrix_F]
                matrix_F[submatrix_length + submatrix_length % 2 + row_matrix_F][right_column_matrix_F] = sub_matrix_E[row_matrix_F][left_column_matrix_F]
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
                 multiplication_of_numbers += (A[row_matrix_A][column_matrix_A] * matrix_F[column_matrix_A][number_column_matrix_A])
            multiplication_A_and_F[row_matrix_A][number_column_matrix_A] = multiplication_of_numbers
            number_column_matrix_A += 1
    print("\nПроизведение матриц A и F: ")
    matrix_output(N, multiplication_A_and_F)

    #транспонирование матрицы F
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