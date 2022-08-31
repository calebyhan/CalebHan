import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.ArrayList;

/**
 * Write a description of class Pigeon here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Pigeon extends Actor
{
    /**
     * Act - do whatever the Pigeon wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act()
    {
        // Add your action code here.
    }
    
    public boolean touch() {
        if (!isTouching(Feather1.class) && !isTouching(Feather2.class) && !isTouching(Feather3.class)) {
            return false;
        }
        return true;
    }
}
