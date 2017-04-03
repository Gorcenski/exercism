module LeapYear

let isLeapYear x = 
    (x % 4) = 0 && not ((x % 100) = 0) || (x % 400) = 0