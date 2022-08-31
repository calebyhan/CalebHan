import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Show stairwell
 * 
 * @author Caleb Han and Elynn An
 */
public class Stairwell extends World
{
    private boolean first;
    
    public Stairwell(boolean f) {    
        super(900, 570, 1);
        first = f;
        // if in c1
        if (first) {
            C1_7 c1_7 = new C1_7();
            addObject(c1_7, 450, 285);
        }
    }

    public void act() {
        int[] pos = getMouse();
        Title.music();
        if (!first) {
            Title.GLOBAL_T += 1;
        }
        if (pos[0] != 0 && first) {
            C2 s = new C2();
            Greenfoot.setWorld(s);
        } else if (!first) {
            removeObjects(getObjects(null));
            Choice_st Choice_st = new Choice_st();
            addObject(Choice_st, 450, 285);
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
