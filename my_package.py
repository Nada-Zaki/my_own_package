
class my_own_package():
    
    def bulk_rename(self, filePath, fileName, fileType):
        import os
        self.count=1
        for name in os.listdir(os.chdir(filePath)):
            self.dst = fileName+"_{}.".format(self.count)+fileType
            self.src = name 
            os.rename(self.src, self.dst)
            self.count+=1
        os.chdir('../')


    def find_index(self, st, ch):
        self.index = []
        for i,char in enumerate(st):
            if (char == ch):
                self.index.append(i)

        return self.index    


    def splitting(self, st,ch):
            self.index = []
            for i,char in enumerate(st):
                if (char == ch):
                    self.index.append(i)
            self.index.reverse()
            self.index.append(-1)
            self.index.reverse()

            self.res=[]
            for a in range(len(self.index)):
                if a  == len(self.index)-1:
                    self.res.append(st[self.index[a]+1:])
                    break
                else :
                    self.res.append(st[self.index[a]+1:self.index[a+1]])
                

            return self.res
