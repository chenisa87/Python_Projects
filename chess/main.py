"""
---------------------------------------------------
|    | a  | b  | c  | d  | e  | f  | g  | h  |    |
---------------------------------------------------
| 8  | BR | BN | BB | BQ | BK | BB | BN | BR | 8  |
---------------------------------------------------
| 7  | BP | BP | BP | BP | BP | BP | BP | BP | 7  |
---------------------------------------------------
| 6  |    |    |    |    |    |    |    |    | 6  |
---------------------------------------------------
| 5  |    |    |    |    |    |    |    |    | 5  |
---------------------------------------------------
| 4  |    |    |    |    |    |    |    |    | 4  |
---------------------------------------------------
| 3  |    |    |    |    |    |    |    |    | 3  |
---------------------------------------------------
| 2  | WP | WP | WP | WP | WP | WP | WP | WP | 2  |
---------------------------------------------------
| 1  | WR | WN | WB | WQ | WK | WB | WN | WR | 1  |
---------------------------------------------------
|    | a  | b  | c  | d  | e  | f  | g  | h  |    |
---------------------------------------------------
"""
import re

class Chess:
    def __init__(self):
        self.board = self.make_new_board()
        self.loc = {
            "a8":(0,0),"b8":(0,1),"c8":(0,2),"d8":(0,3),"e8":(0,4),"f8":(0,5),"g8":(0,6),"h8":(0,7),
            "a7":(1,0),"b7":(1,1),"c7":(1,2),"d7":(1,3),"e7":(1,4),"f7":(1,5),"g7":(1,6),"h7":(1,7),
            "a6":(2,0),"b6":(2,1),"c6":(2,2),"d6":(2,3),"e6":(2,4),"f6":(2,5),"g6":(2,6),"h6":(2,7),
            "a5":(3,0),"b5":(3,1),"c5":(3,2),"d5":(3,3),"e5":(3,4),"f5":(3,5),"g5":(3,6),"h5":(3,7),
            "a4":(4,0),"b4":(4,1),"c4":(4,2),"d4":(4,3),"e4":(4,4),"f4":(4,5),"g4":(4,6),"h4":(4,7),
            "a3":(5,0),"b3":(5,1),"c3":(5,2),"d3":(5,3),"e3":(5,4),"f3":(5,5),"g3":(5,6),"h3":(5,7),
            "a2":(6,0),"b2":(6,1),"c2":(6,2),"d2":(6,3),"e2":(6,4),"f2":(6,5),"g2":(6,6),"h2":(6,7),
            "a1":(7,0),"b1":(7,1),"c1":(7,2),"d1":(7,3),"e1":(7,4),"f1":(7,5),"g1":(7,6),"h1":(7,7)
        }
        self.white_team = ["WR","WN","WB","WQ","WK","WP"]
        self.black_team = ["BR","BN","BB","BQ","BK","BP"]

    def make_new_board(self):
        board = [['--' for _ in range(8)] for _ in range(8)]
        board[0] = ["BR","BN","BB","BQ","BK","BB","BN","BR"]
        board[1] = ["BP","BP","BP","BP","BP","BP","BP","BP"]
        
        board[6] = ["WP","WP","WP","WP","WP","WP","WP","WP"]
        board[7] = ["WR","WN","WB","WQ","WK","WB","WN","WR"]
        return board

    def check_is_good_move(self,ox,oy,nx,ny):
        return False
    
    def move_white_chess(self):
        print("")
        move = input("Please input loc , loc:")
        print("")
        loc1 , loc2 = re.split(r"[,\s]+",move)
        print("")
        ox , oy = self.loc[loc1]
        nx , ny = self.loc[loc2]
        if self.check_is_good_move(ox,oy,nx,ny):
            self.board[nx][ny] = self.board[ox][oy]
            self.board[ox][oy] = "--"
        else:
            print("Please try again.")
            self.move_white_chess()

    
    def move_black_chess(self):
        print("")
        move = input("Please input loc , loc:")
        print("")
        loc1 , loc2 = re.split(r"[,\s]+",move)
        print("")
        ox , oy = self.loc[loc1]
        nx , ny = self.loc[loc2]
        self.board[nx][ny] = self.board[ox][oy]
        self.board[ox][oy] = "--"

    def __str__(self):
        board = self.board
        string_rep =  "---------------------------------------------------\n"
        string_rep += "|    | a  | b  | c  | d  | e  | f  | g  | h  |    |\n"
        string_rep += "---------------------------------------------------\n"
        i = 8
        for row in board:
            string_rep += f"| {i}  |"
            for piece in row:
                string_rep += f" {piece} |"
            string_rep += f" {i}  |\n"
            string_rep += "---------------------------------------------------\n"
            i -= 1
        string_rep += "|    | a  | b  | c  | d  | e  | f  | g  | h  |    |\n"
        string_rep += "---------------------------------------------------\n"   
        return string_rep
    
if __name__ == "__main__":
    chess = Chess()
    
    while True:
        print(chess)
        chess.move_white_chess()
        print(chess)
        chess.move_black_chess()
