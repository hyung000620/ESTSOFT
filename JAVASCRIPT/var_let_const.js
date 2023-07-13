// console.log(1 == "1");
// console.log(1 === "1");

// console.log(null == undefined);
// console.log(null === undefined);

// console.log(true == "1");
// console.log(true === "1");

// console.log([1] == 1);
// console.log([1] === 1);

const end = 100;
let sum = 0;
for (let i=1; i<end; i++){
   if (i % 2 === 0){
       sum += i;
   }
}
console.log(`전체 합은 ${sum}입니다.`)