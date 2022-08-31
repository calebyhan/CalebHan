import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class End here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class End extends World
{
    private int life;

    public End(int l) {    
        super(900, 570, 1);
        life = l;
        setScore();
        Stats s = new Stats();
        addObject(s, 450, 285);
    }
    
    
    //if clicked on textboxes
    public void act() {
        int[] pos = getMouse();
        if (pos[0] >= 28 && pos[0] <= 138 && pos[1] >= 518 && pos[1] <= 543) {
            Credits s = new Credits(2, life);
            Greenfoot.setWorld(s);
        } else if (pos[0] >= 739 && pos[0] <= 876 && pos[1] >= 518 && pos[1] <= 543) {
            Title s = new Title(true);
            Greenfoot.setWorld(s);
        }
    }
    
    
    //get number of clues/interviewed
    public int[] getStats() {
        int[] ret = {0, 0};
        for (boolean v : Title.clues) {
            if (v) ret[0] += 1;
        }
        for (boolean v : Title.interviewed) {
            if (v) ret[1] += 1;
        }
        return ret;
    }
    
    //set all number textboxes
    public void setScore() {
        int sum = 0;
        if (getStats()[0] == 2) {
            Credits_1 c1 = new Credits_1();
            addObject(c1, 450, 285);
            sum += 2;
        } else {
            Credits_2 c2 = new Credits_2();
            addObject(c2, 450, 285);
            sum += 3;
        }
        if (getStats()[1] == 4) {
            Credits_3 c3 = new Credits_3();
            addObject(c3, 450, 285);
            sum += 4;
        } else if (getStats()[1] == 5) {
            Credits_4 c4 = new Credits_4();
            addObject(c4, 450, 285);
            sum += 5;
        } else {
            Credits_5 c5 = new Credits_5();
            addObject(c5, 450, 285);
            sum += 6;
        } 
        if (life == 0) {
            Credits_6 c6 = new Credits_6();
            addObject(c6, 450, 285);
        } else if (life == 1) {
            Credits_7 c7 = new Credits_7();
            addObject(c7, 450, 285);
            sum += 1;
        } else if (life == 2) {
            Credits_8 c8 = new Credits_8();
            addObject(c8, 450, 285);
            sum += 2;
        } else {
            Credits_9 c9 = new Credits_9();
            addObject(c9, 450, 285);
            sum += 3;
        }
        if (Title.GLOBAL_T >= 12500) {
            Credits_10 c10 = new Credits_10();
            addObject(c10, 450, 285);
            sum += 1;
        } else if (Title.GLOBAL_T < 12500 && Title.GLOBAL_T > 7500) {
            Credits_11 c11 = new Credits_11();
            addObject(c11, 450, 285);
            sum += 2;
        } else {
            Credits_12 c12 = new Credits_12();
            addObject(c12, 450, 285);
            sum += 3;
        }
        if (sum == 7) {
            Credits_13 c13 = new Credits_13();
            addObject(c13, 450, 285);
        } else if (sum == 8) {
            Credits_14 c14 = new Credits_14();
            addObject(c14, 450, 285);
        } else if (sum == 9) {
            Credits_15 c15 = new Credits_15();
            addObject(c15, 450, 285);
        } else if (sum == 10) {
            Credits_16 c16 = new Credits_16();
            addObject(c16, 450, 285);
        } else if (sum == 11) {
            Credits_17 c17 = new Credits_17();
            addObject(c17, 450, 285);
        } else if (sum == 12) {
            Credits_18 c18 = new Credits_18();
            addObject(c18, 450, 285);
        } else if (sum == 13) {
            Credits_19 c19 = new Credits_19();
            addObject(c19, 450, 285);
        } else if (sum == 14) {
            Credits_20 c20 = new Credits_20();
            addObject(c20, 450, 285);
        } else {
            Credits_21 c21 = new Credits_21();
            addObject(c21, 450, 285);
        }
        if (Title.tries == 1) {
            Credits_22 c22 = new Credits_22();
            addObject(c22, 450, 285);
        } else if (Title.tries == 2) {
            Credits_23 c23 = new Credits_23();
            addObject(c23, 450, 285);
        } else if (Title.tries ==3) {
            Credits_24 c24 = new Credits_24();
            addObject(c24, 450, 285);
        } else if (Title.tries == 4) {
            Credits_25 c25 = new Credits_25();
            addObject(c25, 450, 285);
        } else if (Title.tries == 5) {
            Credits_26 c26 = new Credits_26();
            addObject(c26, 450, 285);
        } else {
            Credits_27 c27 = new Credits_27();
            addObject(c27, 450, 285);
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
