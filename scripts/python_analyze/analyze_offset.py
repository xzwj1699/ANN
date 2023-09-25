from matplotlib import pyplot as plt
import numpy as np

origin_offsets, greedy_offsets = [], []

c_4_max = 2 << 4
c_8_max = 2 << 8
c_16_max = 2 << 16
c_32_max = 2 << 32

origin_bucket = [0, 0, 0, 0]
greedy_bucket = [0, 0, 0, 0]

f1 = open("../../build/offset.txt")
lines = f1.readlines()
print("Step 1")
for line in lines:
    offset = abs(int(line))
    if offset < c_4_max:
        origin_bucket[0] = origin_bucket[0] + 1
    elif offset < c_8_max:
        origin_bucket[1] = origin_bucket[1] + 1
    elif offset < c_16_max:
        origin_bucket[2] = origin_bucket[2] + 1
    elif offset < c_32_max:
        origin_bucket[3] = origin_bucket[3] + 1
    origin_offsets.append(offset)

f2 = open("../../build/new_offset.txt")
lines = f2.readlines()
print("Step 2")
for line in lines:
    offset = abs(int(line))
    if offset < c_4_max:
        greedy_bucket[0] = greedy_bucket[0] + 1
    elif offset < c_8_max:
        greedy_bucket[1] = greedy_bucket[1] + 1
    elif offset < c_16_max:
        greedy_bucket[2] = greedy_bucket[2] + 1
    elif offset < c_32_max:
        greedy_bucket[3] = greedy_bucket[3] + 1
    greedy_offsets.append(offset)

print("Step 3")
sort_origin = np.sort(origin_offsets)
log_origin = np.log2(sort_origin)
# cum_origin = np.cumsum(log_origin)
# origin_offsets.sort()
print("Step 4")
sort_greedy = np.sort(greedy_offsets)
log_greedy = np.log2(sort_greedy)
# cum_greedy = np.cumsum(log_greedy)
# greedy_offsets.sort()
y = np.arange(len(sort_origin)) / len(sort_origin)
# x = np.arange(100000)
print("Step 5")
plt.plot(log_origin, y, label="Origin")
plt.plot(log_greedy, y, label="Greedy")
plt.xlim(0, 24)
plt.xticks([0, 4, 8, 12, 16, 20, 24], ["0", "4", "8", "12", "16", "20", "24"])
plt.legend()
print("Step 6")
plt.savefig("offset.png")
print("Step 7")
f1.close()
f2.close()

origin_bucket = np.array(origin_bucket) / np.sum(origin_bucket)
greedy_bucket = np.array(greedy_bucket) / np.sum(greedy_bucket)
print(origin_bucket)
print(greedy_bucket)