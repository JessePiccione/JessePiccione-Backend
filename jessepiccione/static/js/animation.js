
document.addEventListener('DOMContentLoaded', function(event){
    addDelayToElements('initial-zip'); addDelayToElements('initial-flip');
    addDelayToElements('zippy-letters');addDelayToElements('flippy-letters');
    
    let item = document.querySelector('.zippy-letters');
    item.addEventListener('animationend',async (event) =>{
       await wait(1200);
       event.target.parentNode.classList.remove('initial-zip'); 
    });
    item = document.querySelector('.flippy-letters');
    item.addEventListener('animationend',async (event) =>{
        await wait(1200)
        event.target.parentNode.classList.remove('initial-flip'); 
     });
    
})
async function wait(ms){
    return new Promise(resolve => setTimeout(resolve,ms));
}
function addDelayToElements(hoverClass){
    let delay = .05;
    let items = document.querySelectorAll(`.${hoverClass} > p`);

    items.forEach((item, index) =>{
        item.style.transitionDelay= `${(index*delay)}s`;
        item.style.animationDelay = `${(index*delay)}s`;
    })
}