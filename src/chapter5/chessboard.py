valid = {
    '1h': 'bking', 
    '6c': 'wqueen', 
    '2g': 'bbishop', 
    '5h': 'bqueen', 
    '3e': 'wking'
}

too_much_kings = {
    '1h': 'bking',
    '3e': 'wking',
    '4e': 'wking',
}

too_much_pawns = {
    '1h': 'bking',
    '3e': 'wking',
    '5a': 'wpawn',
    '5b': 'wpawn',
    '5c': 'wpawn',
    '5d': 'wpawn',
    '5e': 'wpawn',
    '5f': 'wpawn',
    '5g': 'wpawn',
    '5h': 'wpawn',
    '6h': 'wpawn',
}

invalid_position = {
    '1h': 'bking', 
    '3e': 'wking',
    '9z': 'bpawn',
}

too_much_white_pieces = {
    '1h': 'bking', 
    '3e': 'wking',
    '5a': 'wpawn',
    '5b': 'wpawn',
    '5c': 'wpawn',
    '5d': 'wpawn',
    '5e': 'wpawn',
    '5f': 'wpawn',
    '5g': 'wpawn',
    '5h': 'wpawn',
    '2a': 'wqueen',
    '3a': 'wbishop',
    '4a': 'wbishop',
    '6a': 'wknight',
    '7a': 'wknight',
    '8a': 'wrook',
    '1a': 'wrook',
    '2b': 'wqueen',
}

too_much_black_pieces = {
    '1h': 'bking', 
    '3e': 'wking',
    '5a': 'bpawn',
    '5b': 'bpawn',
    '5c': 'bpawn',
    '5d': 'bpawn',
    '5e': 'bpawn',
    '5f': 'bpawn',
    '5g': 'bpawn',
    '5h': 'bpawn',
    '2a': 'bqueen',
    '3a': 'bbishop',
    '4a': 'bbishop',
    '6a': 'bknight',
    '7a': 'bknight',
    '8a': 'brook',
    '1a': 'brook',
    '2b': 'bqueen',
}

def is_valid_chessboard(board):
    kings = check_kings(board)
    pawns = check_pawns(board)
    positions = check_positions(board)
    numbers = check_pieces_number(board)
    return kings and pawns and positions and numbers

def check_kings(board):
    pieces = list(board.values())
    kings = ['bking', 'wking']
    for king in kings:
        if pieces.count(king) != 1:
            print(f"Error: got {pieces.count(king)} {king}, but wanted 1")
            return False
    return True

def check_pawns(board):
    pieces = list(board.values())
    pawns = ['bpawn', 'wpawn']
    for pawn in pawns:
        if pieces.count(pawn) > 8:
            print(f"Error: got {pieces.count(pawn)} {pawn}, but has to be equal or less than 8")
            return False
    return True

def posible_positions():
    letters = 'abcdefgh'
    numbers = '12345678'
    return [n + l for l in letters for n in numbers]

def check_positions(board):
    positions = list(board.keys())
    posible = posible_positions()
    for p in positions:
        if p not in posible:
            print(f"Error: {p} not a valid position!")
            return False
    return True

def check_pieces_number(board):
    pieces = list(board.values())
    black = 0
    white = 0
    for p in pieces:
        if p[0] == 'b': 
            black += 1
        elif p[0] == 'w': 
            white += 1
        else: 
            print(f"Error: Invalid piece name {p}")
            return False
    if black > 16:
        print(f"Error: black has more than 16 pieces")
        return False
    if white > 16:
        print(f"Error: white has more than 16 pieces")
        return False
    return True

print(is_valid_chessboard(valid))
print(is_valid_chessboard(too_much_kings))
print(is_valid_chessboard(too_much_pawns))
print(is_valid_chessboard(invalid_position))
print(is_valid_chessboard(too_much_white_pieces))
print(is_valid_chessboard(too_much_black_pieces))
