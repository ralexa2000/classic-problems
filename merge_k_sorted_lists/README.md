###Merge k Sorted Lists

The problem is to merge an array of `k` linked-lists, each one is sorted in ascending order.

The idea is to divide all linked-lists into pairs and merge them in linear time. Then to divide the rest of the lists into pairs and merge them. And repeate this until we have just one linked-list.
The time complexity of this algorithm is `O(N log k)`, where `N` is the total number of items in all linked-lists.