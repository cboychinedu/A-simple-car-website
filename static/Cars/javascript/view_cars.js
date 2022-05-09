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