
import random
class Mon():

  def __init__(self, name, stats, typing):
    self.name = name
    self.stats = stats
    self.typing = typing


PokemonArray = [Mon("bulbasaur", 318,["grass", "poison"]),Mon("ivysaur", 405,["grass", "poison"]),
                Mon("venusaur", 525,["grass", "poison"]), Mon("charmander", 309,["fire"]),
                Mon("charmeleon", 405, ["fire"]),Mon("charizard", 534, ["fire","flying"]),
                Mon("squirtle", 314, ["water"]), Mon("wartortle", 405, ["water"]),
                Mon("blastoise", 530, ["water"]), Mon("caterpie", 195, ["bug"]),
                Mon("metapod", 205, ["bug"]), Mon("butterfree", 395, ["bug", "flying"]),
                Mon("weedle", 195, ["bug","poison"]),Mon("kakuna",205,["bug","poison"]),
                Mon("beedrill",395,["bug","poison"]),Mon("pidgey",251,["normal","flying"]),
                Mon("pidgeotto", 349,["normal", "flying"]),Mon("pidgeot", 479,["normal","flying"]),
                Mon("rattata",253,["normal"]),Mon("raticate",413,["normal"]),
                Mon("spearow", 262,["normal","flying"]), Mon("fearow",442,["normal","flying"]),
                Mon("ekans",288,["poison"]),Mon("arbok",448,["poison"]),
                Mon("pikachu",320,["electric"]),Mon("raichu",485,["electric"]),
                Mon("sandshrew",300,["ground"]),Mon("sandslash",450,["ground"]),
                Mon("nidoran",275,["poison"]),Mon("nidorina",365,["poison"]),
                Mon("nidoqueen",505,["poison","ground"]),Mon("nidoran",273,["poison"]),
                Mon("nidorino",365,["poison"]),Mon("nidoking",505,["poison","ground"]),
                Mon("clefairy",323,["normal"]),Mon("clefable",483,["normal"]),
                Mon("vulpix",299,["fire"]),Mon("ninetales",505,["fire"]),
                Mon("jigglypuff",270,["normal"]),Mon("wigglytuff",435,["normal"]),
                Mon("zubat",245,["poison","flying"]),Mon("golbat",455,["poison","flying"]),
                Mon("oddish",320,["grass","poison"]),Mon("gloom",395,["grass","poison"]),
                Mon("vileplume",490,["grass","poison"]),Mon("paras",285,["bug","grass"]),
                Mon("parasect",405,["bug","grass"]),Mon("venonat",305,["bug","poison"]),
                Mon("venomoth",450,["bug","poison"]),Mon("diglett",265,["ground"]),
                Mon("dugtrio",425,["ground"]),Mon("meowth",290,["normal"]),
                Mon("persian",440,["normal"]),Mon("psyduck",320,["water"]),
                Mon("golduck",500,["water"]),Mon("mankey",305,["fighting"]),
                Mon("primeape",455,["fighting"]),Mon("growlithe",350,["fire"]),
                Mon("arcanine",555,["fire"]),Mon("poliwag",300,["water"]),
                Mon("poliwhirl",385,["water"]),Mon("poliwrath",510,["water","fighting"]),
                Mon("abra",310,["psychic"]),Mon("kadabra",400,["psychic"]),
                Mon("alakazam",500,["psychic"]),Mon("machop",305,["fighting"]),
                Mon("machoke",405,["fighting"]),Mon("machamp",505,["fighting"]),
                Mon("bellsprout",300,["grass","poison"]),Mon("weepinbell",390,["grass","poison"]),
                Mon("victreebel",490,["grass","poison"]),Mon("tentacool",335,["water","poison"]),
                Mon("tentacruel",515,["water","poison"]),Mon("geodude",300,["rock","ground"]),
                Mon("graveler",390,["rock","ground"]),Mon("golem",495,["rock","ground"]),
                Mon("ponyta",410,["fire"]),Mon("rapidash",500,["fire"]),
                Mon("slowpoke",315,["water","psychic"]),Mon("slowbro",490,["water","psychic"]),
                Mon("megnemite",325,["electric"]),Mon("magneton",465,["electric"]),
                Mon("farfetch'd",377,["normal","flying"]),Mon("doduo",310,["normal","flying"]),
                Mon("dodrio",470,["normal","flying"]),Mon("seel",325,["water"]),
                Mon("dewgong",475,["water","ice"]),Mon("grimer",325,["poison"]),
                Mon("muk",500,["poison"]),Mon("shelder",305,["water"]),
                Mon("cloyster",525,["water","ice"]),Mon("gastly",310,["ghost","poison"]),
                Mon("haunter",405,["ghost","poison"]),Mon("gengar",500,["ghost","poison"]),
                Mon("onix",385,["rock","ground"]),Mon("drowzee",328,["psychic"]),
                Mon("hypno",483,["psychic"]),Mon("krabby",325,["water"]),
                Mon("kingler",475,["water"]),Mon("volorb",330,["electric"]),
                Mon("electrode",490,["electric"]),Mon("exeggcute",325,["grass","psychic"]),
                Mon("exeggutor",530,["grass","psychic"]),Mon("cubone",320,["ground"]),
                Mon("marowak",475,["ground"]),Mon("hitmonlee",455,["fighting"]),
                Mon("hitmonchan",455,["fighting"]),Mon("lickitung",385,["normal"]),
                Mon("koffing",340,["poison"]),Mon("weezing",490,["poison"]),
                Mon("rhyhorn",345,["rock","ground"]),Mon("rhydon",485,["rock","ground"]),
                Mon("chansey",450,["normal"]),Mon("tangela",435,["grass"]),
                Mon("kangaskhan",490,["normal"]),Mon("horsea",295,["water"]),
                Mon("seadra",440,["water"]),Mon("goldeen",320,["water"]),
                Mon("seaking",450,["water"]),Mon("staryu",340,["water"]),
                Mon("starmie",520,["water","psychic"]),Mon("mr.mime",460,["psychic"]),
                Mon("scyther",500,["bug","flying"]),Mon("jynx",455,["ice","psychic"]),
                Mon("electabuzz",490,["electric"]),Mon("magmar",495,["fire"]),
                Mon("pinsir",500,["bug"]),Mon("tauros",490,["normal"]),
                Mon("magikarp",200,["water"]),Mon("gyarados",540,["water","flying"]),
                Mon("lapras",535,["water","ice"]),Mon("ditto",288,["normal"]),
                Mon("eevee",325,["normal"]),Mon("vaporeon",525,["water"]),
                Mon("jolteon",525,["electric"]),Mon("flareon",525,["fire"]),
                Mon("porygon",395,["normal"]),Mon("omanyte",355,["rock","water"]),
                Mon("omastar",495,["rock","water"]),Mon("kabuto",355,["rock","water"]),
                Mon("kabutops",495,["rock","water"]),Mon("aerodactyl",515,["rock","flying"]),
                Mon("snorlax",540,["normal"]),Mon("articuno",580,["ice","flying"]),
                Mon("zapdos",580,["electric","flying"]),Mon("moltres",580,["fire","flying"]),
                Mon("dratini",300,["dragon"]),Mon("dragonair",420,["dragon"]),
                Mon("dragonite",600,["dragon","flying"]),Mon("mewtwo",680,["psychic"]),
                Mon("mew",600,["psychic"])]


def randomTeamsFive():
  teamArray=[{},{},{},{},{}]
  team0=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team1=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team2=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team3=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team4=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  teamArray[0]=team0
  teamArray[1]=team1
  teamArray[2]=team2
  teamArray[3]=team3
  teamArray[4]=team4
  return teamArray

def randomTeamsTen():
  teamArray=[{},{},{},{},{},{},{},{},{},{}]
  team0=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team1=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team2=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team3=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team4=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team5=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team6=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team7=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team8=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team9=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  teamArray[0]=team0
  teamArray[1]=team1
  teamArray[2]=team2
  teamArray[3]=team3
  teamArray[4]=team4
  teamArray[5]=team5
  teamArray[6]=team6
  teamArray[7]=team7
  teamArray[8]=team8
  teamArray[9]=team9
  return teamArray

def randomTeamsTwenty():
  teamArray=[{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
  team0=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team1=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team2=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team3=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team4=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team5=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team6=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team7=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team8=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team9=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team10=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team11=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team12=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team13=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team14=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team15=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team16=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team17=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team18=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  team19=[random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray),random.choice(PokemonArray)]
  teamArray[0]=team0
  teamArray[1]=team1
  teamArray[2]=team2
  teamArray[3]=team3
  teamArray[4]=team4
  teamArray[5]=team5
  teamArray[6]=team6
  teamArray[7]=team7
  teamArray[8]=team8
  teamArray[9]=team9
  teamArray[10]=team10
  teamArray[11]=team11
  teamArray[12]=team12
  teamArray[13]=team13
  teamArray[14]=team14
  teamArray[15]=team15
  teamArray[16]=team16
  teamArray[17]=team17
  teamArray[18]=team18
  teamArray[19]=team19
  return teamArray

parents = [[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}]]
def mutate():
  return random.choice(PokemonArray)


def fitness_func_stat(team):
  total = 0
  for mon in team:
    total += mon.stats
  
  return total


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
    team_fit = fitness_func_combo(team)
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

def new_gen_stat(parent_arr, mutation_rate):
  
  new_gen = [[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}]]
  new_gen[0] = parent_arr[0]
  for x in range(1,20):
    for y in range(6):
      new_gen[x][y] = parent_arr[random.randint(0,4)][y]
  
  for x in range(mutation_rate):
    new_gen[18][random.randint(0,5)] = mutate()
  for x in range(mutation_rate):
    new_gen[19][random.randint(0,5)] = mutate()
  # print("--------")
  # for z in range(10):
  #   print("000000000000")
  #   tot = 0
  #   for mon in new_gen[z]:
  #     print(mon.name + ": %s" %mon.stats)
  #     tot += mon.stats
  #   print(tot)
  #   print("00000000000")
  # print("----------")
    
  return new_gen

def run_stat(generations, init_pop, mutation_rate):
  pop = init_pop
  for x in range(generations):
    #print("______ %s _______" %x)
    find_parents_stat(pop)
    pop = new_gen_stat(parents, mutation_rate)
    
  find_parents_stat(pop)
  
  return parents[0]

def fitness_func_cov(team):
  types = []
  for mon in team:
    for type in mon.typing:
      types.append(type)
  fitness = list(set(types))
  return len(fitness)


def fitness_func_se(team):
  types = []
  for mon in team:
    for type in mon.typing:
      types.append(type)
  fitness = list(set(types))
  score = 0
  for type in fitness:
    if type == "water":
      score += 3
    if type == "ice":
      score += 3
    if type == "grass":
      score += 3
    if type == "bug":
      score += 3
    if type == 'ground':
      score += 2
    if type == 'rock':
      score += 2
    if type == 'electric':
      score += 2
    if type == 'ghost':
      score += 2
    
    if type == "fighting":
      score+=1
    if type == "fire":
      score+=1
    if type == "poison":
      score+=1
    if type == "flying":
      score+=1
    
  return score

def fitness_func_combo(team):
  stat = fitness_func_stat(team)/(3800*2)
  #coverage = fitness_func_cov(team)/36
  effective = fitness_func_se(team)/(24*2)
  fitness = stat + effective
  #print(fitness)
  return fitness

# avg = 0
# avg_fit = 0
# y = 0

# for x in range(1000):
#   test = run_stat(500,randomTeamsTwenty(),2)
#   total = 0
#   avg_fit+=(fitness_func_cov(test)/12)
#   for mon in test:
#     print(mon.name + ": %s" %mon.stats)
#     total += mon.stats
#   print("totals stats: %s" %total)
#   avg += total
#   y += fitness_func_cov(test)

# test = run_stat(500,randomTeamsTwenty(),2)
# total = 0

# for mon in test:
#   print(mon.name + ": %s" %mon.stats)
#   total += mon.stats


# print(avg_fit/10)

# print(avg/1000)
# y = y / 1000
# print(y)








          




# worst = 5000
# best = 0
# count = 1
# bestt = {}

# worstt = {}

# arr = randomTeamsTwenty()
# index = 1
  
  
# for team in arr:
#     total = 0
#     print("team %s ---------" %index)
#     for mon in team:
#       print(mon.name + ": %s"  %mon.stats)
#       total += mon.stats
#     print("team stats: %s"  %total)
#     print("--------")
#     index += 1
#     if total > best:
#       best = total
#       bestt = team
#     if total < worst:
#       worst = total
#       worstt = team

# print("best")
# for mon in bestt:
#     print(mon.name)
# print(best)
# print("-----------")
# print("worst")
# for mon in worstt:
#     print(mon.name)
# print(worst)
# count += 1

# print(best)
# print(worst)
# print(count)


team1 = run_stat(5,randomTeamsTwenty(),2)
team1fit = fitness_func_combo(team1)
team1fitscore = team1fit/4080

team2 = run_stat(20,randomTeamsTwenty(),2)
team2fit = fitness_func_combo(team2)
team2fitscore = team2fit/4080

team3 = run_stat(500,randomTeamsTwenty(),2)
team3fit = fitness_func_combo(team3)
team3fitscore = team3fit/4080


for mon in team1:
  print(mon.name)
print(team1fit)
#print(team1fitscore)

for mon in team2:
  print(mon.name)
print(team2fit)
#print(team2fitscore)

for mon in team3:
  print(mon.name)
print(team3fit)
#print(team3fitscore)