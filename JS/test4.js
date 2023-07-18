function makeTenWithPromise(number){
    return new Promise((resolve,reject)=>{
        if(typeof number!='number'){
            reject(new Error("유효하지 않은 숫자입니다."));
        }else{
            let answer = 10-number;
            resolve(answer);
        }
    })
}

makeTenWithPromise(5)
    .then(res =>{console.log(res);})
    .catch(error =>{console.error(error);});