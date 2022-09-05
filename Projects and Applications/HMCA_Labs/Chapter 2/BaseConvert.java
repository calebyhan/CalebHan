/*
Name: Caleb Han
Purpose:Converts base 10 numbers to another base (at most 4 digits in the other base). The base 10 number and the base are input.
*/

import java.util.Scanner;

public class Main {
  public static void main (String[] args) {
  int base; // the new base
  int base10Num; // the number in base 10
  int maxNumber; // the maximum number that will fit in 4 digits in the new base
  int place0; // digit in the 1's (base^0) place
  int place1; // digit in the base^1 place
  int place2; // digit in the base^2 place
  int place3; // digit in the base^3 place
  String baseBNum = new String (""); // the number in the new base
  Scanner scan = new Scanner(System.in);
    
  // read in the base 10 number and the base
  System.out.println();
  System.out.println ("Base Conversion Program");
  System.out.println();
  System.out.print ("Please enter a base (2 - 9): ");
  base = scan.nextInt();
    
  // Compute the maximum base 10 number that will fit in 4 digits
  // in the new base and tell the user what range the number they
  // want to convert must be in
  maxNumber = (int)Math.pow(base, 4) - 1;
  System.out.print ("Please enter a base 10 number to convert: ");
  base10Num = scan.nextInt();

  // First compute place0 -- the units place. Remember this comes
  // from the first division so it is the remainder when the
  // base 10 number is divided by the base (HINT %).
  place0 = base10Num % base;
    
  // Then compute the quotient (integer division / will do it!) -
  base10Num /= base;
    
  // You can either store the result back in base10Num or declare a
  // new variable for the quotient
  // Now compute place1 -- this is the remainder when the quotient
  place1 = base10Num % base;
    
  // from the preceding step is divided by the base.
  // Then compute the new quotient
  base10Num /= base;
    
  // Repeat the idea from above to compute place2 and the next quotient
  place2 = base10Num % base;
  base10Num /= base;
    
  // Repeat again to compute place3
  place3 = base10Num % base;
  base10Num /= base;
    
  // Print the result (see notes in lab)
  baseBNum = baseBNum + place3 + place2 + place1 + place0;
  System.out.println(baseBNum);
  }
}
