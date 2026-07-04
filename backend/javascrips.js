
const buttom = document.querySelector(".buttom");
const displayTextPassword = document.querySelector(".display-text-password");

buttom.addEventListener("click", async () =>{
    try{
        const result = await fetch("http://127.0.0.1:5000/aleatory-password")
        const dates = await result.json();

        displayTextPassword.innerHTML = dates.result;

    }catch(error){
        displayTextPassword.innerHTML = "An error has occurred"
    }
})









