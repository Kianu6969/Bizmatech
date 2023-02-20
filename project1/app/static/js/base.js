
const modal = document.querySelector('.modal-popup-add-product');
const addBtn = document.querySelector('.add-product');
const closeBtn = document.querySelector('.close_btn');

addBtn.addEventListener('click', function(){
	modal.style.display = 'flex';
});


closeBtn.addEventListener('click', function(){
	modal.style.display = 'none';
});


// Update

const update = document.querySelector('.modal-container-update');
const updateBtn = document.querySelector('.update');
let toggle = false;

updateBtn.addEventListener('click', function(){

	if (toggle == false) {
		updateBtn.textContent = 'close';
		updateBtn.style.background = 'green';
		update.style.display = 'flex';
		toggle = true;
	}
	else{
		updateBtn.textContent = 'update'
		updateBtn.style.background = '#4D455D';
		update.style.display = 'none';
		toggle = false;
	}
	
});

