import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.ArrayList;

/**
 * Final battle
 * 
 * @author Caleb Han and Elynn An
 */
public class Final_battle extends World
{
    private Pigeon p;
    private int t, spawn, life, fealeft, track;
    private boolean dialogue, first, r1, r2, rr1, rr2, rr3;
    private ArrayList<Actor> fea = new ArrayList<Actor>();
    
    public Final_battle() {    
        super(900, 570, 1);
        t = spawn = fealeft = track = 0;
        life = 3;
        p = new Pigeon();
        dialogue = first = true;
        Title.tries += 1;
        r1 = true;
        r2 = false;
        rr1 = rr2 = rr3 = false;
        p.getImage().scale((int)((double)(p.getImage().getWidth()) * 0.15), (int)((double)(p.getImage().getHeight()) * 0.15));
        addObject(p, 100, 400);
        Ricardo r = new Ricardo();
        r.getImage().scale((int)((double)(r.getImage().getWidth()) * 0.12), (int)((double)(r.getImage().getHeight()) * 0.12));
        addObject(r, 850, 410);
        Textbox t = new Textbox();
        addObject(t, 450, 285);
        displayLife();
        Title.music(true);
    }
    
    public void act() {
        int[] pos = getMouse();
        track = 0;
        Title.GLOBAL_T += 1;
        if (fealeft == 15) {
            Epilogue s = new Epilogue(life);
            Greenfoot.setWorld(s);
        }
        if (dialogue && first) {
            if (r1) {
                R1 R1 = new R1();
                addObject(R1, 450, 285);
                r1 = false;
                r2 = true;
            } else if (pos[0] != 0 && !r1 && r2) {
                R2 R2 = new R2();
                removeObjects(getObjects(R1.class));
                addObject(R2, 450, 285);
                r2 = false;
            } else if (pos[0] != 0 && !r1 && !r2) {
                removeObjects(getObjects(R2.class));
                removeObjects(getObjects(Textbox.class));
                Greenfoot.delay(10);
                dialogue = first = false;
            }
        }
        if (fealeft == 3 && dialogue) {
            boolean threshold = checkwin();
            if (threshold && !rr1) {
                Textbox t = new Textbox();
                addObject(t, 450, 285);
                R3 r3 = new R3();
                addObject(r3, 450, 285);
                rr1 = true;
            } else if (!threshold && !rr1) {
                Textbox t = new Textbox();
                addObject(t, 450, 285);
                R6 r6 = new R6();
                addObject(r6, 450, 285);
                rr1 = true;
            } else if (pos[0] != 0) {
                removeObjects(getObjects(R3.class));
                removeObjects(getObjects(R6.class));
                removeObjects(getObjects(Textbox.class));
                dialogue = false;
            }
        } else if (fealeft == 6 && dialogue) {
            boolean threshold = checkwin();
            if (threshold && !rr2) {
                Textbox t = new Textbox();
                addObject(t, 450, 285);
                R4 r4 = new R4();
                addObject(r4, 450, 285);
                rr2 = true;
            } else if (!threshold && !rr2) {
                Textbox t = new Textbox();
                addObject(t, 450, 285);
                R7 r7 = new R7();
                addObject(r7, 450, 285);
                rr2 = true;
            } else if (pos[0] != 0) {
                removeObjects(getObjects(R4.class));
                removeObjects(getObjects(R7.class));
                removeObjects(getObjects(Textbox.class));
                dialogue = false;
            }
        } else if (fealeft == 10 && dialogue) {
            boolean threshold = checkwin();
            if (threshold && !rr3) {
                Textbox t = new Textbox();
                addObject(t, 450, 285);
                R5 r5 = new R5();
                addObject(r5, 450, 285);
                rr3 = true;
            } else if (!threshold && !rr3) {
                Textbox t = new Textbox();
                addObject(t, 450, 285);
                R8 r8 = new R8();
                addObject(r8, 450, 285);
                rr3 = true;
            } else if (pos[0] != 0) {
                removeObjects(getObjects(R5.class));
                removeObjects(getObjects(R8.class));
                removeObjects(getObjects(Textbox.class));
                dialogue = false;
            }
        }
        else if (!dialogue) {
            timer();
            moveFeathers();
            if (t >= spawn) {
                fealeft += 1;
                newFeather();
                t = 0;
                if ((fealeft == 3 && !rr1)|| (fealeft == 6 && !rr2) || (fealeft == 10 && !rr3)) {
                    dialogue = true;
                }
            }
            if (p.getY() < 340) {
                p.setLocation(p.getX(), 340);
            }
            if (p.getY() > 470) {
                p.setLocation(p.getX(), 470);
            }
            if (p.getY() >= 340 && p.getY() <= 470) {
                if (Greenfoot.isKeyDown("up")) {
                    p.setLocation(p.getX(), p.getY() - 5);
                } else if (Greenfoot.isKeyDown("down")) {
                    p.setLocation(p.getX(), p.getY() + 5);
                }
            }
            if (track > 0) {
                life -= 1;
                GreenfootSound death1 = new GreenfootSound("deathSound.mp3");
                death1.play();
                death1.setVolume(40);
                displayLife();
            }   
        }
    }
    
    public void timer() {
        t += 1;
    }
    
    public boolean checkwin() {
        if (fealeft == 3) {
            if (life == 3) {
                return true;
            } else if (life <= 2) {
                return false;
            }
        } else if (fealeft == 6) {
            if (life == 3) {
                return true;
            } else if (life <= 2) {
                return false;
            }
        } else if (fealeft == 10) {
            if (life >= 2) {
                return true;
            } else if (life == 1) {
                return false;
            }
        }
        return false;
    }
    
    public void displayLife() {
        removeObjects(getObjects(Egg.class));
        removeObjects(getObjects(Egged.class));
        Egg e1 = new Egg();
        e1.getImage().scale((int)((double)(e1.getImage().getWidth()) * 0.2), (int)((double)(e1.getImage().getHeight()) * 0.2));
        Egg e2 = new Egg();
        e2.getImage().scale((int)((double)(e2.getImage().getWidth()) * 0.2), (int)((double)(e2.getImage().getHeight()) * 0.2));
        Egg e3 = new Egg();
        e3.getImage().scale((int)((double)(e3.getImage().getWidth()) * 0.2), (int)((double)(e3.getImage().getHeight()) * 0.2));
        Egged ed1 = new Egged();
        ed1.getImage().scale((int)((double)(ed1.getImage().getWidth()) * 0.2), (int)((double)(ed1.getImage().getHeight()) * 0.2));
        Egged ed2 = new Egged();
        ed2.getImage().scale((int)((double)(ed2.getImage().getWidth()) * 0.2), (int)((double)(ed2.getImage().getHeight()) * 0.2));
        Egged ed3 = new Egged();
        ed3.getImage().scale((int)((double)(ed3.getImage().getWidth()) * 0.2), (int)((double)(ed3.getImage().getHeight()) * 0.2));
        if (life == 3) {
            addObject(e1, 20, 30);
            addObject(e2, 60, 30);
            addObject(e3, 100, 30);
        } else if (life == 2) {
            addObject(e1, 20, 30);
            addObject(e2, 60, 30);
            addObject(ed3, 100, 30);
        } else if (life == 1) {
            addObject(e1, 20, 30);
            addObject(ed2, 60, 30);
            addObject(ed3, 100, 30);
        } else if (life == 0) {
            Death s = new Death();
            Greenfoot.setWorld(s);
        }
    }
    
    public void moveFeathers() {
        for (int i = 0; i < fea.size(); i++) {
            if (fea.get(i).getWorld() != null && fea.get(i).getX() == 100) {
                GreenfootSound dodge = new GreenfootSound("featherDodge.mp3");
                dodge.play();
                dodge.setVolume(60);
            }
            if (fea.get(i).getWorld() != null) {
                fea.get(i).setLocation(fea.get(i).getX() - 10, fea.get(i).getY());
            }
            if (p.touch()) {
                track += 1;
            }
            if (fea.get(i).getWorld() == null) {
                fea.remove(i);
            }
        }
    }
    
    public void newFeather() {
        if (t >= spawn) {
            int[][] positions = {{810, 420}, {810, 410}, {810, 390}};
            Feather1 f1 = new Feather1(p);
            f1.setRotation(269);
            f1.getImage().scale((int)((double)(f1.getImage().getWidth()) * 0.15), (int)((double)(f1.getImage().getHeight()) * 0.15));
            Feather2 f2 = new Feather2(p);
            f2.setRotation(269);
            f2.getImage().scale((int)((double)(f2.getImage().getWidth()) * 0.15), (int)((double)(f2.getImage().getHeight()) * 0.15));
            Feather3 f3 = new Feather3(p);
            f3.setRotation(269);
            f3.getImage().scale((int)((double)(f3.getImage().getWidth()) * 0.15), (int)((double)(f3.getImage().getHeight()) * 0.15));
            Actor[] feathers = {f1, f2, f3};
            Actor randf = feathers[(int)(Math.random() * 3)];
            int[] position = positions[(int)(Math.random() * 3)];
            addObject(randf, position[0], position[1]);
            spawn = (int)(Math.random() * 50) + 149;
            fea.add(randf);
            GreenfootSound shoot = new GreenfootSound("featherShoot.mp3");
            shoot.play();
            shoot.setVolume(60);
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
