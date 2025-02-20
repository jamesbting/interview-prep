Solution
Overview

In design questions like these, we are expected to design a custom data structure (using already existing data structures) that will support some given functionalities. For example, you might be aware of a popular design questionMin Stack, where the data structure can return the minimum element in the stack at any time.

Here, we need to design a data structure, in which we can:

    store a(key, value)pair at a giventimestampand
    get akey'svalueat atimeequal to or just less than the giventimestamp.

The interviewer will expect us to give him the most optimal solution.
In this article, we will start from the sub-optimal approach and try to optimize it further.

Approach 1: Hashmap + Linear Search
Intuition

We can think of making some buckets for each givenkey, then in each bucket, we can store avalueat the indextimestamp.
Because in thegetfunction we have to search fortimestampfor a particularkey, so it's wise to place alltimestampscollectively in a group for eachkey.

It is a 2-dimensional array where the first index will represent thekey, the second index will represent thetimestampand thevalueis stored at that location.
But instead of using arrays, we will use hashmaps because an array can only have integer numbers as key/index, but in the hashmap, we have control of the key, and it can be whatever we want, integer, string, character, etc.

buckets

The hashmap will store the givenkeyas akeyandanother hashmapasvalue. The inner hashmap will store giventimestampaskeyand givenvalueasvalue.
So, we made a bucket for eachkeyand each bucket will store alltimestampandvaluepairs associated with it.

    Our data structurekeyTimeMapwill look like this:
    HashMap(key, HashMap(timestamp, value)).


    set(key, value, timestamp)function:
    To store avaluefor a givenkeyandtimestamp, we need to store it at the(key, timestamp)location inkeyTimeMap.

    keyTimeMap[key][timestamp] = value;


    get(key, timestamp)function:
    We have to return avaluefrom thekeybucket, which hastimeequal to or just less than the giventimestamp.
    So, we can iterate on all the times starting fromtimestamptill1, and check if avalueis stored for the current time or not, if stored we can return it, otherwise check for the previous time.
    If at the end no value was found we have to return an empty string.

    for (currTime = timestamp till 1) {
        if (currTime exists in 'keyTimeMap[key]' bucket) {
            return keyTimeMap[key][currTime];
        }
    }
    return "";


Algorithm

    Create a hashmapkeyTimeMapwhich stores string as key and another hashmap as value, as discussed above.

    In theset()function, storevalueattimestamplocation inkeybucket ofkeyTimeMap, i.e.keyTimeMap[key][timestamp] = value.

    In theget()function, we iterate on all times in decreasing order fromtimestamptill1.
        For any time while iterating if there exists a value inkey'sbucket, we return thatvalue.
        Otherwise, in the end, we return an empty string.

Implementation
Complexity Analysis

IfMis the number of set function calls,Nis the number of get function calls, andLis average length of key and value strings.

    Time complexity:

        In theset()function, in each call, we store avalueat(key, timestamp)location, which takesO(L)time to hash the string.
        Thus, forMcalls overall it will take,O(M⋅L)time.

        In theget()function, in each call, we iterate linearly fromtimestampto1which takesO(timestamp)time and again to hash the string it takesO(L)time.
        Thus, forNcalls overall it will take,O(N⋅timestamp⋅L)time.

        Note:This approach can be TLE, since the time complexity is not optimal given the current data range in the problem description.

    Space complexity:

        In theset()function, in each call we store onevaluestring of lengthL, which takesO(L)space.
        Thus, forMcalls we may storeMunique values, so overall it may takeO(M⋅L)space.

        In theget()function, we are not using any additional space.
        Thus, for allNcalls it is a constant space operation.


Approach 2: Sorted Map + Binary Search
Intuition

In the previous approach, thesetfunction is efficient, but in thegetfunction we iterate linearly over the time range. If thetimestampsin the inner map were sorted, then we can use binary search to find the target time more efficiently.

Thus, we can use a sorted map instead of a hashmap.
A sorted map keeps the stored key-value pairs sorted based on the key.

    Note:If you are not much familiar with Binary Search you can read about it in ourLeetCode Explore Card. In this approach, we will be using in-build binary search functions which will save time during the interview.

    So now our data structurekeyTimeMapwill look like:
    HashMap(key, SortedMap(timestamp, value)).


    set(key, value, timestamp)function:
    To store avaluefor a givenkeyandtimestamp, we just need to store it at the(key, timestamp)location inkeyTimeMap.

    keyTimeMap[key][timestamp] = value;


    get(key, timestamp)function:
    We have to return avaluefrom thekeybucket, which hastimeequal to or just less than the giventimestamp.
    So, we will find theupper_boundof the giventimestamp,upper_boundfunction returns an iterator pointing to the first element that isgreater than the searched value. Thus, the left element of the iterator will be equal to or just smaller than the searched value.

    Ifupper_boundpoints to the beginning of the map it means notimeless than or equal to the giventimestampexists in the map thus we return a null string.
    Otherwise, the targettimeexists at one position left of the position pointed by theupper_bound.

    it = results[key].upper_bound(timestamp);
    if (it == results[key].begin()) {
        return "";
    }
    return prev(it)->second;

    Note:Java has a little different implementation, here we will use thefloorKeymethod,
    which returns a key equal to or less than searched key ornullif no such key exists that satisfies the above condition.

Algorithm

    Create a hashmapkeyTimeMapwhich stores string as key and a sorted map as value, as discussed.

    In theset()function, storevalueatkey,timestamplocation inkeyTimeMap.

    In theget()function, we find time equal to or less thantimestampusing binary-search on SortedMap.
        If no time equal to or less thantimestampexists, we return an empty string.
        Otherwise, we return the value stored at the time equal to or just less thantimestamp.

Implementation
Complexity Analysis

IfMis the number of set function calls,Nis the number of get function calls, andLis average length of key and value strings.

    Time complexity:

        In theset()function, in each call we store avalueat(key, timestamp)location, which takesO(L⋅logM)time as the internal implementation of sorted maps is some kind of balanced binary tree and in worst case we might have to comparelogMnodes (height of tree) of lengthLeach with our key.
        Thus, forMcalls overall it will take,O(L⋅M⋅logM)time.

        In theget()function, we will find correctkeyin our map, which can takeO(L⋅logM)time and then use binary search on that bucket which can have at mostMelements, which takesO(logM)time.
        peekitemin python will also takeO(logN)time to get the value, but the upper bound remains the same.
        Thus, forNcalls overall it will take,O(N⋅(L⋅logM+logM))time.

    Space complexity:

        In theset()function, in each call we store onevaluestring of lengthL, which takesO(L)space.
        Thus, forMcalls we may storeMunique values, so overall it may takeO(M⋅L)space.

        In theget()function, we are not using any additional space.
        Thus, for allNcalls it is a constant space operation.


Approach 3: Array + Binary Search
Intuition

If we read the problem statement carefully, it is mentioned that"All the timestamps of set are strictly increasing", thus even if we use an array to store the timestamps, they will be pushed in sorted order. But we also need to storevalueswith eachtimestamp, so we will store(timestamp, value)pairs in thekey'sbucket which will be an array.

    So now our data structurekeyTimeMapwill look like this:
    HashMap(key, Array(Pair(timestamp, value))).


    set(key, value, timestamp)function:
    To store avaluefor a givenkeyandtimestamp, we just need to push the(timestamp, value)pair in the bucket ofkey.

    keyTimeMap[key].push_back(make_pair(timestamp, value));


    get(key, timestamp)function:
    We need to returnvaluein thekeybucket, which hastimejust less than or equal to the giventimestamp.
    Similarly here also, we will use binary search to find the time equal to or less than the giventimestamp.


    Note:In this approach, we will write our own implementation of the binary search. We will not focus on how binary search works, but if you are new to it you can visit thisLeetCode Explore Card.


Algorithm

    Create a hashmapkeyTimeMapwhich stores string as key and an array of pairs as value, as discussed.

    In theset()function, push(timestamp, value)pair in bucketkeyinkeyTimeMap.

    In theget()function, we find time equal to or less thantimestampusing binary-search on the array.
        If no time equal to or less thantimestampexists, we return an empty string.
        Otherwise, we return the value stored at the time equal to or just less thantimestamp.

Implementation
Complexity Analysis

IfMis the number of set function calls,Nis the number of get function calls, andLis average length of key and value strings.

    Time complexity:

        In theset()function, in each call, we push a(timestamp, value)pair in thekeybucket, which takesO(L)time to hash the string.
        Thus, forMcalls overall it will take,O(M⋅L)time.

        In theget()function, we use binary search on thekey'sbucket which can have at mostMelements and to hash the string it takesO(L)time, thus overall it will takeO(L⋅logM)time for binary search.
        And, forNcalls overall it will take,O(N⋅L⋅logM)time.

    Space complexity:

        In theset()function, in each call we store onevaluestring of lengthL, which takesO(L)space.
        Thus, forMcalls we may storeMunique values, so overall it may takeO(M⋅L)space.

        In theget()function, we are not using any additional space.
        Thus, for allNcalls it is a constant space operation.
