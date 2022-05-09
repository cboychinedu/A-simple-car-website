// Debug 
console.log("This script was created by Mbonu Chinedum")

// When the user scrools the page, execute myFunction
window.onscroll = function() {staticScroll()};

// Get the header id
let header = document.getElementById("main-nav");

// Get the offset position of the navbar
let sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scrool position. Remove
// "sticky" when you leave the scroll position
function staticScroll()
{
    // Code execution
    if ( window.pageYOffset > sticky )
    {
        // if the condition is met, execute the code below
        header.classList.add("sticky");
    }

    // Else condition
    else
    {
        // code execution
        header.classList.remove("sticky");
    }
};

// Creating a function for creating html tag 
let create_tag = (tagName) => {
    tagName = document.createElement(tagName)

    // return the created tag name 
    return tagName; 
}; 

// Create a div element 
// display_cars_div.innerHTML = `
//     <div class="image-div">
//         <img class="image-data" src="/static/Uploads/08-05-2022-04:33:05.jpg" alt="" srcset="">
//     </div>

// `; 

// Getting the main dom element 
let data_values; 
let display_cars_div = create_tag("div"); 
let button_div = create_tag("div")
let first_div_cars = document.getElementById("first-div-cars")



var slideIndex = 1;
showDivs(slideIndex);


function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  let i;
  let x = document.getElementsByClassName("display-cars");

  // 
  if (n > x.length) {
      slideIndex = 1
    }

  // 
  if (n < 1) {
    slideIndex = x.length
    }

   //  
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";  
  }
  
  // 
  x[slideIndex-1].style.display = "flex";  
}

// Getting the dom elements for the buttons 
let viewCar = (event) => {
    console.log(event); 
}

// Using ajax
// $.ajax({
//     // Setting ajax configurations
//     type: "POST",
//     url: "/polling_units_results",
//     crossDomain: true,
//     contentType: "application/json",
// })
// // On successful connection, execute the code block below
// .done((data, textStatus, request) =>
// {

// }

// Getting the dom element 
let data; 
let url; 
let search_value; 
let result_div = document.getElementById("result-div")
let modal = document.getElementById("myModal");
let searchbtn = document.getElementById("search-car");
let search_value_btn = document.getElementById("search-value")
let span = document.getElementsByClassName("close")[0];

// Creating an element called display cars 
let display_cars = document.createElement("div")

// When the user clicks the button, open the modal 
searchbtn.onclick = function() {
  modal.style.display = "block";

  // Creating a post request to retrive data from the server 
  // Using ajax 
  search_value = search_value_btn.value; 

  // Converting to lower case 
  search_value = search_value.toLowerCase(); 
  data = JSON.stringify({ "search_value": search_value }); 
  url = "/api/search";
  
  // 
  fetch(url, {
    method: 'POST', 
    body: data, 
    headers: {
      'Content-type': 'application/json; charset=UTF-8'
    }
  })
  .then(response => response.json())
  .then(data => {
      // 
      if (data.status == "success") {
          // 
          data = data["data"]

          // 
          for ( let i = 0; i < data.length; i++ ) {
              // 
              username = data[i][0] || ""
              email_address = data[i][1] || ""
              date = data[i][2] || ""
              car_name = data[i][3] || "" 
              model_name = data[i][4] || ""
              version_number = data[i][5] || "" 
              car_desc = data[i][6] || "" 
              car_price = data[i][7] || "" 
              image_path = data[i][8] || ""

              // Building the html page 
              display_cars.classList.add("display-cars"); 
              display_cars.id = "display-cars"; 
              display_cars.innerHTML = `
                    <div class="image-div"> 
                        <img class="image-data" src="${image_path}" alt="" srcset=""> 
                    </div> 
                    <div class="car-prop-div"> 
                        <h3 class="model"> ${model_name} </h3> 
                        <h3 class="version"> ${version_number} </h3> 
                        <h3 class="price"> ${car_price} </h3> 
                        <h4> Posted by: ${username} </h4>
                        <p class="car-description">  
                              ${car_desc}
                        </p> 
                        <div class="button-div"> 
                            <button class="view-car"> View Car </button> 
                            <button class="delete-car" id="delete-car"> Buy Car </button> 
                        </div> 
                    </div>
              `; 


              // Appending display cars into the result div 
              result_div.appendChild(display_cars)



          }
      }

  }); 

  // 
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}