function squareWithCallback(number, callback) {
    if (typeof number !== 'number') {
        const error = new Error('유효하지 않은 숫자입니다.');
        callback(error, undefined);
        return;
    }

    const result = number * number;
    callback(null, result);
}

function cb(error, result) {
    if (error) {
        console.log(error);
        return;
    }

    console.log('결과:', result);
}
squareWithCallback(1232312,cb);