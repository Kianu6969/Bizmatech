
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
		updateBtn[x].textContent = 'Close';
		updateBtn[x].style.background = '#F1F1F1';
		updateBtn[x].style.color = '#4D455D';
		updateBtn[x].style.fontWeight = 'bold';
		updateBtn[x].style.border = '1px solid #4D455D';
		update[x].style.height = '10vh';
		toggle = true;
	}
	else{
		updateBtn[x].textContent = 'Update'
		updateBtn[x].style.background = '#4D455D';
		updateBtn[x].style.color = '#F1F1F1';
		update[x].style.height = '0vh';
		toggle = false;
	}
	
});
}


