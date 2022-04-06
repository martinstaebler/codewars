
def pickPeaks(num_arr):
    arr_pos = []
    arr_peak = []
    current_pos = None
    current_peak = None
    pos_and_peaks = {}

    for x in range(1,len(num_arr)):
        gradient = num_arr[x] - num_arr[x-1]
        if gradient > 0:
            current_pos = x
            current_peak = num_arr[x]
        elif gradient < 0 and current_pos != None:
            arr_pos.append(current_pos)
            arr_peak.append(current_peak)
            current_pos = None
            current_peak = None

    pos_and_peaks['pos'] = arr_pos
    pos_and_peaks['peaks'] = arr_peak
    return pos_and_peaks

print(pickPeaks([0, 1, 2, 5, 1, 0])) #should return {pos: [3], peaks: [5]}
print(pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])) #should return {pos: [3, 7], peaks: [6, 3]}
print(pickPeaks([1, 2, 2, 2, 1])) #should return {pos: [1], peaks: [2]}
print(pickPeaks([1, 2, 2, 2, 3])) #should return {pos: [], peaks: []}
