const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(url)
.then(response => response.json())
.then(data => {
  document.getElementById('character').textContent = data.name;
})
.catch(error => console.error('Fail to fetch data name'));
