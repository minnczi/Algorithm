class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 1st element: remaining number of senators
        # 2nd element: number of banned senators in that round
        senators = deque()
        senators.extend(senate)

        count_dict = {"R": ["Radiant", senate.count("R"), 0], "D": [
            "Dire", senate.count("D"), 0]}

        while senators:
            s = senators[0]
            # opposite team
            o = "R" if s == "D" else "D"

            # case 1: senator gets banned
            if count_dict[s][2] >= 1:
                senators.popleft()
                count_dict[s][1] -= 1
                count_dict[s][2] -= 1

            # case 2: senator claims victory
            elif count_dict[o][1] == 0:
                return count_dict[s][0]

            # case 3: senator bans another senator
            else:
                count_dict[o][2] += 1
                senators.rotate(-1)
