var sex = 0;
var age = 0;
var age_counter = 0;
var siblings = [];
var parents = [];
var fare = 0;
var class_b = [];
var alone = 0;
var survived = 0;
const total = 891;
let button;
var show = false;

function preload() {
  table = loadTable('/titanic.csv', 'csv', 'header');
}

function setup() {
  createCanvas(400, 400);
  setSelects();

  avg();

  textSize(16);
  noStroke();
  textAlign(LEFT);

  button = createButton('Submit');
  button.position(340, 10);

}

function draw() {
  background(220);
  type2.disable(type1.value());
  button.mousePressed(calculate);
  if (show) {
    text("Pick a value.", 10, 50);
  } else {
    if (type2.value() != 'Pick an optional category') {
      if (type1.value() == 'sex') {
        if (type2.value() == 'age') {

        } else if (type2.value() == 'siblings') {

        } else if (type2.value() == 'parents') {

        } else if (type2.value() == 'fare') {

        } else if (type2.value() == 'class') {

        } else if (type2.value() == 'alone') {

        } else if (type2.value() == 'survived') {

        }
      } else if (type1.value() == 'age') {
        if (type2.value() == 'sex') {

        } else if (type2.value() == 'siblings') {

        } else if (type2.value() == 'parents') {

        } else if (type2.value() == 'fare') {

        } else if (type2.value() == 'class') {

        } else if (type2.value() == 'alone') {

        } else if (type2.value() == 'survived') {

        }
      } else if (type1.value() == 'siblings') {
        if (type2.value() == 'age') {

        } else if (type2.value() == 'sex') {

        } else if (type2.value() == 'parents') {

        } else if (type2.value() == 'fare') {

        } else if (type2.value() == 'class') {

        } else if (type2.value() == 'alone') {

        } else if (type2.value() == 'survived') {

        }
      } else if (type1.value() == 'parents') {
        if (type2.value() == 'age') {

        } else if (type2.value() == 'siblings') {

        } else if (type2.value() == 'sex') {

        } else if (type2.value() == 'fare') {

        } else if (type2.value() == 'class') {

        } else if (type2.value() == 'alone') {

        } else if (type2.value() == 'survived') {

        }
      } else if (type1.value() == 'fare') {
        if (type2.value() == 'age') {

        } else if (type2.value() == 'siblings') {

        } else if (type2.value() == 'parents') {

        } else if (type2.value() == 'sex') {

        } else if (type2.value() == 'class') {

        } else if (type2.value() == 'alone') {

        } else if (type2.value() == 'survived') {

        }
      } else if (type1.value() == 'class') {
        if (type2.value() == 'age') {

        } else if (type2.value() == 'siblings') {

        } else if (type2.value() == 'parents') {

        } else if (type2.value() == 'fare') {

        } else if (type2.value() == 'sex') {

        } else if (type2.value() == 'alone') {

        } else if (type2.value() == 'survived') {

        }
      } else if (type1.value() == 'alone') {
        if (type2.value() == 'age') {

        } else if (type2.value() == 'siblings') {

        } else if (type2.value() == 'parents') {

        } else if (type2.value() == 'fare') {

        } else if (type2.value() == 'class') {

        } else if (type2.value() == 'sex') {

        } else if (type2.value() == 'survived') {

        }
      } else if (type1.value() == 'survived') {
        if (type2.value() == 'age') {

        } else if (type2.value() == 'siblings') {

        } else if (type2.value() == 'parents') {

        } else if (type2.value() == 'fare') {

        } else if (type2.value() == 'class') {

        } else if (type2.value() == 'alone') {

        } else if (type2.value() == 'sex') {

        }
      }
    } else {
      if (type1.value() == 'sex') {
        let dis = sex/total;
        text(dis, 10, 50);
      } else if (type1.value() == 'age') {
        let dis = age/age_counter;
        text(dis, 10, 50);
      } else if (type1.value() == 'siblings') {
        let dis = {};
        for (const n of siblings) {
          dis[n] = dis[n] ? siblings[n] + 1 : 1;
        }
        for (count in dis) {
          disp = toString(count) + ": " + 
          text(count, 10, 50);
        }
      } else if (type1.value() == 'parents') {
        let dis = sex/total;
        text(dis, 10, 50);
      } else if (type1.value() == 'fare') {
        let dis = sex/total;
        text(dis, 10, 50);
      } else if (type1.value() == 'class') {
        let dis = sex/total;
        text(dis, 10, 50);
      } else if (type1.value() == 'alone') {
        let dis = sex/total;
        text(dis, 10, 50);
      } else if (type1.value() == 'survived') {
        let dis = sex/total;
        text(dis, 10, 50);
      }
    }
  }
}

function setSelects() {
  type1 = createSelect()
  type1.position(10, 10)
  type1.option('Pick a category')
  type1.option('sex')
  type1.option('age')
  type1.option('siblings')
  type1.option('parents')
  type1.option('fare')
  type1.option('class')
  type1.option('alone')
  type1.option('survived');
  type1.selected('Pick a category');
  type2 = createSelect()
  type2.position(150, 10)
  type2.option('Pick an optional category');
  type2.option('sex')
  type2.option('age')
  type2.option('siblings')
  type2.option('parents')
  type2.option('fare')
  type2.option('class')
  type2.option('alone')
  type2.option('survived');
  type2.selected('Pick an optional category');
}

function calculate() {
  if (type1.value() == 'Pick a category') {
    setSelects()
    show = true;
    console.log("a");
  } else {
    setSelects()
    show = false;
  }
}

function avg() {
  for (let i = 0; i < table.getRowCount(); i++) {
    for (let j = 0; j < table.getColumnCount(); j++) {
      if (j == 0 && table.getString(i, j) == 'male') {
        sex +=1;
      } else if (j == 1 && table.getString(i, j) != "") {
        age += parseInt(table.getString(i, j));
        age_counter += 1;
      } else if (j == 2) {
        siblings.push(parseInt(table.getString(i, j)))
      } else if (j == 3) {
        parents.push(parseInt(table.getString(i, j)))
      } else if (j == 4) {
        fare += parseInt(table.getString(i, j));
      } else if (j == 6) {
        class_b.push(parseInt(table.getString(i, j)))
      } else if (j == 8 && table.getString(i, j) == 'TRUE') {
        alone += parseInt(table.getString(i, j));
      } else if (j == 9 && table.getString(i, j) == '1') {
        survived += parseInt(table.getString(i, j));
      }
    }
  }
}
