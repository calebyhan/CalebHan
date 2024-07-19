/*
Name: Caleb Han
Program: RiggedCoin
Purpose: Race to 5 heads in a row
*/

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    final double RP = 0.75;
    int rcCounter = 0;
    int rcFinal = 0;
    int cCounter = 0;
    int cFinal = 0;

    RiggedCoin rc1 = new RiggedCoin(RP);
    Coin c1 = new Coin();

    while (rcCounter < 5) {
      rc1.flip();
      if (rc1.toString().equals("Heads")) {
        rcCounter += 1;
      } else {
        rcCounter = 0;
      }
      rcFinal += 1;
    }

    while (cCounter < 5) {
      c1.flip();
      if (c1.toString().equals("Heads")) {
        cCounter += 1;
      } else {
        cCounter = 0;
      }
      cFinal += 1;
    }

    if (rcFinal < cFinal) {
      System.out.println("Rigged coin wins.");
    } else if (rcFinal > cFinal) {
      System.out.println("Normal coin wins.");
    } else {
      System.out.println("Tie.");
    }
    System.out.println("It took the rigged coin " + rcFinal + " tries to get 5 in a row.");
    System.out.println("It took the regular coin " + cFinal + " tries to get 5 in a row.");
  }
}
