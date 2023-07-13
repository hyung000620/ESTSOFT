const examples = [
    [0, ''],
    [false, 'false'],
    [null, undefined],
    [NaN, NaN],
    [0, false],
    [0, '\n'],
    ['', '0'],
    ['false', false],
    [[], false],
    [[], ''],
    [[], 0],
    [[0], false],
    [[null], false],
    [[undefined], false],
    [{}, false],
    [true, 1],
    [true, '1'],
    [true, [1]],
    [true, { value: 1 }],
    ['1', [1]],
    [undefined, null],
    [Infinity, Infinity],
    [Infinity, 'Infinity'],
    [() => {}, () => {}]
  ];

// examples.forEach(([a,b]) =>{
//     console.log(`${a} == ${b}: ${a==b}`);
//     console.log(`${a} === ${b}: ${a===b}`);
// });

let x = 2
let y = 2
if ((++x)===(++y)){
    console.log("true")
}