import time
from typing import List, Dict

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int, coins: List[int]) -> Dict[int, int]:
    '''
    Makes change using a greedy heuristic (optimal for canonical coin systems).
        Args:
            amount: int, the amount of money to make change for
            coins: list of int, the denominations of coins available
        Returns a dictionary with coin denominations as keys and their counts as values.
    '''
    if amount < 0:
        raise ValueError("Amount must be non-negative.")
    if any(c <= 0 for c in coins):
        raise ValueError("Coin denominations must be positive.")
    
    coins = sorted(coins, reverse=True)  # Sort coins in descending order
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    if amount > 0:
        raise ValueError("Cannot make change for the given amount with the provided coin denominations.")
    return result

def find_min_coins(amount: int, coins: List[int]) -> Dict[int, int]:
    '''
      Makes change using DP - dynamic programming (optimal for any coin system).
        Args:
            amount: int, the amount of money to make change for
            coins: list of int, the denominations of coins available
        Returns a dictionary with coin denominations as keys and their counts as values.
    '''
    if amount < 0:
        raise ValueError("Amount must be non-negative.")
    if any(c <= 0 for c in coins):
        raise ValueError("Coin denominations must be positive.")

    n = len(coins)
    INF = float('inf')

    # create table K for storing the minimum number of coins for sums 0..amount
    # K[i][w] - minimum number of coins to make sum w using the FIRST i coins (coins[0..i-1])
    K = [[INF for w in range(amount + 1)] for i in range(n + 1)]
    # base case: 0 coins are needed to make sum 0 (regardless of i)
    for i in range(n + 1):
        K[i][0] = 0.0

    for i in range(1, n + 1):
        coin = coins[i - 1]
        for w in range(1, amount + 1):
            best = K[i - 1][w]  # best without using coin i-1
            if coin <= w and K[i][w - coin] + 1 < best:
                best = K[i][w - coin] + 1
            K[i][w] = best

    # if we cannot make change for the amount, raise an error
    if K[n][amount] == INF:
        raise ValueError("Cannot make change for the given amount with the provided coin denominations.")

    # reconstruct the dictionary {denomination: count} from the table K
    res: Dict[int, int] = {}
    i, w = n, amount
    while w > 0 and i > 0:
        # if the value matches the row above — we didn't take coin i-1
        if K[i][w] == K[i - 1][w]:
            i -= 1
        else:
            # we took coin i-1: record it and reduce the remaining amount
            coin = coins[i - 1]
            res[coin] = res.get(coin, 0) + 1
            w -= coin

    if w != 0:
        raise ValueError("Reconstruction failed.")

    return res

if __name__ == "__main__":
    amount = 1130000
    try:
        print("-" * 40)
        t0 = time.perf_counter()
        change = find_coins_greedy(amount, coins)
        dt = time.perf_counter() - t0
        print(f"Greedy: change for \033[92m{amount}\033[0m using  coins {coins}: \033[92m{change}\033[0m")
        print(f"Greedy: elapsed: {dt*10000:.6f} ms")
        print("-" * 40)
        t0 = time.perf_counter()
        change = find_min_coins(amount, coins)
        dt = time.perf_counter() - t0
        print(f"DP: change for \033[92m{amount}\033[0m using  coins {coins}: \033[92m{change}\033[0m")
        print(f"DP: elapsed: {dt*10000:.6f} ms")
    except ValueError as e:
        print(f"Error: {e}")