import java.io.*;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

class Main {
  static boolean turn = true;
  static Board board;

  public static void main(String[] args) throws IOException {
    // create board object
    board = new Board();
    board.display();
  }

  public static void move(String move) throws IOException {
    if (board.move(move)) {
      turn = !turn;
    }
    board.display();
  }

  protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    String data = request.getParameter("data");
    System.out.println(data);
    move(data);

    // Send a response to the client
    response.setCharacterEncoding("UTF-8");
    response.setContentType("text/plain");
    String ret = turn ? "white" : "black";
    response.getWriter().write(""+ret);
  }
}