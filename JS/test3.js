function makeCoffee() {
    return new Promise(resolve =>{
        setTimeout(()=> {
            console.log("샷을 넣습니다");
            resolve();
        }, 3000);
    });
}

function addMilk() {
    return new Promise(resolve =>{
        setTimeout(()=> {
            console.log("우유를 넣습니다");
            resolve();
        }, 2000);
    });
}

//promise/then
makeCoffee().then(()=>{
    addMilk().then(()=>{
        console.log("라떼가 완성되었습니다.")
    })
});


//async/await
async function finishLatte() {
    await makeCoffee();
    await addMilk();
    console.log("라떼가 완성되었습니다");
}

finishLatte();