/*
Name: Caleb Han
Purpose: roll dice
*/

class Main {
  public static void main(String[] args) {
    // get rolls
    int roll1 = (int)(Math.random() * 6) + 1;
    int roll2 = (int)(Math.random() * 6) + 1;

    //print output
    System.out.println("Rolls: " + roll1 + ", " + roll2);
    System.out.println("Sum of rolls: " + (roll1+roll2));
  }
}
