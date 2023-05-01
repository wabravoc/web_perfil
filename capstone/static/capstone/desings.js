addEventListener('DOMContentLoaded',()=>{document.querySelector('#New_contact').addEventListener('click',()=>register_contact());const btn_menu=document.querySelector('.btn_menu')
if(btn_menu){btn_menu.addEventListener('click',()=>{const menu_items=document.querySelector('.menu_items')
menu_items.classList.toggle('mostrar')})}
const secciones=document.querySelectorAll('.seccion')
const menuItems=document.querySelectorAll('.menu_item')
const funcionObserver=entries=>{entries.forEach(entry=>{if(entry.isIntersecting){const itemActual=Array.from(menuItems).find(item=>item.dataset.url===entry.target.id)
itemActual.classList.add('active')
for(const item of menuItems){if(item!=itemActual){item.classList.remove('active')}}}})}
const observer=new IntersectionObserver(funcionObserver,{root:null,rootMargin:'0px',threshold:0.8})
secciones.forEach(seccion=>observer.observe(seccion))})
function register_contact(){const f_name=document.getElementById("first_name").value;const l_name=document.getElementById("last_name").value;const cel=document.getElementById("celphone").value;const email=document.getElementById("email").value;const message=document.getElementById("message").value;fetch('/register',{method:'POST',body:JSON.stringify({f_name:f_name,l_name:l_name,cel:cel,email:email,message:message,})}).then(response=>response.json()).then(result=>{alert(result.message)});return!1}