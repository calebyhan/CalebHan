/*
Name: Caleb Han
Program: CreditCard
Purpose: Simulates a credit card
*/

import java.util.*;
import java.text.DecimalFormat;

class Main {
  public static void main(String[] args) {
    double lastBal, interest, newBal, charge;

    Scanner scan = new Scanner(System.in);
    DecimalFormat df = new DecimalFormat("#.##");

    System.out.println("Welcome to the Bank of Mrs. Finchum");

    System.out.println();
    System.out.println("What was your balance last month: ");
    lastBal = scan.nextDouble();
    
    interest = lastBal * .05;

    newBal = lastBal + interest;

    System.out.println("Enter the amount of a charge (enter -1 for none): ");
    charge = scan.nextDouble();
    if (charge != -1) newBal += charge;
    while (charge < 0) {
      System.out.println("Error: invalid input");
      System.out.println("Enter the amount of a charge (enter 0 to exit): ");
      charge = scan.nextDouble();
    }
    while (charge > 0) {
      System.out.println("Enter the amount of a charge (enter -1 to exit): ");
      charge = scan.nextDouble();
      if (charge != -1) {
        while (charge < 0) {
          System.out.println("Error: invalid input");
          System.out.println("Enter the amount of a charge (enter 0 to exit): ");
          charge = scan.nextDouble();
        }
      }
      
      if (charge > 0) newBal += charge;
    }

    if (newBal <= 0) {
      System.out.println("Minimum payment: 0");
    } else if (newBal < 100 && newBal > 0) {
      System.out.println("Minimum payment: 20");
    } else if (newBal >= 100 && newBal <= 500) {
      System.out.println("Minimum payment: 100");
    } else {
      System.out.println("Minimum payment: " + df.format(newBal * 0.75));
    }
  }
}
