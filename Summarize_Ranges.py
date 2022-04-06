# https://www.codewars.com/kata/55fb6537544ae06ccc0000dc/train/python

def summary_ranges_2(nums):
    nums = sorted(list(set(nums)))
    list_ranges = []
    if len(nums)< 1:
        return list_ranges
    else:
        first_value = str(nums[0])
        range_open = True
        for index in range(1, len(nums)):
            range_open = True
            if nums[index] - nums[index-1] > 1:
                list_ranges.append(first_value + "->" + str(nums[index-1]))
                if index < len(nums)-1:
                    range_open = False
                    first_value = str(nums[index])
                else:
                    list_ranges.append(str(nums[index]))
                    range_open = False
        if range_open:
            list_ranges.append(first_value) 
            
        return(list_ranges)

def summary_ranges_1(nums):
    nums = sorted(list(set(nums)))
    list_ranges = []

    if len(nums) < 2:
        return nums
    else:
        range_open = True
        range_start = nums[0]
        for index in range(1, len(nums)):
            range_open = True
            if nums[index] - nums[index-1] > 1:
                if nums[index-1] == range_start:
                    list_ranges.append(range_start)
                    #range_open = False
                else:
                    list_ranges.append(f'{range_start}->{nums[index-1]}')
                    #range_open = False
                range_start = nums[index]
                
        #if range_open == True:
        if nums[len(nums)-1] == range_start:
            list_ranges.append(range_start)
        else:
            list_ranges.append(f'{range_start}->{nums[index]}')                

        return list_ranges

def summary_ranges(nums):
    nums = sorted(list(set(nums)))
    if len(nums) < 1:
        return nums
    else:
        num_range = 0
        list_ranges = [[]]
        for index in range(1, len(nums)):
            list_ranges[num_range].append(nums[index-1])
            if nums[index] - nums[index-1] > 1:
                list_ranges.append([])
                num_range += 1
        list_ranges[num_range].append(nums[len(nums)-1])
        return [f'{x[0]}->{x[-1]}' if len(x) > 1 else str(x[0]) for x in list_ranges]

print(summary_ranges([]))#, [])
print(summary_ranges([1, 1, 1, 1]))#, ['1'])
print(summary_ranges([1, 2, 3, 4]))#, ['1->4'])
print(summary_ranges([0, 1, 2, 5, 6, 9]))#, ["0->2", "5->6", "9"])
print(summary_ranges([0, 1, 2, 3, 4, 5, 6, 7]))#, ["0->7"])
print(summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]))# == ["0->7", "9->10"]
print(summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]))# == ["-2", "0->7", "9->10", "12"]
