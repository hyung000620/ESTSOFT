var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString();
var n = parseInt(input);
// var n = 5
for (var i = 0; i < n; i++) {
    let res = "";
    for (var j = 0; j < n; j++) {
        if (n-1-i <= j) {
            res += '*';
        } else {
            res += ' ';
        }
    }
    console.log(res)
}