// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.

#pragma once

#include <bits/stdint-uintn.h>
#include <cstddef>
#include <cstdint>
#include <fstream>
#include <functional>
#ifdef _WINDOWS
#include <numeric>
#endif
#include <string>
#include <vector>
#include <map>

#include "distance.h"
#include "parameters.h"

namespace diskann
{
struct QueryStats
{
    float total_us = 0; // total time to process query in micros
    float io_us = 0;    // total time spent in IO
    float cpu_us = 0;   // total time spent in CPU

    unsigned n_4k = 0;         // # of 4kB reads
    unsigned n_8k = 0;         // # of 8kB reads
    unsigned n_12k = 0;        // # of 12kB reads
    unsigned n_ios = 0;        // total # of IOs issued
    unsigned read_size = 0;    // total # of bytes read
    unsigned n_cmps_saved = 0; // # cmps saved
    unsigned n_cmps = 0;       // # cmps
    unsigned n_cache_hits = 0; // # cache_hits
    unsigned n_cache_miss = 0; // # cache_miss
    unsigned n_hops = 0;       // # search hops
    std::vector<uint64_t> visited_block_id;
    // std::map<unsigned int, uint32_t> first_layer_visit_count;

    QueryStats() {
        visited_block_id = {};
        // first_layer_visit_count = {};
    }
    ~QueryStats() {
        // delete visited_block_id;
        // delete first_layer_visit_count;
    }
    // std::pair<uint32_t, uint32_t> n_hit_miss = std::make_pair<uint32_t, uint32_t>(0, 0);
};

template <typename T>
inline T get_percentile_stats(QueryStats *stats, uint64_t len, float percentile,
                              const std::function<T(const QueryStats &)> &member_fn)
{
    std::vector<T> vals(len);
    for (uint64_t i = 0; i < len; i++)
    {
        vals[i] = member_fn(stats[i]);
    }

    std::sort(vals.begin(), vals.end(), [](const T &left, const T &right) { return left < right; });

    auto retval = vals[(uint64_t)(percentile * len)];
    vals.clear();
    return retval;
}

template <typename T>
inline double get_mean_stats(QueryStats *stats, uint64_t len, const std::function<T(const QueryStats &)> &member_fn)
{
    double avg = 0;
    for (uint64_t i = 0; i < len; i++)
    {
        avg += (double)member_fn(stats[i]);
    }
    return avg / len;
}

template <typename T>
inline double get_ratio(QueryStats *stats, uint64_t len, const std::function<T(const QueryStats &)> &member_fn_1, const std::function<T(const QueryStats &)> &member_fn_2)
{
    uint64_t hit = 0, miss = 0;
    for (uint64_t i = 0; i < len; i++) {
        hit += member_fn_1(stats[i]);
        miss += member_fn_2(stats[i]);
    }
    return hit * 1.0 / (hit + miss);
}

template <typename T>
inline std::map<unsigned int, uint32_t> get_merged_count(QueryStats *stats, uint64_t len)
{
    std::map<unsigned int, uint32_t> count;
    // for (uint64_t i = 0; i < len; i++) {
    //     for (auto &x: stats[i].first_layer_visit_count) {
    //         if (count.find(x.first) == count.end()) {
    //             count[x.first] = x.second;
    //         } else {
    //             count[x.first] = count[x.first] + x.second;
    //         }
    //     }
    // }
    return count;
}

template <typename T>
inline std::vector<std::pair<uint64_t, uint64_t>> get_merged_visited_blocks(QueryStats *states, uint64_t len)
{
    std::vector<std::pair<uint64_t, uint64_t>> res;
    for (uint64_t i = 0; i < len; i++) {
        for (auto k: states[i].visited_block_id) {
            res.push_back({i, k});
        }
    }
    return res;
}

} // namespace diskann
