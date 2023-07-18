// function A(call){
//     call();
// }

// var c = console;
// function B(){
//     c.log("나는 B");
// }

// A(B);
function findUser(id, cb){
    const user = {
        id: id,
        name: "User" + id,
        email: id + "@test.com",
    };
    cb(user);
}
findUser(1, function(user){
    console.log("user: ", user);
});

