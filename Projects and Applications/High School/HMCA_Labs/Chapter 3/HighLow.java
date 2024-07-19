/*
Name: Caleb Han
Program: HighLow
Purpose: Plays highlow with user
*/

import java.util.*;

class Main {
  public static void main(String[] args) {
    int player, bot;
    boolean running = true;

    Scanner scan = new Scanner(System.in);
    Random random = new Random();

    while (running) {
      System.out.println("What number do you want to guess: ");
      player = scan.nextInt();
      bot = random.nextInt(10) + 1;
      while (player < 1 || player > 10) {
        System.out.println("Error: invalid input");
        System.out.println("What number do you want to guess: ");
        player = scan.nextInt();
      }
      while (player != bot) {
        if (player > bot) {
          System.out.println("High");
        } else {
          System.out.println("Low");
        }
        System.out.println("What number do you want to guess: ");
        player = scan.nextInt();
      }
      System.out.println("You guessed it!");

      System.out.println("Quit? y/n: ");
      String quit = scan.next().toLowerCase();
      while (!(quit.equals("y") || quit.equals("n"))) {
        System.out.println("Error: invalid input");
        System.out.println("Quit? y/n: ");
        quit = scan.next().toLowerCase();
      }
      if (quit.equals("y")) running = false;
    }
  }
}
