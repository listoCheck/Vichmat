import math
import numpy as np
import matplotlib.pyplot as plt


def equation_1(x):
    return -1.38 * x ** 3 - 5.42 * x ** 2 + 2.57 * x + 10.95


def equation_2(x):
    return x ** 3 - 1.89 * x ** 2 - 2 * x + 1.76


def equation_3(x):
    return 2 * x ** 3 + 3.41 * x ** 2 - 23.74 * x + 2.95


def derivative_1(x):
    return -4.14 * x ** 2 - 10.84 * x + 2.57


def derivative_2(x):
    return 3 * x ** 2 - 3.78 * x - 2


def derivative_3(x):
    return 6 * x ** 2 + 6.82 * x - 23.74


def plot_function(f, a, b):
    x = np.linspace(a, b, 400)
    y = [f(xi) for xi in x]
    plt.plot(x, y, label='Функция')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


def bisection_method(f, a, b, eps):
    if f(a) * f(b) > 0:
        print("Ошибка: на данном интервале нет корня или их несколько.")
        return
    plot_function(f, a, b)
    n = 0
    while abs(b - a) > eps:
        x = (a + b) / 2
        if f(x) == 0:
            break
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        n += 1
        print(f"Найденный корень: {x}, Значение функции в корне: {f(x)}, Число итераций: {n}")

    return


def newton_method(f, df, x0, eps):
    n = 0
    while True:
        x = x0 - f(x0)/df(x0)
        print(f"Найденный корень: {x}, Значение функции в x: {f(x)}, Значение производной функции в x: {df(x)}, Число итераций: {n}")
        if (x - x0) <= eps or abs(f(x)/df(x)) <= eps or abs(f(x)) <= eps:
            break
        n += 1
        x0 = x


def simple_iteration_method(f, x0, tol):
    print("Метод простой итерации заглушка")
    return None


def get_input_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
            return [float(value.strip()) for value in data]
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return None


def get_user_input():
    choice = input("Введите имя файла для загрузки данных или оставьте пустым для ручного ввода: ").strip()
    if choice:
        return get_input_from_file(choice)
    else:
        return [
            float(input("Введите левую границу интервала: ")),
            float(input("Введите правую границу интервала: ")),
            float(input("Введите погрешность вычисления: "))
        ]


def main():
    while True:
        print("Выберите тип программы:")
        print("1: Нелинейное уравнение")
        print("2: Система нелинейных уравнений")
        print("3: Выход")
        prog_type = input("Введите номер типа: ")
        if prog_type == "3":
            break

        print("Выберите уравнение:")
        print("1: -1.38*x^3 - 5.42*x^2 + 2.57*x + 10.95")
        print("2: x^3 - 1.89*x^2 - 2*x + 1.76")
        print("3: 2*x^3 + 3.41*x^2 - 23.74*x + 2.95")
        eq_choice = input("Введите номер уравнения: ")

        equations = {"1": equation_1, "2": equation_2, "3": equation_3}
        derivatives = {"1": derivative_1, "2": derivative_2, "3": derivative_3}
        f = equations.get(eq_choice)
        df = derivatives.get(eq_choice)

        if not f:
            print("Некорректный выбор уравнения.")
            continue

        print("Выберите метод:")
        print("1: Метод половинного деления")
        print("2: Метод Ньютона")
        print("3: Метод простой итерации")
        method_choice = input("Введите номер метода: ")

        input_data = get_user_input()
        if not input_data:
            continue

        if method_choice == "1":
            bisection_method(f, input_data[0], input_data[1], input_data[2])
        elif method_choice == "2":
            newton_method(f, df, input_data[0], input_data[2])
        elif method_choice == "3":
            simple_iteration_method(f, input_data[0], input_data[2])
        else:
            print("Некорректный выбор метода.")
            continue

        again = input("Еще раз? [y/n]: ")
        if again.lower() != "y":
            break


main()
