/*
Name: Caleb Han
Program: Vowels
Purpose: Counts number of vowels in sentence
*/

import java.util.*;

class Main {
  public static void main(String[] args) {
    boolean running = true;

    Scanner scan = new Scanner(System.in);

    while (running) {
      System.out.println("Enter a sentence: ");
      String sentence = scan.nextLine().toLowerCase();
      int count = 0;
      for (int i = 0; i < sentence.length(); i++) {
        if (sentence.charAt(i) == 'a' || sentence.charAt(i) == 'e' || sentence.charAt(i) == 'i' || sentence.charAt(i) == 'o' || sentence.charAt(i) == 'u') {
          count++;
        }
      }
      System.out.println("Number of vowels: " + count);
      System.out.println("Quit? y/n: ");
      String quit = scan.nextLine().toLowerCase();
      while (!(quit.equals("y") || quit.equals("n"))) {
        System.out.println("Error: invalid input");
        System.out.println("Quit? y/n: ");
        quit = scan.nextLine().toLowerCase();
      }
      if (quit.equals("y")) running = false;
    }
  }
}
