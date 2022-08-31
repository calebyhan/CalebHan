import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Show Epilogue
 * 
 * @author Caleb Han and Elynn An
 */
public class Epilogue extends World
{
    private int life;
    private boolean move;

    public Epilogue(int l) {    
        super(900, 570, 1); 
        life = l;
        move = false;
        Textbox t = new Textbox();
        addObject(t, 450, 285);
        Epilogue_t e = new Epilogue_t();
        addObject(e, 450, 285);
        GreenfootSound woohoo = new GreenfootSound("woohoo.mp3");
        woohoo.play();
        woohoo.setVolume(40);
    }
    
    public void act() {
        int[] pos = getMouse();
        if (pos[0] != 0 && !move) {
            removeObjects(getObjects(null));
            move = true;
        } else if (pos[0] !=0 && move) {
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
