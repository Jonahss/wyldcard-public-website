---
title: "Game Design through the lens of computational complexity"
description: "Why play board games when we have video games? A look at game design through the lens of computational complexity."
pubDate: 2023-06-02
---

One can look at both video games and boardgames as simulations and arrange them along an axis of how much computation is needed to *run* the simulation. Note that we're not discussing how complex it is to find the optimal strategy for a game, but instead are looking at how many calculations are needed to run the rules of the game. For example, each turn, does one need to increment a counter? Calculate income from the bank? Roll dice and calculate strength modifiers for a battle? Calculating the optimal strategy for winning a game of Chess is a difficult math problem, but implementing the rules of Chess with a computer program is simple.

So, lets arrange common games along this axis of increasing complexity of simulation: roughly the number of calculations required to run each turn of a game:

![](/images/blog/game-design-through-the-lens-of-computational-complexity/01.webp)

I've also divided the games into two groups: Physical and Digital, tabletop games and video games.

First, we have Tic Tac Toe: extremely simple, take turns putting a symbol in one of nine places and check for three-in-a-row. So simple to calculate and simulate that it's commonly used in programming interviews. Then we move on to Checkers, more board spaces, a few edge-cases like double-jumps and kinging. Then Chess: different pieces with different movement rules, a few edge-cases like check and en passant. I put Solitaire next, slightly more complicated than playing Chess because we've added an element of randomness. Next up, Settlers of Catan and Monopoly, we've got dice rolls, moving pieces, resources. Jumping in complexity we have games like Magic the Gathering and Terraforming Mars, each turn can have multiple cascading actions which trigger more actions, etc. Now, larger Role-playing games like Dungeon and Dragons and Final Fantasy. Our first major video game (besides Solitaire). We're transitioning into complexity suited for computers. Final Fantasy could be played on paper, while Dungeons and Dragons could be played on a computer. Getting more complicated, we have the 18xx financial train games, wargames such as Warhammer, and Advance wars. Complex turn-based games with lots of stats to calculate and lots of edge-cases, still on the border between tedius gameplay and requiring a computer. Going further into simulations we've got Minecraft, Rollercoaster Tycoon, Starcraft, these require updating hundreds or thousands of game elements every second, strictly computer territory. Portal has a full physics engine, including science-fiction physics, and Kerbal Space Program is simulating orbital mechanics (fiendishly complicated). At the top, Microsoft Flight Simulator which simulates physics, aerodynamics, and many elements from the real world.

As you can see, as we step up in complexity, the games move from the real world into the digital world. At a certain point, digital computers are neccessary to keep up with the computations required to run the game. Doing these computations by hand might take a day to calculate a few minutes of gametime. At the boundary, we have tabletop games which are so complicated that many players don't have the patience to calculate turns by hand and video games which are seen as simplistic by today's standards.

#### **Why play board games when we have video games?**

Could all these games be implemented on a computer? Sure! Except people choose to continue to play these games in the physical world whenever they can. While the video game industry is now larger than movies, music, and sports combined, boardgames are more popular than ever before. If videogames were strictly superior to boardgames, you'd expect the popularity of boardgames to be shrinking. Instead, it's growing. This indicates that tabletop gaming satisfies some entertainment itch that video games can't scratch.

#### **Human Interaction**

What do boardgames have that video games lack? Chiefly, human interaction.

![](/images/blog/game-design-through-the-lens-of-computational-complexity/02.webp)

Boardgames are played in person, sitting accross a table from your oponnents and teammates. You get to see their triumphant smiles or hear their cries of despair. Laughs and jokes, tabletalk, the human emotion and interaction is there. Sure, you can play a video game in a room full of people all shouting at the screen, or have voice channels with online players, but the level of interaction is still abstracted and removed. With tabletop gaming, everyone sits around a table and looks at each other rather than focusing on a screen. Imagine a game of Uno where everyone is groaning about a draw-plus-four, or a game of spoons with people wildly scrambling for silverware. Imagine that moment when you discover a killer combo and build up a turn that escalates and escalates while your friends stare on in mounting horror. Imagine a night of Dungeons and Dragons, four hours in, a table littered with paper, books, snacks and dice. I was once in a Settlers of Catan tournament and everyone was so serious, it was completely un-fun. There was one table of people talking and laughing, commenting on the game, cajoling and cheering each other, *this* was the fun table!

#### **Physicality**

When comparing boardgames to video games, one can also point to a vague sense of "physicality". This is hard to define, but there's definitely something there. Games which come with metal coins are just so *satisfying*. They really make a clink when you hand them over to someone else or stack them in little piles. When contemplating a board, you can walk all around it, viewing it from different angles. When building a deck of Magic cards, my process is to arrange them in piles, covering tables and spilling onto the floor. This is because I think spatially, and this sort of arrangement isn't possible with the limited screen space of computer user interfaces.

#### **Bringing more human interaction and physicality to video games**

Virtual Reality is trying to bring more human interaction and physical immersion into the digital world, in order to make games more enjoyable and offer more variety. Meta's whole thesis for VR is that if they can implement better social cues, such as seeing people's facial expressions and better audio integration for speaking, people would be able to enjoy digital experiences as much as they enjoy physical ones.

#### **Bringing more computation to tabletop games**

Could all these games be implemented in the physical world? Not yet! As the computational complexity of a game increases, we are pushed into implementing it in the digital realm. Over the years, games designers have developed new technologies which help to run computations in the real world using physical devices. Dice and cards can give randomness, counters and tables can store data. Game designers have built up a collection of tricks and tools for pushing the complexity we can implement on a physicale table with cheap components. This unlocks more complex simulations for gaming, while keeping the physicality and human interaction that players enjoy.

#### **My contribution: Wyldcard**

With [Wyldcard](/wyldcard.io/index), I'm introducing a digital computer into a tabletop game in a way which preserves the human interaction and physicality. Hiding the complexity of the computer, Wyldcards have pictures that can change, and memory chips which maintain state between games. I'm attempting to make a new game component like dice and counters which can perform more computation, unlocking game mechanics previously only available to video games.

Examples of game mechanics that Wyldcard makes possible can be found on the [crowdfunding campaign page](https://www.crowdsupply.com/wyldcard/wyldcard-devkit) where I'm selling Wyldcard DevKits which can be programmed in JavaScript to implement your own games.
