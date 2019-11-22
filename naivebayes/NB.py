import re


class NaiveBayes:
    def __init__(self):
        self.vectorFeature1={}
        self.vectorFeature2={}
        self.label1Count=0
        self.label2Count=0
        self.feature1Count=0
        self.feature2Count=0
        self.feature1Probability=0
        self.feature2Probability=0
        self.rePattern=re.compile('[.?!~`@^#,\-:$;<>_\[\]=+|0-9%"/\s]+')
        self.feature1TrainPath="D:\\fallingspace\\machinelearning\\data\\suda\\train_positive_review.txt"
        self.feature2TrainPath="D:\\fallingspace\\machinelearning\\data\\suda\\train_negative_review.txt"
        self.feature1DevelopPath="D:\\fallingspace\\machinelearning\\data\\suda\\develop_positive_review.txt"
        self.feature2DevelopPath="D:\\fallingspace\\machinelearning\\data\\suda\\develop_negative_review.txt"

    def train(self):
        # 读取Feature1的样本
        with open(self.feature1TrainPath,"r",encoding="utf-8") as fp:
            lines=fp.readlines()
            self.label1Count=len(lines)
            for  item in lines:
                item=re.sub(self.rePattern," ",item)
                words=item.split()
                for word in words:
                    self.vectorFeature1[word]=self.vectorFeature1.get(word,0)+1
        
        # 读取Feature2的样本
        with open(self.feature2TrainPath,"r",encoding="utf-8") as fp:
            lines=fp.readlines()
            self.label2Count=len(lines)
            for  item in lines:
                item=re.sub(self.rePattern," ",item)
                words=item.split()
                for word in words:
                    self.vectorFeature2[word]=self.vectorFeature2.get(word,0)+1
        
        # 计算先验概率以及相应的条件概率
        self.feature1Count= sum([n for _,n in self.vectorFeature1.items()])
        self.feature2Count= sum([n for _,n in self.vectorFeature2.items()])

        labelSum=self.label1Count+self.label2Count
        self.feature1Probability=self.label1Count/labelSum
        self.feature2Probability=self.label2Count/labelSum

        