import random
import Stat
import ChampCov


parents = [
    [{}, {}, {}, {}, {}, {}],
    [{}, {}, {}, {}, {}, {}],
    [{}, {}, {}, {}, {}, {}],
    [{}, {}, {}, {}, {}, {}],
    [{}, {}, {}, {}, {}, {}],
]


def fitness_func_combo(team):
    print("here")
    print(team)
    print("here")
    stat = Stat.fitness_func_stat(team) / (3800 * 2)
    # coverage = fitness_func_cov(team)/36
    effective = ChampCov.fitness_func_se(team) / (24 * 2)
    fitness = stat + effective
    # print(fitness)
    return fitness


def new_gen_combo(parent_arr, mutation_rate, size, mutate):

    new_gen = []
    for x in range(size):
        new_gen.append([{}, {}, {}, {}, {}, {}])
    new_gen[0] = parent_arr[0]
    for x in range(1, size):
        for y in range(6):
            new_gen[x][y] = parent_arr[random.randint(0, 4)][y]

    mutations = size - mutation_rate
    for x in range(mutations, size):
        new_gen[x][random.randint(0, 5)] = mutate()
    return new_gen


def find_parents_combo(team_pool):

    one = None
    two = None
    three = None
    four = None
    five = None
    one_fit = 0

    two_fit = 0

    three_fit = 0

    four_fit = 0

    five_fit = 0
    for team in team_pool:
        team_fit = fitness_func_combo(team)
        if team_fit > five_fit:
            if team_fit > four_fit:
                if team_fit > three_fit:
                    if team_fit > two_fit:
                        if team_fit > one_fit:
                            one_fit = team_fit
                            five = four
                            four = three
                            three = two
                            two = one
                            one = team

                        else:
                            two_fit = team_fit
                            five = four
                            four = three
                            three = two
                            two = team
                    else:
                        three_fit = team_fit
                        five = four
                        four = three
                        three = team
                else:
                    four_fit = team_fit
                    five = four
                    four = team
            else:
                five_fit = team_fit
                five = team
    if one:
        parents[0] = one
    if two:
        parents[1] = two
    if three:
        parents[2] = three
    if four:
        parents[3] = four
    if five:
        parents[4] = five
    return


def run_combo(generations, init_pop, mutation_rate, size, mut_func):
    pop = init_pop
    best_team_per_gen = []
    for x in range(generations):

        find_parents_combo(pop)
        best_team_per_gen.append(parents[0])
        pop = new_gen_combo(parents, mutation_rate, size, mut_func)

    find_parents_combo(pop)
    best_team_per_gen.append(parents[0])

    return best_team_per_gen


def initialize(generations, init_pop, pool_size, mutation, mutate):

    return run_combo(generations, init_pop, mutation, pool_size, mutate)
