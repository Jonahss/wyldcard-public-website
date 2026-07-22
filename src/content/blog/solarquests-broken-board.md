---
title: "Solarquest’s Broken Board"
description: "Solarquest is a nostalgic board game from my childhood, but not a great game. Not only is it simple Space Monopoly, its board design has a spot you can never land on!"
pubDate: 2022-09-15
---

#### You’ll never land on Jupiter Research Lab

Solarquest is a terrible board game near and dear to my heart. It’s so cool! It’s about space and as a middle-schooler I knew the names of a surprising number of moons in our solar system. The players are little rocket ships, and there are these incredibly satisfying-feeling shiny metal pieces which represent “fuel stations”. (My father says that these metal pieces are [rivet blanks](https://www.mcmaster.com/rivets/rivet-type~solid/head-type~flush-mount-1/material~steel/), game designers are always looking for cheap components).

But Solarquest is just Space Monopoly with Extra Flair. You go around the board in your space-car, buying space-properties, and paying for space-rent with space-money. There’s a few additional rules like your rocketship uses gas and if you run out of gas YOU LOSE THE GAME. Oh, and you can shoot your friends with LASERS and if you happen to roll double sixes, your target LOSES THE GAME.  
  
One time, my high school board game group sat down for an afternoon of experiencing this silly game, and my friend lost on the first turn due to this rule. He had to sit in my mom’s dining room watching the rest of us play for the next few hours.

Did I mention the game never ends? One day, my cousin and I sat down to “finally finish this game, no matter what”. We played for hours, reaching a point where we had a pile of money between us that we shoved back and forth each time someone owed rent to the other. No side ever came out ahead.

Fifteen years later, I brought the game for some laughs at our weekly board game night. Picking up a special Red Shift card when “thirteen” is rolled on the dice (a one and a three) brought the expected laughs. While playing, I started to idly wonder why some of the spots on the board seemed to be landed upon much more than others. This must just be random coincidence, but the names of the spots resonated in my childhood memories. *Of course* I landed on Mimas *again*.

I was on the lookout for a simple computer script I could write, as a way of learning the programming language Rust, which I needed for development on [Wyldcard](/wyldcard.io/index).

I decided to simulate the Solarquest board, and count how often pieces landed on each property. My suspicions were confirmed! Some spots are landed-upon much more often, and one spot *is impossible to land on*.

Let’s take a look at the board:

![](/images/blog/solarquests-broken-board/01.webp)

It’s a big loop, with smaller loops around some major planets in the solar system. What’s key are the “gravity wells” at each fork in the path. You can never land on a gravity well, they represent the gravitational pull of the planet you’re currently orbiting. If you don’t roll a number high enough to get past them, you have to go around the planet again. This mechanic is what causes the board to have an uneven probability of landing on each spot. Rather than do the math, I simulated 100,000 players rolling through 40 rounds of the game ([code on github](https://github.com/Jonahss/solarquest-monte-carlo)).

![](/images/blog/solarquests-broken-board/02.webp)

Not evenly distributed at all! You’re four times more likely to land on Miranda than on Phobos.

And look, Jupiter Research Lab isn’t landed on a single time!

(Okay, technically there is a SINGLE WAY to land on Jupiter Research Lab, which would be to roll a thirteen, and happen to draw the “OXYGEN LEAK” Red Shift card, which sends you “to next research lab”. So if you happen to be in orbit around Jupiter, roll a 13, and then draw this card from a pile of 35, congratulations you now own Jupiter Research Lab and you don’t need to make the beds since nobody will ever come and visit)

For those of you looking to improve your Solarquest strategy (in this completely random game), one of your only choices is whether to buy a property. The answer is always “YES” because properties can be sold back to the bank at face value. One of the only meaningful choices in the game is **which property to sell when you need cash**. In that case, refer to this handy guide which lists the properties ordered by how many standard deviations they are from the average likelihood of being landed upon:

![](/images/blog/solarquests-broken-board/03.webp)

For the rest of you, this game is worth an hour of laughs, and if you’re a kid: it’s cooler than Monopoly.
