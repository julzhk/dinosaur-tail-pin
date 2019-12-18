Pin the Tail on the Dinosaur!
=

This simple Raspberry Pi project is a version of the popular and familiar game:
'Pin the tail on the donkey'. 

This version uses the magnetometer in the SenseHat to detect correct pinning - and emit a roar! 

You'll need:
=

* A Raspberry Pi with SenseHat
* An external speaker (connected via the phones jack)
* A Magnet (on the pin)
* A dinosaur picture (to pin a tail on) 

Notes for a beginner coder
=

In spite of this being a really simple project, I'm happy with some of the techniques used:

Object Oriented:
-

* SoundPlayer:
The 'SoundPlayer' class has 2 methods: 'play' and 'stop'. It's advantage is all the messy details of selecting and playing
a sound file are separate from the rest of the program. It means we can re-use, extend and reason about this bit of functionality
separately.
* Random.choices: 
This function is given a list, and 'choices' selects one at random.  
* Flexible:
If you want to just play a particular sound file, you can pass in the filename in the play method
If you have an entirely different list of sound files to choose from, you can override that too.
* These are just some of the ways extensibility & encapsulation is helped by Object-oriented programming. 

RollingAvg:
-
This class is based on the built-in 'Deque' data structure, from the 'collections' library - which is worth a extended study. There's lots of 
useful things in it: Data structures that can make a hard problem a lot simpler - so worth a look.

This RollingAvg class calculates a rolling average, by storing a given number of previous items, and averaging them.
When a new item is added, the oldest item it discarded. This is a built-in feature of the 'deque' data structure, and as
you can see, it makes this calculation really straightforwards.

The Rest
==
The rest of the program is just an infinite loop. If the reading from the magnetometer is much greater than 
the rolling average. emit a random roar. If it's a good bit smaller, then stop the roar.

The reason a rolling average is used (and not a hard-coded, or baseline reading) is that the reading changes over time
I assume it's due to the circuits getting warmer? No real idea, but the solution is the measure a degree of change, 
rather than anything too fixed.

Hope this brief explanation is useful! 

---
JH  2019 December

 