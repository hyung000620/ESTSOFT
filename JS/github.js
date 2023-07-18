const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class HttpError extends Error{
    constructor(res){
        super(`${res.status} for ${res.url}`);
        this.name = 'HttpError';
        this.res = res;
    }
}

function loadJson(url){
    return fetch(url).then(res => {
        if(res.status == 200){
            return res.json();
        }else{
            throw new HttpError(res);
        }
    });
}

function demoGithubUser(){
    rl.question('Github Username을 입력하세요.',(name)=>{
        return loadJson(`https://api.github.com/users/${name}`)
        .then(user =>{
            for(key in user){
                console.log(`${key}: ${user[key]}`);
            }
        })
        .catch(err =>{
            if(err instanceof HttpError && err.res.status == 404){
                console.log("사용자 없어!");
                return demoGithubUser();
            }else{
                throw err;
            }
        });
    });
}

demoGithubUser();