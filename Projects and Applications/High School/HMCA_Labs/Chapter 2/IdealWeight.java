/*
* Name: Caleb Han
* Purpose of Code: compute the ideal weight for both males and females
*/

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    final int height = 60;
    
    // get input for feet and inches
    System.out.println("How much do you tall in foot: ");
    int feet = scan.nextInt();
    System.out.println("How much do you tall in inches: ");
    int inches = scan.nextInt();
    
    // get workaround for error cases
    if (feet < 5) {
      System.out.println("Error, feet has to be at least 5.");
    } else if (inches > 12) {
      System.out.println("Error, inches has to be below 13.");
    } else {
      inches += feet*12;
      int to_calculate = inches - height;

      // calculate and output values
      System.out.println("If male: " + (106 + to_calculate * 6) + "lb.");
      System.out.println("Acceptable values: " + (106 + to_calculate * 6) * 0.925 + " - " + (106 + to_calculate * 6)  * 1.075 + ".");
      System.out.println("If female: " + (100 + to_calculate * 5) + "lb.");
      System.out.println("Acceptable values: " + (100 + to_calculate * 5) * 0.925 + " - " + (100 + to_calculate * 5)  * 1.075 + ".");
    }
  }
}
