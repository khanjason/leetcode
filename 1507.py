class Solution:
    def reformatDate(self, date: str) -> str:
        li=date.split(' ')
        dic={"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        day=li[0][:-2]
        year=li[2]
        mon=dic[li[1]]
        if len(day)==1:
            day='0'+day
        return year+'-'+mon+'-'+day
