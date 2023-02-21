class Point {
  public int x;
  public int y;

  // point constructor
  public Point (int inX, int inY) {
    this.x = inX;
    this.y = inY;
  }

  // adds a vector to v(x,y)
  public void add (Point v) {
    this.x += v.x;
    this.y += v.y;
  }
}
