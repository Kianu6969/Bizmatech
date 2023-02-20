
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

const update = document.getElementsByClassName('modal-container-update');
const updateBtn = document.getElementsByClassName('update');
let toggle = false;


for(let x = 0; x < updateBtn.length; x++){
	updateBtn[x].addEventListener('click', function(){

	if (toggle == false) {
		updateBtn[x].textContent = 'close';
		updateBtn[x].style.background = 'green';
		update[x].style.display = 'flex';
		toggle = true;
	}
	else{
		updateBtn[x].textContent = 'update'
		updateBtn[x].style.background = '#4D455D';
		update[x].style.display = 'none';
		toggle = false;
	}
	
});
}


