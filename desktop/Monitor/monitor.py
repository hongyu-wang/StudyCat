from win32gui import GetForegroundWindow
from win32process import GetWindowThreadProcessId
from psutil import Process, NoSuchProcess
import datetime

class Monitor:
    def __init__(self, listFile):
        self.categories = ["Very Unproductive", "Unproductive", "Neutral",
                           "Productive", "Very Productive"]
        self.record = [None] * 5
        self.active = None
        self.threadID = None
        self.procName = None
        self.prevStamp = None
        self.processLists = []
        self.processLists = listFile
        self.usageInfo = {}
        self.modifier = [-5, -2, 1, 2, 5]
        self.affection = 50

    def getAffection(self):
        print(self.record)
        for i in range(0, len(self.record)):
            self.affection += (self.record[i].seconds)/10 * self.modifier[i] if self.record[i] != None else 0
        self.affection = 0 if self.affection < 0 else self.affection
        self.affection = 100 if self.affection > 100 else self.affection
        self.record = [None] * 5
        return self.affection

    def pollMostUsed(self):

        if len(self.usageInfo) == 0:
            return ""

        mostUsed = max(self.usageInfo, key=self.usageInfo.get)
        self.usageInfo = {}
        return mostUsed

    def pollLatestProcess(self):

        for processes in self.processLists:
                if self.procName.name() in processes:
                    if self.record[self.processLists.index(processes)] == None:
                        self.record[self.processLists.index(processes)] = \
                            datetime.datetime.now() - self.prevStamp
                    else:
                        self.record[self.processLists.index(processes)] += \
                            datetime.datetime.now() - self.prevStamp
        self.initVars()
        if self.procName in self.usageInfo:
            self.usageInfo[self.procName.name()] += 1
        else:
            self.usageInfo[self.procName.name()] = 1
        return self.procName

    def initVars(self):
        self.active = GetForegroundWindow()
        self.threadID, processID = GetWindowThreadProcessId(self.active)
        self.prevStamp = datetime.datetime.now()
        try:
            self.procName = Process(processID)
        except NoSuchProcess:
            pass

    def readList(self, file):
        with open(file) as f:
            lines = f.readlines()

        for line in lines:
            self.processLists.append(line.strip("\n").split(","))

    def updateAffectionUsingProcess(self, process, whitelist, time=60):
        for i in range(0, len(whitelist)):
            if process in whitelist[i]:
                if self.record[i] is not None:
                    self.record[i] += datetime.timedelta(0, time)
                else:
                    self.record[i] = datetime.timedelta(0, time)

                return 1
        return 0

    def updateAffectionByCategory(self, category, time=60):
        if category not in self.categories:
            return
        index = self.categories.index(category)
        if self.record[index] is not None:
            self.record[index] += datetime.timedelta(0, time)
        else:
            self.record[index] = datetime.timedelta(0, time)
            