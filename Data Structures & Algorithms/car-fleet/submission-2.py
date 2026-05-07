class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)
        slowestTime = (target - cars[0][0]) / cars[0][1]
        fleets = 1
        for i in range(1, len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if time > slowestTime:
                fleets += 1
                slowestTime = time
        return fleets
