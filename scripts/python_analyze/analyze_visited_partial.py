from matplotlib import pyplot as plt
import numpy as np

def in_area_1(x, y):
    return y <= x * 1.1 + 15000 and y >= x * 1.1 + 7000

def in_area_2(x, y):
    return y <= x * 1.1 and y >= x * 1.1 - 6000 

if __name__ == "__main__":
    f = open("../../build/visited_10")
    lines = f.readlines()
    datas = []
    hit = 0
    miss = 0
    time = []
    block_ids = []
    t = 0
    last_q_id = 0
    last_2_hops_x = []
    last_2_hops_y = []
    last_5_hops_x = []
    last_5_hops_y = []
    first_5_hops_x = []
    first_5_hops_y = []
    last_query_hops_x = []
    last_query_hops_y = []
    in_area, sample = 0, 0
    for line in lines:
        splited = line.split(' ')
        q_id = int(splited[0])
        if last_q_id != q_id:
            last_2_hops_x.extend(last_query_hops_x[-2:])
            last_2_hops_y.extend(last_query_hops_y[-2:])
            last_5_hops_x.extend(last_query_hops_x[-5:])
            last_5_hops_y.extend(last_query_hops_y[-5:])
            first_5_hops_x.extend(last_query_hops_x[-6:])
            first_5_hops_y.extend(last_query_hops_y[-6:])
            time.extend(last_query_hops_x)
            block_ids.extend(last_query_hops_y)
            last_query_hops_x = []
            last_query_hops_y = []
        block_id = int(splited[1])
        last_query_hops_x.append(t)
        last_query_hops_y.append(block_id)
        if in_area_1(t, block_id) or in_area_2(t, block_id):
            in_area += 1
        if t >= 100000 and t <= 120000 and block_id >= 0 and block_id <= 25000:
            sample += 1
        t += 1
        last_q_id = q_id

    # print(hit * 1.0 / (hit + miss))

    upper_bounds = [x * 1.1 + 15000 for x in range(len(block_ids))]
    middle_bounds = [x * 1.1 + 7000 for x in range(len(block_ids))]
    middle_bounds_2 = [x * 1.1 for x in range(len(block_ids))]
    lower_bounds = [x * 1.1 - 6000 for x in range(len(block_ids))]
    print("total visit num: " + str(len(block_ids)) + ", visit in area: " + str(in_area))
    print("ratio: " + str(in_area * 1.0 / len(block_ids)))
    print("sample: " + str(sample) + ", density: " + str(sample / (20000 * 25000)))
    dense = len(block_ids) - sample * 1.0 / (20000 * 25000) * (len(time) * max(block_ids))
    print("ratio: " + str(dense / len(block_ids)))
    plt.scatter(time[:], block_ids[:], s=0.0003)
    plt.plot(time, upper_bounds)
    plt.plot(time, middle_bounds)
    plt.plot(time, middle_bounds_2)
    plt.plot(time, lower_bounds)
    plt.xlabel("Sequence")
    plt.ylabel("Block ID")
    plt.title("Visit Pattern w/ Cache Size 1%")
    plt.savefig("visited_1M_1%_cachesize-1.png")
    plt.clf()
    plt.scatter(first_5_hops_x[:], first_5_hops_y[:], s=0.003)
    plt.savefig("visited_1M_1%_cachesize-2.png")
    # plt.scatter(last_2_hops_x[:], last_2_hops_y[:], s=0.003)
    # plt.savefig("visited_1M_1%_cachesize-2.png")
    # plt.scatter(last_5_hops_x[:], last_5_hops_y[:], s=0.003)
    # plt.savefig("visited_1M_1%_cachesize-3.png")
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