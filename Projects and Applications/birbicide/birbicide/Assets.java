import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Art assets
 * 
 * @author Caleb Han and Elynn An
 */
public class Assets extends World
{
    private int prev, life;
    
    //if come from end
    public Assets(int p, int l) {    
        super(900, 570, 1); 
        prev = p;
        life = l;
    }
    
    //if come from title
    public Assets(int p) {
        super(900, 570, 1);
        prev = p;
        life = -1;
    }
    
    public void act() {
        int[] pos = getMouse();
        if (pos[0] >= 32 && pos[0] <= 92 && pos[1] >= 520 && pos[1] <= 545) {
            if (life == -1) {
                Credits s = new Credits(prev);
                Greenfoot.setWorld(s);
            } else {
                Credits s = new Credits(prev, life);
                Greenfoot.setWorld(s);
            }
        }
    }
    
    public int[] getMouse() {
        int[] pos = new int[2];
        MouseInfo mouse = Greenfoot.getMouseInfo();
        if (mouse != null) {
            pos[0] = mouse.getX();
            pos[1] = mouse.getY();
        }
        if (Greenfoot.mouseClicked(null)) {
            return pos;
        }
        pos[0] = pos[1] = 0;
        return pos;
    }
}
