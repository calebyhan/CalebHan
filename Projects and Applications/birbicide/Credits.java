import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Show credits
 * 
 * @author Caleb Han and Elynn An
 */
public class Credits extends World
{
    private int prev, life;
    
    //if come from title
    public Credits(int p) {    
        super(900, 570, 1); 
        prev = p;
        life = -1;
    }
    
    //if come from end
    public Credits(int p, int l) {    
        super(900, 570, 1); 
        prev = p;
        life = l;
    }
    
    public void act() {
        int[] pos = getMouse();
        if (pos[0] >= 33 && pos[0] <= 94 && pos[1] >= 518 && pos[1] <= 543) {
            retWorld(prev);
        } else if (pos[0] >= 782 && pos[0] <= 876 && pos[1] >= 518 && pos[1] <= 543) {
            if (life == -1) {
                Assets s = new Assets(prev);
                Greenfoot.setWorld(s);
            } else {
                Assets s = new Assets(prev, life);
                Greenfoot.setWorld(s);
            }
        }
    }
    
    public void retWorld(int pr) {
        if (pr == 1) {
            Title s = new Title();
            Greenfoot.setWorld(s);
        } else {
            End s = new End(life);
            Greenfoot.setWorld(s);
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
