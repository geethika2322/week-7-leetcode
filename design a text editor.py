class TextEditor:

    def __init__(self):
        self.st=""
        self.cur=0

    def addText(self, text: str) -> None:
        self.st=self.st[:self.cur]+text+self.st[self.cur:]
        self.cur+=len(text)

    def deleteText(self, k: int) -> int:
        if(self.cur>k):
            self.st=self.st[:self.cur-k]+self.st[self.cur:]
            self.cur-=k
            return(k)
        else:
            self.st=self.st[self.cur:]
            z=self.cur
            self.cur=0
            return(z)
    def cursorLeft(self, k: int) -> str:
        if(self.cur>k):
            self.cur-=k
        else:
            self.cur=0
        z=self.st[:self.cur][-10:]
        return(z)

    def cursorRight(self, k: int) -> str:
        if(len(self.st)-self.cur>k):
            z=self.st[self.cur:self.cur+k]
            self.cur+=k
        else:
            self.cur=len(self.st)
        z=self.st[:self.cur][-10:]
        return(z)
