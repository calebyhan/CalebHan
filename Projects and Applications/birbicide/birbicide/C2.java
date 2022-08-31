import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Chapter 2
 * 
 * @author Caleb Han and Elynn An
 */
public class C2 extends World
{    
    public C2() {    
        super(900, 570, 1);
        Choice c = new Choice();
        addObject(c, 450, 285);
    }
    
    //go investigate rooms or suspects
    public void act() {
        int pos[] = getMouse();
        Title.music();
        Title.GLOBAL_T += 1;
        if (pos[0] >= 105 && pos[0] <= 428 && pos[1] >= 492 && pos[1] <= 515) {
            investigate_r();
        } else if (pos[0] >= 590 && pos[0] <= 842 && pos[1] >= 492 && pos[1] <= 515) {
            investigate_s();
        }
    }
    
    //investigate suspects
    public void investigate_s() {
        Inv_s s = new Inv_s();
        Greenfoot.setWorld(s);
    }
    
    //investigate rooms
    public void investigate_r() {
        Inv_r s = new Inv_r();
        Greenfoot.setWorld(s);
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
