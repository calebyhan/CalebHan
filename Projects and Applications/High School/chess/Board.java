import java.awt.image.BufferedImage;
import java.io.*;
import java.util.Scanner;
import java.util.*;
import java.lang.*;
import javax.imageio.ImageIO;
import java.awt.*;
import javax.swing.*;

class Board {
  // stores the ids of rooks, bishops, etc as they appear on the board
  private final int[] pieceIDS = {4, 2, 3, 5, 6, 3, 2, 4};
  
  // stores all the maps for piece id to image file
  private Hashtable<Integer, String> fileMapping;
  
  // arrays for the pieces
  public Piece[] whitePieces;
  private Piece[] blackPieces;

  private boolean whiteTurn = true;
  public boolean end = false;

  // 2d array of all the locations of the pieces
  public int[][] board;

  // board constructor
  public Board() {
    whitePieces = new Piece[16];
    blackPieces = new Piece[16];
    board = new int[8][8];
    fileMapping = new Hashtable<Integer, String>();
    
    for (int i = 0; i < 8; i++) {
      int j = i + 1;

      // populates the pawns into the board
      whitePieces[i] = new Piece(1, j, new Point(j, 1));
      board[i][1] = j;
      blackPieces[i] = new Piece(1, -j, new Point(j, 6));
      board[i][6] = - j;

      // stores file names for pawns
      fileMapping.put(1, getFileName(1, true));
      fileMapping.put(-1, getFileName(1, false));

      // populates the rest of the pieces
      int type = pieceIDS[i];
      whitePieces[i + 8] = new Piece(type, j + 8, new Point(j, 0));
      board[i][0] = j + 8;
      blackPieces[i + 8] = new Piece(type, -(j + 8), new Point(j, 7));
      board[i][7] = - j - 8;

      // stores file names for other pieces
      fileMapping.put(type, getFileName(type, true));
      fileMapping.put(-type, getFileName(type, false));
    }
  }

  // handles pawn promotion
  private int promotePawn(boolean white) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("What piece do you want to promote the pawn to? [q]ueen, [k]night, [b]ishop, [r]ook: ");
    Map<Character, Integer> promotions = new HashMap<Character, Integer>();
    promotions.put('k', 2);
    promotions.put('b', 3);
    promotions.put('r', 4);
    promotions.put('q', 5);

    Character[] promotion = {'k', 'b', 'r', 'q'};
    Character promote = scanner.nextLine().trim().charAt(0);

    while (true) {
      boolean found = false;
      for (Character p : promotion) {
        if (p.equals(promote)) {
          found = true;
          break;
        }
      }
      if (found) {
        break;
      }
      System.out.println("Invalid input. Try again.");
      promote = scanner.nextLine().trim().charAt(0);
    }

    System.out.println(promote);
      
    if (white) {
      return promotions.get(promote);
    } else {
      return promotions.get(promote);
    }
  }
  
  // checks if rook move is legal
  private boolean checkRook(int locationX, int locationY, int destinationX, int destinationY) {
    if (locationX != destinationX && locationY != destinationY) {
      return false;
    }
    
    // checks the direction in which you are going - if the y's match you are going in the y direction
    if (locationX == destinationX) {
      // gets the direction in which the rook has to move
      int sign = (locationY > destinationY) ?  1 : -1;
      int tempDestY = destinationY + sign;

      // checks each spot on the board and makes sure it is empty to allow passage for the rook
      while (tempDestY != locationY) {
        if (board[locationX][tempDestY] != 0) {
          return false;
        } else {
          tempDestY += sign;
        }
      }
    }
      
    // same thing as last statement but for the other direction
    else if (locationY == destinationY) {
      int sign = (locationX > destinationX) ?  1 : -1;
      int tempDestX = destinationX + sign;
      while (tempDestX != locationX) {
        if (board[tempDestX][locationY] != 0) {
          return false;
        } else {
          tempDestX += sign;
        } 
      }
    }

    // checks if the destination and location pieces have the same sign
    if (board[destinationX][destinationY] * board[locationX][locationY] > 0) {
      return false;
    }
    return true;
  }

  // checks if pawn move is legal
  private boolean checkPawn(int locationX, int locationY, int destinationX, int destinationY) {
    if (locationX - destinationX != 0) {
      if (board[locationX][locationY] > 0) {
        if (destinationY - locationY == 1 && Math.abs(destinationX - locationX) == 1 && board[destinationX][destinationY] < 0) {
          if (destinationY == 7) {
            whitePieces[xyToPiece(locationX, locationY).id - 1].type = promotePawn(true);
          }
          return true;
        }
      } else {
        if (locationY - destinationY == 1 && Math.abs(destinationX - locationX) == 1 && board[destinationX][destinationY] > 0) {
          if (destinationY == 0) {
            blackPieces[xyToPiece(locationX, locationY).id - 1].type = promotePawn(false);
          }
          return true;
        }
      }
      return false;
    }
    // logic if pawn starts on original row (can move 1 or 2)
    if ((locationY == 1 || locationY == 6) && Math.abs(destinationY - locationY) == 2) {
      if (board[locationX][locationY] > 0) {
        if ((board[destinationX][destinationY] != 0) || (board[destinationX][destinationY - 1] != 0)) {
          return false;
        }
      } else {
        if ((board[destinationX][destinationY] != 0) || (board[destinationX][destinationY + 1] != 0)) {
          return false;
        }
      }
      return true;
    } 

    // logic for moving for any other row
    else if (Math.abs(destinationY - locationY) == 1) {
      Scanner scanner = new Scanner(System.in);
      if (board[locationX][locationY] > 0) {
        if (board[destinationX][destinationY] != 0) {
          return false;
        }
        if (destinationY == 7) {
          whitePieces[xyToPiece(locationX, locationY).id - 1].type = promotePawn(true);
        }
      } else {
        if (board[destinationX][destinationY] != 0) {
          return false;
        }
        if (destinationY == 0) {
          blackPieces[xyToPiece(locationX, locationY).id - 1].type = promotePawn(false);
        }
      }
      return true;
    } else {
      return false;
    }
  }

  // checks if bishop move is legal
  private boolean checkBishop(int locationX, int locationY, int destinationX, int destinationY) {
    if (Math.abs(locationX - destinationX) != Math.abs(locationY - destinationY)) {
      return false;
    } else {
      int signX = (locationX > destinationX) ?  1 : -1;
      int signY = (locationY > destinationY) ?  1 : -1;
      int tempDestX = destinationX + signX;
      int tempDestY = destinationY + signY;
      while (tempDestX != locationX) {
        if (board[tempDestX][tempDestY] != 0) {
          return false;
        }
        else {
          tempDestX += signX;
          tempDestY += signY;
        }
      }
    }
    // checks if the piece is the same color
    if (board[destinationX][destinationY] * board[locationX][locationY] > 0) {
      return false;
    }
    return true;
  }

  // checks if knight move is legal
  private boolean checkKnight(int locationX, int locationY, int destinationX, int destinationY) {
    int yDiff = Math.abs(locationY - destinationY);
    int xDiff = Math.abs(locationX - destinationX);
    if (!(Math.max(xDiff, yDiff) == 2 && Math.min(xDiff, yDiff) == 1)) {
      return false;
    } else if (board[locationX][locationY] * board[destinationX][destinationY] > 0) {
      return false;
    }
    return true;
  }

  // checks if queen move is legal
  private boolean checkQueen(int locationX, int locationY, int destinationX, int destinationY) {
    if (checkRook(locationX, locationY, destinationX, destinationY) || checkBishop(locationX, locationY, destinationX, destinationY)) {
      return true;
    }
    return false;
  }

  // checks if king move is legal
  private boolean checkKing(int locationX, int locationY, int destinationX, int destinationY) {
    if (Math.abs(locationX - destinationX) <= 1 && Math.abs(locationY - destinationY) <= 1) {
      if (board[destinationX][destinationY] * board[locationX][locationY] > 0) {
        return false;
      } else {
        return true;
      }
    } else {
      return false;
    }
  }

  // takes care of the piece movement
  private void movingPiece(int x1, int y1, int x2, int y2, Piece temp) {
    temp.setLoc(x2, y2);
    board[x2][y2] = board[x1][y1];
    board[x1][y1] = 0;
  }
  
  // moves piece to location from input
  public boolean move(String input) {
    char[] inp = input.toCharArray();
    Piece temp = xyToPiece(inp[0] - 'a', inp[1] - '1');
    
    int locationY = inp[1] - '1';
    int locationX = inp[0] - 'a';
    int destinationY = inp[3] - '1';
    int destinationX = inp[2] - 'a';

    if (locationX == destinationX && locationY == destinationY) {
      System.out.println("Bro thinks he's chatGPT ☠");
      return false;
    }
    
    if (temp == null) {
      System.out.println("There is no piece at this location!");
      return false;
    }

    if ((whiteTurn && board[locationX][locationY] < 0) || (!whiteTurn && board[locationX][locationY] > 0)) {
      return false;
    }
    
    if (temp.type == 4) {
      if (!checkRook(locationX, locationY, destinationX, destinationY)) {
        return false;
      }
      movingPiece(locationX, locationY, destinationX, destinationY, temp);
    } else if (temp.type == 1) {
        if (!checkPawn(locationX, locationY, destinationX, destinationY)) {
          return false;
        }
        movingPiece(locationX, locationY, destinationX, destinationY, temp);
    } else if (temp.type == 3) {
        if (!checkBishop(locationX, locationY, destinationX, destinationY)) {
          return false;
        }
        movingPiece(locationX, locationY, destinationX, destinationY, temp);
    } else if (temp.type == 6) {
        if (!checkKing(locationX, locationY, destinationX, destinationY)) {
          return false;
        }
        movingPiece(locationX, locationY, destinationX, destinationY, temp);
    } else if (temp.type == 5) {
        if (!checkQueen(locationX, locationY, destinationX, destinationY)) {
          return false;
        }
         movingPiece(locationX, locationY, destinationX, destinationY, temp);
    } else if (temp.type == 2) {
        if (!checkKnight(locationX, locationY, destinationX, destinationY)) {
          return false;
        }
        movingPiece(locationX, locationY, destinationX, destinationY, temp);
    }

    whiteTurn = !whiteTurn;
    
    return true;
  }


  // xy coordinates to piece
  private Piece xyToPiece(int x, int y) {
    if (board[x][y] < 0) {
      for (Piece piece : blackPieces) {
        if (piece.id == board[x][y]) {
          return piece;
        }
      }
    } else {
      for (Piece piece : whitePieces) {
        if (piece.id == board[x][y]) {
          return piece;
        }
      }
    }
    return null;
  }

  // gets file from directory imgs from id input
  private String getFileName(int id, boolean white) {
    String[] files = {"_p.png", "_k.png", "_b.png", "_r.png", "_q.png", "_ki.png"};
    if (white) {
      return "imgs/w" + files[id - 1];
    }
    else {
      return "imgs/b" + files[id - 1];
    }
  }

  // scales BufferedImage object to desired size (w, h)
  private static BufferedImage scale(BufferedImage image, int w, int h) {
    BufferedImage scaledImage = null;
    if (image != null) {
      scaledImage = new BufferedImage(w, h, image.getType());
      Graphics2D graphics2D = scaledImage.createGraphics();
      graphics2D.drawImage(image, 0, 0, w, h, null);
      graphics2D.dispose();
    }
    return scaledImage;
  }
  
  // displays image to the output
  private void DisplayImage() throws IOException {
    BufferedImage img=ImageIO.read(new File("newBoard.png"));
    ImageIcon icon=new ImageIcon(img);
    JFrame frame=new JFrame();
    frame.setLayout(new FlowLayout());
    frame.setSize(200,300);
    JLabel lbl=new JLabel();
    lbl.setIcon(icon);
    frame.add(lbl);
    frame.setVisible(true);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  }
  
  // displays the board
  public void display() throws IOException {
    BufferedImage bord = null;
    bord = ImageIO.read(new File("imgs/board.png"));

    BufferedImage combined = new BufferedImage(bord.getWidth(), bord.getHeight(), BufferedImage.TYPE_INT_ARGB);

    boolean drawn = false;
    for (int i = 0; i < 8; i++) {
      for (int j = 0; j < 8; j++) {
        if (board[i][j] != 0) {
          int newType = xyToPiece(i, j).id > 0 ? xyToPiece(i, j).type : -xyToPiece(i, j).type;
          BufferedImage image = ImageIO.read(new File(fileMapping.get(newType)));
          BufferedImage newImage = scale(image, 150, 150);

          int w = Math.max(bord.getWidth(), newImage.getWidth());
          int h = Math.max(bord.getHeight(), newImage.getHeight());

          if (drawn == false) {
            Graphics g = combined.getGraphics();
            g.drawImage(bord, 0, 0, null);
            drawn = true;
          }

          Graphics g = combined.getGraphics();
          int newx = i; //ayeyee now we can debug the actual moving things LMAO
          int newy = 7 - j; // ye
          g.drawImage(newImage, 50 + newx * 162, 20 + newy * 162, null);
        }
      }
    }
    ImageIO.write(combined, "PNG", new File("newBoard.png"));
    DisplayImage();
  }
}