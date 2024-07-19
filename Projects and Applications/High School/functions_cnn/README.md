Uses Convoluted Neural Networks (CNN) to recognize various functions such as circles, ellipses, parabolas, and linear functions.

Dataset trained and validated combined from [Fede Herz](https://www.kaggle.com/datasets/fhernand23/simple-shapes) and [Yefeng Xia](https://www.kaggle.com/datasets/kopfgeldjaeger/function-graphs-polynomial).

Example run:
```
Train model? WARNING takes at least 6 hours depending on computer. If not, use given saved model. [y]es/[n]o: n

If circle, ellipse, square root equations, enter [y]es: n
Enter a equation for the ai to guess as (y = ) in terms of x: x+1
1/1 [==============================] - 0s 149ms/step

linear function - 0.9878997206687927
parabolic function - 0.01071228552609682
cubic function - 0.0013856554869562387
```

<details>
  <summary>Layers</summary>
  
  ```
  Model: "sequential1"
  _________________________________________________________________
   Layer (type)                Output Shape              Param #
  =================================================================
   conv2d_3 (Conv2D)           (None, 224, 224, 32)      896

   max_pooling2d_3 (MaxPooling  (None, 112, 112, 32)     0
   2D)

   conv2d_4 (Conv2D)           (None, 112, 112, 32)      9248

   max_pooling2d_4 (MaxPooling  (None, 56, 56, 32)       0
   2D)

   conv2d_5 (Conv2D)           (None, 56, 56, 64)        18496

   max_pooling2d_5 (MaxPooling  (None, 28, 28, 64)       0
   2D)

   dropout_1 (Dropout)         (None, 28, 28, 64)        0

   flatten_1 (Flatten)         (None, 50176)             0

   dense_2 (Dense)             (None, 128)               6422656

   dense3 (Dense)             (None, 7)                 903

  =================================================================
  Total params: 6,452,199
  Trainable params: 6,452,199
  Non-trainable params: 0
  _________________________________________________________________
  ```

</details>

<details>
  <summary>Epochs</summary>

```
Epoch 1/250
196/196 [==============================] - 95s 484ms/step - loss: 1.8226 - accuracy: 0.2064 - val_loss: 1.7394 - val_accuracy: 0.1964
Epoch 2/250
196/196 [==============================] - 96s 488ms/step - loss: 1.7146 - accuracy: 0.2233 - val_loss: 1.6943 - val_accuracy: 0.1964
Epoch 3/250
196/196 [==============================] - 98s 502ms/step - loss: 1.6863 - accuracy: 0.2335 - val_loss: 1.6763 - val_accuracy: 0.1971
Epoch 4/250
196/196 [==============================] - 97s 495ms/step - loss: 1.6724 - accuracy: 0.2512 - val_loss: 1.6639 - val_accuracy: 0.3842
Epoch 5/250
196/196 [==============================] - 101s 514ms/step - loss: 1.6597 - accuracy: 0.2860 - val_loss: 1.6490 - val_accuracy: 0.5404
Epoch 6/250
196/196 [==============================] - 100s 510ms/step - loss: 1.6501 - accuracy: 0.3041 - val_loss: 1.6361 - val_accuracy: 0.6612
Epoch 7/250
196/196 [==============================] - 100s 511ms/step - loss: 1.6360 - accuracy: 0.3453 - val_loss: 1.6199 - val_accuracy: 0.6543
Epoch 8/250
196/196 [==============================] - 106s 540ms/step - loss: 1.6171 - accuracy: 0.3949 - val_loss: 1.6031 - val_accuracy: 0.5641
Epoch 9/250
196/196 [==============================] - 101s 517ms/step - loss: 1.5992 - accuracy: 0.4295 - val_loss: 1.5821 - val_accuracy: 0.7395
Epoch 10/250
196/196 [==============================] - 88s 450ms/step - loss: 1.5802 - accuracy: 0.4766 - val_loss: 1.5554 - val_accuracy: 0.7464
Epoch 11/250
196/196 [==============================] - 88s 448ms/step - loss: 1.5535 - accuracy: 0.5116 - val_loss: 1.5285 - val_accuracy: 0.7474
Epoch 12/250
196/196 [==============================] - 87s 445ms/step - loss: 1.5187 - accuracy: 0.5785 - val_loss: 1.4941 - val_accuracy: 0.7469
Epoch 13/250
196/196 [==============================] - 87s 445ms/step - loss: 1.4806 - accuracy: 0.6375 - val_loss: 1.4539 - val_accuracy: 0.8431
Epoch 14/250
196/196 [==============================] - 87s 445ms/step - loss: 1.4378 - accuracy: 0.6860 - val_loss: 1.4077 - val_accuracy: 0.7957
Epoch 15/250
196/196 [==============================] - 87s 444ms/step - loss: 1.3849 - accuracy: 0.7188 - val_loss: 1.3498 - val_accuracy: 0.8258
Epoch 16/250
196/196 [==============================] - 87s 445ms/step - loss: 1.3267 - accuracy: 0.7491 - val_loss: 1.2923 - val_accuracy: 0.8246
Epoch 17/250
196/196 [==============================] - 87s 445ms/step - loss: 1.2697 - accuracy: 0.7774 - val_loss: 1.2345 - val_accuracy: 0.8206
Epoch 18/250
196/196 [==============================] - 87s 445ms/step - loss: 1.2104 - accuracy: 0.7917 - val_loss: 1.1810 - val_accuracy: 0.8105
Epoch 19/250
196/196 [==============================] - 87s 446ms/step - loss: 1.1541 - accuracy: 0.8097 - val_loss: 1.1222 - val_accuracy: 0.8337
Epoch 20/250
196/196 [==============================] - 87s 444ms/step - loss: 1.0919 - accuracy: 0.8220 - val_loss: 1.0626 - val_accuracy: 0.8579
Epoch 21/250
196/196 [==============================] - 87s 445ms/step - loss: 1.0325 - accuracy: 0.8324 - val_loss: 1.0077 - val_accuracy: 0.8658
Epoch 22/250
196/196 [==============================] - 87s 446ms/step - loss: 0.9746 - accuracy: 0.8407 - val_loss: 0.9541 - val_accuracy: 0.8517
Epoch 23/250
196/196 [==============================] - 88s 447ms/step - loss: 0.9197 - accuracy: 0.8515 - val_loss: 0.9016 - val_accuracy: 0.8653
Epoch 24/250
196/196 [==============================] - 87s 446ms/step - loss: 0.8695 - accuracy: 0.8596 - val_loss: 0.8545 - val_accuracy: 0.8641
Epoch 25/250
196/196 [==============================] - 87s 444ms/step - loss: 0.8223 - accuracy: 0.8657 - val_loss: 0.8088 - val_accuracy: 0.8708
Epoch 26/250
196/196 [==============================] - 87s 445ms/step - loss: 0.7803 - accuracy: 0.8679 - val_loss: 0.7663 - val_accuracy: 0.8754
Epoch 27/250
196/196 [==============================] - 88s 447ms/step - loss: 0.7341 - accuracy: 0.8781 - val_loss: 0.7266 - val_accuracy: 0.8758
Epoch 28/250
196/196 [==============================] - 87s 444ms/step - loss: 0.6921 - accuracy: 0.8826 - val_loss: 0.6871 - val_accuracy: 0.8780
Epoch 29/250
196/196 [==============================] - 87s 444ms/step - loss: 0.6551 - accuracy: 0.8828 - val_loss: 0.6514 - val_accuracy: 0.8828
Epoch 30/250
196/196 [==============================] - 87s 445ms/step - loss: 0.6164 - accuracy: 0.8892 - val_loss: 0.6173 - val_accuracy: 0.8856
Epoch 31/250
196/196 [==============================] - 87s 445ms/step - loss: 0.5833 - accuracy: 0.8928 - val_loss: 0.5879 - val_accuracy: 0.8866
Epoch 32/250
196/196 [==============================] - 87s 445ms/step - loss: 0.5538 - accuracy: 0.8960 - val_loss: 0.5572 - val_accuracy: 0.8916
Epoch 33/250
196/196 [==============================] - 87s 443ms/step - loss: 0.5237 - accuracy: 0.8989 - val_loss: 0.5349 - val_accuracy: 0.8885
Epoch 34/250
196/196 [==============================] - 87s 445ms/step - loss: 0.4975 - accuracy: 0.9002 - val_loss: 0.5214 - val_accuracy: 0.8718
Epoch 35/250
196/196 [==============================] - 87s 443ms/step - loss: 0.4733 - accuracy: 0.9024 - val_loss: 0.4887 - val_accuracy: 0.8952
Epoch 36/250
196/196 [==============================] - 87s 444ms/step - loss: 0.4486 - accuracy: 0.9078 - val_loss: 0.4679 - val_accuracy: 0.8978
Epoch 37/250
196/196 [==============================] - 87s 444ms/step - loss: 0.4271 - accuracy: 0.9123 - val_loss: 0.4509 - val_accuracy: 0.8967
Epoch 38/250
196/196 [==============================] - 87s 444ms/step - loss: 0.4086 - accuracy: 0.9113 - val_loss: 0.4342 - val_accuracy: 0.8969
Epoch 39/250
196/196 [==============================] - 87s 444ms/step - loss: 0.3902 - accuracy: 0.9124 - val_loss: 0.4186 - val_accuracy: 0.8969
Epoch 40/250
196/196 [==============================] - 87s 444ms/step - loss: 0.3717 - accuracy: 0.9167 - val_loss: 0.4040 - val_accuracy: 0.8962
Epoch 41/250
196/196 [==============================] - 87s 446ms/step - loss: 0.3536 - accuracy: 0.9180 - val_loss: 0.3917 - val_accuracy: 0.8967
Epoch 42/250
196/196 [==============================] - 88s 448ms/step - loss: 0.3365 - accuracy: 0.9212 - val_loss: 0.3736 - val_accuracy: 0.9045
Epoch 43/250
196/196 [==============================] - 87s 445ms/step - loss: 0.3235 - accuracy: 0.9242 - val_loss: 0.3609 - val_accuracy: 0.9038
Epoch 44/250
196/196 [==============================] - 87s 445ms/step - loss: 0.3097 - accuracy: 0.9262 - val_loss: 0.3479 - val_accuracy: 0.9108
Epoch 45/250
196/196 [==============================] - 87s 444ms/step - loss: 0.2958 - accuracy: 0.9300 - val_loss: 0.3333 - val_accuracy: 0.9132
Epoch 46/250
196/196 [==============================] - 87s 444ms/step - loss: 0.2829 - accuracy: 0.9324 - val_loss: 0.3285 - val_accuracy: 0.9086
Epoch 47/250
196/196 [==============================] - 87s 443ms/step - loss: 0.2722 - accuracy: 0.9340 - val_loss: 0.3128 - val_accuracy: 0.9172
Epoch 48/250
196/196 [==============================] - 87s 445ms/step - loss: 0.2618 - accuracy: 0.9356 - val_loss: 0.3036 - val_accuracy: 0.9187
Epoch 49/250
196/196 [==============================] - 87s 443ms/step - loss: 0.2511 - accuracy: 0.9370 - val_loss: 0.2951 - val_accuracy: 0.9184
Epoch 50/250
196/196 [==============================] - 87s 445ms/step - loss: 0.2422 - accuracy: 0.9405 - val_loss: 0.2851 - val_accuracy: 0.9225
Epoch 51/250
196/196 [==============================] - 87s 444ms/step - loss: 0.2308 - accuracy: 0.9434 - val_loss: 0.2789 - val_accuracy: 0.9215
Epoch 52/250
196/196 [==============================] - 88s 447ms/step - loss: 0.2248 - accuracy: 0.9408 - val_loss: 0.2768 - val_accuracy: 0.9146
Epoch 53/250
196/196 [==============================] - 87s 445ms/step - loss: 0.2168 - accuracy: 0.9437 - val_loss: 0.2718 - val_accuracy: 0.9136
Epoch 54/250
196/196 [==============================] - 87s 446ms/step - loss: 0.2092 - accuracy: 0.9469 - val_loss: 0.2526 - val_accuracy: 0.9292
Epoch 55/250
196/196 [==============================] - 87s 445ms/step - loss: 0.2031 - accuracy: 0.9488 - val_loss: 0.2489 - val_accuracy: 0.9270
Epoch 56/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1952 - accuracy: 0.9520 - val_loss: 0.2495 - val_accuracy: 0.9225
Epoch 57/250
196/196 [==============================] - 87s 446ms/step - loss: 0.1893 - accuracy: 0.9504 - val_loss: 0.2360 - val_accuracy: 0.9313
Epoch 58/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1827 - accuracy: 0.9552 - val_loss: 0.2302 - val_accuracy: 0.9321
Epoch 59/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1756 - accuracy: 0.9576 - val_loss: 0.2226 - val_accuracy: 0.9347
Epoch 60/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1722 - accuracy: 0.9558 - val_loss: 0.2212 - val_accuracy: 0.9330
Epoch 61/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1656 - accuracy: 0.9573 - val_loss: 0.2144 - val_accuracy: 0.9371
Epoch 62/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1615 - accuracy: 0.9573 - val_loss: 0.2126 - val_accuracy: 0.9349
Epoch 63/250
196/196 [==============================] - 87s 446ms/step - loss: 0.1560 - accuracy: 0.9595 - val_loss: 0.2014 - val_accuracy: 0.9388
Epoch 64/250
196/196 [==============================] - 87s 446ms/step - loss: 0.1518 - accuracy: 0.9622 - val_loss: 0.1976 - val_accuracy: 0.9397
Epoch 65/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1476 - accuracy: 0.9630 - val_loss: 0.1933 - val_accuracy: 0.9416
Epoch 66/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1437 - accuracy: 0.9633 - val_loss: 0.1899 - val_accuracy: 0.9428
Epoch 67/250
196/196 [==============================] - 87s 443ms/step - loss: 0.1378 - accuracy: 0.9671 - val_loss: 0.1845 - val_accuracy: 0.9450
Epoch 68/250
196/196 [==============================] - 87s 446ms/step - loss: 0.1361 - accuracy: 0.9670 - val_loss: 0.1789 - val_accuracy: 0.9474
Epoch 69/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1327 - accuracy: 0.9665 - val_loss: 0.1780 - val_accuracy: 0.9455
Epoch 70/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1284 - accuracy: 0.9692 - val_loss: 0.1791 - val_accuracy: 0.9447
Epoch 71/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1258 - accuracy: 0.9694 - val_loss: 0.1666 - val_accuracy: 0.9529
Epoch 72/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1234 - accuracy: 0.9683 - val_loss: 0.1669 - val_accuracy: 0.9517
Epoch 73/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1201 - accuracy: 0.9702 - val_loss: 0.1616 - val_accuracy: 0.9536
Epoch 74/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1182 - accuracy: 0.9711 - val_loss: 0.1590 - val_accuracy: 0.9555
Epoch 75/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1152 - accuracy: 0.9718 - val_loss: 0.1587 - val_accuracy: 0.9541
Epoch 76/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1110 - accuracy: 0.9729 - val_loss: 0.1574 - val_accuracy: 0.9526
Epoch 77/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1081 - accuracy: 0.9750 - val_loss: 0.1501 - val_accuracy: 0.9569
Epoch 78/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1051 - accuracy: 0.9758 - val_loss: 0.1470 - val_accuracy: 0.9577
Epoch 79/250
196/196 [==============================] - 87s 444ms/step - loss: 0.1037 - accuracy: 0.9746 - val_loss: 0.1444 - val_accuracy: 0.9589
Epoch 80/250
196/196 [==============================] - 87s 445ms/step - loss: 0.1014 - accuracy: 0.9758 - val_loss: 0.1421 - val_accuracy: 0.9600
Epoch 81/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0974 - accuracy: 0.9770 - val_loss: 0.1428 - val_accuracy: 0.9584
Epoch 82/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0962 - accuracy: 0.9774 - val_loss: 0.1371 - val_accuracy: 0.9617
Epoch 83/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0945 - accuracy: 0.9778 - val_loss: 0.1354 - val_accuracy: 0.9620
Epoch 84/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0916 - accuracy: 0.9775 - val_loss: 0.1344 - val_accuracy: 0.9622
Epoch 85/250
196/196 [==============================] - 88s 451ms/step - loss: 0.0912 - accuracy: 0.9791 - val_loss: 0.1279 - val_accuracy: 0.9644
Epoch 86/250
196/196 [==============================] - 88s 448ms/step - loss: 0.0865 - accuracy: 0.9813 - val_loss: 0.1307 - val_accuracy: 0.9627
Epoch 87/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0865 - accuracy: 0.9807 - val_loss: 0.1268 - val_accuracy: 0.9648
Epoch 88/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0830 - accuracy: 0.9818 - val_loss: 0.1219 - val_accuracy: 0.9658
Epoch 89/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0836 - accuracy: 0.9799 - val_loss: 0.1207 - val_accuracy: 0.9663
Epoch 90/250
196/196 [==============================] - 88s 449ms/step - loss: 0.0785 - accuracy: 0.9823 - val_loss: 0.1197 - val_accuracy: 0.9667
Epoch 91/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0784 - accuracy: 0.9826 - val_loss: 0.1182 - val_accuracy: 0.9667
Epoch 92/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0755 - accuracy: 0.9825 - val_loss: 0.1207 - val_accuracy: 0.9641
Epoch 93/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0747 - accuracy: 0.9809 - val_loss: 0.1148 - val_accuracy: 0.9677
Epoch 94/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0739 - accuracy: 0.9829 - val_loss: 0.1122 - val_accuracy: 0.9682
Epoch 95/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0725 - accuracy: 0.9829 - val_loss: 0.1126 - val_accuracy: 0.9679
Epoch 96/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0706 - accuracy: 0.9847 - val_loss: 0.1068 - val_accuracy: 0.9711
Epoch 97/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0677 - accuracy: 0.9842 - val_loss: 0.1055 - val_accuracy: 0.9713
Epoch 98/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0682 - accuracy: 0.9829 - val_loss: 0.1054 - val_accuracy: 0.9701
Epoch 99/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0663 - accuracy: 0.9844 - val_loss: 0.1033 - val_accuracy: 0.9720
Epoch 100/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0644 - accuracy: 0.9863 - val_loss: 0.1007 - val_accuracy: 0.9730
Epoch 101/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0628 - accuracy: 0.9864 - val_loss: 0.1019 - val_accuracy: 0.9727
Epoch 102/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0616 - accuracy: 0.9848 - val_loss: 0.0984 - val_accuracy: 0.9734
Epoch 103/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0609 - accuracy: 0.9866 - val_loss: 0.0989 - val_accuracy: 0.9727
Epoch 104/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0593 - accuracy: 0.9864 - val_loss: 0.0950 - val_accuracy: 0.9746
Epoch 105/250
196/196 [==============================] - 88s 448ms/step - loss: 0.0596 - accuracy: 0.9876 - val_loss: 0.0940 - val_accuracy: 0.9749
Epoch 106/250
196/196 [==============================] - 88s 451ms/step - loss: 0.0580 - accuracy: 0.9864 - val_loss: 0.0925 - val_accuracy: 0.9751
Epoch 107/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0554 - accuracy: 0.9882 - val_loss: 0.0928 - val_accuracy: 0.9754
Epoch 108/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0550 - accuracy: 0.9876 - val_loss: 0.0903 - val_accuracy: 0.9756
Epoch 109/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0538 - accuracy: 0.9874 - val_loss: 0.0901 - val_accuracy: 0.9758
Epoch 110/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0533 - accuracy: 0.9892 - val_loss: 0.0905 - val_accuracy: 0.9768
Epoch 111/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0518 - accuracy: 0.9898 - val_loss: 0.0909 - val_accuracy: 0.9768
Epoch 112/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0517 - accuracy: 0.9893 - val_loss: 0.0856 - val_accuracy: 0.9768
Epoch 113/250
196/196 [==============================] - 87s 443ms/step - loss: 0.0495 - accuracy: 0.9898 - val_loss: 0.0866 - val_accuracy: 0.9775
Epoch 114/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0498 - accuracy: 0.9880 - val_loss: 0.0831 - val_accuracy: 0.9770
Epoch 115/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0469 - accuracy: 0.9906 - val_loss: 0.0834 - val_accuracy: 0.9773
Epoch 116/250
196/196 [==============================] - 87s 443ms/step - loss: 0.0470 - accuracy: 0.9903 - val_loss: 0.0830 - val_accuracy: 0.9785
Epoch 117/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0464 - accuracy: 0.9904 - val_loss: 0.0823 - val_accuracy: 0.9787
Epoch 118/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0460 - accuracy: 0.9907 - val_loss: 0.0808 - val_accuracy: 0.9785
Epoch 119/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0455 - accuracy: 0.9895 - val_loss: 0.0796 - val_accuracy: 0.9789
Epoch 120/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0443 - accuracy: 0.9914 - val_loss: 0.0796 - val_accuracy: 0.9792
Epoch 121/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0442 - accuracy: 0.9911 - val_loss: 0.0780 - val_accuracy: 0.9792
Epoch 122/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0437 - accuracy: 0.9912 - val_loss: 0.0769 - val_accuracy: 0.9799
Epoch 123/250
196/196 [==============================] - 96s 488ms/step - loss: 0.0421 - accuracy: 0.9919 - val_loss: 0.0751 - val_accuracy: 0.9801
Epoch 124/250
196/196 [==============================] - 94s 479ms/step - loss: 0.0417 - accuracy: 0.9922 - val_loss: 0.0750 - val_accuracy: 0.9806
Epoch 125/250
196/196 [==============================] - 91s 464ms/step - loss: 0.0402 - accuracy: 0.9928 - val_loss: 0.0762 - val_accuracy: 0.9801
Epoch 126/250
196/196 [==============================] - 88s 452ms/step - loss: 0.0397 - accuracy: 0.9915 - val_loss: 0.0745 - val_accuracy: 0.9809
Epoch 127/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0387 - accuracy: 0.9919 - val_loss: 0.0746 - val_accuracy: 0.9804
Epoch 128/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0397 - accuracy: 0.9915 - val_loss: 0.0742 - val_accuracy: 0.9806
Epoch 129/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0377 - accuracy: 0.9928 - val_loss: 0.0719 - val_accuracy: 0.9813
Epoch 130/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0376 - accuracy: 0.9927 - val_loss: 0.0703 - val_accuracy: 0.9823
Epoch 131/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0368 - accuracy: 0.9928 - val_loss: 0.0718 - val_accuracy: 0.9821
Epoch 132/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0368 - accuracy: 0.9922 - val_loss: 0.0720 - val_accuracy: 0.9828
Epoch 133/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0354 - accuracy: 0.9936 - val_loss: 0.0691 - val_accuracy: 0.9828
Epoch 134/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0351 - accuracy: 0.9930 - val_loss: 0.0696 - val_accuracy: 0.9825
Epoch 135/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0345 - accuracy: 0.9938 - val_loss: 0.0679 - val_accuracy: 0.9830
Epoch 136/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0338 - accuracy: 0.9939 - val_loss: 0.0676 - val_accuracy: 0.9828
Epoch 137/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0351 - accuracy: 0.9925 - val_loss: 0.0658 - val_accuracy: 0.9835
Epoch 138/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0327 - accuracy: 0.9939 - val_loss: 0.0662 - val_accuracy: 0.9835
Epoch 139/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0325 - accuracy: 0.9951 - val_loss: 0.0666 - val_accuracy: 0.9833
Epoch 140/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0299 - accuracy: 0.9947 - val_loss: 0.0652 - val_accuracy: 0.9835
Epoch 141/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0324 - accuracy: 0.9938 - val_loss: 0.0660 - val_accuracy: 0.9837
Epoch 142/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0299 - accuracy: 0.9946 - val_loss: 0.0658 - val_accuracy: 0.9840
Epoch 143/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0302 - accuracy: 0.9943 - val_loss: 0.0635 - val_accuracy: 0.9849
Epoch 144/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0298 - accuracy: 0.9949 - val_loss: 0.0640 - val_accuracy: 0.9842
Epoch 145/250
196/196 [==============================] - 88s 448ms/step - loss: 0.0299 - accuracy: 0.9949 - val_loss: 0.0641 - val_accuracy: 0.9847
Epoch 146/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0296 - accuracy: 0.9944 - val_loss: 0.0629 - val_accuracy: 0.9844
Epoch 147/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0284 - accuracy: 0.9952 - val_loss: 0.0614 - val_accuracy: 0.9861
Epoch 148/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0282 - accuracy: 0.9947 - val_loss: 0.0614 - val_accuracy: 0.9861
Epoch 149/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0283 - accuracy: 0.9947 - val_loss: 0.0623 - val_accuracy: 0.9854
Epoch 150/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0272 - accuracy: 0.9943 - val_loss: 0.0613 - val_accuracy: 0.9856
Epoch 151/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0262 - accuracy: 0.9949 - val_loss: 0.0593 - val_accuracy: 0.9864
Epoch 152/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0266 - accuracy: 0.9960 - val_loss: 0.0596 - val_accuracy: 0.9861
Epoch 153/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0254 - accuracy: 0.9952 - val_loss: 0.0599 - val_accuracy: 0.9864
Epoch 154/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0255 - accuracy: 0.9955 - val_loss: 0.0604 - val_accuracy: 0.9861
Epoch 155/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0253 - accuracy: 0.9960 - val_loss: 0.0617 - val_accuracy: 0.9856
Epoch 156/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0259 - accuracy: 0.9955 - val_loss: 0.0603 - val_accuracy: 0.9861
Epoch 157/250
196/196 [==============================] - 87s 443ms/step - loss: 0.0244 - accuracy: 0.9952 - val_loss: 0.0583 - val_accuracy: 0.9864
Epoch 158/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0237 - accuracy: 0.9957 - val_loss: 0.0580 - val_accuracy: 0.9868
Epoch 159/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0230 - accuracy: 0.9960 - val_loss: 0.0574 - val_accuracy: 0.9866
Epoch 160/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0236 - accuracy: 0.9955 - val_loss: 0.0579 - val_accuracy: 0.9864
Epoch 161/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0229 - accuracy: 0.9957 - val_loss: 0.0564 - val_accuracy: 0.9864
Epoch 162/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0228 - accuracy: 0.9965 - val_loss: 0.0567 - val_accuracy: 0.9868
Epoch 163/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0219 - accuracy: 0.9970 - val_loss: 0.0560 - val_accuracy: 0.9868
Epoch 164/250
196/196 [==============================] - 88s 452ms/step - loss: 0.0215 - accuracy: 0.9962 - val_loss: 0.0569 - val_accuracy: 0.9864
Epoch 165/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0225 - accuracy: 0.9955 - val_loss: 0.0554 - val_accuracy: 0.9871
Epoch 166/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0213 - accuracy: 0.9960 - val_loss: 0.0562 - val_accuracy: 0.9864
Epoch 167/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0218 - accuracy: 0.9963 - val_loss: 0.0550 - val_accuracy: 0.9871
Epoch 168/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0212 - accuracy: 0.9967 - val_loss: 0.0563 - val_accuracy: 0.9866
Epoch 169/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0203 - accuracy: 0.9967 - val_loss: 0.0552 - val_accuracy: 0.9864
Epoch 170/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0203 - accuracy: 0.9967 - val_loss: 0.0536 - val_accuracy: 0.9876
Epoch 171/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0195 - accuracy: 0.9971 - val_loss: 0.0538 - val_accuracy: 0.9876
Epoch 172/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0199 - accuracy: 0.9967 - val_loss: 0.0538 - val_accuracy: 0.9868
Epoch 173/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0198 - accuracy: 0.9962 - val_loss: 0.0534 - val_accuracy: 0.9880
Epoch 174/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0192 - accuracy: 0.9962 - val_loss: 0.0528 - val_accuracy: 0.9876
Epoch 175/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0185 - accuracy: 0.9967 - val_loss: 0.0525 - val_accuracy: 0.9883
Epoch 176/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0188 - accuracy: 0.9960 - val_loss: 0.0522 - val_accuracy: 0.9883
Epoch 177/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0189 - accuracy: 0.9963 - val_loss: 0.0526 - val_accuracy: 0.9876
Epoch 178/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0182 - accuracy: 0.9971 - val_loss: 0.0512 - val_accuracy: 0.9880
Epoch 179/250
196/196 [==============================] - 87s 443ms/step - loss: 0.0178 - accuracy: 0.9965 - val_loss: 0.0550 - val_accuracy: 0.9873
Epoch 180/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0174 - accuracy: 0.9971 - val_loss: 0.0513 - val_accuracy: 0.9876
Epoch 181/250
196/196 [==============================] - 88s 452ms/step - loss: 0.0171 - accuracy: 0.9971 - val_loss: 0.0525 - val_accuracy: 0.9866
Epoch 182/250
196/196 [==============================] - 86s 438ms/step - loss: 0.0183 - accuracy: 0.9968 - val_loss: 0.0515 - val_accuracy: 0.9878
Epoch 183/250
196/196 [==============================] - 86s 441ms/step - loss: 0.0167 - accuracy: 0.9968 - val_loss: 0.0514 - val_accuracy: 0.9878
Epoch 184/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0165 - accuracy: 0.9971 - val_loss: 0.0524 - val_accuracy: 0.9873
Epoch 185/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0170 - accuracy: 0.9965 - val_loss: 0.0514 - val_accuracy: 0.9878
Epoch 186/250
196/196 [==============================] - 88s 448ms/step - loss: 0.0162 - accuracy: 0.9974 - val_loss: 0.0501 - val_accuracy: 0.9888
Epoch 187/250
196/196 [==============================] - 88s 449ms/step - loss: 0.0166 - accuracy: 0.9971 - val_loss: 0.0499 - val_accuracy: 0.9880
Epoch 188/250
196/196 [==============================] - 88s 451ms/step - loss: 0.0150 - accuracy: 0.9974 - val_loss: 0.0497 - val_accuracy: 0.9883
Epoch 189/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0154 - accuracy: 0.9976 - val_loss: 0.0495 - val_accuracy: 0.9883
Epoch 190/250
196/196 [==============================] - 87s 444ms/step - loss: 0.0156 - accuracy: 0.9979 - val_loss: 0.0503 - val_accuracy: 0.9883
Epoch 191/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0152 - accuracy: 0.9978 - val_loss: 0.0487 - val_accuracy: 0.9885
Epoch 192/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0147 - accuracy: 0.9979 - val_loss: 0.0493 - val_accuracy: 0.9885
Epoch 193/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0143 - accuracy: 0.9982 - val_loss: 0.0490 - val_accuracy: 0.9888
Epoch 194/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0144 - accuracy: 0.9974 - val_loss: 0.0482 - val_accuracy: 0.9888
Epoch 195/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0142 - accuracy: 0.9973 - val_loss: 0.0484 - val_accuracy: 0.9890
Epoch 196/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0136 - accuracy: 0.9979 - val_loss: 0.0480 - val_accuracy: 0.9890
Epoch 197/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0147 - accuracy: 0.9976 - val_loss: 0.0483 - val_accuracy: 0.9885
Epoch 198/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0133 - accuracy: 0.9974 - val_loss: 0.0484 - val_accuracy: 0.9890
Epoch 199/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0135 - accuracy: 0.9974 - val_loss: 0.0505 - val_accuracy: 0.9888
Epoch 200/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0129 - accuracy: 0.9978 - val_loss: 0.0476 - val_accuracy: 0.9890
Epoch 201/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0131 - accuracy: 0.9978 - val_loss: 0.0476 - val_accuracy: 0.9892
Epoch 202/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0127 - accuracy: 0.9978 - val_loss: 0.0478 - val_accuracy: 0.9892
Epoch 203/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0124 - accuracy: 0.9979 - val_loss: 0.0471 - val_accuracy: 0.9890
Epoch 204/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0124 - accuracy: 0.9979 - val_loss: 0.0468 - val_accuracy: 0.9892
Epoch 205/250
196/196 [==============================] - 88s 450ms/step - loss: 0.0113 - accuracy: 0.9981 - val_loss: 0.0474 - val_accuracy: 0.9890
Epoch 206/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0125 - accuracy: 0.9978 - val_loss: 0.0469 - val_accuracy: 0.9892
Epoch 207/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0118 - accuracy: 0.9979 - val_loss: 0.0464 - val_accuracy: 0.9892
Epoch 208/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0123 - accuracy: 0.9974 - val_loss: 0.0468 - val_accuracy: 0.9892
Epoch 209/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0118 - accuracy: 0.9974 - val_loss: 0.0466 - val_accuracy: 0.9890
Epoch 210/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0114 - accuracy: 0.9979 - val_loss: 0.0465 - val_accuracy: 0.9895
Epoch 211/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0110 - accuracy: 0.9979 - val_loss: 0.0474 - val_accuracy: 0.9892
Epoch 212/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0107 - accuracy: 0.9981 - val_loss: 0.0464 - val_accuracy: 0.9895
Epoch 213/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0107 - accuracy: 0.9984 - val_loss: 0.0456 - val_accuracy: 0.9892
Epoch 214/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0107 - accuracy: 0.9981 - val_loss: 0.0463 - val_accuracy: 0.9895
Epoch 215/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0105 - accuracy: 0.9981 - val_loss: 0.0465 - val_accuracy: 0.9892
Epoch 216/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0101 - accuracy: 0.9982 - val_loss: 0.0456 - val_accuracy: 0.9900
Epoch 217/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0101 - accuracy: 0.9982 - val_loss: 0.0452 - val_accuracy: 0.9895
Epoch 218/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0103 - accuracy: 0.9981 - val_loss: 0.0455 - val_accuracy: 0.9897
Epoch 219/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0097 - accuracy: 0.9984 - val_loss: 0.0453 - val_accuracy: 0.9895
Epoch 220/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0096 - accuracy: 0.9982 - val_loss: 0.0451 - val_accuracy: 0.9883
Epoch 221/250
196/196 [==============================] - 89s 454ms/step - loss: 0.0096 - accuracy: 0.9984 - val_loss: 0.0453 - val_accuracy: 0.9897
Epoch 222/250
196/196 [==============================] - 88s 449ms/step - loss: 0.0093 - accuracy: 0.9982 - val_loss: 0.0448 - val_accuracy: 0.9900
Epoch 223/250
196/196 [==============================] - 88s 448ms/step - loss: 0.0093 - accuracy: 0.9986 - val_loss: 0.0451 - val_accuracy: 0.9895
Epoch 224/250
196/196 [==============================] - 88s 448ms/step - loss: 0.0087 - accuracy: 0.9987 - val_loss: 0.0446 - val_accuracy: 0.9900
Epoch 225/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0091 - accuracy: 0.9986 - val_loss: 0.0443 - val_accuracy: 0.9897
Epoch 226/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0087 - accuracy: 0.9984 - val_loss: 0.0447 - val_accuracy: 0.9902
Epoch 227/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0092 - accuracy: 0.9984 - val_loss: 0.0449 - val_accuracy: 0.9897
Epoch 228/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0091 - accuracy: 0.9987 - val_loss: 0.0464 - val_accuracy: 0.9902
Epoch 229/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0090 - accuracy: 0.9981 - val_loss: 0.0446 - val_accuracy: 0.9897
Epoch 230/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0082 - accuracy: 0.9987 - val_loss: 0.0451 - val_accuracy: 0.9902
Epoch 231/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0081 - accuracy: 0.9989 - val_loss: 0.0450 - val_accuracy: 0.9897
Epoch 232/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0085 - accuracy: 0.9981 - val_loss: 0.0447 - val_accuracy: 0.9900
Epoch 233/250
196/196 [==============================] - 88s 448ms/step - loss: 0.0077 - accuracy: 0.9987 - val_loss: 0.0450 - val_accuracy: 0.9902
Epoch 234/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0075 - accuracy: 0.9989 - val_loss: 0.0445 - val_accuracy: 0.9897
Epoch 235/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0079 - accuracy: 0.9984 - val_loss: 0.0436 - val_accuracy: 0.9897
Epoch 236/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0075 - accuracy: 0.9989 - val_loss: 0.0435 - val_accuracy: 0.9900
Epoch 237/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0074 - accuracy: 0.9986 - val_loss: 0.0443 - val_accuracy: 0.9897
Epoch 238/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0071 - accuracy: 0.9989 - val_loss: 0.0438 - val_accuracy: 0.9900
Epoch 239/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0074 - accuracy: 0.9987 - val_loss: 0.0435 - val_accuracy: 0.9900
Epoch 240/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0069 - accuracy: 0.9990 - val_loss: 0.0443 - val_accuracy: 0.9897
Epoch 241/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0067 - accuracy: 0.9986 - val_loss: 0.0432 - val_accuracy: 0.9900
Epoch 242/250
196/196 [==============================] - 87s 447ms/step - loss: 0.0066 - accuracy: 0.9992 - val_loss: 0.0437 - val_accuracy: 0.9904
Epoch 243/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0067 - accuracy: 0.9987 - val_loss: 0.0438 - val_accuracy: 0.9902
Epoch 244/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0068 - accuracy: 0.9986 - val_loss: 0.0441 - val_accuracy: 0.9897
Epoch 245/250
196/196 [==============================] - 88s 447ms/step - loss: 0.0062 - accuracy: 0.9987 - val_loss: 0.0433 - val_accuracy: 0.9902
Epoch 246/250
196/196 [==============================] - 88s 449ms/step - loss: 0.0059 - accuracy: 0.9992 - val_loss: 0.0437 - val_accuracy: 0.9900
Epoch 247/250
196/196 [==============================] - 88s 448ms/step - loss: 0.0061 - accuracy: 0.9987 - val_loss: 0.0429 - val_accuracy: 0.9900
Epoch 248/250
196/196 [==============================] - 87s 445ms/step - loss: 0.0065 - accuracy: 0.9992 - val_loss: 0.0430 - val_accuracy: 0.9900
Epoch 249/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0060 - accuracy: 0.9992 - val_loss: 0.0431 - val_accuracy: 0.9900
Epoch 250/250
196/196 [==============================] - 87s 446ms/step - loss: 0.0060 - accuracy: 0.9992 - val_loss: 0.0434 - val_accuracy: 0.9904
```

</details>

Validation accuracy: 99.04%

![Epochs](https://cdn.discordapp.com/attachments/905301278647783428/1065400297205280858/w48SQSqu3VJQAAAABJRU5ErkJggg.png)
