﻿namespace Leap
open System
open NUnit.Framework

[<TestFixture>]
type Test() = 

    [<Test>]
    member x.TestCase() =
        Assert.IsTrue(true)

