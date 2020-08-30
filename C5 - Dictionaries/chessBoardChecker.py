def is_valid_chessboard(chessboard):

    keys = list(chessboard.keys())
    values = list(chessboard.values())

    print(values)

    outcome_data = {'outcome': 'Pass',
                    'message': 'There were no errors found in the chessboard arrangement.'}

    bking_count = 0
    wking_count = 0
    white_count = 0
    black_count = 0
    wpawn_count = values.count('wpawn')
    bpawn_count = values.count('bpawn')

    for v in values:
        if v == 'bking':
            bking_count = bking_count + 1
        if v == 'wking':
            wking_count = wking_count + 1
        if v.startswith('b'):
            black_count = black_count + 1
        if v.startswith('w'):
            white_count = white_count + 1

    if bking_count > 1:
        outcome_data['outcome'] = 'Fail'
        outcome_data['message'] = 'Error: more than one black king'
        return(outcome_data)
    if wking_count > 1:
        outcome_data['outcome'] = 'Fail'
        outcome_data['message'] = 'Error: more than one white king'
        return(outcome_data)
    if black_count > 16:
        outcome_data['outcome'] = 'Fail'
        outcome_data['message'] = 'Error: more than 16 black pieces'
        return(outcome_data)
    if white_count > 16:
        outcome_data['outcome'] = 'Fail'
        outcome_data['message'] = 'Error: more than 16 white pieces'
        return(outcome_data)
    if bpawn_count > 8:
        outcome_data['outcome'] = 'Fail'
        outcome_data['message'] = 'Error: more than 8 black pawns'
        return(outcome_data)
    if wpawn_count > 8:
        outcome_data['outcome'] = 'Fail'
        outcome_data['message'] = 'Error: more than 8 white pawns'
        return(outcome_data)
    for k in keys:
        if int(k[0]) > 8:
            outcome_data['outcome'] = 'Fail'
            outcome_data['message'] = 'Error: illegal y position'
            return(outcome_data)
        if k[1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            outcome_data['outcome'] = 'Fail'
            outcome_data['message'] = 'Error: illegal x position'
            return(outcome_data)

    return(outcome_data)


sample_chessboard = {'1h': 'bking', '6c': 'wqueen',
                     '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3p': 'wpawn'}

sample_results = is_valid_chessboard(sample_chessboard)

print('Outcome: ' + sample_results['outcome'])
print('Message: ' + sample_results['message'])
