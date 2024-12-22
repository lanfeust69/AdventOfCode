use std::{collections::{VecDeque, HashMap, HashSet}, io::{self, BufRead}, fs::File};

fn pseudo_random(mut n: u32) -> u32 {
    n = ((n << 6) ^ n) & ((1 << 24) - 1);
    n = ((n >> 5) ^ n) & ((1 << 24) - 1);
    ((n << 11) ^ n) & ((1 << 24) - 1)
}

fn main() {
    let f = File::open("test.in").expect("file not found");
    let mut res = 0u64;
    let mut seeds = Vec::new();
    let mut by_deltas: HashMap<_, i32> = HashMap::new();
    for line in io::BufReader::new(f).lines() {
        let seed = line.expect("error").trim().parse::<u32>().unwrap();
        seeds.push(seed);
        let mut n = seed;
        let mut deltas = VecDeque::new();
        let mut seen = HashSet::new();
        let mut prev = (n % 10) as i32;
        for _ in 0..2000 {
            n = pseudo_random(n);
            let price = (n % 10) as i32;
            deltas.push_back(price - prev);
            if deltas.len() > 4 {
                deltas.pop_front();
            }
            if deltas.len() == 4 {
                let key = (deltas[0], deltas[1], deltas[2], deltas[3]);
                if !seen.contains(&key) {
                    seen.insert(key);
                    *by_deltas.entry(key).or_default() += price;
                }
            }
            prev = price;
        }
        res += n as u64;
    }

    println!("{}", res);
    println!("{}", by_deltas.values().max().unwrap());
}
