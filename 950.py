class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        '''while deck!=[]:
            top=deck[0]
            deck=deck[1:len(deck)]
            if deck!=[]:
                nex=deck[0]
                deck=deck[1:len(deck)]
                deck.append(nex)'''
     

        deck=sorted(deck)        
        res=[]
        while deck!=[]:
            if res:
                p=res.pop()
                res=[p]+res
            t=deck.pop()
            res=[t]+res
        return res
    
    
