class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        results = [0 for i in range(len(temperatures))]
        s_temps = []

        for i in range(len(temperatures)):
            pointer = len(s_temps) - 1
            while s_temps and pointer >= 0 and temperatures[i] > s_temps[pointer]:
                if results [pointer] == 0:
                    results[pointer] = i - pointer
                pointer -= 1

            s_temps.append(temperatures[i])
        
        return results