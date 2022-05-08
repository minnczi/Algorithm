def find_num_songs(songs):
    ans = songs[0]
    
    if songs[1]:
        if songs[1] > songs[2]:
            ans += songs[2]*2 + 1
        else:
            ans += songs[1]*2
        if songs[3]:
            ans += songs[3]
        return ans
    elif songs[0] + songs[1] == 0:
        ans = songs[3]
        if songs[2]:
            ans += 1
    return ans

songs = list(map(int, input().split()))
print(find_num_songs(songs))