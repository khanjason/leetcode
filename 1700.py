class Solution:
    def covtohash(self,li1,li2):
        s1=''.join(str(x) for x in li1)
        s2=''.join(str(x) for x in li2)
        ss=s1+'|'+s2
        return ss
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        sett=set()
        while sandwiches:
            if i>len(sandwiches)-1:
                i=0
            
            sand=sandwiches[0]
            sandwiches=sandwiches[1:]
            if students[0]==sand:
                students=students[1:]
            else:
                sandwiches=[sand]+sandwiches
                s=students[0]
                students=students[1:]
                students.append(s)
            
            if self.covtohash(sandwiches,students) not in sett:
                sett.add(self.covtohash(sandwiches,students))
            else:
                return len(students)
            i=i+1
        return len(students)
