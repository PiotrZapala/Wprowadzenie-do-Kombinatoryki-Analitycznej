from random import randint

def fisher_yates_algorithm(n):
    permutation = [i for i in range(1,n+1)]
    for i in range(n-1, 0, -1):
        j = randint(0, i)
        permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation

def permutations_without_fixed_point(permutations):
    n = len(permutations)
    permutations_without_fixed_points = []

    for j in range(n):
        permutation = permutations[j]
        fixed_points = 0
        i = 0

        while fixed_points == 0:
            if permutation[i] == i+1:
                fixed_points += 1
            else:
                if i+1 == len(permutation):
                    permutations_without_fixed_points.append(permutation)
                    break
                else:
                    i += 1

    average_number_of_permutations_without_fixed_points = len(permutations_without_fixed_points)/n
    return average_number_of_permutations_without_fixed_points

def permutations_with_one_fixed_point(permutations):
    n = len(permutations)
    permutations_with_one_fixed_point = []

    for j in range(n):
        permutation = permutations[j]
        fixed_points = 0
        i = 0

        while i < len(permutation):
            if permutation[i] == i + 1:
                fixed_points += 1
            i += 1

        if fixed_points == 1:
            permutations_with_one_fixed_point.append(permutation)

    average_number_of_permutations_with_one_fixed_point = len(permutations_with_one_fixed_point)/n
    return average_number_of_permutations_with_one_fixed_point

def find_cycles_in_permutations(permutations):
    n = len(permutations)
    total_number_of_cycles = 0

    for i in range(n):
        permutation = permutations[i]
        true_false_table = [False for _ in range(len(permutation))]
        number_of_cycles_in_current_permutation = 0

        for j in range(len(permutation)):
            element_from_random_permutation = permutation[j]
            if true_false_table[j] == False:
                true_false_table[j] = True
                while element_from_random_permutation != j+1:
                    true_false_table[element_from_random_permutation - 1] = True
                    element_from_random_permutation = permutation[element_from_random_permutation - 1]
                number_of_cycles_in_current_permutation += 1

        total_number_of_cycles += number_of_cycles_in_current_permutation

    average_of_cycles_per_permutation = total_number_of_cycles / n
    return average_of_cycles_per_permutation

def main1():
    num_simulations = int(input("Podaj liczbę symulacji: "))
    permutation_size = int(input("Podaj wielkość permutacji: "))
    permutations = []
    for _ in range(num_simulations):
        permutation = fisher_yates_algorithm(permutation_size)
        permutations.append(permutation)
    result1 = permutations_without_fixed_point(permutations)
    print(f"Permutacje bez punktu stałego: {result1}")
    result2 = permutations_with_one_fixed_point(permutations)
    print(f"Permutacje z jednym punktem stałym: {result2}")
    result3 = find_cycles_in_permutations(permutations)
    print(f"Cykle w permutacjach: {result3}")
    
def main2():
    num_simulations = int(input("Podaj liczbę symulacji: "))
    permutation_size = int(input("Podaj wielkość permutacji: "))
    permutations = []
    for _ in range(num_simulations):
        permutation = fisher_yates_algorithm(permutation_size)
        permutations.append(permutation)
    result1 = permutations_without_fixed_point(permutations)
    print(f"Permutacje bez punktu stałego: {result1}")
    result2 = permutations_with_one_fixed_point(permutations)
    print(f"Permutacje z jednym punktem stałym: {result2}")
    result3 = find_cycles_in_permutations(permutations)
    print(f"Cykle w permutacjach: {result3}")

if __name__ == "__main__":
    main1()
    main2()