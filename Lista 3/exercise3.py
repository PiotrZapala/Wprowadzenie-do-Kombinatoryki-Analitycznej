from random import randint
import matplotlib.pyplot as plt

def fisher_yates_algorithm(n):
    permutation = [i for i in range(1,n+1)]
    for i in range(n-1, 0, -1):
        j = randint(0, i)
        permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation

def count_average_number_of_fixed_points(permutations):
    total_number_of_fixed_points = 0
    for permutation in permutations:
        number_of_fixed_points = 0
        for i in range(len(permutation)):
            if i + 1 == permutation[i]:
                number_of_fixed_points += 1    
        total_number_of_fixed_points += number_of_fixed_points
    return total_number_of_fixed_points/len(permutations)

def main():
    n = 101
    permutations = [[] for _ in range(n)]
    average_number_of_fixed_points = []
    for i in range(1, n):
        for _ in range(1, 10000):
            permutations[i-1].append(fisher_yates_algorithm(i))
    for j in range(len(permutations)-1):
        average_number_of_fixed_points.append(count_average_number_of_fixed_points(permutations[j]))

    plt.plot(range(1, n), average_number_of_fixed_points, marker='o')
    plt.title('Średnia liczba punktów stałych w zależności od rozmiaru permutacji')
    plt.xlabel('Rozmiar permutacji')
    plt.ylabel('Średnia liczba punktów stałych')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

#X_{i} = {1 jeśli i jest punktem stałym permutacji, 0 w przeciwnym przypadku}
#Średnia liczba punktów stałych (1/n)* /sum from i=1 to n (E(X_{i}))
#Ponieważ każda zmienna losowa X_{i} ma wartość oczekiwaną równą prawdopodobieństwu
#E(X_{i} = P(i jest punktem stałym), prawdopodobieństwo że i jest punktem stałym wynosi 1/n
#Zatem mamy, że średnia liczba punktów stałych = (1/n)* /sum from i = 1 to n (1/n) = (1/n)*n = 1