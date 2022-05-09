// 

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

// 
// Getting the dom elements for the buttons 
let viewCar = (event) => {
    console.log(event); 
}

deleteCar = (image_path) => {
    console.log(event)

    // Getting the name of the image to delete 
    let listValue = image_path.split("/")
    image_name = listValue[listValue.length - 1]; 

    // Creating a delete request to the server 
    // Using ajax 
    $.ajax({
        // Setting the configurations 
        type: "DELETE", 
        url: "/api/delete-car", 
        crossDomain: true, 
        contentType: "application/json", 
        data: JSON.stringify({ "image_name": image_name})
    })
    .done((data) => {
        // 
        if (data.status === "success") {
            location.reload(); 
        }

        // 
        else {
            alert("Error, cannot delete data.")
        }
    })
    
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