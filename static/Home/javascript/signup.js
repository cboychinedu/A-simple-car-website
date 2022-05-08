// Debug 
console.log('This script was created by Mbonu Chinedum'); 

// Getting some necessary dom elements 
flash_message = document.getElementById("flash_message"); 



// Adding event listener for the flash message 
document.addEventListener("click", (event) =>{
    // If the user clicks on the page 
    flash_message.style.display = "none"; 
})