import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Title and instructions pages
 * 
 * @author Caleb Han and Elynn An
 */
public class Title extends World
{
    public static boolean[] clues = {false, false, false};
    public static boolean[] interviewed = {false, false, false, false, false, false};
    public static GreenfootSound bg_i = new GreenfootSound("BG_I.wav");
    public static boolean playing = false;
    public static int GLOBAL_T, tries;
    private static GreenfootSound bg_l = new GreenfootSound("BG_L.wav");
    
    public Title() {   
        super(900, 570, 1);
        Greenfoot.start();
        //plays intro
        bg_i.play();
        bg_i.setVolume(40);
        tries = 0;
    }
    
    //constructor to not reset music/reset game
    public Title(boolean b) {   
        super(900, 570, 1);
        clues = new boolean[]{false, false, false};
        interviewed = new boolean[]{false, false, false, false, false, false};
        tries = GLOBAL_T = 0;
    }
    
    public void act() {
        int[] pos = getMouse();
        //plays looped continuation if intro is over
        music();
        if (pos[0] >= 343 && pos[0] <= 561 && pos[1] >= 326 && pos[1] <= 351) {
            Instructions s = new Instructions();
            Greenfoot.setWorld(s);
        }
        else if (pos[0] >= 403 && pos[0] <= 496 && pos[1] >= 384 && pos[1] <= 412) {
            Choice_c s = new Choice_c();
            Greenfoot.setWorld(s);
        }
        else if (pos[0] >= 382 && pos[0] <= 514 && pos[1] >= 444 && pos[0] <= 474) {
            Credits s = new Credits(1);
            Greenfoot.setWorld(s);
        }
    }
    
    public static void music() {
        if (!bg_i.isPlaying() && !playing) {
            bg_l.setVolume(40);
            bg_l.playLoop();
            playing = true;
        }
    }
    
    public static void music(boolean stop) {
        if (stop) {
            bg_l.stop();
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