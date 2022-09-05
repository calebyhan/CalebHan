/*
Name: Caleb Han
Program: Three
Purpose: Powers of three
*/

import java.util.*;

class Main {
  public static void main(String[] args) {
    int power, current = 1;

    Scanner scan = new Scanner(System.in);

    System.out.println("What power do you want: ");
    power = scan.nextInt();
    while (power < 0) {
      System.out.println("Error: invalid input");
      System.out.println("What power do you want: ");
      power = scan.nextInt();
    }
    if (power != 0) {
      System.out.println("Current power: 0 | Current value: 1");
    }
    for (int i = 0; i < power - 1; i++) {
      current *= 3;
      System.out.println("Current power: " + (i + 1) + " | Current value: " + current);
    }
  }
}
