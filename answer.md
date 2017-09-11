[Insert the correct output for SecretTest3 here]
## Result for 10000 (first 500 characters)

13211321322113311213212312311211131122211213211331121321123123211231131122211211131221131112311332211213211321223112111311222112132113213221123123211231132132211231131122211311123113322112111312211312111322111213122112311311123112112322211213211321322113312211223113112221121113122113111231133221121321132132211331121321232221123123211231132132211231131122211331121321232221123113112221131112311332111213122112311311123112112322211211131221131211132221232112111312211322111312211213211312111322211231

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Write a brief explanation about how your code works here!]

## The Trick of the Function
The question is called "Look and Say", and the trick is exactly what the name of the question said.

Starting from "1", when you see "1", you read "I see one 1", so the next string is the description of the last string, aka "11" (one 1). Then you can read the string "11" as "two 1", aka "21".

## Implementation
The code has two parts: `main` function as a global entry, and `look_and_say` function to deal with each string.

According to the description, the next result will have to be calculated using the last result, so `main` function will constantly call `look_and_say` function until the needed result is calculated.

`look_and_say` function takes a string (aka "the last string"), go over it for only one time, which make the time complexity be O(n).

Image `look_and_say` function split "the last string" into groups of repeating characters, like this:
```
'13112221' => ['1', '3', '11', '222', '1']
```
Then all we need to do is to build the result string by adding the length of every element of the array mentioned above, and also add the repeating character of the element. The `look_and_say` function works exactly this way, except it does not really create the array. Instead, it scans the string and saves positions as needed.

In `look_and_say` function, `current_element` saves the last repeated element, `last_index` indicates where the repeating of `current_element` started, and `current_index` indicates the character that is being scanned. `result` is the result string which will be build along with the scanning.

## About Performance
When the input number is bigger than 50, the performance of calculating the whole answer is unacceptable on my computer, and the last input that will be checked before 10000 is 20, whose result has a length of 302. So the `main` function only save the first 500 characters of the results.