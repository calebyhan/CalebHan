import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.Random;

/**
 * Investigation of rooms
 * 
 * @author Caleb Han and Elynn An
 */
public class Inv_r extends World
{
    private boolean viewed, clue, move, cant;

    public Inv_r() {    
        super(900, 570, 1);
        clue = move = cant = false;
        Choice_st Choice_st = new Choice_st();
        addObject(Choice_st, 450, 285);
    }
    
    public void act() {
        int pos[] = getMouse();
        Title.music();
        Title.GLOBAL_T += 1;
        if (pos[0] != 0 && viewed) {
            removeObjects(getObjects(null));
            Choice_st Choice_st = new Choice_st();
            addObject(Choice_st, 450, 285);
            move = false;
        } else if (pos[0] != 0 && clue) {
            removeObjects(getObjects(null));
            Lab l = new Lab();
            addObject(l, 450, 285);
            Greenfoot.delay(180);
            removeObjects(getObjects(null));
            St_clue2 sc2 = new St_clue2();
            addObject(sc2, 450, 285);
            Footprints f = new Footprints();
            addObject(f, 450, 285);
            move = true;
            clue = false;
            viewed = true;
        } else if (pos[0] != 0 && move) {
            removeObjects(getObjects(null));
            Choice_st Choice_st = new Choice_st();
            addObject(Choice_st, 450, 285);
            move = false;
        }
        if (!clue && !move) {
            if (pos[0] >= 117 && pos[0] <= 314 && pos[1] >= 460 && pos[1] <= 480) {
                clue = true;
                if (viewed && !move) {
                    removeObjects(getObjects(null));
                    Cant_clue e = new Cant_clue();
                    addObject(e, 450, 285);
                    clue = false;
                } else if (Title.clues[0]) {
                    viewed = true;
                } else {
                    Title.clues[0] = true;
                    removeObjects(getObjects(null));
                    Find_clue fc = new Find_clue();
                    addObject(fc, 450, 285);
                    Greenfoot.delay(140);
                    removeObjects(getObjects(null));
                    St_clue1 sc1 = new St_clue1();
                    addObject(sc1, 450, 285);
                    Footprints f = new Footprints();
                    addObject(f, 450, 285);
                }
            } else if (pos[0] >= 117 && pos[0] <= 359 && pos[1] >= 523 && pos[1] <= 544) {
                removeObjects(getObjects(null));
                Dedscene s = new Dedscene(false);
                Greenfoot.setWorld(s);
            } else if (pos[0] >= 499 && pos[0] <= 674 && pos[1] >= 460 && pos[1] <= 480) {
                removeObjects(getObjects(null));
                Garden s = new Garden(false);
                Greenfoot.setWorld(s);
            } else if (pos[0] >= 499 && pos[0] <= 759 && pos[1] >= 523 && pos[1] <= 544) {
                C2 s = new C2();
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
