function makeCoffee(callback) {
    setTimeout(function () {
        console.log("샷을 만듭니다");
        callback();
    }, 3000);
}

function addMilk(callback) {
    setTimeout(function () {
        console.log("우유를 넣습니다");
        callback();
    }, 2000);
}

function finishLatte() {
    console.log("라떼가 완성되었습니다");
}

makeCoffee(function () {
    addMilk(finishLatte);
});