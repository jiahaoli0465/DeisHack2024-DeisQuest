window.addEventListener("DOMContentLoaded", () => {
    console.log("home")

    let addEventButtons = document.getElementsByClassName("add-event")
    let questList = document.getElementById("quests-list")

    for(let btn of addEventButtons){

        btn.addEventListener("click", ()=>{
            btn.disabled = true;
            btn.innerHTML = "Event added!"

            let eventName = btn.parentNode.parentNode.firstElementChild.firstChild.nextSibling.innerHTML
            let eventDate = btn.parentNode.parentNode.firstElementChild.firstChild.nextSibling.nextElementSibling.innerHTML 
            console.log(eventDate)

            questList.insertAdjacentHTML("beforeend", `<li class="list-group-item"><a href="/task" class="list-group-link custom-link">${eventName} (${eventDate}) (1 pt)</a></li>`)
        })

        setTimeout(()=>{
            console.log("alte")
        }, "1000")

        console.log("do the thing")
    }
})