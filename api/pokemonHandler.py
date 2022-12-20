from flask_restful import Resource, reqparse
import Mon
import json


class PokemonHandler(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("poolSize", type=str)
        parser.add_argument("mutationRate", type=str)
        parser.add_argument("fitnessFunction", type=str)

        args = parser.parse_args()

        teams = Mon.run_control(args)

        best_teams = []
        for team in teams:
            mons = []
            for mon in team:
                mon_json = mon.toJson()
                mons.append(mon_json)
            best_teams.append(mons)

        return best_teams
