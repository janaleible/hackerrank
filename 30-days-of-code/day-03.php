<?php

$stdin = fopen("php://stdin", "r");
fscanf($stdin, "%d\n", $n);
fclose($stdin);

function weird(int $n): bool {
    return odd($n) || (
        $n >= 6 and $n <= 20
    );
}

function odd(int $n): bool {
    return $n % 2 == 1;
}

if(weird($n)) {
    echo 'Weird';
} else {
    echo 'Not Weird';
}
