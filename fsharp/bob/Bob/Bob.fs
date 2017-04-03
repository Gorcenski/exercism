module Bob

let hey (msg : string) =
    if not(String.exists(fun c -> not(System.Char.IsWhiteSpace(c))) msg) then "Fine. Be that way!"
    elif (String.exists(fun c -> System.Char.IsLetter(c)) msg)
        && (msg.ToUpper()) = msg then "Whoa, chill out!"
    elif msg.EndsWith("?") then "Sure."
    else "Whatever."
