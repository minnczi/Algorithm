class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        curr_altitude = 0
        for i in range(len(gain)):
            curr_altitude += gain[i]
            max_altitude = max(max_altitude, curr_altitude)
        return max_altitude
