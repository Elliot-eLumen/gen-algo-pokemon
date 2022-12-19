
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

def new_gen_stat(parent_arr, mutation_rate):
  
    new_gen = [[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}]]
    new_gen[0] = parent_arr[0]
    for x in range(1,20):
      for y in range(6):
        new_gen[x][y] = parent_arr[random.randint(0,4)][y]
    
    for x in range(mutation_rate):
      new_gen[18][random.randint(0,5)] = Mon.mutate()
    for x in range(mutation_rate):
      new_gen[19][random.randint(0,5)] = Mon.mutate()


def find_parents_stat(team_pool):
  
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


def run_stat(generations, init_pop, mutation_rate):
    pop = init_pop
    for x in range(generations):
    
      find_parents_stat(pop)
      pop = new_gen_stat(parents, mutation_rate)
      
    find_parents_stat(pop)
    
    return parents[0]


