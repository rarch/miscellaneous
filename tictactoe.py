#! /usr/bin/env python

SIZE = 3
ONE = 1
ZERO = 0
PLAYERS=2
START_BOARD = [['1','2','3'],\
               ['4','5','6'],\
               ['7','8','9']]
X = 'x'
O = 'o'

class Board:
    """class for the tic tac toe board"""
    def __init__(self, board):
        assert isinstance(board,list), 'Board must be list'
        assert len(board) == SIZE, 'Board must have 3 rows'
        for row in board:
            assert isinstance(row,list), 'Each row must be list'
            assert len(row) == SIZE, 'Each row must have 3 vals'
            for val in row:
                assert isinstance(val,str), 'Each val must be str'
                assert len(val) == ONE, 'Each location must have a single char (space is empty)'
        self.myboard = board
    def __str__(self):
        return '\n--+---+--\n'.join(' | '.join(row) for row in self.myboard)
    def setSquare(self,index_plus_one,c):
        assert isinstance(index_plus_one,int), 'Must pass int for square'
        assert index_plus_one>ZERO, 'Must be between 1 and 9 inclusive'
        assert index_plus_one<=SIZE*SIZE, 'Must be between 1 and 9 inclusive'
        assert isinstance(c,str), 'Must pass char'
        assert len(c)==ONE, 'Must pass single char'

        self.myboard[(index_plus_one-1)/SIZE][(index_plus_one-1)%SIZE] = c

    def getVal(self,index_plus_one=None):
        if index_plus_one:
            assert isinstance(index_plus_one,int), 'Must pass int for square'
            assert index_plus_one>ZERO, 'Must be between 1 and 9 inclusive'
            assert index_plus_one<=SIZE*SIZE, 'Must be between 1 and 9 inclusive'
            return self.myboard[(index_plus_one-1)/SIZE][(index_plus_one-1)%SIZE]
        return '0'

    def getRow(self,row):
        assert isinstance(row,int), 'Must pass int for row'
        assert row>=ZERO, 'Must be between 0 and 2 inclusive'
        assert row<SIZE, 'Must be between 0 and 2 inclusive'
        return self.myboard[row]

    def getCol(self,col):
        assert isinstance(col,int), 'Must pass int for col'
        assert col>=ZERO, 'Must be between 0 and 2 inclusive'
        assert col<SIZE, 'Must be between 0 and 2 inclusive'
        return [row[col] for row in self.myboard]

    def getD(self,d):
        assert isinstance(d,int), 'Must pass int for diag'
        assert (d==ZERO) or (d==ONE),'Must be between 0 and 1 inclusive'
        if d == ZERO:
            return [self.myboard[i][i] for i in xrange(0,SIZE)]
        if d == ONE:
            return [self.myboard[SIZE-ONE-i][i] for i in xrange(0,SIZE)]

class Game:
    """class for the tic tac toe game"""
    def __init__(self):
        self.myboard=Board(START_BOARD)
        self.moves=ZERO
        self.players = [Player(X), Player(O)]
        self.lastmove=None
        print '\nPlayers:',', '.join(map((lambda p: str(p.myname)),self.players))

    def announce(self):
        print str(self.players[self.moves%PLAYERS].myname),'to move'
        print 'Board:\n',str(self.myboard)

    def is_over(self):
        if self.lastmove:

            vals_d1 = None
            vals_d2 = None
            #list(set(get row/col/diag )) will return the different values in that row/col/diag
            # if there are multiple different values, for that row/col/diag, there will be a length greater than 1
            # this indicates the game is not over
            # if len==1, then there's only one value, which means all original values have been overwritten by the same player
            # so the game is over
            vals_r = list(set(self.myboard.getRow(self.lastmove[0])))
            vals_c = list(set(self.myboard.getCol(self.lastmove[1])))
            if self.lastmove[0]==self.lastmove[1]:
                vals_d1 = list(set(self.myboard.getD(0)))
                if self.lastmove[0]==2: # middle square, two sets of diagonals
                    vals_d2 = list(set(self.myboard.getD(0)))
            elif self.lastmove[0]+self.lastmove[1] == SIZE-ONE:
                vals_d1 = list(set(self.myboard.getD(0)))
            return (len(vals_r) == ONE) or (len(vals_c) == ONE) or \
                ( vals_d1 and (len(vals_d1) == ONE) ) or ( vals_d2 and (len(vals_d2) == ONE) )

        return False # havent started
    

    def announce_winner(self):
        print str(self.players[(self.moves-1)%PLAYERS].myname),'wins!'


    def play_turn(self):
        val=''
        while (not val.isdigit()):
            myinput = raw_input(str(self.players[self.moves%PLAYERS].myname)+', move where?: ')
            try:
                i=int(myinput)
            except ValueError:
                exit('Pass valid int')
            val = self.myboard.getVal(i)

        self.myboard.setSquare(i,self.players[self.moves%PLAYERS].mychar)
        self.lastmove = [(i-1)/SIZE,(i-1)%SIZE]
        self.moves = self.moves+1

class Player:
    """class for each player"""
    def __init__(self,c):
        assert isinstance(c,str), 'Pass a character'
        assert len(c) == ONE, 'Pass a single character'
        self.mychar = c
        self.promptName()
    def promptName(self):
        self.myname = raw_input('Enter name for Player '+str(self.mychar)+': ')
    # def move(self):

# class ComputerPlayer(Player):
#     def __init__(self, *args, **kwargs):
#         super(self.__class__, self).__init__(*args, **kwargs)

def main():
    tictactoe = Game()

    while (not tictactoe.is_over()):
        tictactoe.announce()
        tictactoe.play_turn()

    print 'Board:\n',str(tictactoe.myboard)
    tictactoe.announce_winner()

if __name__ =='__main__':
    main()

####################################################
# strategy (should be no-lose)

# go first: choose corner
#     if they choose side next to you
#         choose other side next to you
#     if they choose corner next to you
#         choose opposite corner
#     if they choose opposite side
#         choose adjacent corner
#     if they choose middle
#         choose opposite corner

# go second:
#     if they choose corner
#         choose middle
#     if they choose middle
#         play a corner square
#         if the next move does not threaten a win
#             play a corner squre

# if opponent threatens win:
#     prevent win
# if you can win:
#     do it

# threaten win:
# any two in column or row with third in that column or row empty
#     with [x,y] either x or y is constant for these 3 squares
# opposite corners with middle empty or corner and middle with opposite corner empty
#     [0,2] and [2,0] or [0,0] and [2,2] with [1,1] empty, or
#     [1,1] with [0,2] -> [2,0] empty, or
#     [1,1] with [2,0] -> [0,2] empty, or
#     [1,1] with [2,2] -> [0,0] empty, or
#     [1,1] with [0,0] -> [2,2] empty

####################################################

# need to have array of empty squares
# corners [0,2],[2,0],[0,0],[2,2]
# center [1,1]
# sides [0,1],[1,0],[1,2],[2,1]

# prompt for name before init of player -> decided on type of player based on name

# need to define move() for player
#     if name startswith Computer
#          or startswith computer
