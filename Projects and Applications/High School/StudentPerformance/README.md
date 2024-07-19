[Dataset by Jakki Seshapanpu](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

`summary(data)`
```
    gender          race.ethnicity     parental.level.of.education
 Length:1000        Length:1000        Length:1000
 Class :character   Class :character   Class :character
 Mode  :character   Mode  :character   Mode  :character



    lunch           test.preparation.course   math.score     reading.score   
 Length:1000        Length:1000             Min.   :  0.00   Min.   : 17.00  
 Class :character   Class :character        1st Qu.: 57.00   1st Qu.: 59.00
 Mode  :character   Mode  :character        Median : 66.00   Median : 70.00  
                                            Mean   : 66.09   Mean   : 69.17  
                                            3rd Qu.: 77.00   3rd Qu.: 79.00
                                            Max.   :100.00   Max.   :100.00  
 writing.score
 Min.   : 10.00  
 1st Qu.: 57.75
 Median : 69.00
 Mean   : 68.05
 3rd Qu.: 79.00  
 Max.   :100.00
 ```

Linear Regression of Gender vs Math
```
Residuals:
    Min      1Q  Median      3Q     Max 
-0.6698 -0.4760 -0.3070  0.5019  0.7345

Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
(Intercept)     0.115975   0.069758   1.663   0.0967 .
data$math.score 0.005538   0.001029   5.383 9.12e-08 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.4931 on 998 degrees of freedom
Multiple R-squared:  0.02822,   Adjusted R-squared:  0.02724
F-statistic: 28.98 on 1 and 998 DF,  p-value: 9.12e-08
```

Linear Regression of Gender vs Reading
```
Residuals:
    Min      1Q  Median      3Q     Max
-0.9184 -0.4500 -0.2492  0.4852  0.7759 

Coefficients:
                    Estimate Std. Error t value Pr(>|t|)
(Intercept)         1.060635   0.074299  14.275  < 2e-16 ***
data$reading.score -0.008366   0.001051  -7.959 4.68e-15 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.485 on 998 degrees of freedom
Multiple R-squared:  0.05969,   Adjusted R-squared:  0.05875
F-statistic: 63.35 on 1 and 998 DF,  p-value: 4.681e-15
```

Linear Regression of Gender vs Writing
```
Residuals:
    Min      1Q  Median      3Q     Max 
-1.0573 -0.4330 -0.1902  0.4679  0.8346

Coefficients:
                    Estimate Std. Error t value Pr(>|t|)
(Intercept)         1.156421   0.069243   16.70   <2e-16 ***
data$writing.score -0.009910   0.000993   -9.98   <2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.4769 on 998 degrees of freedom
Multiple R-squared:  0.09074,   Adjusted R-squared:  0.08983
F-statistic: 99.59 on 1 and 998 DF,  p-value: < 2.2e-16
```

Linear Regression of Lunch vs Math
```
Residuals:
    Min      1Q  Median      3Q     Max
-1.0207 -0.4668  0.1898  0.3560  0.8767 

Coefficients:
                  Estimate Std. Error t value Pr(>|t|)
(Intercept)     -0.0871625  0.0634583  -1.374     0.17
data$math.score  0.0110784  0.0009359  11.837   <2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.4485 on 998 degrees of freedom
Multiple R-squared:  0.1231,    Adjusted R-squared:  0.1222
F-statistic: 140.1 on 1 and 998 DF,  p-value: < 2.2e-16
```

Linear Regression of Lunch vs Reading
```
Residuals:
    Min      1Q  Median      3Q     Max
-0.8771 -0.5534  0.2509  0.3638  0.6800

Coefficients:
                   Estimate Std. Error t value Pr(>|t|)
(Intercept)        0.124332   0.071417   1.741    0.082 .  
data$reading.score 0.007527   0.001010   7.451    2e-13 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.4662 on 998 degrees of freedom
Multiple R-squared:  0.0527,    Adjusted R-squared:  0.05175
F-statistic: 55.52 on 1 and 998 DF,  p-value: 2.003e-13
```

Linear Regression of Lunch vs Writing
```
Residuals:
    Min      1Q  Median      3Q     Max
-0.8924 -0.5362  0.2470  0.3554  0.7116 

Coefficients:
                    Estimate Std. Error t value Pr(>|t|)
(Intercept)        0.1180469  0.0674072   1.751   0.0802 .  
data$writing.score 0.0077432  0.0009667   8.010 3.19e-15 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.4643 on 998 degrees of freedom
Multiple R-squared:  0.0604,    Adjusted R-squared:  0.05946
F-statistic: 64.16 on 1 and 998 DF,  p-value: 3.186e-15
```

Linear Regression of Test Prep vs Math
```
Residuals:
    Min      1Q  Median      3Q     Max
-0.6698 -0.4760 -0.3070  0.5019  0.7345

Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
(Intercept)     0.115975   0.069758   1.663   0.0967 .
data$math.score 0.005538   0.001029   5.383 9.12e-08 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.4931 on 998 degrees of freedom
Multiple R-squared:  0.02822,   Adjusted R-squared:  0.02724
F-statistic: 28.98 on 1 and 998 DF,  p-value: 9.12e-08
```

Linear Regression of Test Prep vs Reading
```
Residuals:
    Min      1Q  Median      3Q     Max
-0.9184 -0.4500 -0.2492  0.4852  0.7759 

Coefficients:
                    Estimate Std. Error t value Pr(>|t|)
(Intercept)         1.060635   0.074299  14.275  < 2e-16 ***
data$reading.score -0.008366   0.001051  -7.959 4.68e-15 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.485 on 998 degrees of freedom
Multiple R-squared:  0.05969,   Adjusted R-squared:  0.05875 
F-statistic: 63.35 on 1 and 998 DF,  p-value: 4.681e-15
```

Linear Regression of Test Prep vs Writing
```
Residuals:
    Min      1Q  Median      3Q     Max 
-1.0573 -0.4330 -0.1902  0.4679  0.8346

Coefficients:
                    Estimate Std. Error t value Pr(>|t|)
(Intercept)         1.156421   0.069243   16.70   <2e-16 ***
data$writing.score -0.009910   0.000993   -9.98   <2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.4769 on 998 degrees of freedom
Multiple R-squared:  0.09074,   Adjusted R-squared:  0.08983
F-statistic: 99.59 on 1 and 998 DF,  p-value: < 2.2e-16
```

Math vs Reading
![Math vs Reading](https://cdn.discordapp.com/attachments/905301278647783428/1068283399548190760/plot.png)

Math vs Writing
![Math vs Writing](https://cdn.discordapp.com/attachments/905301278647783428/1068283892710264893/plot.png)

Reading vs Writing
![Reading vs Writing](https://cdn.discordapp.com/attachments/905301278647783428/1068284142560751636/plot.png)
