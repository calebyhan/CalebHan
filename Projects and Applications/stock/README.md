Text-based application that fetches from `alphavantage` and `newsapi v2` (`https://www.alphavantage.co/query`, `https://newsapi.org/v2/everything`)

Returns basic information such as stock value, market capitalization, and company description. Custom algorithm included that recommends buy or not.

Example run:

```
Enter a company symbol: apl

1 - Applied Blockchain Inc (APLD)
2 - Apple Hospitality REIT Inc (APLE)
3 - Apolo Gold & Energy Inc (APLL)
4 - Alpha Pro Tech Ltd (APL.FRK)
5 - Appulse Corp (APL.TRV)
6 - Appili Therapeutics Inc (APLIF)
7 - HEDGED INCOME FUND INVESTOR (APLIX)
8 - Appili Therapeutics Inc (APLI.TRT)
9 - APLAB LTD.-$ (APLAB.BSE)
10 - APL APOLLO TUBES LTD. (APLAPOLLO.BSE)
11 - N/A

Choose the correct corresponding number: 11
Enter a company symbol: appl

1 - APPLESEED FUND INVESTOR CLASS (APPLX)
2 - Apple Green Holding Inc (AGPL)
3 - Apple Hospitality REIT Inc (APLE)
4 - Apple Inc (AAPL)
5 - Apple Inc (AAPL34.SAO)
6 - Apple Inc (APC.DEX)
7 - Apple Inc (APC.FRK)
8 - Apple Inc. (0R2V.LON)
9 - Apple Finance Limited (500014.BSE)
10 - Apple Flavor Fragrance Group Company Ltd (603020.SHH)
11 - N/A

Choose the correct corresponding number: 4

-------------------
Symbol: AAPL

Company Name: Apple Inc

Asset Type: Common Stock

Stock Value: 145.4900

Market Capitalization: 2360773181000

Recommend Buy: False / Reason: 5 inconsistent increases of 1% from last closing price

Company description: Apple Inc. is an American multinational technology company that specializes in consumer electronics, computer 
software, and online services. Apple is the world's largest technology company by revenue (totalling $274.5 billion in 2020) and, 
since January 2021, the world's most valuable company. As of 2021, Apple is the world's fourth-largest PC vendor by unit sales, and 
fourth-largest smartphone manufacturer. It is one of the Big Five American information technology companies, along with Amazon, 
Google, Microsoft, and Facebook.
-------------------
```
