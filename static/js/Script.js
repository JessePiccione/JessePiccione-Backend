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
    loadAssistant(event);
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
async function loadAssistant(event){
    //load intial message from assistant 
    await loadMessage(event, 'Give a greetings message to someone who just visited the JessePiccione.info website.');
    get('#assistantForm').addEventListener('submit', sendMessage);
}
async function sendMessage(event){
    event.preventDefault()
    var messageElement = get('#assistantMessage');
    const message = messageElement.value;
    const date = new Date(Date.now());
    messageElement.value = '';
    var messageRows = get('#assistantMessageRows');
    messageRows.innerHTML += `<div class='row mb-2'>
    <div class='col-2'></div>
    <div class='col-10 end-0'>
        <div class='card' data-bs-theme='light'> 
            <div class='card-body'>
                ${message}
            </div>
            <div class='card-footer text-end'>
            ${date.getFullYear()}-${date.getMonth()}-${date.getDay()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}.${date.getMilliseconds()}
            </div>
        </div>
    </div>
</div>`
messageRows.scrollTop = messageRows.scrollHeight
loadMessage(event, message)
}
async function loadMessage(event, message){
    event.preventDefault();
    var messageRows = get("#assistantMessageRows")
    messageRows.innerHTML += `<div class='row mb-2'>
    <div class='col-10 position-relative end-0'>
        <div class='card' data-bs-theme='light'>
            <div class='card-body placeholder-glow'>
                <span class='placeholder col-7'></span>
                <span class='placeholder col-4'></span> 
                <span class='placeholder col-4'></span>
                <span class='placeholder col-6'></span>
                <span class='placeholder col-5'></span>
                <span class='placeholder col-4'></span>
            </div>
            <div class='d-flex align-items-center card-footer placeholder-glow'>
                Loading... 
                <div class="spinner-border spinner-border-sm ms-auto" role="status" aria-hidden="true"></div>
            </div>
        </div>
    </div>
</div>`;
    const body = {
        'message':message
    } 
    const req = await fetch('/assistant/message',  
    {
            method:"POST",
            headers:{
                'X-CSRFToken':document.getElementsByName('csrfmiddlewaretoken')[0].value
            },
            body: JSON.stringify(body)
        }
    );
    var res = await req.text() + ""
    res = JSON.parse(res)
    date = new Date(res.time);
    messageRows.children[messageRows.children.length-1].remove()
    messageRows.innerHTML += `<div class='row mb-2'>
    <div class='col-10 position-relative end-0'>
        <div class='card' data-bs-theme='light'>
            <div class='card-body'>
                ${res.message}
            </div>
            <div class='card-footer'>
                ${date.getFullYear()}-${date.getMonth()}-${date.getDay()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}.${date.getMilliseconds()}
            </div>
        </div>
    </div>
</div>`
    messageRows.scrollTop = messageRows.scrollHeight
}