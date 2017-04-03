module Gigasecond

let gigasecond (date:System.DateTime) =
    System.DateTime.op_Addition(date,
         new System.TimeSpan(pown 10L 16)).Date
