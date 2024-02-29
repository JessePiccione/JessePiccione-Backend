document.addEventListener('DOMContentLoaded', loadDOM);
function get(name){
    return document.querySelector(name);
}
function getAll(name){
    return document.querySelectorAll(name);
}
async function loadDOM(event){
    loadViewName(event,'home');
    getAll('.nav-link').forEach((element)=>{
        element.addEventListener("click",function(event){loadViewName(event,element.id)})
    })
}
async function loadViewName(event, name){
    const req = await fetch("/"+name+'/',
        {
         method:'POST',
         headers:{
            'X-CSRFToken':document.getElementsByName('csrfmiddlewaretoken')[0].value
         }   
        }
    );
    const main = get("#mainContentContainer").innerHTML = await req.text()
    getAll('.active').forEach((element)=>{
        element.classList.remove('active');
    })
    get('#'+name).classList.add('active')
    event.preventDefault()
}
