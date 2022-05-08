// Debug 
console.log("This script was created by Mbonu Chinedum")
let data_values; 
let display_cars_div = document.getElementById("display-cars"); 

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

// Getting data 
$.ajax({
    // 
    type: "POST", 
    url: "/api/cars", 
    crossDomain: true, 
    contentType: "application/json",
})
// 
.done((data, textStatus, req) => {
    console.log(data); 
    data_values = data.data; 
})


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