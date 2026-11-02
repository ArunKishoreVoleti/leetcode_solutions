from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Finds the minimum number of arrows needed to burst all balloons.

        The approach:
        1. Sort balloons by their ending coordinates.
        2. Shoot an arrow at the end of the first balloon.
        3. Shoot another arrow only when the next balloon starts after the
           current arrow position.

        Args:
            points (List[List[int]]): Balloon intervals, where each interval
                contains its start and end coordinates.

        Returns:
            int: The minimum number of arrows needed.
        """
        if not points:
            return 0

        balloons_by_end = sorted(points, key=lambda balloon: balloon[1])
        arrows = 1
        arrow_position = balloons_by_end[0][1]

        # Reuse the current arrow if it falls within the next balloon.
        for start, end in balloons_by_end[1:]:
            if start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows
