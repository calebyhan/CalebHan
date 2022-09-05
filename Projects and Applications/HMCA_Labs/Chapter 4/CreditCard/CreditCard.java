import java.util.Scanner;
import java.text.NumberFormat;

public class CreditCard {
  private String accHolder;
  private int ccNum;
  private double prevBal;

  public CreditCard(String a, int n, double b) {
    accHolder = a;
    ccNum = n;
    prevBal = b;
  }

  public void lastInterest() {
    System.out.println("Calculating interest for " + accHolder);
    prevBal *= 1.2;
  }

  public void updateBal() {
    Scanner scan = new Scanner(System.in);
    System.out.println("Do you want to enter a payment for " + accHolder + " (y/n): ");
    String answer = scan.next().toLowerCase();
    while (!(answer.equals("y") || answer.equals("n"))) {
      System.out.println("Error: invalid input");
      System.out.println("Do you want to enter a payment for " + accHolder + " (y/n): ");
      answer = scan.next().toLowerCase();
    }
    if (answer.equals("y")) {
      boolean running = true;
      System.out.println("Enter a payment for " + accHolder + ", 0 to enter none/exit: ");
      double charge = scan.nextDouble();
      while (charge < 0) {
        System.out.println("Error: invalid input");
        System.out.println("Enter a payment for " + accHolder + ", 0 to enter none/exit: ");
        charge = scan.nextDouble();
      }
      prevBal -= charge;
      if (charge == 0) running = false;
      while (running) {
        System.out.println("Enter a payment for " + accHolder + ", 0 to enter none/exit: ");
        charge = scan.nextDouble();
        if (charge == 0) running = false;
        while (charge < 0) {
          System.out.println("Error: invalid input");
          System.out.println("Enter a payment for " + accHolder + ", 0 to enter none/exit: ");
          charge = scan.nextDouble();
          if (charge == 0) running = false;
        }
        prevBal -= charge;
      }
    }
  }

  public void updateCharge() {
    Scanner scan = new Scanner(System.in);
    System.out.println("Do you want to enter a charge for " + accHolder + " (y/n): ");
    String answer = scan.next().toLowerCase();
    while (!(answer.equals("y") || answer.equals("n"))) {
      System.out.println("Error: invalid input");
      System.out.println("Do you want to enter a charge for " + accHolder + " (y/n): ");
      answer = scan.next().toLowerCase();
    }
    if (answer.equals("y")) {
      boolean running = true;
      System.out.println("Enter a charge for " + accHolder + ", 0 to enter none/exit: ");
      double charge = scan.nextDouble();
      while (charge < 0) {
        System.out.println("Error: invalid input");
        System.out.println("Enter a charge for " + accHolder + ", 0 to enter none/exit: ");
        charge = scan.nextDouble();
      }
      prevBal += charge;
      if (charge == 0) running = false;
      while (running) {
        System.out.println("Enter a charge for " + accHolder + ", 0 to enter none/exit: ");
        charge = scan.nextDouble();
        if (charge == 0) running = false;
        while (charge < 0) {
          System.out.println("Error: invalid input");
          System.out.println("Enter a charge for " + accHolder + ", 0 to enter none/exit: ");
          charge = scan.nextDouble();
          if (charge == 0) running = false;
        }
        prevBal += charge;
      }
    }
  }

  public void changeName(String n) {
    accHolder = n;
  }

  public String toString() {
    NumberFormat formatter = NumberFormat.getCurrencyInstance();
    String forBal = formatter.format(prevBal);
    String sCC = "" + ccNum;
    String lastFour = sCC.substring(sCC.length() - 4, (sCC.length()));
    return "Account name: " + accHolder + "\nLast 4 digits: " + lastFour + "\nCredit Card Balance: " + forBal;
  }
}
