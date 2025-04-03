document.getElementById('add_item').addEventListener('click', function () {
  const newElement = document.createElement('li');
  newElement.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newElement);
});
