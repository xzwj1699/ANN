from matplotlib import pyplot as plt
import numpy as np
f = open("../../build/visited_10")
lines = f.readlines()
datas = []
hit = 0
miss = 0
time = []
block_id = []
t = 0
for line in lines:
    splited = line.split(' ')
    time.append(t)
    block_id.append(int(splited[1]))
    t += 1

# print(hit * 1.0 / (hit + miss))

plt.scatter(time[:], block_id[:], s=0.001)
plt.xlabel("Sequence")
plt.ylabel("Block ID")
plt.title("Visit Pattern w/ Cache Size 1%")
plt.savefig("visited_1M_1%_cachesize-40.png")
# plt.show()

# datas = sorted(datas, key=lambda x: x[2], reverse=True)
# datas = datas[:1000]
# print(datas[:30])
# keys = [x[0] for x in datas]
# cached = [x[1] for x in datas]
# freq = [x[2] for x in datas]
# x_pos = np.arange(len(freq))

# cached_x_pos, cached_x_freq, uncached_x_pos, uncached_x_freq = [], [], [], []

# for i in np.arange(len(keys)):
#     if cached[i] == 1:
#         cached_x_pos.append(x_pos[i])
#         cached_x_freq.append(freq[i])
#     else:
#         uncached_x_pos.append(x_pos[i])
#         uncached_x_freq.append(freq[i])

# plt.bar(cached_x_pos, cached_x_freq, width=1, color="red", label="Cached")
# # plt.bar(uncached_x_pos, uncached_x_freq, width=1, color="green", label="Uncached")
# plt.xlim(0, 1000)
# plt.ylim(0, 2000)
# plt.legend()

# # plt.plot(np.arange(len(freq)), freq)
# plt.savefig("cache_20-cached.pdf")