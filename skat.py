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

    def getAmountPlayers():
        playerAmount = len(Player.allPlayers)
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

    def calculateWinner():
        max = Player.getAmountPlayers()
        Player.winnerPoints.append('')
        for i in range(0, max):

            if Player.allPlayers[i].points > Player.winnerPoints[0]:
                Player.winnerPoints.clear()
                Player.winnerIndex.clear()
                Player.winnerPoints.append(Player.allPlayers[i].points)
                Player.winnerIndex.append(Player.allPlayers[i].index)
            elif Player.allPlayers[i].points == Player.winnerPoints[0]:
                Player.winnerPoints.append(Player.allPlayers[i].points)
                Player.winnerIndex.append(Player.allPlayers[i].index)
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
