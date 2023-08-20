T = int(input())

for tc in range(1, T+1):
    all_nums = []
    all_nums.extend('0123456789')

    sheep = int(input())
    round = 1

    while len(all_nums) > 0:
        total = str(sheep * round)
        for i in total:
            if i in all_nums:
                all_nums.remove(i)
        round += 1
    
    print('#%d %d' % (tc, (round-1) * sheep))
