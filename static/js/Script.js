document.addEventListener('DOMContentLoaded', loadHomeView);

async function loadHomeView(event){
    event.preventDefault();
    const response =  await fetch('/home');
    const main = document.getElementById('mainContentContainer').innerHTML = await response.text();
}
//TODO add in work experience view
async function loadExperienceView(event){
    event.preventDefault();
}
//TODO add in Education function 
async function loadEducationView(event){
    event.preventDefault();
}
//TODO add in Projects view
async function loadProjectsView(event){
    event.preventDefault();
}
//TODO add in SKills view
async function loadSkillsView(event){
    event.preventDefault();
}

