function wakeUp() {
    console.log("아침에 일어나서 강의듣기!");
}

function eatLunch() {
    return new Promise(resolve => {
        setTimeout(function() {
            console.log("점심시간에 점심먹기!");
            resolve();
        }, 3000);
    });
}

function endClass() {
    console.log("강의가 끝났다! 놀아야지!");
}

async function startDay() {
    wakeUp();
    await eatLunch();
    endClass();
}

startDay();