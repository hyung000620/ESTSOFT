// 1. 함수를 선언
// console.log(add(3,5));
console.log(add(3,5));

function add(a, b){
    return a + b;
}

// 2. 함수 표현식
let subtract = function(a, b){
    return a - b;
}

// 3. 화살표 함수
let subtract2 = (a, b) => {
    return a - b;
};
console.log(subtract2(3, 5));

var multiply = (a, b) => {
    return a * b
};