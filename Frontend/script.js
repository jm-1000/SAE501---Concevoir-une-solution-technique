const url = "http://127.0.0.1:8080"

liElem = function(util) {
    return `
        <li>
            <div>
                <label id=${util['id']}> ${util['nom']} </label> 
                <input id="btn" type="button" value="Suprimer">
                <input id="btn" type="button" value="Imprimer">
            </div>
            <div>
                <label>Mot de passe : ${util['passwd']}</label>
                <label>Mail : ${util['mail']}</label>
                <label>Status : ${util['status']}</label>
            </div>
        </li> 
    `
}

fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json()
    })
    .then(data => {
        ulElem = document.querySelector('ul')
        data['utilisateurs'].forEach(util => {
            
                ulElem.innerHTML += liElem(util)
        });
        document.querySelector('section p').style.display = "none"

        document.querySelectorAll('section div:first-child label').forEach(elem => {
            elem.addEventListener('click', (e) => {
                e.target.parentElement.nextElementSibling.style.display = 'block'
            })
        })

        document.querySelectorAll('section li').forEach(elem => {
            elem.addEventListener('mouseleave', (e) => {
                e.target.lastElementChild.style.display = 'none'
            })
        })

        document.querySelectorAll('section label + input').forEach(elem => {
            elem.addEventListener('click', (e) => {
                postRequest({
                    id: e.target.parentElement.querySelector('label').id
                }) 
            })
        })

        document.querySelectorAll('section input + input').forEach(elem => {
            elem.addEventListener('click', (e) => {
            util = e.target.parentElement.parentElement.querySelectorAll('label:first-child')
            document.body.innerHTML = `
                <div style="display:block;">
                    <p>Utilisateur : ${util[0].innerHTML}</p>
                    <p>${util[1].innerHTML}</p>
                </div>  `
            window.print()    
            location.reload()
            })
        })
    })


function postRequest(data) {
    fetch(url, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 
            'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
        .then(response => {
            location.reload()
        })
}


document.querySelector('aside form').addEventListener('submit', (e) => {
    e.preventDefault()
    postRequest({
        nom: e.target[0].value,
        mail: e.target[1].value
    }) 
})


