try{
    const idx = 4;
    const arr = [1,2,3];
    console.log(arr[idx]);
    throw new Error("에러가 발생했습니다.");
}catch(err){
    console.log(err.message);
}