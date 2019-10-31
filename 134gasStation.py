"""
leetcode 134 加油站
一条环路上有N个加油站，每个加油站有gas[i]升汽油，现在有一辆油箱容量无限的汽车，初始油箱为空，从加油站i开往加油站j需要耗费cost[i]升汽油，问给定N个加油站的存储的汽油gas和两个加油站之间的花费cost，是否能够从某个加油站开始环形一周？若能够环形一周，返回出发的加油站，不行责任返回-1.
贪心算法思路：将加油站0设为起始加油站，记录总的油量和当前油量，若当前油量为负，重置当前油量，将起始点设为下一个加油站。若总油量小于0返回-1，否则返回当前起始点。
"""

from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, curr_tank = 0, 0
        start_station = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                curr_tank = 0
                start_station = i + 1
        return start_station if total_tank >= 0 else -1