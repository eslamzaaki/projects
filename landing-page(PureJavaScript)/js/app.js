/**
 * 
 * Manipulating the DOM exercise.
 * Exercise programmatically builds navigation,
 * scrolls to anchors from navigation,
 * and highlights section in viewport upon scrolling.
 * 
 * Dependencies: None
 * 
 * JS Version: ES2015/ES6
 * 
 * JS Standard: ESlint
 * 
*/

/**
 * Define Global Variables
 * 
*/
const sections = document.querySelectorAll("section");
/**
 * End Global Variables
 * Start Helper Functions
 * 
**///////////////////////////////////////////////////////////////////////////////////////////////////////
let hideNavBar = _ => {
    if (document.querySelector(".page__header").style.display != 'none' && document.documentElement.scrollTop != 0) {
        document.querySelector(".page__header").style.display = 'none';
    }
}
/////////////////////////////////////////////////////////////////
let displayNavBar = _ => {
    if (document.querySelector(".page__header").style.display != 'block') {
        document.querySelector(".page__header").style.display = 'block';
    }
}

//////////////////////////////////////////////////////////
let toTop = _ => {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
//////////////////////////////////////////////////////////
function displayContent() {

    const content = this.nextElementSibling;

    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
}
/**
 * End Helper Functions
 * Begin Main Functions
 * 
 *
*/////////////////////////////////////////////////////////////////////////////////////////////////////////

// build the nav
let creatNav = _ => {
    const virt_dom = document.createDocumentFragment();

    for (const section of sections) {
        const new_li = document.createElement("li");
        const new_a = document.createElement("a");
        new_a.href = `#${section.getAttribute('id')}`;
        new_a.classList.add("menu__link");
        new_a.textContent = section.getAttribute('data-nav');
        new_li.appendChild(new_a);
        virt_dom.appendChild(new_li);
    }
    document.getElementById("navbar__list").appendChild(virt_dom);

}

// Add class 'active' to section when near top of viewport
let addActiveClass = _ => {

    const offsetTop = document.getElementById("sections").offsetTop;//ofsset from top of document to start of sections
    //clear all sections from active state
    for (const sectione of sections) {
        if (sectione.classList.contains('active')) { sectione.classList.remove("active"); }
    }
    //add active class
    for (const section of sections) {
        const top = Math.abs(section.getBoundingClientRect().top);//top respect to document top
        if (top > 0 && top < offsetTop - 100) {
            section.classList.add("active");
            break;
        }
    }
}

// Scroll to anchor ID using scrollTO event
let anchorhandler = (ev) => {
    let section = document.querySelector(ev.target.href);
    ev.preventDefault();             //prevent default action of anchor
    ev.target.scrollIntoView(section);

}

// display  top button while scrolling
let displayToTop = _ => {
    const mybutton = document.getElementById("myBtn");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}
/**
 * End Main Functions
 * Begin Events
 *
*////////////////////////////////////////////////////////////////////////////////////////////////////////

// Build menu 
creatNav();

// Scroll to section on link click
document.getElementById("navbar__list").addEventListener("click", anchorhandler);

// Set sections as active
window.onscroll = _ => {
    displayNavBar();                 //display navbar while scrolling
    setTimeout(addActiveClass, 100); //add active class to section close to top of view port
    setTimeout(displayToTop, 100);   //display to top button
    setTimeout(hideNavBar, 4000);   // hide navbar after 4 sec of stop scrolling
}

//go to top of page  when click top  button
document.getElementById('myBtn').addEventListener('click', toTop);

//make sections collisaple 
var coll = document.getElementsByClassName("collapsible");

//add click Event listner  to each section content to display this content
for (const collis of coll) {
    collis.addEventListener("click", displayContent);
}