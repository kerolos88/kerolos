var list = document.querySelector('#sidenav .tabList');
var navBtn = document.getElementById('openNavBtn');
var pageElements = document.querySelectorAll('*');
var resultBtn = document.getElementById('getResultBtn');
var nationalIdInput = document.getElementById('nationalId');

const students = {
    "30811112703295": {
        name: "صهيب عبدالرحيم",
        score: 505,
        level: "Grade 11",
        percentage: "99%",
        violations: 0,
        behavior: "Excellent",
        absence: 0,
        minus: 0
    },
    "30810232700145": {
        name: "سلمي محمود",
        score: 420,
        level: "Grade 11",
        percentage: "85%",
        violations: 1,
        behavior: "very good ",
        absence: 2,
        minus: 30
    },
    "30706112700034": {
        name: "محمود حسين",
        score: 100,
        level: "Grade 11",
        percentage: "43%",
        violations: 0,
        behavior: "very bad",
        absence: 18,
        minus: 310
    }
    ,
    "30809012709062": {
        name: "فاطمة الزهراء",
        score: 210,
        level: "Grade 11",
        percentage: "76%",
        violations: 4,
        behavior: "trying to be better",
        absence: 6,
        minus: 60
    }
    ,
    "30809012714198": {
        name: "خالد محمد احمد",
        score: 490,
        level: "Grade 11",
        percentage: "95%",
        violations: 2,
        behavior:"Excellent",
        absence: 0,
        minus: 20
    }
    
    
};



function showStudentData() {
    const nationalId = nationalIdInput.value.trim();
    const student = students[nationalId];

    if (student) {
        document.getElementById("studName").innerText = student.name;
        document.getElementById("studScore").innerText = student.score;
        document.getElementById("studLevel").innerText = student.level;
        document.getElementById("studPercent").innerText = student.percentage;
        document.getElementById("studViolation").innerText = student.violations;
        document.getElementById("studBehave").innerText = student.behavior;
        document.getElementById("studAbsence").innerText = student.absence;
        document.getElementById("studMinus").innerText = student.minus;
    } else {
        alert("الطالب غير موجود");
    }
}



function openNav(event) {
  if (list && navBtn) {
    list.style.display = "flex";
    navBtn.style.display = "none";
    event.stopPropagation();
  }
}


function closeNav() {
  if (list && navBtn) {
    list.style.display = "none";
    navBtn.style.display = "block";
  }
}


if (list) {
  list.addEventListener('click', (event) => {
    event.stopPropagation();
  });
}


pageElements.forEach(function (element) {
  if (element !== navBtn && element !== list) {
    element.addEventListener('click', closeNav);
  }
});


if (navBtn) {
  navBtn.addEventListener('click', openNav);
}

if (resultBtn) {
  resultBtn.addEventListener('click', showStudentData);
}
