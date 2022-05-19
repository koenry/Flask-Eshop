const serverName = '127.0.0.1';

const queryAllEdit = document.querySelectorAll('button');
queryAllEdit.forEach(el => el.addEventListener('click', event => {
  alert('Added!')
  let a = event.target.id 
  let aa = document.getElementById(a+'a').textContent
  let aaa = aa.replace("price:", " ")
  fetch(`http://${serverName}:5000/postmethod`, {
  method: 'POST',
  body: JSON.stringify([a, aaa]), 
  headers: new Headers({
    'Content-Type': 'application/json'
  })
})
}));


  
