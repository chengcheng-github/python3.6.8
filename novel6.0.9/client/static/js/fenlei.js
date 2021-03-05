$(function () { 
  function divChangeColor(){
    var divs = document.getElementsByClassName("ticai");
    var len = divs.length;
    for(var i=0;i<len;i++){
        divs[i].onclick = function(){
            for(var j=0;j<len;j++){
                divs[j].style.backgroundColor = "white";
            }
            this.style.backgroundColor = "yellow";
        };
    };
  };














})