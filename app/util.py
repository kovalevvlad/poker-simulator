def check_argument(argument_is_valid, error_message):
    if not argument_is_valid:
        raise ValueError(error_message)


def card_list_from_comma_separated_string(string):
    from poker.card import Card
    card_strs = [] if string == "" else string.split(',')
    cards = []
    for card_str in card_strs:
        if len(card_str) != 2:
            raise ValueError('{} is not a valid representation of a card'.format(card_str))
        cards.append(Card(card_str[0], card_str[1]))
    return cards
