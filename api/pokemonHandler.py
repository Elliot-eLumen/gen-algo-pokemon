from flask_restful import Resource, reqparse
import Mon


class PokemonHandler(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("poolSize", type=str)
        parser.add_argument("mutationRate", type=str)
        parser.add_argument("fitnessFunction", type=str)

        args = parser.parse_args()

        return Mon.run_control(args)
