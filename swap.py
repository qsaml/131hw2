'''
Swaps the first and last items of a list.
Params:
  list: The list to be modified.

Returns:
  list: The modified list.
'''


def swap_last_item(list):
    list[0], list[len(list) - 1] = list[len(list) - 1], list[0]
    return list