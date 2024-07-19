/*
Name: Caleb Han
Program: Factorial
Purpose: Factorial
*/

import java.util.*;

class Main {
  public static void main(String[] args) {
    int factorial, current = 1;

    Scanner scan = new Scanner(System.in);

    System.out.println("What factorial do you want: ");
    factorial = scan.nextInt();
    while (factorial < 0) {
      System.out.println("Error: invalid input");
      System.out.println("What factorial do you want: ");
      factorial = scan.nextInt();
    }

    for (int i = 1; i < factorial + 1; i++) {
      current *= i;
    }

    System.out.println("The factorial of " + factorial + " is " + current);
  }
}
