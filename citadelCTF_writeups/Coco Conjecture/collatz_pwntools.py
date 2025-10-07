#!/usr/bin/env python3
# collatz_ctf_final_fast.py
# Fully optimized and exact Collatz client for Citadel CTF
from pwn import remote
import re
import sys
import time

HOST = 'chall_citadel.cryptonitemit.in'
PORT = 61234
TIMEOUT = 10

# Memoization cache: store number -> steps to 1
# Only cache numbers smaller than a reasonable threshold
CACHE_LIMIT = 10_000_000
cache = {1: 0}

def collatz_steps(n: int) -> int:
    """
    Exact iterative Collatz step count with safe memoization.
    Each transformation counts as 1 step.
    """
    original = n
    sequence = []
    while n not in cache:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    # Steps from known cached value
    steps = cache[n]

    # Backfill cache for all new numbers in sequence
    for x in reversed(sequence):
        steps += 1
        if x < CACHE_LIMIT:
            cache[x] = steps

    return steps

def extract_challenge_number(line: bytes) -> int | None:
    """
    Extract the integer immediately following 'Round X:'.
    """
    match = re.search(rb'Round \d+: (\d+)', line)
    if match:
        return int(match.group(1))
    return None

def main():
    try:
        r = remote(HOST, PORT, timeout=TIMEOUT)
    except Exception as e:
        print("Connection error:", e, file=sys.stderr)
        return

    try:
        while True:
            try:
                line = r.recvline(timeout=6)
            except Exception as e:
                print("Recv failed:", e)
                break

            if not line:
                print("Connection closed by server.")
                break

            print("SERVER:", line.strip().decode(errors='replace'))

            if b'citadel{' in line:
                print("FLAG/END:", line.strip().decode(errors='replace'))
                break

            n = extract_challenge_number(line)
            if n is None or n < 1:
                continue

            start = time.time()
            ans = collatz_steps(n)
            elapsed = time.time() - start

            payload = (str(ans) + '\n').encode()
            try:
                r.send(payload)
            except Exception as e:
                print("Send failed:", e)
                break

            print(f"Received integer: {n} -> Sent: {ans} (calc {elapsed:.4f}s)")

    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        try:
            r.close()
        except:
            pass

if __name__ == '__main__':
    main()
