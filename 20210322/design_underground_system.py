from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.d = {}
        self.timeSum = defaultdict(int)
        self.cnt = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.d[id]
        travel = (startStation, stationName)
        self.timeSum[travel] += t - startTime
        self.cnt[travel] += 1

        del self.d[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        return self.timeSum[travel] / self.cnt[travel]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)