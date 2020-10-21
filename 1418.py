class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        #order[i][0]=customer
        #order[i][1]=tablenumber
        #order[i][2]=food
        #displaytable columns : menu, rows: table numbers , stores orders
        tab={} #key : table number, lists of numbers
        displaytable=[["Table"]]#,"Beef Burrito","Ceviche","Fried Chicken","Water"]]
        tmptable=[]
        for o in orders:
            if o[2] not in tmptable:
                tmptable.append(o[2])
        displaytable[0]=displaytable[0]+sorted(tmptable)
        tables=[]
        foods=[]
        for table in orders:
            if table[1] not in tab.keys():
                tab[table[1]]=[]
            tab[table[1]]=tab[table[1]]+[table[2]]
        for key,v in tab.items():
            tmp=[key]
            for n in range(1,len(displaytable[0])):
                tmp.append(0)
            for item in v:
                for i in range(len(displaytable[0])):
                    if item==displaytable[0][i]:#"Beef Burrito":
                        tmp[i]=tmp[i]+1
                
            for t in range(len(tmp)):
                tmp[t]=str(tmp[t])
            foods.append(tmp)
        for k in tab.keys():
            tables.append(int(k))
        tables=sorted(tables)
        for ki in tables:
            displaytable.append([str(ki)])
        
        for li in range(len(displaytable)):
            for food in foods:
                if displaytable[li][0]==food[0]:
                    displaytable[li]=displaytable[li]+food[1:]
        return displaytable
