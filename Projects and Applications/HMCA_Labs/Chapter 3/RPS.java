/*
Name: Caleb Han
Program: RPS
Purpose: Rock Paper Scissors
*/

import java.util.*;

class Main {
  public static void main(String[] args) {
    boolean running = true;
    String bot;

    Scanner scan = new Scanner(System.in);
    Random random = new Random();

    while (running) {
      System.out.println("What will you play: (r, p, s) ");
      String player = scan.next().toLowerCase();
      while (!(player.equals("r") || player.equals("p") || player.equals("s"))) {
        System.out.println("Error: invalid input");
        System.out.println("What will you play: (r, p, s) ");
        player = scan.next().toLowerCase();
      }

      int bot_roll = random.nextInt(3) + 1;
      if (bot_roll == 1) {
        bot = "r";
      } else if (bot_roll == 2) {
        bot = "p";
      } else {
        bot = "s";
      }

      System.out.println("Player: " + player + " | Bot: " + bot);

      if (player.equals(bot)) {
        System.out.println("Draw.");
      }
      if (player.equals("r") && bot.equals("s")) {
        System.out.println("Player wins");
      }
      if (player.equals("r") && bot.equals("p")) {
        System.out.println("Bot wins");
      }
      if (player.equals("s") && bot.equals("r")) {
        System.out.println("Bot wins");
      }
      if (player.equals("s") && bot.equals("p")) {
        System.out.println("Player wins");
      }
      if (player.equals("p") && bot.equals("s")) {
        System.out.println("Bot wins");
      }
      if (player.equals("p") && bot.equals("r")) {
        System.out.println("Player wins");
      }

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
