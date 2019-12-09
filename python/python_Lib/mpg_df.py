class Car:
    
    def __init__(self, m1,dis,y,cyl,trans,drv,cty,hwy,fl,cl):
        self.cCom = m1
        self.cMod = m2
        self.cDis = int(dis)
        self.cYear = int(y)
        self.cCyl = int(cyl)
        self.cTrans = trans
        self.cDrv = drv
        self.cCty = int(cty)
        self.cHwy = int(hwy)
        self.cFl = fl
        self.cClass = cl
        
    
    def print_test(self):
        print("제조사 : {}, 연비 : {}".format(self.cCom,self.cCty))
    