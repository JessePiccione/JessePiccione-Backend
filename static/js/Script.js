//dom event listeners for JessePiccione.info 
document.addEventListener('DOMContentLoaded', loadDOM);
function get(name){
    return document.querySelector(name);
}
function getAll(name){
    return document.querySelectorAll(name);
}
async function loadDOM(event){
    form = get('#messageForm');
    form.addEventListener('submit', interceptMessage)
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
    const main = get("#mainContentContainer");
    main.classList.add('transitionOut')
    await wait(500);
    main.innerHTML = await req.text()
    main.classList.remove('transitionOut')
    main.classList.add("transitionIn")
    await wait(500);
    getAll('.active').forEach((element)=>{
        element.classList.remove('active');
    })
    get('#'+name).classList.add('active')
    main.classList.remove('transitionIn')
    event.preventDefault()
}
//script to communicate with GPT Assistant Model.
async function loadAssistant(event){
    //load intial message from assistant 
    await loadMessage(event, 'Give a greetings message to someone who just visited the JessePiccione.info website.');
    get('#assistantForm').addEventListener('submit', sendMessage);
}
async function sendMessage(event){
    event.preventDefault()
    var messageElement = get('#assistantMessage');
    const message = messageElement.value;
    const date = new Date();
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
            ${date.toLocaleString()}
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
</div>`;
    messageRows.scrollTop = messageRows.scrollHeight
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
    date = new Date(Date.now());
    messageRows.children[messageRows.children.length-1].remove()
    messageRows.innerHTML += `<div class='row mb-2'>
    <div class='col-10 position-relative end-0'>
        <div class='card' data-bs-theme='light'>
            <div class='card-body'>
                ${res.message}
            </div>
            <div class='card-footer'>
                ${date.toLocaleString()}
            </div>
        </div>
    </div>
</div>`
    messageRows.scrollTop = messageRows.scrollHeight
}
//message intercepter
async function interceptMessage(event){
    event.preventDefault();
    form = get('#messageForm')
    formdata = new FormData(form);
    formdata.delete('csrfmiddlewaretoken');
    console.log(formdata)
    fetch(form.action,{
        method:'POST',
        headers:{
            'X-CSRFToken':document.getElementsByName('csrfmiddlewaretoken')[0].value
         },
        body: formdata})
    .then(response =>response.status)
    .then(data=> {
        if(data==201){
            alert('Message Successfully Sent!')
        }
        else{
            alert('Message Was Not Successfully Sent')
        }
        location.reload()
    })
}
