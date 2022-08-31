import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.Random;

/**
 * Show crime scene
 * 
 * @author Caleb Han and Elynn An
 */
public class Dedscene extends World
{
    private boolean first, viewed, clue, move, cant;

    public Dedscene(boolean f) {    
        super(900, 570, 1);
        first = f;
        viewed = false;
        clue = move = cant = false;
        // if in c1
        if (first) {
            C1_5 c1_5 = new C1_5();
            addObject(c1_5, 450, 285);
        }  else {
            D_room d = new D_room();
            addObject(d, 450, 285);
            Choice_d Choice_d = new Choice_d();
            addObject(Choice_d, 450, 285);
        }
    }
    
    public void act() {
        int[] pos = getMouse();
        Title.music();
        if (!first) {
            Title.GLOBAL_T += 1;
        }
        D_room d = new D_room();
        if (pos[0] != 0 && viewed) {
            removeObjects(getObjects(null));
            addObject(d, 450, 285);
            Choice_d Choice_d = new Choice_d();
            addObject(Choice_d, 450, 285);
            move = false;
        } else if (pos[0] != 0 && clue) {
            removeObjects(getObjects(null));
            addObject(d, 450, 285);
            Lab l = new Lab();
            addObject(l, 450, 285);
            Greenfoot.delay(180);
            removeObjects(getObjects(null));
            addObject(d, 450, 285);
            Dr_clue2 dr2 = new Dr_clue2();
            addObject(dr2, 450, 285);
            Slash s = new Slash();
            addObject(s, 450, 285);
            move = true;
            clue = false;
            viewed = true;
        } else if (pos[0] != 0 && move) {
            removeObjects(getObjects(null));
            addObject(d, 450, 285);
            Choice_d Choice_d = new Choice_d();
            addObject(Choice_d, 450, 285);
            move = false;
        }
        if (pos[0] != 0 && first) {
            Garden s = new Garden(true);
            Greenfoot.setWorld(s);
        }
        if (!clue && !move) {
            if (pos[0] >= 144 && pos[0] <= 316 && pos[1] >= 459 && pos[1] <= 480) {
                clue = true;
                if (viewed && !move) {
                    removeObjects(getObjects(null));
                    addObject(d, 450, 285);
                    Cant_clue e = new Cant_clue();
                    addObject(e, 450, 285);
                    clue = false;
                } else if (Title.clues[1]) {
                    viewed = true;
                } else {
                    Title.clues[1] = true;
                    removeObjects(getObjects(null));
                    addObject(d, 450, 285);
                    Find_clue fc = new Find_clue();
                    addObject(fc, 450, 285);
                    Greenfoot.delay(140);
                    removeObjects(getObjects(null));
                    addObject(d, 450, 285);
                    Dr_clue1 dr1 = new Dr_clue1();
                    addObject(dr1, 450, 285);
                }
            } else if (pos[0] >= 501 && pos[0] <= 744 && pos[1] >= 459 && pos[1] <= 480) {
                removeObjects(getObjects(null));
                Inv_r s = new Inv_r();
                Greenfoot.setWorld(s);
            }
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
