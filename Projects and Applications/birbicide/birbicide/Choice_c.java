import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Choose from C1 or C2
 * 
 * @author Caleb Han and Elynn An
 */
public class Choice_c extends World
{
    public Choice_c() {    
        super(900, 570, 1);
    }
    
    //choose c1 or c2
    public void act() {
        int[] pos = getMouse();
        Title.GLOBAL_T += 1;
        if (pos[0] >= 189 && pos[0] <= 353 && pos[1] >= 80 && pos[1] <= 298) {
            C1 s = new C1();
            Greenfoot.setWorld(s);
        } else if (pos[0] >= 541 && pos[0] <= 717 && pos[1] >= 80 && pos[1] <= 298) {
            C2 s = new C2();
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
