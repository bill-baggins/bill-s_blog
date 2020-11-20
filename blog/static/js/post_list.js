let fastfib = (n) => {
    if(type(n) != "number") return "Invalid input.";
    n = BigInt(n);
    if(n == 0 || n == 1) {
        return n;
    }
    let a, b, c, x, y;
    a = b = x = 1n;
    c = y = 0n;
    while(n) {
        if(n%2 == 0) {
            let temp = [a*a + b*b, a*b + b*c, b*b + c*c];
            a = temp[0];
            b = temp[1];
            c = temp[2];
            n /= 2;
        } else {
            let temp = [a*x + b*y, b*x + c*y];
            x = temp[0];
            y = temp[1];
            n--;
        }
    }
    return y;
}