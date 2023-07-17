// function Person(name, age){
//     this.name = name;
//     this.age = age;

//     this.sayHello = function(){
//         console.log(`안녕하세요! 제 이름은 ${name}, 그리고 나이는 ${age}입니다.`)
//     };
// }

// let Human = new Person("김도언", 20);

// Human.sayHello();


// class Person{
//     constructor(name, age){
//         this.name = name;
//         this.age = age;
//     }
//     sayHello() {
//         console.log(`안녕하세요! 제 이름은 ${this.name}, 그리고 나이는 ${this.age}입니다.`)
//     }
// }

// let Human = new Person("김도언", 20);
// Human.sayHello();

let rectangle = class {
    constructor(height, width){
        this.height = height
        this.width = width
    }
    calcArea(){
        return this.height * this.width;
    }
};

const square = new rectangle(10, 20);
console.log(square.calcArea());