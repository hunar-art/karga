// Adding event listener on the page-
document.addEventListener('keydown',handleInputFocusTransfer);

function handleInputFocusTransfer(e){

  const focusableInputElements= document.querySelectorAll(`input`);

  //Creating an array from the node list
  const focusable= [...focusableInputElements]; 

  //get the index of current item
  const index = focusable.indexOf(document.activeElement); 

  // Create a variable to store the idex of next item to be focussed
  let nextIndex = 0;

  if (e.keyCode === 38) {
    // up arrow
    e.preventDefault();
    nextIndex= index > 0 ? index-1 : 0;
    focusableInputElements[nextIndex].focus();
  }
  else if (e.keyCode === 40) {
    // down arrow
    e.preventDefault();
    nextIndex= index+1 < focusable.length ? index+1 : index;
    focusableInputElements[nextIndex].focus();
  }
}
