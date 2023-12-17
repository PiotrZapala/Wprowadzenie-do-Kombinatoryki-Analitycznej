from sympy import sympify

def calculate_inverse_of_function(expression, n):
    b = [0] * (n + 1)
    b[0] = 1

    for i in range(1, n + 1):
        sum_ak_b = 0
        for k in range(1, i + 1):
            a_k = float(sympify(expression).subs('n', k))
            sum_ak_b += a_k * b[i - k]
        b[i] = -(1 / sympify(expression).subs('n', 0)) * sum_ak_b

    return b

def main():
    func = input("Podaj wzór funkcji: ")
    count_of_elements = int(input("Podaj liczbę wyrazów do obliczenia: "))
    result = calculate_inverse_of_function(func, count_of_elements)
    print(result)

if __name__ == "__main__":
    main()