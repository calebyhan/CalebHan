import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Death here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Death extends World
{
    public Death() {    
        super(900, 570, 1); 
        GreenfootSound death2 = new GreenfootSound("deathSound2.mp3");
        death2.play();
        death2.setVolume(40);
    }
    
    //play again or end
    public void act() {
        int[] pos = getMouse();
        if (pos[0] >= 159 && pos[0] <= 450 && pos[1] >= 301 && pos[1] <= 475) {
            Final_battle s = new Final_battle();
            Greenfoot.setWorld(s);
        } else if (pos[0] >= 601 && pos[0] <= 718 && pos[1] >= 450 && pos[1] <= 475) {
            End s = new End(0);
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
