
import Mon
import random




parents = [[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}]]

def fitness_func_cov(team):
  types = []
  for mon in team:
    for type in mon.typing:
      types.append(type)
  fitness = list(set(types))
  return len(fitness)



def new_gen_cov(parent_arr, mutation_rate, size):
  
    new_gen = []
    for x in range(size):
      new_gen.append([{},{},{},{},{},{}])
    new_gen[0] = parent_arr[0]
    for x in range(1,size):
      for y in range(6):
        new_gen[x][y] = parent_arr[random.randint(0,4)][y]
    
    mutations = size - mutation_rate
    for x in range(mutations, size):
      new_gen[x][random.randint(0,5)] = Mon.mutate()


def find_parents_cov(team_pool):
  
    one=None
    two=None
    three =None
    four=None
    five=None
    one_fit = 0
    
    two_fit = 0
    
    three_fit = 0
    
    four_fit = 0
    
    five_fit = 0
    for team in team_pool:
      team_fit = fitness_func_cov(team)
      if team_fit > five_fit:
        if team_fit > four_fit:
          if team_fit > three_fit:
            if team_fit > two_fit:
              if team_fit > one_fit:
                one_fit = team_fit
                one = team
              else:
                two_fit = team_fit
                two = team
            else:
              three_fit = team_fit
              three = team
          else:
            four_fit=team_fit
            four = team
        else:
          five_fit=team_fit
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


def run_cov(generations, init_pop, mutation_rate, size):
    pop = init_pop
    for x in range(generations):
    
      find_parents_cov(pop)
      pop = new_gen_cov(parents, mutation_rate, size)
      
    find_parents_cov(pop)
    
    return parents[0]

def initialize(generations, pool_size, mutation):
  if pool_size == 5:
    init_pop = Mon.randomTeamsFive()
    pop_size=5
  if pool_size == 10:
    init_pop = Mon.randomTeamsTen()
    pop_size=10
  if pool_size == 20:
    init_pop = Mon.randomTeamsTwenty()
    pop_size = 20
  run_cov(generations, init_pop, mutation, pop_size)





