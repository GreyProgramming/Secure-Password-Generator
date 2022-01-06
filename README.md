# Secure-Password-Generator
A generator with random words

(Obligatory nod to https://xkcd.com/936/)

So one of the things I have been thinking about lately is password security. We all know that length and complexity are important, which is why I despise any website that says 'Passwords should be between 8 and 12 characters'...

![Hey, MyLowe - Hit me up for better security](https://2.bp.blogspot.com/-vusPyiwEGXY/W5DP5_doPmI/AAAAAAAJSqo/xPsvSLGLFh0gtyAcsJRy8U9vGsmGQVXBACLcBGAs/s640/Cai_uFEVIAAa3sq%255B1%255D.jpg)

But when you get to the range of completely random characters; you are open to a different issue:

%M3^UJx2ctn+qq+7

Human falibility. Our brains don't remember things like this very well. Heck, we struggle with years a lot of the time.

So, as outlined in the XKCD comic above, a better method is to pull 4 random words and concatenate them all together.

Using security.org's password strength checker - https://www.security.org/how-secure-is-my-password/ - We find that correcthorsebatterystaple would take a brute force method "1 hundred quadrillion years" - 100,000,000,000,000,000 - With current computing power.

The issues that we see there though are that the password is all lower case, so if we were to use CamalCase - CorrectHorseBatteryStaple - This increases to 6 septillion years.

The reason for this is that we have added in an entirely new set of symbols and thus an extra layer of complexity, which has multiplied our expected brute force time by 60 million years

If we build on this, we can seperate the words and insert numbers between them - 1Correct2Horse3Battery4Staple is 7 Decillion years - that's 33 zeros.

And adding a single exclamation mark to the end brings us to 3 hundred undecillion years. - That's 300,000,000,000,000,000,000,000,000,000,000,000,000, with modern computing power. Obviously if we create quantum computing tomorrow, we will need to adjust that a bit, but otherwise - given that the entire universe is only 13.8 Billion years old, I think we're good.

That's why I wanted to create this, I couldn't find a generator online that followed these practices, making an easy to remember but near impossible to crack password.

It hangs slightly while generating the words, but to pull a password at random, I got 2Indictable7Reionisation5Noneconomists5Roopy0#, which would take a computer about 4 hundred unvigintillion years to crack

One of the things I had to be careful of is that some words in the random word list have spaces in, so I have a line that when it is joining the whole thing together, it replaces spaces with a hyphen.
