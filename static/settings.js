function startTheme() {
    setTheme();
    setInterval(setTheme, 5 * 60 * 1000);
}

function setTheme() {
    const temaGuardado = localStorage.getItem("data-theme");
    const htmlBody = document.getElementById('html-body');

    if (temaGuardado) {
        htmlBody.setAttribute("data-theme", temaGuardado);
    } else {
        setAndDefineTheme();
    }
}

function setAndDefineTheme() {
    const hora = new Date().getHours();
    const nuevoTema = (hora >= 6 && hora < 18) ? "light" : "dark";

    const htmlBody = document.getElementById('html-body');
    const temaActual = htmlBody.getAttribute("data-theme");

    if (temaActual !== nuevoTema) {
        htmlBody.setAttribute("data-theme", nuevoTema);
        localStorage.setItem("data-theme", nuevoTema);
    }
}

let toogleNavStat = false;
const nav = document.getElementById('responsive-nav');

function toogleNav() {
    if (!toogleNavStat) {
        nav.classList.add('active');
        toogleNavStat = true;
    } else {
        nav.classList.remove('active');
        toogleNavStat = false;
    }
}