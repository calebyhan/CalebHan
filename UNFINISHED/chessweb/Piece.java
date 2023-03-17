class Piece {
  // see README.md for type and id labels
  public int type;
  public int id;
  
  public Point location;

  // piece constructor
  public Piece(int inType, int inId, Point inLocation) {
    this.type = inType;
    this.id = inId;
    this.location = inLocation;
  }

  public void setLoc(int x, int y) {
    this.location = new Point(x, y);
  }
}