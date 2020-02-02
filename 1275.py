class Solution:
    def detect(self,bigger,short):
        c=0
        for item in bigger:
            if item in short:
                c=c+1
        
        if c>=3:
            return True
    def checkemp(self,board):
        for row in board:
            for thing in row:
                if thing =='':
                    return True
        return False
    
    
    def display(self,board):
        for t in board:
            print(t)
            print()
    
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        board=[['','',''],['','',''],['','','']]
        winning=[[[0,0],[0,1],[0,2]],[[0,0],[1,0],[2,0]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,2],[1,2],[2,2]],[[0,1],[1,1],[2,1]],[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]
        boo=True
        crosses=[]
        noughts=[]
        for thing in moves:
            
                if boo==True:
                    board[thing[0]][thing[1]]='X'
                    crosses.append([thing[0],thing[1]])
                    boo=False
                elif boo==False:
                    board[thing[0]][thing[1]]='O'
                    noughts.append([thing[0],thing[1]])
                    
                    boo=True
        for item in winning:
            
            if self.detect(item,crosses):
                
                return('A')
            if self.detect(item,noughts):
                
                return('B')
        
                
        self.display(board)
        if self.checkemp(board):
            return ("Pending")
        return("Draw")      
