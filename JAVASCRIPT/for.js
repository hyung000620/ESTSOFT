// let sum = 0;

// for (let i = 1; i <= 100; i++) {
//   sum += i;
// }

// console.log(sum);

// let numbers = [1,2,3,4,5];
// numbers.push(5)
// numbers.pop()
// numbers.splice(1,2)
// console.log(numbers.slice(0,3))

// let tmp = 0;
// for(let i=1; i<=1000; i++){
//     if(i%2==0){
//         tmp+=i;
//     }
// }
// console.log(tmp);



// const fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n');
const NM = input
.shift()
.split(' ')
.map(num => parseInt(num));
const N = NM.shift();
const M = NM.shift();
const cardArr = input
.shift()
.split(' ')
.map(num => parseInt(num));
let max = 0;

// ------input 부분------//


for(let i=0; i<N-2; i++){
    for(let j=i+1; j<N-1; j++){
        for(let k=j+1; k<N; k++){
            let sum = cardArr[i] + cardArr[j] + cardArr[k];
            if (sum > max && sum <= M){
                max = sum;
            }
        }
    }
}
console.log(max);