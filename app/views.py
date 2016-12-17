from flask import jsonify, request, abort

from util import card_list_from_comma_separated_string
from . import app
from poker.simulator import probability_of_winning


@app.route('/')
def index():
    return "Hello, Poker World!"


@app.route('/estimate', methods=['GET'])
def estimate():
    essential_fields = ['my_hand', 'opponent_count', 'table']
    if any(key not in request.args for key in essential_fields):
        return abort(400, "one of the following fields has not been specified - {}".format(','.join(essential_fields)))
    else:
        try:
            my_hand = card_list_from_comma_separated_string(request.args.get('my_hand'))
            table_cards = card_list_from_comma_separated_string(request.args.get('table'))
            opponent_count = int(request.args.get('opponent_count'))
            return jsonify(probability=probability_of_winning(my_hand, opponent_count, table_cards))
        except ValueError as e:
            abort(400, str(e))
