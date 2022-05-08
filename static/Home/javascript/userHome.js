// Debug 
console.log('This script was created by Mbonu Chinedum'); 

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


// Getting some necessary dom elements 
flash_message = document.getElementById("flash_message"); 



// Adding event listener for the flash message 
document.addEventListener("click", (event) =>{
    // If the user clicks on the page 
    flash_message.style.display = "none"; 
})