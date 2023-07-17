// const fruits = ['사과', '바나나', '수박'];

// for (const fruit in fruits){
//     console.log(fruit, typeof fruit, fruits[fruit])
// }

// for (const fruit of fruits){
//     console.log(fruit, typeof fruit, fruits[fruit])
// }

// fruits.forEach((fruit,index) => {
//     console.log(fruit, typeof fruit, fruits[index])
// });


// const numbers = [1,2,3,4,5];

// const square = numbers.map((numbers)=>{
//     return numbers**2;
// });

// console.log(square)

// const numbers = [1,2,3,4,5];

// const sum = numbers.reduce((hap, number)=>{
//     return hap +number
// }, 0);

// console.log(sum)


const numbers = [1,2,4,5,10];

const even = numbers.filter((number)=>{
    return number%2 ==0
});

console.log(even)

