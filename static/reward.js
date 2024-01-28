


window.addEventListener("DOMContentLoaded", ()=>{
    console.log("window loadeed")
    let claims = document.getElementsByClassName("claim")

    for(let claim of claims){
        console.log("a")
        claim.addEventListener("click", ()=>{
            console.log("cloicked")

            claim.setAttribute("style", "background-color:green;color:white;")
            claim.innerHTML = "Claimed!"
            claim.disabled = true;
        })
    }
})

