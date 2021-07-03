let themeMode = document.getElementById("themeMode");
let themeCtrl = document.getElementById("themeCtrl");
var themeBox = document.getElementById("themebx");
let navList = document.getElementById("navList");
let socialMediaBox = document.getElementById("socialMedia");
let socCtrl = document.getElementById("socCtrl");
let ham = document.getElementById("hamburger");
let navbar = document.getElementById("headerNav");

// Hamburger menu js for mid-low screens
function ctrlHam() {
    if (navbar.classList.contains("headerDisp")) {
        navbar.classList.remove("headerDisp");
        console.log("in");
    }
    else {
        navbar.classList.add("headerDisp");
        console.log("out");
    }
}
ham.addEventListener("click", ctrlHam);


// Toggle Theme
themeMode.addEventListener("click", (e) => {
    if (document.documentElement.hasAttribute("theme")) {
        document.documentElement.removeAttribute("theme");
        themeMode.innerHTML = ` <i class="fa fa-moon-o" id="themeMode"></i>`;
    } else {
        document.documentElement.setAttribute("theme", "dark");
        themeMode.innerHTML = ` <i class="fa fa-sun-o" id="themeMode"></i>`;
    }
});


// Lf Box Controller
function ctrlSocico() {
    if (socCtrl.classList.contains("fa-angle-left")) {
        socialMediaBox.style.left = "-60px";
        socCtrl.classList.add("fa-angle-right");
        socCtrl.classList.remove("fa-angle-left");
    } else if (socCtrl.classList.contains("fa-angle-right")) {
        socialMediaBox.style.left = "0px";
        socCtrl.classList.add("fa-angle-left");
        socCtrl.classList.remove("fa-angle-right");
    }
}
socCtrl.addEventListener("click", ctrlSocico);
