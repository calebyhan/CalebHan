public class Text {
  public static void clear() {
    System.out.print("\033[H\033[2J");
    System.out.flush();
  }
  public static void wait(double t) {
    try {
      Thread.sleep((int) (t * 1000));
    }
    catch (Exception e) {
      e.printStackTrace();
    }
  }
  public static void smoothPrint(String prompt) {
    for (char c : prompt.toCharArray()) {
      System.out.print(c);
      wait(0.05);
    }
  }
}