// import std;
#include <iostream>
#include <array>
#include <vector>
#include <unordered_map>
#include <chrono>

using namespace std;

struct blueprint {
    array<int, 4> ore_costs{};
    int clay_cost{};
    int obs_cost{};
};

vector<blueprint> blueprints{
    {{4, 2, 3, 2}, 14, 7},
    {{2, 3, 3, 3}, 8, 12},
    {{4, 4, 4, 2}, 8, 15},
    {{4, 4, 3, 4}, 19, 15},
    {{4, 4, 2, 3}, 8, 9}
};

blueprint cur{};
long long steps{};
long long hits{};
unordered_map<long long, int> cache;

int eval(int time, int ore_robots, int clay_robots, int obs_robots, int geode_robots, int ore, int clay, int obs) {
    if (time == 0)
        return geode_robots;
    long long key = (long long)time | (ore << 5) | (clay << 10) | (obs << 15) |
        (ore_robots << 20) | (clay_robots << 25) | ((long long)obs_robots << 30) | ((long long)geode_robots << 35);
    steps++;
    if (steps % 100000000 == 0)
        cout << "step " << steps << endl;
    auto it = cache.find(key);
    if (it != cache.end()) {
        hits++;
        return it->second;
    }
    bool can_build_ore = cur.ore_costs[0] <= ore;
    bool can_build_clay = cur.ore_costs[1] <= ore;
    bool can_build_obs = cur.ore_costs[2] <= ore && cur.clay_cost <= clay;
    bool can_build_geode = cur.ore_costs[3] <= ore && cur.obs_cost <= obs;
    bool enough_ore_robots = true;
    for (int i = 1; i < 4; ++i)
        if (ore_robots < cur.ore_costs[i]) {
            enough_ore_robots = false;
            break;
        }
    if (enough_ore_robots)
        can_build_ore = false;
    bool enough_clay_robots = clay_robots >= cur.clay_cost;
    if (enough_clay_robots)
        can_build_clay = false;
    bool enough_obs_robots = obs_robots >= cur.obs_cost;
    if (enough_obs_robots)
        can_build_obs = false;
    bool must_build = false;
    if (can_build_ore && can_build_clay) {
        if (clay_robots == 0 || (can_build_obs && (obs_robots == 0 || can_build_geode)))
            must_build = true;
    }
    if (enough_obs_robots && can_build_geode) {
        must_build = true;
    }
    if (enough_ore_robots && enough_clay_robots && can_build_obs && can_build_geode) {
        must_build = true;
    }
    int best = 0;
    if (!must_build)
        best = geode_robots + eval(time - 1, ore_robots, clay_robots, obs_robots, geode_robots, ore + ore_robots, clay + clay_robots, obs + obs_robots);
    if (can_build_ore)
        best = max(best, geode_robots + eval(time - 1, ore_robots + 1, clay_robots, obs_robots, geode_robots,
            ore + ore_robots - cur.ore_costs[0], clay + clay_robots, obs + obs_robots));
    if (can_build_clay)
        best = max(best, geode_robots + eval(time - 1, ore_robots, clay_robots + 1, obs_robots, geode_robots,
            ore + ore_robots - cur.ore_costs[1], clay + clay_robots, obs + obs_robots));
    if (can_build_obs)
        best = max(best, geode_robots + eval(time - 1, ore_robots, clay_robots, obs_robots + 1, geode_robots,
            ore + ore_robots - cur.ore_costs[2], clay + clay_robots - cur.clay_cost, obs + obs_robots));
    if (can_build_geode)
        best = max(best, geode_robots + eval(time - 1, ore_robots, clay_robots, obs_robots, geode_robots + 1,
            ore + ore_robots - cur.ore_costs[3], clay + clay_robots, obs + obs_robots - cur.obs_cost));
    return cache[key] = best;
}

int main() {
    int res = 1;
    for (int i = 0; i < blueprints.size(); ++i) {
        cur = blueprints[i];
        cache.clear();
        steps = 0;
        hits = 0;
        cout << "starting " << i << endl;
        chrono::system_clock::time_point startTime = chrono::system_clock::now();
        int v = eval(31, 1, 0, 0, 0, 0, 0, 0);
        auto elapsed = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now() - startTime);
        cout << "found " << v << " in " << steps << " steps and " << elapsed.count() <<
            "ms, with " << hits << " hits in cache with " << cache.size() << " entries" << endl;
        if (i >= 2)
            res *= v;
    }
    cout << res << endl;
}
