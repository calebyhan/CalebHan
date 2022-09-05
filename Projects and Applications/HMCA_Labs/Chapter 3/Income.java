/*
Name: Caleb Han
Program: Income
Purpose: Calculate new income
*/

import java.util.*;
import java.text.DecimalFormat;

class Main {
  public static void main(String[] args) {
    double income;
    final double perfect = 1.07, good = 1.04, bad = 1.02;

    Scanner scan = new Scanner(System.in);
    DecimalFormat df = new DecimalFormat("#.##");

    System.out.println("Type your income: ");
    income = scan.nextDouble();
    while (income < 0) {
      System.out.println("Error: invalid input");
      System.out.println("Type your income: ");
      income = scan.nextDouble();
    }

    System.out.println("Type your rating: perfect, good, bad (p, g, b): ");
    String rating = scan.next().toLowerCase();

    while (!(rating.equals("p") || rating.equals("g") || rating.equals("b"))) {
      System.out.println("Error: invalid input");
      System.out.println("Type your rating: perfect, good, bad (p, g, b): ");
      rating = scan.next().toLowerCase();
    }
    System.out.println("Previous income: " + income);
    if (rating.equals("p")) {
      rating = "perfect";
      income *= perfect;
    } else if (rating.equals("g")) {
      rating = "good";
      income *= good;
    } else {
      rating = "bad";
      income *= bad;
    }
    System.out.println("Rating: " + rating);
    System.out.println("Updated income: " + df.format(income));
  }
}
