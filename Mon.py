
import random
import Stat
import Combo
import ChampCov
import GenCov
import sys
class Mon():

  def __init__(self, name, stats, typing, id):
    self.name = name
    self.stats = stats
    self.typing = typing
    self.id = id


PokemonArray = [Mon("bulbasaur", 318,["grass", "poison"],1),Mon("ivysaur", 405,["grass", "poison"],2),
                Mon("venusaur", 525,["grass", "poison"],3), Mon("charmander", 309,["fire"],4),
                Mon("charmeleon", 405, ["fire"],5),Mon("charizard", 534, ["fire","flying"],6),
                Mon("squirtle", 314, ["water"],7), Mon("wartortle", 405, ["water"],8),
                Mon("blastoise", 530, ["water"],9), Mon("caterpie", 195, ["bug"],10),
                Mon("metapod", 205, ["bug"],11), Mon("butterfree", 395, ["bug", "flying"],12),
                Mon("weedle", 195, ["bug","poison"],13),Mon("kakuna",205,["bug","poison"],14),
                Mon("beedrill",395,["bug","poison"],15),Mon("pidgey",251,["normal","flying"],16),
                Mon("pidgeotto", 349,["normal", "flying"],17),Mon("pidgeot", 479,["normal","flying"],18),
                Mon("rattata",253,["normal"],19),Mon("raticate",413,["normal"],20),
                Mon("spearow", 262,["normal","flying"],21), Mon("fearow",442,["normal","flying"],22),
                Mon("ekans",288,["poison"],23),Mon("arbok",448,["poison"],24),
                Mon("pikachu",320,["electric"],25),Mon("raichu",485,["electric"],26),
                Mon("sandshrew",300,["ground"],27),Mon("sandslash",450,["ground"],28),
                Mon("nidoran",275,["poison"],29),Mon("nidorina",365,["poison"],30),
                Mon("nidoqueen",505,["poison","ground"],31),Mon("nidoran",273,["poison"],32),
                Mon("nidorino",365,["poison"],33),Mon("nidoking",505,["poison","ground"],34),
                Mon("clefairy",323,["normal"],35),Mon("clefable",483,["normal"],36),
                Mon("vulpix",299,["fire"],37),Mon("ninetales",505,["fire"],38),
                Mon("jigglypuff",270,["normal"],39),Mon("wigglytuff",435,["normal"],40),
                Mon("zubat",245,["poison","flying"],41),Mon("golbat",455,["poison","flying"],42),
                Mon("oddish",320,["grass","poison"],43),Mon("gloom",395,["grass","poison"],44),
                Mon("vileplume",490,["grass","poison"],45),Mon("paras",285,["bug","grass"],46),
                Mon("parasect",405,["bug","grass"],47),Mon("venonat",305,["bug","poison"],48),
                Mon("venomoth",450,["bug","poison"],49),Mon("diglett",265,["ground"],50),
                Mon("dugtrio",425,["ground"],51),Mon("meowth",290,["normal"],52),
                Mon("persian",440,["normal"],53),Mon("psyduck",320,["water"],54),
                Mon("golduck",500,["water"],55),Mon("mankey",305,["fighting"],56),
                Mon("primeape",455,["fighting"],57),Mon("growlithe",350,["fire"],58),
                Mon("arcanine",555,["fire"],59),Mon("poliwag",300,["water"],60),
                Mon("poliwhirl",385,["water"],61),Mon("poliwrath",510,["water","fighting"],62),
                Mon("abra",310,["psychic"],63),Mon("kadabra",400,["psychic"],64),
                Mon("alakazam",500,["psychic"],65),Mon("machop",305,["fighting"],66),
                Mon("machoke",405,["fighting"],67),Mon("machamp",505,["fighting"],68),
                Mon("bellsprout",300,["grass","poison"],69),Mon("weepinbell",390,["grass","poison"],70),
                Mon("victreebel",490,["grass","poison"],71),Mon("tentacool",335,["water","poison"],72),
                Mon("tentacruel",515,["water","poison"],73),Mon("geodude",300,["rock","ground"],74),
                Mon("graveler",390,["rock","ground"],75),Mon("golem",495,["rock","ground"],76),
                Mon("ponyta",410,["fire"],77),Mon("rapidash",500,["fire"],78),
                Mon("slowpoke",315,["water","psychic"],79),Mon("slowbro",490,["water","psychic"],80),
                Mon("megnemite",325,["electric"],81),Mon("magneton",465,["electric"],82),
                Mon("farfetch'd",377,["normal","flying"],83),Mon("doduo",310,["normal","flying"],84),
                Mon("dodrio",470,["normal","flying"],85),Mon("seel",325,["water"],86),
                Mon("dewgong",475,["water","ice"],87),Mon("grimer",325,["poison"],88),
                Mon("muk",500,["poison"],89),Mon("shelder",305,["water"],90),
                Mon("cloyster",525,["water","ice"],91),Mon("gastly",310,["ghost","poison"],92),
                Mon("haunter",405,["ghost","poison"],93),Mon("gengar",500,["ghost","poison"],94),
                Mon("onix",385,["rock","ground"],95),Mon("drowzee",328,["psychic"],96),
                Mon("hypno",483,["psychic"],97),Mon("krabby",325,["water"],98),
                Mon("kingler",475,["water"],99),Mon("volorb",330,["electric"],100),
                Mon("electrode",490,["electric"],101),Mon("exeggcute",325,["grass","psychic"],102),
                Mon("exeggutor",530,["grass","psychic"],103),Mon("cubone",320,["ground"],104),
                Mon("marowak",475,["ground"],105),Mon("hitmonlee",455,["fighting"],106),
                Mon("hitmonchan",455,["fighting"],107),Mon("lickitung",385,["normal"],108),
                Mon("koffing",340,["poison"],109),Mon("weezing",490,["poison"],110),
                Mon("rhyhorn",345,["rock","ground"],111),Mon("rhydon",485,["rock","ground"],112),
                Mon("chansey",450,["normal"],113),Mon("tangela",435,["grass"],114),
                Mon("kangaskhan",490,["normal"],115),Mon("horsea",295,["water"],116),
                Mon("seadra",440,["water"],117),Mon("goldeen",320,["water"],118),
                Mon("seaking",450,["water"],119),Mon("staryu",340,["water"],120),
                Mon("starmie",520,["water","psychic"],121),Mon("mr.mime",460,["psychic"],122),
                Mon("scyther",500,["bug","flying"],123),Mon("jynx",455,["ice","psychic"],124),
                Mon("electabuzz",490,["electric"],125),Mon("magmar",495,["fire"],126),
                Mon("pinsir",500,["bug"],127),Mon("tauros",490,["normal"],128),
                Mon("magikarp",200,["water"],129),Mon("gyarados",540,["water","flying"],130),
                Mon("lapras",535,["water","ice"],131),Mon("ditto",288,["normal"],132),
                Mon("eevee",325,["normal"],133),Mon("vaporeon",525,["water"],134),
                Mon("jolteon",525,["electric"],135),Mon("flareon",525,["fire"],136),
                Mon("porygon",395,["normal"],137),Mon("omanyte",355,["rock","water"],138),
                Mon("omastar",495,["rock","water"],139),Mon("kabuto",355,["rock","water"],140),
                Mon("kabutops",495,["rock","water"],141),Mon("aerodactyl",515,["rock","flying"],142),
                Mon("snorlax",540,["normal"],143),Mon("articuno",580,["ice","flying"],144),
                Mon("zapdos",580,["electric","flying"],145),Mon("moltres",580,["fire","flying"],146),
                Mon("dratini",300,["dragon"],147),Mon("dragonair",420,["dragon"],148),
                Mon("dragonite",600,["dragon","flying"],149),Mon("mewtwo",680,["psychic"],150),
                Mon("mew",600,["psychic"],151)]


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


def mutate():
  return random.choice(PokemonArray)

def main():
  setupObj = {}
  args = sys.argv[:1]
  if len(args) > 1 :
    print("too many arguments")
  else:
    setupObj= args[0]
  if setupObj.fitness == '-stat':
    Stat.initialize(setupObj.generations, setupObj.size, setupObj.mutations)
  if setupObj.fitness == '-gencov':
    GenCov.initialize(setupObj.generations, setupObj.size, setupObj.mutations)
  if setupObj.fitness == '-champcov':
    ChampCov.initialize(setupObj.generations, setupObj.size, setupObj.mutations)
  if setupObj.fitness == '-combo':
    Combo.initialize(setupObj.generations, setupObj.size, setupObj.mutations)



# def fitness_func_stat(team):
#   total = 0
#   for mon in team:
#     total += mon.stats
  
#   return total


# def find_parents_stat(team_pool):
  
#   one=None
#   two=None
#   three =None
#   four=None
#   five=None
#   one_fit = 0
  
#   two_fit = 0
  
#   three_fit = 0
  
#   four_fit = 0
  
#   five_fit = 0
#   for team in team_pool:
#     team_fit = fitness_func_combo(team)
#     if team_fit > five_fit:
#       if team_fit > four_fit:
#         if team_fit > three_fit:
#           if team_fit > two_fit:
#             if team_fit > one_fit:
#               one_fit = team_fit
#               one = team
#             else:
#               two_fit = team_fit
#               two = team
#           else:
#             three_fit = team_fit
#             three = team
#         else:
#           four_fit=team_fit
#           four = team
#       else:
#         five_fit=team_fit
#         five = team
#   if one:
#     parents[0] = one 
#   if two:
#     parents[1] = two
#   if three:
#     parents[2] = three
#   if four:
#     parents[3] = four
#   if five:
#     parents[4] = five
#   return

# def new_gen_stat(parent_arr, mutation_rate):
  
#   new_gen = [[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}],[{},{},{},{},{},{}]]
#   new_gen[0] = parent_arr[0]
#   for x in range(1,20):
#     for y in range(6):
#       new_gen[x][y] = parent_arr[random.randint(0,4)][y]
  
#   for x in range(mutation_rate):
#     new_gen[18][random.randint(0,5)] = mutate()
#   for x in range(mutation_rate):
#     new_gen[19][random.randint(0,5)] = mutate()
  
    
#   return new_gen

# def run_stat(generations, init_pop, mutation_rate):
#   pop = init_pop
#   for x in range(generations):
   
#     find_parents_stat(pop)
#     pop = new_gen_stat(parents, mutation_rate)
    
#   find_parents_stat(pop)
  
#   return parents[0]

# def fitness_func_cov(team):
#   types = []
#   for mon in team:
#     for type in mon.typing:
#       types.append(type)
#   fitness = list(set(types))
#   return len(fitness)


# def fitness_func_se(team):
#   types = []
#   for mon in team:
#     for type in mon.typing:
#       types.append(type)
#   fitness = list(set(types))
#   score = 0
#   for type in fitness:
#     if type == "water":
#       score += 3
#     if type == "ice":
#       score += 3
#     if type == "grass":
#       score += 3
#     if type == "bug":
#       score += 3
#     if type == 'ground':
#       score += 2
#     if type == 'rock':
#       score += 2
#     if type == 'electric':
#       score += 2
#     if type == 'ghost':
#       score += 2
    
#     if type == "fighting":
#       score+=1
#     if type == "fire":
#       score+=1
#     if type == "poison":
#       score+=1
#     if type == "flying":
#       score+=1
    
#   return score

# def fitness_func_combo(team):
#   stat = fitness_func_stat(team)/(3800*2)
#   #coverage = fitness_func_cov(team)/36
#   effective = fitness_func_se(team)/(24*2)
#   fitness = stat + effective
#   #print(fitness)
#   return fitness

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


# team1 = run_stat(5,randomTeamsTwenty(),2)
# team1fit = fitness_func_combo(team1)
# team1fitscore = team1fit/4080

# team2 = run_stat(20,randomTeamsTwenty(),2)
# team2fit = fitness_func_combo(team2)
# team2fitscore = team2fit/4080

# team3 = run_stat(500,randomTeamsTwenty(),2)
# team3fit = fitness_func_combo(team3)
# team3fitscore = team3fit/4080


# for mon in team1:
#   print(mon.name)
# print(team1fit)
#print(team1fitscore)

# for mon in team2:
#   print(mon.name)
# print(team2fit)
#print(team2fitscore)

# for mon in team3:
#   print(mon.name)
# print(team3fit)
#print(team3fitscore)