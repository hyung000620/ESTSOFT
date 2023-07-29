function isPrime(number){
    if(number <= 1){
        return false;
    }
    for (let i=2; i<number; i++){
        if(number%i===0){
            return false;
        }
    }
    return true;
}

function findPrimes(start, end){
    let primes = [];
    for(let num = start; num <=end; num++){
        if(isPrime(num)){
            primes.push(num)
        }
    }
    return primes
}


const startNum = 1;
const endNum = 100;
const primesList = findPrimes(startNum, endNum);

console.log("1에서 100까지의 소수:");
for(const prime of primesList){
    console.log(prime)
}