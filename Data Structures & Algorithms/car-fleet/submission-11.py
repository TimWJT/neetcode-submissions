class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        
        cars.sort(reverse=True)

        print(cars)
        
        stack = []  # stack of times-to-target for each fleet
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # If this car takes longer than the fleet ahead, it's a new fleet.
            # Otherwise it catches up and merges.
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)