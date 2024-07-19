Different methods of handling prime numbers. Most sources are credited to Wikipedia and appropiately following sources. All code used is by no means perfectly optimized, and all data shown should be merely used as reference.

# Generating Primes

## Prime sieves

### [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

This method of finding primes is perhaps the most famous, as it is simple yet clever. As you iterate through each integer from 2 to $\sqrt{n}$, you eliminate its multiples. The theoretical time complexity is $O(n \log{\log{n}})$.

A sample pseudocode is as follows:

```
algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n, initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n
        if A[i] is true
            for j = i², i²+i, i²+2i, i²+3i, ..., not exceeding n
                set A[j] := false

    return all i such that A[i] is true.
```

![Sieve of Eratosthenes](https://cdn.discordapp.com/attachments/905301278647783428/1087886676954722304/image.png)

| Power | Time (seconds)        |
| ----- | --------------------- |
| 0     | 0.0 (negligible)      |
| 1     | 0.0 (negligible)      |
| 2     | 0.0 (negligible)      |
| 3     | 0.0009982585906982422 |
| 4     | 0.006980419158935547  |
| 5     | 0.07981514930725098   |
| 6     | 0.8839259147644043    |
| 7     | 9.926632642745972     |
| 8     | 105.78479337692261    |
| 9     | 1128.1615352630615    |

| Power | Log Time (log seconds) |
| ----- | ---------------------- |
| 0     | -10.0                  |
| 1     | -10.0                  |
| 2     | -10.0                  |
| 3     | -3.0007569             |
| 4     | -2.15611849            |
| 5     | -1.09791467            |
| 6     | -0.05358413            |
| 7     | 0.99680195             |
| 8     | 2.02442324             |
| 9     | 3.05237129             |


### [Sieve of Sundaram](https://en.wikipedia.org/wiki/Sieve_of_Sundaram)

This more recent method is a variant of the Sieve of Eratosthenes. We first take a list of numbers from 1 to n. We then remove all numbers in the form $i + j + 2ij$ where:
* $i,j\in\mathbb{N},\ 1 \le i \le j$
* $i + j + 2ij \le n$

Then, we are left with all primes to 2n + 2 (except for 2) when multiplying the remaining numbers and adding 1. The theoretical time complexity is $O(n \log{n})$.

A sample pseudocode is as follows:

```
algorithm Sieve of Sundaram is
    input: an integer n > 1.
    output: all prime numbers from 3 through 2n + 2.

    handle if n is less than 3

    let k be (n - 3) // 2 + 1

    let A be an array of Boolean values, indexed by integers 1 to n, initially all set to true.
    
    let i, j be equal to 1

    for i = 0, 1, 2, 3, ..., not exceeding (√n - 3) // 2 + 1
        for j in between ((2 * i + 3) * (2 * i + 3) - 3) // 2 and (n - 3) // 2 + 1 with step 2 * i + 3
            set A[j] as False

    return all i such that A[i] is true.
```

![Sieve of Sundaram](https://cdn.discordapp.com/attachments/905301278647783428/1088078932307353670/image.png)

| Power | Time (seconds)        |
| ----- | --------------------- |
| 0     | 0.0 (negligible)      |
| 1     | 0.0 (negligible)      |
| 2     | 0.0 (negligible)      |
| 3     | 0.0 (negligible)      |
| 4     | 0.003995418548583984  |
| 5     | 0.004004478454589844  |
| 6     | 0.10068106651306152   |
| 7     | 2.3013129234313965    |
| 8     | 29.09872841835022     |
| 9     | 381.39671087265015    |

| Power | Log Time (log seconds) |
| ----- | ---------------------- |
| 0     | -10.0                  |
| 1     | -10.0                  |
| 2     | -10.0                  |
| 3     | -10.0                  |
| 4     | -2.39843771            |
| 5     | -2.39745403            |
| 6     | -0.99705219            |
| 7     | 0.36197568             |
| 8     | 1.46387401             |
| 9     | 2.58137694             |

### [Sieve of Atkin](https://en.wikipedia.org/wiki/Sieve_of_Atkin)

This sieve is similar to the previous sieves, but does some preliminary work then marks off the squares of primes. The theoretical time complexity is $O(n)$.

A sample pseudocode is as follows:

```
limit ← 1000000000        // arbitrary search limit

// set of wheel "hit" positions for a 2/3/5 wheel rolled twice as per the Atkin algorithm
s ← {1,7,11,13,17,19,23,29,31,37,41,43,47,49,53,59}

// Initialize the sieve with enough wheels to include limit:
for n ← 60 × w + x where w ∈ {0,1,...,limit ÷ 60}, x ∈ s:
    is_prime(n) ← false

// Put in candidate primes:
//   integers which have an odd number of
//   representations by certain quadratic forms.
// Algorithm step 3.1:
for n ≤ limit, n ← 4x²+y² where x ∈ {1,2,...} and y ∈ {1,3,...} // all x's odd y's
    if n mod 60 ∈ {1,13,17,29,37,41,49,53}:
        is_prime(n) ← ¬is_prime(n)   // toggle state
// Algorithm step 3.2:
for n ≤ limit, n ← 3x²+y² where x ∈ {1,3,...} and y ∈ {2,4,...} // only odd x's
    if n mod 60 ∈ {7,19,31,43}:                                 // and even y's
        is_prime(n) ← ¬is_prime(n)   // toggle state
// Algorithm step 3.3:
for n ≤ limit, n ← 3x²-y² where x ∈ {2,3,...} and y ∈ {x-1,x-3,...,1} //all even/odd
    if n mod 60 ∈ {11,23,47,59}:                                   // odd/even combos
        is_prime(n) ← ¬is_prime(n)   // toggle state

// Eliminate composites by sieving, only for those occurrences on the wheel:
for n² ≤ limit, n ← 60 × w + x where w ∈ {0,1,...}, x ∈ s, n ≥ 7:
    if is_prime(n):
        // n is prime, omit multiples of its square; this is sufficient 
        // because square-free composites can't get on this list
        for c ≤ limit, c ← n² × (60 × w + x) where w ∈ {0,1,...}, x ∈ s:
            is_prime(c) ← false

// one sweep to produce a sequential list of primes up to limit:
output 2, 3, 5
for 7 ≤ n ≤ limit, n ← 60 × w + x where w ∈ {0,1,...}, x ∈ s:
    if is_prime(n): output n
```

![Sieve of Atkin](https://cdn.discordapp.com/attachments/905301278647783428/1088157274922557450/image.png)

| Power | Time (seconds)        |
| ----- | --------------------- |
| 0     | 0.0 (negligible)      |
| 1     | 0.0 (negligible)      |
| 2     | 0.0 (negligible)      |
| 3     | 0.0 (negligible)      |
| 4     | 0.0 (negligible)      |
| 5     | 0.0029921531677246094 |
| 6     | 0.04687356948852539   |
| 7     | 0.984621524810791     |
| 8     | 12.938156366348267    |
| 9     | 171.72893929481506    |

| Power | Log Time (log seconds) |
| ----- | ---------------------- |
| 0     | -10.0                  |
| 1     | -10.0                  |
| 2     | -10.0                  |
| 3     | -10.0                  |
| 4     | -10.0                  |
| 5     | -2.52401616            |
| 6     | -1.32907197            |
| 7     | -0.00673067430         |
| 8     | 1.11187240             |
| 9     | 2.23484349             |

# Checking Primes

## Brute Force

This method is done by checking if the number is divisible by any number from 2 to $\sqrt{n}$. The theoretical time complexity is $O(\sqrt{n})$.

![Brute Force](https://cdn.discordapp.com/attachments/905301278647783428/1088178506648797305/image.png)

| Power | Time (seconds)        |
| ----- | --------------------- |
| 0     | 0.0 (negligible)      |
| 1     | 0.0 (negligible)      |
| 2     | 0.0 (negligible)      |
| 3     | 0.0 (negligible)      |
| 4     | 0.0 (negligible)      |
| 5     | 0.0 (negligible)      |
| 6     | 0.0 (negligible)      |
| 7     | 0.0 (negligible)      |
| 8     | 0.0 (negligible)      |
| 9     | 0.0009698867797851562 |

| Power | Log Time (log seconds) |
| ----- | ---------------------- |
| 0     | -10.0                  |
| 1     | -10.0                  |
| 2     | -10.0                  |
| 3     | -10.0                  |
| 4     | -10.0                  |
| 5     | -10.0                  |
| 6     | -10.0                   |
| 7     | -10.0                   |
| 8     | -10.0                   |
| 9     | -3.01327892             |

## Primality testing

# Nth prime

asd