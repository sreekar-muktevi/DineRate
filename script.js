
function changeColor1() {
    clear();
    el = document.getElementById("btn1");
    if (el.style.color != '#fc0') {
      el.style.color = "#fc0";
      }
    }
  
  function changeColor2() {
    clear();
    changeColor1()
    el = document.getElementById("btn2");
    if (el.style.color != '#fc0') {
      el.style.color = "#fc0";
    }
    }
  
  function changeColor3() {
    clear();
    changeColor2()
    el = document.getElementById("btn3");
    if (el.style.color != '#fc0') {
      el.style.color = "#fc0";
    }
    }
  
  function changeColor4() {
    clear();
    changeColor3()
    el = document.getElementById("btn4");
    if (el.style.color != '#fc0') {
      el.style.color = "#fc0";
    }
    }
  
  function changeColor5() {
    clear();
    changeColor4()
    el = document.getElementById("btn5");
    if (el.style.color != '#fc0') {
      el.style.color = "#fc0";
    }
    }
  
function clear(){
    allStars = document.getElementsByClassName("buttons")
    if (allStars.style.color != "#00000"){
        allStars.style.color = "#00000";
  }
}