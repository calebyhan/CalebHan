/*
* Name: Caleb Han
* Purpose of Code: Determine how much paint is needed to paint the walls of a room given its length, width, and height
*/

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    final int COVERAGE = 350; //paint covers 350 sq ft/gal
    
    //declare integers length, width, and height;
    int length, width, height, doors, windows;
    
    //declare double totalSqFt;
    double totalSqFt;
    
    //declare double paintNeeded;
    double paintNeeded;
    
    //declare and initialize Scanner object
    Scanner scan = new Scanner(System.in);
    
    //Prompt for and read in the length of the room
    System.out.println("Input the length: ");
    length = scan.nextInt();
    
    //Prompt for and read in the width of the room
    System.out.println("Input the width: ");
    width = scan.nextInt();
    
    //Prompt for and read in the height of the room
    System.out.println("Input the height: ");
    height = scan.nextInt();
    System.out.println("How many windows: ");
    windows = scan.nextInt();
    System.out.println("How many doors: ");
    doors = scan.nextInt();
    
    //Compute the total square feet to be painted--think
    //about the dimensions of each wall
    totalSqFt = (2 * (height * width) + 2 * (height * length));
    totalSqFt -= ((20 * doors) + (15 * windows));
    
    //Compute the amount of paint needed
    paintNeeded = (int)(totalSqFt / COVERAGE + 0.99);
    
    //Print the length, width, and height of the room and the
    //number of gallons of paint needed.
    System.out.println("With length of " + length + ", width of " + width + ", height of " + height + ", " + windows + " windows, " + doors + " doors, the total paint needed is " + paintNeeded + ".");
  }
}
