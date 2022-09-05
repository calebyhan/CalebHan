/*
Name: Caleb Han
Program: CreditCard
Purpose: Credit card simulator
*/

class Main {
  public static void main(String[] args) {
    CreditCard cc1 = new CreditCard("joe", 1234, 0);
    CreditCard cc2 = new CreditCard("lary", 5678, 100);

    cc2.lastInterest();

    cc1.updateCharge();
    cc1.updateBal();
    cc2.updateCharge();
    cc2.updateBal();

    cc1.changeName("jep");
    System.out.println();
    System.out.println(cc1);
    System.out.println();
    System.out.println(cc2);
  }
}
