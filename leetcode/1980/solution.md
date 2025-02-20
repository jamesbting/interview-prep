Solution
Approach 1: Recursively Generate All Strings

Intuition

In the constraints, we see thatn≤16. Given that there are only216=65536possible binary strings, it is feasible to generate all of them in an attempt to find one that does not appear innums.

We will use a recursive functiongenerate(curr)to generate the binary strings. At each function call,curris the current string we have. First, we check ifcurr.length = n. If it is, we need to stop adding characters and assess if we have an answer. Ifcurris innums, we return an empty string. If it isn't, we returncurr.

Ifcurr.length != n, we will add a character. Since we are generating all strings, we will call bothgenerate(curr + "0")andgenerate(curr + "1"). Note that in our base case, we return an empty string if we did not generate a valid answer. Thus, if either call returns anon-emptystring, the value it returns is a valid answer.

As each call togeneratecreates two more calls, the algorithm will have a time complexity of at leastO(2n). However, we can implement a crucial optimization. We will first callgenerate(curr + "0")and store the value inaddZero. IfaddZerois not an empty string, we can immediately return it as the answer without needing to make the additional call togenerate(curr + "1"). IfaddZerois an empty string, it means all possible paths from adding a"0"lead to invalid answers, and thusgenerate(curr + "1")must generate a valid answer, since it's guaranteed that a valid answer exists.

Why is this optimization such a big deal? Notice that the length ofnumsisn. Thus, if we checkn + 1different strings of lengthn, we will surely find a valid answer. By returningaddZeroearly, we terminate the recursion as soon as we find a valid answer, thus we won't check more thann + 1strings of lengthn. Without any early returns, we would check2nstrings of lengthn.

Additionally, we will convertnumsto a hash set prior to starting the recursion, so we can have checks inO(1)time complexity in the base case.

Algorithm

    Create a functiongenerate(curr):
        Ifcurr.length = n:
            Ifcurris not innumsSet, returncurr.
            Return an empty string.
        SetaddZero = generate(curr + "0").
        IfaddZerois not an empty string, return it.
        Returngenerate(curr + "1").
    Setn = nums.length.
    Convertnumsto a hash setnumsSet.
    Returngenerate("").

Implementation

Complexity Analysis

Givennas the length ofnums(and the length of each binary string),

    Time complexity:O(n2)

    We requireO(n2)to convertnumsto a hash set.

    Due to the optimization, we checkO(n)binary strings in our recursion. At each call, we perform some string concatenation operations, which costs up toO(n)(unless you have mutable strings like in C++).

    Space complexity:O(n)

    The recursion call stack when generating strings grows to a size ofO(n). The hash set usesO(n)space.


Approach 2: Iterate Over Integer Equivalents

Intuition

Without the optimization, the previous approach would be reasonable when the length ofnumsis not bounded. However,numshas a length ofn. There are many more possible binary strings than there are strings innums.

In fact, since there are onlynstrings innums, we never need to check more thann + 1different binary strings, since at least one of them would not appear innumsand thus be a valid answer. How do we decide whichn + 1binary strings we should check?

Let's start by converting each string innumsto its equivalent base-10 integer. We will store these integers in a hash setintegers. Now, we can simply use a for loop to iterate over the range[0, n](the size of this range isn + 1, so it is guaranteed to contain at least one valid answer). For each number, we check if it is inintegers. If it isn't, it represents a valid answer. We just need to convert it back to a binary string of lengthnand return it.

Note that in some cases, if a valid answer, when converted to a binary string, has a length shorter thann, we need to add "0"s to the beginning to make its length equal ton.

Algorithm

    Createintegers, a hash set containing all the elements ofnumsin their base-10 integer form.
    Initializen = nums.length.
    Iteratenumfrom0ton:
        Ifnumis not inintegers, convert it to a binary string of lengthnand return it.
    The code should never reach this point. Return anything.

Implementation

Complexity Analysis

Givennas the length ofnums(and the length of each binary string),

    Time complexity:O(n2)

    We iterate overnstrings and convert them to integers, costingO(n)for each integer.

    We then iteratenumin the range[0, n]. When we find the answer, we spendO(n)to convert it to a string.

    Space complexity:O(n)

    The hash setintegershas a size ofn.


Approach 3: Random

Intuition

As mentioned before, there are many more possible binary strings than there are "banned" binary strings innums.

We can randomly generate binary strings until we find one that is not innums. Forn = 16, there are216=65536strings we could generate, and only16that would not be valid. Thus, the probability of finding a valid answer is6553665536−16​, over 99.9%.

In general, the probability of generating a valid answer randomly is2n2n−n​. Because2ngrows much faster thann, the probability is very favorable for us.

For ease of implementation, we will start by converting each binary string innumto its base-10 equivalent, then storing these integers in a hash setintegers, just like in approach 2.

Then, we will generate random numbers in the range[0,2n]until we find one not inintegers. Once we do, we convert it to a binary string of lengthnand return it.

Algorithm

    Createintegers, a hash set containing all the elements ofnumsin their base-10 integer form.
    Setansto any value inintegersandn = nums.length.
    Whileansis inintegers:
        Randomly generate an integer between0(inclusive) and2n.
        Setansto the randomly generated integer.
    Convertansto a binary string and return it.

Implementation

Complexity Analysis

Givennas the length ofnums(and the length of each binary string),

    Time complexity:O(∞)

    Technically, the worst-case scenario would see the algorithm running infinitely, always selecting elements inintegers. However, the probability that the algorithm runs for more than a few steps, let alone infinitely, is so low that we can assume it to be effectively 0. This probability also lowers exponentially asnincreases.

    Forn = 16, there is an over 99.9% chance that we find an answer on the first iteration. Forn = 20, we have an over 99.998% chance. Practically, this algorithm runs extremely quickly.

    Space complexity:O(n)

    The hash setintegershas a size ofn.

    We don't count the answer as part of the space complexity.


Approach 4: Cantor's Diagonal Argument

Intuition

Cantor's diagonal argumentis a proof in set theory.

While we do not need to fully understand the proof and its consequences, this approach uses very similar ideas.

We start by initializing the answeransto an empty string. To buildans, we need to assign either"0"or"1"to each indexifor indices0ton - 1. How do we assign them soansis guaranteed to be different from every string innums? We know that two strings are different, as long as they differ by at least one character. We can intentionally construct ouransbased on this fact.

For each indexi, we will check theithcharacter of theithstring innums. That is, we checkcurr = nums[i][i]. We then assignans[i]to the opposite ofcurr. That is, ifcurr = "0", we assignans[i] = "1". Ifcurr = "1", we assignans[i] = "0".

What is the point of this strategy?answill differ from every string inat leastone position. More specifically:

    ansdiffers fromnums[0]innums[0][0].
    ansdiffers fromnums[1]innums[1][1].
    ansdiffers fromnums[2]innums[2][2].
    ...
    ansdiffers fromnums[n - 1]innums[n - 1][n - 1].

Thus, it is guaranteed thatansdoes not appear innumsand is a valid answer.

    This strategy is applicable because both the length ofansand the length of each string innumsare larger than or equal ton, the number of strings innums. Therefore, we can find one unique position for each string innums.

Algorithm

    Initialize the answerans. Note that you should build the answer in an efficient manner according to the programming language you're using.
    Iterateiover the indices ofnums:
        Setcurr = nums[i][i].
        Ifcurr = "0", add"1"toans. Otherwise, add"0"toans.
    Returnans.

Implementation

Complexity Analysis

Givennas the length ofnums(and the length of each binary string),

    Time complexity:O(n)

    We iterate over each string innums. Assuming the string building is efficient, each iteration costsO(1), and joining the answer string at the end costsO(n).

    Space complexity:O(1)

    We don't count the answer as part of the space complexity.
