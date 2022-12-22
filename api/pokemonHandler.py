from flask_restful import Resource, reqparse
import Mon
import json
from flask import request





class PokemonHandler(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("poolSize", type=int)
        parser.add_argument("mutationRate", type=int)
        parser.add_argument("fitnessFunction", type=str)
        parser.add_argument("numGens", type=int)

        args = parser.parse_args()

        teams = Mon.run_control(
            args['numGens'],args["poolSize"], args["mutationRate"], args["fitnessFunction"]
        )

        best_teams = []
        for team in teams:
            mons = []
            for mon in team:
                mon_json = mon.toJson()
                mons.append(mon_json)
            best_teams.append(mons)

        return best_teams
    
   
    def get(self):
      
      
      id = int(request.args.get("id"))

       

      # args = parser.parse_args
      # print(args)


      mon = Mon.PokemonArray[id-1]
      print(mon.name)

      return  mon.toJson()
      