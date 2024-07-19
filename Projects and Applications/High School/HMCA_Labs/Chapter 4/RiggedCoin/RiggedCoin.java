public class RiggedCoin {
  private double rigged;
  private double face;

  public RiggedCoin(double rp) {
    rigged = rp;
    flip();
  }

  public void flip() {
    face = Math.random();
  }

  public boolean isHeads() {
    return (face < rigged);
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
