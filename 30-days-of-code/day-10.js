'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function max_consecutive_ones(string) {
    return Math.max(...string.split('0').map(element => element.length));
}


function main() {
    const n_base_10 = parseInt(readLine(), 10);
    const n_base_2 = n_base_10.toString(2);
    
    console.log(max_consecutive_ones(n_base_2));
}
