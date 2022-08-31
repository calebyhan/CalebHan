import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Instructions here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Instructions extends World
{
    public Instructions() {    
        super(900, 570, 1); 
    }
    
    public void act() {
        int[] pos = getMouse();
        Title.music();
        if (pos[0] >= 31 && pos[0] <= 94 && pos[1] >= 520 && pos[1] <= 543) {
            Title s = new Title(true);
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
