
const serverName = '127.0.0.1';


let test = "True"


document.getElementById("clear").onclick = function(){
    alert('works')
    fetch(`http://${serverName}:5000/clearcart`, {
        method: 'POST',
        body: JSON.stringify('True'), 
        headers: new Headers({
          'Content-Type': 'application/json'
        
        })
      })
      
      
};