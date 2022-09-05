/*
* Name: Caleb Han
* Purpose of Code: calculate area and circumference of circle
*/

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    
    final double PI = 3.14159;
    
    System.out.println("Please enter a value for the radius: ");
    int radius = scan.nextInt();
    
    double area1;
    double circumference1;
    double area2;
    double circumference2;
    
    area1 = Math.PI * Math.pow(radius, 2);
    circumference1 = 2 * Math.PI * radius; 
    
    System.out.println("The area of a circle with radius " + radius +
    " is " + area1);
    System.out.println("The circumference of a circle with radius " + radius +
    " is " + circumference1);
    
    radius *= 2;
    area2 = Math.PI * Math.pow(radius, 2);
    circumference2 = 2 * Math. PI * radius;
    
    System.out.println("The area of a circle with radius " + radius +
    " is " + area2);
    System.out.println("The circumference of a circle with radius " + radius +
    " is " + circumference2);
    
    double areaRatio = area2 / area1;
    double circumferenceRatio = circumference2 / circumference1;
    
    System.out.println("The ratio of the areas: " + areaRatio);
    System.out.println("The ratio of the circumferences: " + circumferenceRatio);
  }
}
