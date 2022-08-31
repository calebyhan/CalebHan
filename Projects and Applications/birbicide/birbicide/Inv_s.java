import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Investications of suspects
 * 
 * @author Caleb Han and Elynn An 
 */
public class Inv_s extends World
{
    private boolean b1, b2, m1, m2, oc1, oc2, oc3, oc4, f1, f2, yc1, ff1;
    
    public Inv_s() {    
        super(900, 570, 1);
        removeObjects(getObjects(null));
        Textbox t = new Textbox();
        if (!checkC()) {
            Choice_S1 c1 = new Choice_S1();
            addObject(t, 450, 285);
            addObject(c1, 450, 285);
        } else {
            Interview i = new Interview();
            addObject(t, 450, 285);
            addObject(i, 450, 285);
        }
        b1 = b2 = m1 = m2 = oc1 = oc2 = oc3 = oc4 = f1 = f2 = yc1 = ff1 = false;
    }
    
    //go through suspects
    public void act() {
        Title.music();
        Title.GLOBAL_T += 1;
        Textbox t = new Textbox();
        if (!checkC()) {
            int[] pos = getMouse();
            if (b1 && !b2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Shivers s = new Shivers();
                    addObject(s, 450, 285);
                    addObject(t, 450, 285);
                    Butler_2 Butler_2 = new Butler_2();
                    addObject(Butler_2, 450, 285);
                    b2 = true;
                }
            } else if (b2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    C2 s = new C2();
                    Greenfoot.setWorld(s);
                }
            }
            else if (m1 && !m2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Toma t1 = new Toma();
                    addObject(t1, 450, 285);
                    addObject(t, 450, 285);
                    Macaw_2 Macaw_2 = new Macaw_2();
                    addObject(Macaw_2, 450, 285);
                    m2 = true;
                }
            } else if (m2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    addObject(t, 450, 285);
                    C2 s = new C2();
                    Greenfoot.setWorld(s);
                }
            }
            else if (oc1 && !oc2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Bean b = new Bean();
                    addObject(b, 450, 285);
                    addObject(t, 450, 285);
                    OChild_2 OChild_2 = new OChild_2();
                    addObject(OChild_2, 450, 285);
                    oc2 = true;
                }
            } else if (oc2 && !oc3) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Bean b = new Bean();
                    addObject(b, 450, 285);
                    addObject(t, 450, 285);
                    OChild_3 OChild_3 = new OChild_3();
                    addObject(OChild_3, 450, 285);
                    oc3 = true;
                }
            } else if (oc3 && !oc4) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Bean b = new Bean();
                    addObject(b, 450, 285);
                    addObject(t, 450, 285);
                    OChild_4 OChild_4 = new OChild_4();
                    addObject(OChild_4, 450, 285);
                    oc4 = true;
                }
            } else if (oc4) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    C2 s = new C2();
                    Greenfoot.setWorld(s);
                }
            }
            else if (f1 && !f2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Moss m = new Moss();
                    addObject(m, 450, 285);
                    addObject(t, 450, 285);
                    Friend_2 Friend_2 = new Friend_2();
                    addObject(Friend_2, 450, 285);
                    f2 = true;
                }
            } else if (f2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    C2 s = new C2();
                    Greenfoot.setWorld(s);
                }
            }
            else if (pos[0] >= 117 && pos[0] <= 215 && pos[1] >= 518 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Shivers s = new Shivers();
                addObject(s, 450, 285);
                addObject(t, 450, 285);
                Butler_1 Butler_1 = new Butler_1();
                addObject(Butler_1, 450, 285);
                b1 = true;
                Title.interviewed[0] = true;
            } else if (pos[0] >= 258 && pos[0] <= 359 && pos[1] >= 518 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Toma t1 = new Toma();
                addObject(t1, 450, 285);
                addObject(t, 450, 285);
                Macaw_1 Macaw_1 = new Macaw_1();
                addObject(Macaw_1, 450, 285);
                m1 = true;
                Title.interviewed[1] = true;
            } else if (pos[0] >= 403 && pos[0] <= 457 && pos[1] >= 518 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Bean b = new Bean();
                addObject(b, 450, 285);
                addObject(t, 450, 285);
                OChild_1 OChild_1 = new OChild_1();
                addObject(OChild_1, 450, 285);
                oc1 = true;
                Title.interviewed[2] = true;
            } else if (pos[0] >= 502 && pos[0] <= 602 && pos[1] >= 518 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Moss m = new Moss();
                addObject(m, 450, 285);
                addObject(t, 450, 285);
                Friend_1 Friend_1 = new Friend_1();
                addObject(Friend_1, 450, 285);
                f1 = true;
                Title.interviewed[3] = true;
            }
        } else if (checkC()) {
            int[] pos = getMouse();
            if (pos[0] != 0 && !ff1) {
                removeObjects(getObjects(null));
                ff1 = true;
                Choice_S2 c2 = new Choice_S2();
                addObject(t, 450, 285);
                addObject(c2, 450, 285);
            }
            if (b1 && !b2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Shivers s = new Shivers();
                    addObject(s, 450, 285);
                    addObject(t, 450, 285);
                    Butler_2 Butler_2 = new Butler_2();
                    addObject(Butler_2, 450, 285);
                    b2 = true;
                }
            } else if (b2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    C2 s = new C2();
                    Greenfoot.setWorld(s);
                }
            }
            else if (m1 && !m2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Toma t1 = new Toma();
                    addObject(t1, 450, 285);
                    addObject(t, 450, 285);
                    Macaw_2 Macaw_2 = new Macaw_2();
                    addObject(Macaw_2, 450, 285);
                    m2 = true;
                }
            } else if (m2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    C2 s = new C2();
                    Greenfoot.setWorld(s);
                }
            }
            else if (oc1 && !oc2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Bean b = new Bean();
                    addObject(b, 450, 285);
                    addObject(t, 450, 285);
                    OChild_2 OChild_2 = new OChild_2();
                    addObject(OChild_2, 450, 285);
                    oc2 = true;
                }
            } else if (oc2 && !oc3) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Bean b = new Bean();
                    addObject(b, 450, 285);
                    addObject(t, 450, 285);
                    OChild_3 OChild_3 = new OChild_3();
                    addObject(OChild_3, 450, 285);
                    oc3 = true;
                }
            } else if (oc3 && !oc4) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Bean b = new Bean();
                    addObject(b, 450, 285);
                    addObject(t, 450, 285);
                    OChild_4 OChild_4 = new OChild_4();
                    addObject(OChild_4, 450, 285);
                    oc4 = true;
                }
            } else if (oc4) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    C2 s = new C2();
                    Greenfoot.setWorld(s);
                }
            }
            else if (f1 && !f2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Moss m = new Moss();
                    addObject(m, 450, 285);
                    addObject(t, 450, 285);
                    Friend_2 Friend_2 = new Friend_2();
                    addObject(Friend_2, 450, 285);
                    f2 = true;
                }
            } else if (f2) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    C2 s = new C2();
                    Greenfoot.setWorld(s);
                }
            }
            else if (yc1) {
                if (pos[0] != 0) {
                    removeObjects(getObjects(null));
                    Final_battle s = new Final_battle();
                    Greenfoot.setWorld(s);
                }
            }
            else if (pos[0] >= 117 && pos[0] <= 215 && pos[1] >= 518 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Shivers s = new Shivers();
                addObject(s, 450, 285);
                addObject(t, 450, 285);
                Butler_1 Butler_1 = new Butler_1();
                addObject(Butler_1, 450, 285);
                b1 = true;
                Title.interviewed[0] = true;
            } else if (pos[0] >= 258 && pos[0] <= 359 && pos[1] >= 518 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Toma t1 = new Toma();
                addObject(t1, 450, 285);
                addObject(t, 450, 285);
                Macaw_1 Macaw_1 = new Macaw_1();
                addObject(Macaw_1, 450, 285);
                m1 = true;
                Title.interviewed[1] = true;
            } else if (pos[0] >= 403 && pos[0] <= 457 && pos[1] >= 518 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Bean b = new Bean();
                addObject(b, 450, 285);
                addObject(t, 450, 285);
                OChild_1 OChild_1 = new OChild_1();
                addObject(OChild_1, 450, 285);
                oc1 = true;
                Title.interviewed[2] = true;
            } else if (pos[0] >= 502 && pos[0] <= 602 && pos[1] >= 518 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Moss m = new Moss();
                addObject(m, 450, 285);
                addObject(t, 450, 285);
                Friend_1 Friend_1 = new Friend_1();
                addObject(Friend_1, 450, 285);
                f1 = true;
                Title.interviewed[3] = true;
            } else if (pos[0] >= 647 && pos[0] <= 744 && pos[1] >= 522 && pos[1] <= 542) {
                removeObjects(getObjects(null));
                Ricardo_h r = new Ricardo_h();
                addObject(r, 450, 285);
                addObject(t, 450, 285);
                YChild YChild = new YChild();
                addObject(YChild, 450, 285);
                yc1 = true;
                Title.interviewed[4] = true;
            }
        }
    }
    
    public boolean checkC() {
        int counter1 = 0;
        int counter2 = 0;
        for (boolean v : Title.clues) {
            if (v) counter1 += 1;
        }
        for (boolean v : Title.interviewed) {
            if (v) counter2 += 1;
        }
        if (counter1 >= 2 && counter2 >= 3) return true;
        return false;
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
