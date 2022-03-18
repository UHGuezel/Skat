import csv
from unicodedata import name


class Player:
    allPlayers = []
    winnerPoints = []
    winnerIndex = []

    def __init__(self, index: int, name: str, points: int):
        self.index = index
        self.name = name
        self.points = points

        Player.allPlayers.append(self)

    def __repr__(self):
        return f"{self.name}, {self.points}"

    @classmethod
    def getAmountPlayers(cls):
        playerAmount = len(cls.allPlayers)
        return(playerAmount)

    def getData():
        with open('data.csv', 'r', encoding='utf-8') as content:
            reader = csv.DictReader(content)
            players = list(reader)
        for player in players:
            Player(
                index=player.get('index'),
                name=player.get('name'),
                points=player.get('points')
            )

    @classmethod
    def calculateWinner(cls):
        max = cls.getAmountPlayers()
        cls.winnerPoints.append('')
        for i in range(0, max):

            if cls.allPlayers[i].points > cls.winnerPoints[0]:
                cls.winnerPoints.clear()
                cls.winnerIndex.clear()
                cls.winnerPoints.append(cls.allPlayers[i].points)
                cls.winnerIndex.append(cls.allPlayers[i].index)
            elif cls.allPlayers[i].points == cls.winnerPoints[0]:
                cls.winnerPoints.append(cls.allPlayers[i].points)
                cls.winnerIndex.append(cls.allPlayers[i].index)
            else:
                pass


def testMain():
    print(f"Amount Player: {len(Player.allPlayers)}")
    print(f"Amount Winners: {len(Player.winnerPoints)}")
    print(f"Highest Points: {Player.winnerPoints}")
    print(f"Index of Winner: {Player.winnerIndex}")
    print("Winners: ", end='')
    for i in range(len(Player.winnerIndex)):
        index = int(Player.winnerIndex[i])
        print(Player.allPlayers[index].name, end=' ')


def main():
    Player.getData()
    Player.calculateWinner()
    testMain()


if __name__ == '__main__':
    main()
