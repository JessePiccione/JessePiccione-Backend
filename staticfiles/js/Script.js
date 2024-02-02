document.addEventListener('DOMContentLoaded', loadHomeView);

async function loadHomeView(event){
    event.preventDefault();
    const response =  await fetch('/home')
    const main = document.getElementById('mainContentContainer').innerHTML = await response.text()
}