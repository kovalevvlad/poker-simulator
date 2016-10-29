from flask import jsonify, request, abort

from util import card_list_from_comma_separated_string
from . import app
from poker.simulator import probability_of_winning


@app.route('/')
def index():
    return "Hello, Poker World!"


@app.route('/estimate', methods=['POST'])
def estimate():
    if any(key not in request.form for key in ['my_hand', 'opponent_count', 'table']):
        return abort(400)
    else:
        try:
            my_hand = card_list_from_comma_separated_string(request.values['my_hand'])
            table_cards = card_list_from_comma_separated_string(request.values['table'])
            opponent_count = int(request.form['opponent_count'])
            return jsonify(probability=probability_of_winning(my_hand, opponent_count, table_cards))
        except ValueError:
            abort(400)
