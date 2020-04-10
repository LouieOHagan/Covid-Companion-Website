document.getElementById("clickAndCollect").addEventListener("click", toggleClickAndCollect)

function toggleClickAndCollect() {
  let checkBox = document.getElementById("clickAndCollect");
  let orderNumber = document.getElementById("orderNumberSection");

  if (checkBox.checked == true){
    orderNumber.style.display = "block";
  } else {
    orderNumber.style.display = "none";
  }
}