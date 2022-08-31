import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.Random;

/**
 * Show garden
 * 
 * @author Caleb Han and Elynn An
 */
public class Garden extends World
{
    private boolean first, i1, i2, viewed, clue, move, cant;

    public Garden(boolean f) {    
        super(900, 570, 1);
        first = f;
        i1 = i2 = false;
        clue = move = cant = false;
        // if in c1
        if (first) {
            Textbox t = new Textbox();
            addObject(t, 450, 285);
            C1_6 c1_6 = new C1_6();
            addObject(c1_6, 450, 285);
        } else {
            G_room g = new G_room();
            addObject(g, 450, 285);
            Choice_g Choice_g = new Choice_g();
            addObject(Choice_g, 450, 285);
        }
    }
    
    // choices with mouse click
    public void act() {
        int[] pos = getMouse();
        Title.music();
        if (!first) {
            Title.GLOBAL_T += 1;
        }
        G_room g = new G_room();
        if (pos[0] != 0 && viewed) {
            removeObjects(getObjects(null));
            addObject(g, 450, 285);
            Choice_g Choice_g = new Choice_g();
            addObject(Choice_g, 450, 285);
            move = false;
        } else if (pos[0] != 0 && clue) {
            removeObjects(getObjects(null));
            addObject(g, 450, 285);
            Lab l = new Lab();
            addObject(l, 450, 285);
            Greenfoot.delay(180);
            removeObjects(getObjects(null));
            addObject(g, 450, 285);
            G_clue2 g2 = new G_clue2();
            addObject(g2, 450, 285);
            Weapon w = new Weapon();
            addObject(w, 450, 285);
            move = true;
            clue = false;
            viewed = true;
        } else if (pos[0] != 0 && move) {
            removeObjects(getObjects(null));
            addObject(g, 450, 285);
            Choice_g Choice_g = new Choice_g();
            addObject(Choice_g, 450, 285);
            move = false;
        }
        if (pos[0] != 0 && first) {
            Stairwell s = new Stairwell(true);
            Greenfoot.setWorld(s);
        }
        if (i1 && !i2) {
            removeObjects(getObjects(null));
            addObject(g, 450, 285);
            Gardener_1 Gardener_1 = new Gardener_1();
            addObject(Gardener_1, 450, 285);
            Pip p = new Pip();
            addObject(p, 450, 285);
            i2 = true;
        } 
        if (!clue && !move) {
            if (pos[0] != 0 && i1 && i2) {
                removeObjects(getObjects(null));
                addObject(g, 450, 285);
                Gardener_2 Gardener_2 = new Gardener_2();
                addObject(Gardener_2, 450, 285);
                Pip p = new Pip();
                addObject(p, 450, 285);
                i1 = false;
            } else if (pos[0] != 0 && !i1 && i2) {
                removeObjects(getObjects(null));
                addObject(g, 450, 285);
                Choice_g Choice_g = new Choice_g();
                addObject(Choice_g, 450, 285);
                i1 = i2 = false;
            } else if (pos[0] >= 118 && pos[0] <= 315 && pos[1] >= 461 && pos[1] <= 480) {
                clue = true;
                if (viewed && !move) {
                    removeObjects(getObjects(null));
                    addObject(g, 450, 285);
                    Cant_clue e = new Cant_clue();
                    addObject(e, 450, 285);
                    clue = false;
                } else if (Title.clues[2]) {
                    viewed = true;
                } else {
                    Title.clues[2] = true;
                    removeObjects(getObjects(null));
                    addObject(g, 450, 285);
                    Find_clue fc = new Find_clue();
                    addObject(fc, 450, 285);
                    Greenfoot.delay(140);
                    removeObjects(getObjects(null));
                    addObject(g, 450, 285);
                    G_clue1 g1 = new G_clue1();
                    addObject(g1, 450, 285);
                    Weapon w = new Weapon();
                    addObject(w, 450, 285);
                }
            } else if (pos[0] >= 118 && pos[0] <= 400 && pos[1] >= 522 && pos[1] <= 543) {
                removeObjects(getObjects(null));
                Inv_r s = new Inv_r();
                Greenfoot.setWorld(s);
            } else if (pos[0] >= 505 && pos[0] <= 840 && pos[1] >= 461 && pos[1] <= 480) {
                removeObjects(getObjects(null));
                Pip p = new Pip();
                addObject(p, 450, 285);
                addObject(g, 450, 285);
                Title.interviewed[5] = true;
                i1 = true;
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
