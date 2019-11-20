import re
import math
import time

class naive:
    
    def __init__(self):
        self.V_p = {}
        self.V_n = {}
        self.pos = 0
        self.neg = 0
        self.r = re.compile('[.?!~`@^#,\-:$;<>_\[\]=+|0-9%"/\s]+')
       
    def train(self):
        with open("D:\\fallingspace\\machinelearning\\data\\suda\\train_positive_review.txt","r",encoding="utf-8") as fp:
            lines = fp.readlines()
            self.pos = len(lines)
            for i in lines:
                i = re.sub(self.r,' ',i)
                words = i.split()
                for m in words:
                    self.V_p[m] = self.V_p.get(m,0) + 1

        with open("D:\\fallingspace\\machinelearning\\data\\suda\\train_negative_review.txt","r",encoding="utf-8") as fp:
            lines = fp.readlines()
            self.neg = len(lines)
            for i in lines:
                i = re.sub(self.r,' ',i)
                words = i.split()
                for m in words:
                    self.V_n[m] = self.V_n.get(m,0) + 1

        # self.V_p = {i:j for i,j in self.V_p.items() if j > 1}
        # self.V_n = {i: j for i, j in self.V_n.items() if j > 1}

        self.count_p = sum([n for _,n in self.V_p.items()])
        self.count_n = sum([n for _,n in self.V_n.items()])

        self.p_n = self.neg / ( self.pos + self.neg )
        self.p_p = self.pos / ( self.pos + self.neg )

    def dev(self):        
        count = 0
        p,n = self.calculate("D:\\fallingspace\\machinelearning\\data\\suda\\develop_positive_review.txt")
        count += p
        print(p,n)
        p,n = self.calculate("D:\\fallingspace\\machinelearning\\data\\suda\\develop_negative_review.txt")
        count += n
        print(p,n)
        print("acc:%f" % (count/400))

    def test(self,filename):
        p,n = self.calculate(filename,True)
        print(p,n)

    def calculate(self,filename,isresult=False):
        p = n = 0
        index = 1
        with open(filename,"r",encoding="utf-8") as fp:
            lines = fp.readlines()
        if isresult:
            f = open("naive.txt","w",encoding="utf-8")
        for i in lines:
            if isresult:
                i = i.split("||")[1]
            i = re.sub(self.r,' ',i)
            prob_n = sum([math.log10((self.V_n.get(m,0) + 1) / (self.count_n + len(self.V_n) + 1)) for m in i.split()]) * self.p_n
            prob_p = sum([math.log10((self.V_p.get(m,0) + 1) / (self.count_p + len(self.V_p) + 1)) for m in i.split()]) * self.p_p
            if prob_p >= prob_n:
                p += 1
                if isresult:
                    f.write("%d\t1\n" % index)
            else:
                n += 1
                if isresult:
                    f.write("%d\t-1\n" % index)
            index += 1
        if isresult:
            f.close()        
        return p,n

if __name__ == "__main__":


    time_start=time.time()

    # filename = "test_review.txt"
    x = naive()
    x.train()
    x.dev()
    # x.test(filename)
    time_end=time.time()
    print('totally cost',time_end-time_start)

    




