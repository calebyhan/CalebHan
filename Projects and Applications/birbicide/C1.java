import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Controls first chapter
 * 
 * @author Caleb Han and Elynn An
 */
public class C1 extends World
{
    private int scene;
    private boolean wait;

    public C1() {    
        super(900, 570, 1);
        scene = 0;
        wait = false;
        Textbox t = new Textbox();
        addObject(t, 450, 285);
    }
    
    // go through texts by click
    public void act() {
        int[] pos = getMouse();
        Title.music();
        if (scene == 0 && !wait) {
            C1_1 c1_1 = new C1_1();
            addObject(c1_1, 450, 285);
            wait = true;
        }
        if (scene == 1 && !wait) {
            C1_2 c1_2 = new C1_2();
            addObject(c1_2, 450, 285);
            wait = true;
        }
        if (scene == 2 && !wait) {
            C1_3 c1_3 = new C1_3();
            addObject(c1_3, 450, 285);
            wait = true;
        }
        if (scene == 3) {
            Flashbacks s = new Flashbacks();
            Greenfoot.setWorld(s);
        }
        if (pos[0] != 0) {
            removeObjects(getObjects(null));
            Textbox t = new Textbox();
            addObject(t, 450, 285);
            scene += 1;
            wait = false;
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
