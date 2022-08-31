import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class feather1 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Feather1 extends Actor
{    
    private Pigeon pigeon;
    
    public Feather1(Pigeon p) {
        pigeon = p;
    }
    /**
     * Act - do whatever the Butler_1 wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act()
    {
        // Add your action code here.
        if (getWorld() != null && isAtEdge() || intersects(pigeon)) {
            getWorld().removeObject(this);
        }
    }
}
