public class Coin {
  private final int HEADS = 0;
  private final int TAILS = 1;

  private double face;

  public Coin() {
    flip();
  }

  public void flip() {
    face = (int) (Math.random() * 2);
  }

  public boolean isHeads() {
    return (face == HEADS);
  }

  public String toString() {
    String faceName;
    if (isHeads()) {
      faceName = "Heads";
    } else {
      faceName = "Tails";
    }
    return faceName;
  }
}
