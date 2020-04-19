/*  - Function that toggles the visibility of the clickAndCollect input field in get-help.html
    - When the function is called by an onclick attribute within the input element the function checks if the box is checked or not
    - The display propery will be set to block or none depending on if it is checked or not.
*/
function toggleClickAndCollect() {
  let checkBox = document.getElementById("clickAndCollect");
  let orderNumber = document.getElementById("orderNumberSection");

  if (checkBox.checked == true){
    orderNumber.style.display = "block";
  } else {
    orderNumber.style.display = "none";
  }
}