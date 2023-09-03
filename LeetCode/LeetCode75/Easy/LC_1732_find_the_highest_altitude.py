class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        curr_altitude = 0
        for i in range(len(gain)):
            curr_altitude += gain[i]
            max_altitude = max(max_altitude, curr_altitude)
        return max_altitude

# Solution using prefix sum list


class Solution2:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [gain[0]]
        for i in range(1, len(gain)):
            prefix_sum.append(prefix_sum[i-1] + gain[i])
        return max(max(prefix_sum), 0)
