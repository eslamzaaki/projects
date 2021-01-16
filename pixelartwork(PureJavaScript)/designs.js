


const tablee=document.getElementById("pixelCanvas");//table object
const picker=document.getElementById("colorPicker");//input color object
var flag=0;//flag to indicate first submit or no so i
var flag2=0;
/***************************************************************************************************/
function makeGridd(event){
    event.preventDefault();
    if(flag===0){flag=1;}//if this first time submit skip next step and make flag=1
    else{tablee.removeChild(document.getElementsByTagName("tbody")[0])}//remove old body of table each time 
    const widthe=document.forms["myform"]["width"].value; //width from form
    const heighte=document.forms["myform"]["height"].value;//height from form
    const tbodyy=document.createElement('tbody');//creat new body for table
          
    for (let i=0;i<heighte;i=i+1){ //loop to creat rows
       var row = document.createElement("tr");
  
     for(let j=0;j<widthe;j=j+1){ //loop to creat columns
    var cell = document.createElement("td");
  row.appendChild(cell); }
      
       tbodyy.appendChild(row);}//append each row to table body
     tablee.appendChild(tbodyy);//append table body to table
        
      };
document.forms[0].addEventListener('submit',makeGridd);  
  /****************************************************************************************************** */  
 function change(event){ event.target.style.backgroundColor=picker.value;};
  
  function pick(event){//listen to click on table
   if(flag2===0){tablee.addEventListener("mousemove",change);flag2=1;}
   else{tablee.removeEventListener("mousemove",change);flag2=0;}       
};
tablee.addEventListener("click",pick);
