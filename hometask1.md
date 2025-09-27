# Conclusions: greedy algorithm vs dynamic programming (coin change)

- **Speed:**
  - greedy  is faster: time per request is **O(k)**, where *k* is the number of denominations. 
  - DP is slower: **O(k·S)**, where *S* is the sum.
- **Memory:**
  - Greedy  **O(1)**
  - DP  **O(S)** (1D) or **O(k·S)** (2D).
- **Optimality:**
  - greedy **does not guarantee the minimum number of coins** for arbitrary denominations
  - DP **always finds the minimum number of coins**.
- **Scaling by sum:**
  - greedy time is almost independent of the sum;
  - DP time and memory **grow linearly** with *S*.

| Algorithm | Sum | Time, ms |
|---|---|---|
| greedy | 113 | 0.050 |
| DP | 113 | 0.859|
| greedy | 1130 | 0.060|
| DP | 1130 | 7.566|
| greedy | 11300 | 0.059|
| DP | 11300 | 76.127|
| greedy | 113000 | 0.059|
| DP | 113000 | 772.132|
| greedy | 1130000 | 0.061|
| DP | 1130000 | 7633.936|

## Behavior with large sums
- For very large *S* (thousands and above), **greedy** scales better and remains stable over time.
- **DP** with large *S* can become a bottleneck (both in terms of time and memory), but ensures optimal results.
