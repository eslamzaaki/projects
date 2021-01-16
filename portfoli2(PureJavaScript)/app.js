const hamburger = document.querySelector('.header .nav-bar .nav-list .hamburger');
const mobile_menu=document.querySelector('.header .nav-bar .nav-list ul');
const menu_item=document.querySelectorAll('.header .nav-bar .nav-list ul li a');
const header=document.querySelector('.header.container');

hamburger.addEventListener('click',()=>{
    hamburger.classList.toggle('active'); 
     mobile_menu.classList.toggle('active');  });

document.addEventListener('scroll',()=>{
    const scroll_position=window.scrollY;
    if(scroll_position>250){
        header.style.backgroundColor='#29323c';
    
    }
    else{
        header.style.backgroundColor='transparent';
    }
});

menu_item.forEach((item)=>{
    item.addEventListener('click',()=>{
        hamburger.classList.toggle('active'); 
        mobile_menu.classList.toggle('active');  
    });
});

let anchorhandler = (ev) => {
    let section = document.querySelector(ev.target.href);
    if(section){
    ev.preventDefault();             //prevent default action of anchor
    ev.target.scrollIntoView(section);}


}
document.getElementById("header").addEventListener("click", anchorhandler);

///////////////////////////////////////////test things not in projects/////////////////////////////////////
const SETTING=[1,2,3,4];
SETTING.push(5,6,7);
console.log(SETTING);
Object.freeze(SETTING);

let test=p1=> p1*2;
console.log(test(12));
console.log(...SETTING)
const arr2=[...SETTING];
let sum=(...arr)=>{
    let total=0;
    for(item of arr){
        total+=item
    }
    return total;
}
console.log(sum(1,5,4,1,3,12)
)
console.log(Math.min(...SETTING));
let eslam='hello from other side';
eslam='newKey';
let user={
    name:'eslam',
    age:32,
    city:'cairo',
    langs:{
        html:'70%',
        css:'80%',
        js:'10%',},
        test (p1,p2) {return p1*p2},
        [eslam]:'value'
    
}
eslam='newKey';
const myobj={
name:'eslam',
age:23,
country:'egypt',
[Symbol.iterator](){

let step=0;
let pros=Object.keys(this);

return{
next(){
    return{
    value:pros[step],
    done:step++===pros.length}
}

}

}
}
//var variable = new Set(iterable)
/* Methods:
>add
>delete
>has
>clear
>forEach(fn(item,index,the))
*/
var collection = new Set([1,2,3,4]);
var newelements =[4,8,10];
for(i of newelements){
    collection.add(i);
}
console.log(collection);