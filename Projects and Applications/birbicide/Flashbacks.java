import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Control flashbacks
 * 
 * @author Caleb Han and Elynn An
 */
public class Flashbacks extends World
{
    public Flashbacks() {    
        super(900, 570, 1);
        Textbox t = new Textbox();
        addObject(t, 450, 285);
        C1_4 c1_4 = new C1_4();
        addObject(c1_4, 450, 285);
    }
    
    public void act() {
        int[] pos = getMouse();
        Title.music();
        if (pos[0] != 0) {
            removeObjects(getObjects(null));
            Dedscene s = new Dedscene(true);
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
