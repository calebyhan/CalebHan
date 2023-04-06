Simple test proving the [law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers).

The theorem states that:
> the average of the results obtained from a large number of trials should be close to the expected value and tends to become closer to the expected value as more trials are performed.

The method of generate a random variable is as follows:

```python
def simulation(n):
    heads = 0
    tails = 0
    for i in range(n):
        if random.choice([0, 1]) == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails
```

Here are the results:

<details>
    <summary>1e2</summary>

|         | Heads | Tails |
|---------|-------|-------|
| Count   | 52    | 48    |
| Percent | 52.0% | 48.0% |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093333589812330546/image.png)
</details>

<details>
    <summary>1e3</summary>

|         | Heads | Tails |
|---------|-------|-------|
| Count   | 504   | 496   |
| Percent | 50.4% | 46.9% |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093333631877001266/image.png)
</details>

<details>
    <summary>1e4</summary>

|         | Heads | Tails |
|---------|-------|-------|
| Count   | 4953  | 5047  |
| Percent | 49.5% | 50.5% |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093333668145139743/image.png)
</details>

<details>
    <summary>1e5</summary>

|         | Heads | Tails |
|---------|-------|-------|
| Count   | 49942 | 50058 |
| Percent | 49.9% | 50.1% |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093333722180358264/image.png)
</details>

<details>
    <summary>1e6</summary>

|         | Heads  | Tails  |
|---------|--------|--------|
| Count   | 499210 | 500790 |
| Percent | 49.9%  | 50.1%  |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093333759702601778/image.png)
</details>

<details>
    <summary>1e7</summary>

|         | Heads   | Tails   |
|---------|---------|---------|
| Count   | 4999033 | 5000967 |
| Percent | 50.0%   | 50.0%   |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093333811871371394/image.png)
</details>

<details>
    <summary>1e8</summary>

|         | Heads    | Tails    |
|---------|----------|----------|
| Count   | 50003622 | 49996378 |
| Percent | 50.0%    | 50.0%    |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093334020240179230/image.png)
</details>

<details>
    <summary>1e9</summary>

|         | Heads     | Tails     |
|---------|-----------|-----------|
| Count   | 500004478 | 499995522 |
| Percent | 50.0%     | 50.0%     |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093335531431149690/image.png)
</details>

<details>
    <summary>1e10</summary>

|         | Heads      | Tails      |
|---------|------------|------------|
| Count   | 4999910999 | 5000089001 |
| Percent | 50.0%      | 50.0%      |

![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093353929657557022/image.png)
</details>

Percentages of heads and tails over time
![Graph](https://cdn.discordapp.com/attachments/905301278647783428/1093354235917242468/image.png)
