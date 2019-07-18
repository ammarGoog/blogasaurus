console.log("I'm working");

//#leb #CLW #hiyyah #elbow
// .secret .colorChange
//https://stackoverflow.com/questions/38498246/how-to-make-an-html-element-appear-and-disappear-again-and-again-with-js

const titles = document.querySelector(".colorChange");
titles.addEventListener('click', () => {
  titles.style.color = 'red';
  titles.style.fontSize = 'x-large';
})

var classname = document.getElementsByClassName("classname");

var myFunction = function() {
    var attribute = this.getAttribute("data-myattribute");
    alert(attribute);
};

for (var i = 0; i < classname.length; i++) {
    classname[i].addEventListener('click', myFunction, false);
}
