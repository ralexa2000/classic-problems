import typing


def calculate_max_water(landscape: typing.List[int]) -> int:
    """
    Given a list of landscape heights returns maximum volume of water
    that can be accumulated after the rain

    Time complexity: O(n)
    Space complexity: O(1)

    :param landscape: list of integer heights
    :return: maximum volume of water
    """
    if not isinstance(landscape, list) or \
            not all(isinstance(height, int) for height in landscape):
        raise TypeError('Input should be a list of integers')

    left, right = 0, len(landscape) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if landscape[left] < landscape[right]:
            if landscape[left] > left_max:
                left_max = landscape[left]
            else:
                water += left_max - landscape[left]
            left += 1
        else:
            if landscape[right] > right_max:
                right_max = landscape[right]
            else:
                water += right_max - landscape[right]
            right -= 1
    return water
