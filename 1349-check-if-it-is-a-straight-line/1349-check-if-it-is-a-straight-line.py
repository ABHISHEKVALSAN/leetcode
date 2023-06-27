class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xc = set()
        yc = set()
        n = len(coordinates)
        p1 = coordinates[0]
        xc.add(p1[0])
        yc.add(p1[1])

        for p in coordinates[1:]:
            xc.add(p[0])
            yc.add(p[1])    
            if p[0]!=p1[0]:
                p2=p    
        if len(xc)==1 or len(yc)==1:
            return True 
        if len(xc)!=n or len(yc)!=n:
            return False
        m = (p1[1]-p2[1])/(p1[0]-p2[0])
        c = p1[1] - m*p1[0]

        for p in coordinates:
            x = p[0]
            y = p[1]
            if m*x+c!=y:
                return False
        return True