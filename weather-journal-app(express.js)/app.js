

/* Global Variables */
const base='http://api.openweathermap.org/data/2.5/weather?zip='
const key='&APPID=c771985d72d094d3458772aae08cfee0&units=imperial'
let temp='';

// Create a new date instance dynamically with JS
let d = new Date();
let newDate = d.getMonth()+'.'+ d.getDate()+'.'+ d.getFullYear();
/*******************************************************************************************************/

/******************************** function to post data to server **************************************/
const postData = async (url = '', data = {}) => {
	 console.log("2->PostData() begin ",data);
  const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(data), // body data type must match "Content-Type" header        
  });

  try {
      const newData = await response.json();
      return newData
  } catch (error) {
      console.log("error", error);
      // appropriately handle the error
  }
}
/**************************************************************************************************** */

/***************************function to get data from openweather.com********************************** */
const getData=async (url)=>{
  const res=await fetch(url) //fetch weather from URL

  try{
      const data=await res.json();
      return data;
  }
    catch(error) {
      console.log("error", error);}}
 /************************************************************************************************** */ 
 //add event listner 
 document.getElementById("generate").addEventListener("click",performAction); 
 
 /*******************************************************chain of promises  **************************/
function performAction(e){
e.preventDefault();
const content=document.getElementById("feelings").value;
const zipcode = document.getElementById("zip").value;
const url=base+zipcode+key;
console.log(" ");
console.log("1->GetData from openweather.com")
getData(url)

.then(function(data){
  // Add data
  
  postData('http://localhost:3000/add', {date:newDate, temp:data.main.temp,content:content} );//send data to server
  
})
.then(function(){
updateUI();}	
 )


}
/*************************************************************************************************** */

/*************************************function to update UI ******************************************/
const updateUI = async () => {

  const request = await fetch('http://localhost:3000/all');
  try{
    const allData = await request.json();
    console.log('3->updateUi() begin',allData);
    document.getElementById('temp').innerHTML ='Temprature:'+ allData.temp;
    document.getElementById('date').innerHTML = 'Date:'+allData.date;
    document.getElementById('content').innerHTML = 'Response:'+allData.content;

  }catch(error){
    console.log("error", error);
  }
}
/**************************************************************************************************** */


