const elementById = document.getElementById('section1');

console.log(elementById);

const elementByClass = document.getElementsByClassName('mySection');

console.log(elementByClass);

const elementsByTag = document.getElementsByTagName('section');

console.log(elementsByTag);

// const elementBySelector = document.querySelector('#section2 > h2')
// console.log(elementBySelector);

// for(let i=1; i<4;i++){
//     let tmp = document.querySelector(`#section${i}>h2`);
//     tmp.style.color = 'red';
//     tmp.style.fontSize = '20px';
// }

// const button = document.getElementById('btn');
// button.addEventListener("click", handleClick);
// const buttonContainer = document.getElementById('btnContainer');

// let newLabel = document.createElement('p');
// newLabel.textContent = "0번 클릭됬습니다!";
// buttonContainer.appendChild(newLabel);
// let clickCount = 0;

// function handleClick(event) {
//     clickCount += 1;

//     newLabel.textContent = clickCount + "번 클릭됬습니다!";

    
    // const bodyTag = document.getElementsByTagName('body')[0];
    // let bodyColor = bodyTag.style.background;
    // if (bodyColor === 'skyblue'){
    //     bodyTag.style.background = '#f0f0f0';
    // } else{
    //     bodyTag.style.background = 'skyblue';
    // }
// }
let modal = document.getElementById("MyModal");

let btn = document.getElementById("myBtn");

let span = document.getElementsByClassName("close")[0];

btn.onclick = function(){
    modal.style.display = "block";
}

span.onclick = function(){
    modal.style.display = "none";
}

window.onclick = function(event){
    if (event.target == modal){
        modal.style.display = "none";
    }
}