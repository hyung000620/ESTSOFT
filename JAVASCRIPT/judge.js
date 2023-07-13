// const num =  require("fs").readFileSync("/dev/stdin").toString()/1;

let N = 216;
let answer = 0;
for(let i=0; i<N; i++){
    let sum = 0;
    let num = i;
    while(num!=0){
        sum += num%10;
        num /=10; 
    }
    if(sum+i ==N){
        answer=i;
        break;
    }
}
