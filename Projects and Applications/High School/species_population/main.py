import pandas as pd
import json
import matplotlib.pyplot as plt
import math
import scipy.stats


def get_data():
    data = pd.read_csv("data/data.csv", encoding="utf-8").values
    output = {}
    for row in data:
        output[row[0]] = {
            "binomial": row[1],
            "common_name": row[11],
            "location": row[12],
            "country": row[13],
            "gcs": [row[18], row[19]],
            "counts": list(row[32:])
        }
    with open("data/data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)


def plots():
    with open("data/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for i in data:
        x = []
        y = []
        for index, count in enumerate(data[i]["counts"]):
            if not math.isnan(count):
                x.append(index + 1950)
                y.append(count)

        plt.xlim(1950, 2020)
        plt.plot(x, y)
        plt.xlabel("Years")
        plt.ylabel("Count")
        plt.title(f"Population counts vs. Years (ID: {i})")
        plt.savefig(f"data/plots/{i}.png")
        plt.clf()


def trends():
    results = {"positive": 0, "negative": 0, "inconclusive": 0, "data": []}
    with open("data/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for i in data:
        x = []
        y = []
        for index, count in enumerate(data[i]["counts"]):
            if not math.isnan(count):
                x.append(index + 1950)
                y.append(count)
        if x != [] and y != []:
            slope, intercept, r, p, std_err = scipy.stats.linregress(x, y)
            results["data"].append([slope, intercept, r, p, std_err])
            if slope > 0:
                results["positive"] += 1
            elif slope < 0:
                results["negative"] += 1
        else:
            results["inconclusive"] += 1
    with open("data/results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)


def analysis():
    with open("data/results.json", "r", encoding="utf-8") as f:
        results = json.load(f)
    total = results["positive"] + results["negative"]
    plt.bar(["Positive", "Negative"], [results["positive"] / total, results["negative"] / total])
    plt.xlabel("Correlation")
    plt.ylabel("Percentage")
    plt.title("Overall results")
    plt.show()
