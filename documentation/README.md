Welcome to the card game battle royale project!

Table of contents:
    - Gameplay
    - How it works
    - Future plans

Gameplay:

This game will be a combination between a battle royale, an auto battler, and a TCG. Players will create their deck, then dive into large online lobbies against other players to see who will be the last one standing.

Every player will have their own game board, here called a realm. Each realm will contain two battle queues - one for the realm's controller, and one for the realm's invader. Players are arranged on an imaginary line - on their left will be their prey, the person whose realm they can invade, and on their right will be their predator, the person who will be invading their own realm.


0000000000000000000000000000000000000


forget the front end for now, just have the front end be a python/linux terminal
so the user will connect and will just have the terminal to communicate with the
server. Build the server to be able to communicate with the front end so that you
can eventually swap out the front end for whatever you end up using. This is the
best idea to move forward with.

So, here's the chain of events

****************************

Client attempts to connect to server
Server confirms connection to client

Client logs in with username and password
Server confirms username and password with data on server/database
Client successfully logs in

Client selects Play Battle Royale (eventually there will be other options)

Client selects what deck they want to use (one premade deck, eventually they can build their own)

Client selects Search For Game
Server puts Client in a lobby
Client waits
Server waits until there are X number of players in the lobby
When there are X players in the lobby, Server creates a Game object with all of the players and their decks

******************************

How the game is played:

Start of game:
Players are randomly assorted into a circular list. The player to the left is their hunter, the
player to the right is their prey

Players draw a hand of X cards and are given a life total of X.

Each player's board, called a realm, will be split into two distinct sections:
The invader queue is a queue of characters played by the player's hunter
The protector queue is a queue of characters played by the player

Players will be playing as specific characters that give them specific perks

Structure of a Turn:

Each turn is broken up into two parts: Setup (better name tbd), and Combat

Setup:

Players may devote one card, getting rid of it from their hand in exchange for resources

Players may spend X devotion to gain one Energy, a resource, on their following turn.

Players may play cards from their hand. Cards are generally played to either a player's own
protector queue or their invading queue that exists in their prey's realm, but some cards
will also be played to their hunter's invading queue in their own realm or to their prey's
protector queue in their prey's realm.

Note: When a player plays a card, the card exists unresolved in that realm's "stack". The
stack is a lsit of cards that will be resolved during the combat phase. Cards are resolved
according to the following rules:

Cards played by the player whose realm it is will always be resolved first. These cards are
resolved in the order in which they are played. After those cards have been resolved, cards
played to a realm by foreign players will be resolved in the order in which they were played.

Note that cards will never be played in your hunter's realm.

Each player has X seconds to complete as many of the above actions as they have devotion for. After
the setup phase has ended, we enter the combat phase:

Cards are resolved in the order in which they are in the queue. Unless otherwise stated, cards in a player's
own realm will be resolved before cards in a foreign realm. For example:

Alice is hunting Bob. Alice has a 2/2 knight in Bob's invading queue, and Bob has a 1/1 Zergling in his protector queue.
During the setup phase, Alice plays a fireball spell in Bob's invading queue targeting Bob's Zergling. Simultaneously
(and unbeknownst to each other), Bob plays a Toughness Potion in his own protector queue targeting his own Zergling.
Because we are in Bob's realm, Bob's cards get resolved first. Bob's Toughness potion gives his Zergling 2 additional
health, meaning it will survive the 2 damage Fireball spell that Alice cast on it.

Now, consider a different scenario.

Alice is hunting Bob. Alice has a 2/2 knight in Bob's invading queue, and Bob has a 1/1 Zergling in his protector queue.
During the setup phase, Bob plays a fireball spell in his own realm targeting Alice's knight. Simultaneously, Alice
plays a Toughness Potion on her knight in Bob's invading queue. Because we're in Bob's realm, Bob's cards get resolved
first. Bob's fireball spell deals 2 damage to Alice's knight, killing the knight. Next, Alice's cards get resolved - she
has a Toughness Potion on the stack targeting her knight, but that card doesn't exist anymore. Therefore, her card fizzles
nothing happens.

Note that some cards will have high priority, meaning they get resolved outside of the normal rules
of card resolution (like a counterspell).

After cards have been resolved, combat happens. The first card (i.e. the card that has been there the longest)
in each queue is the Frontliner.

The first card in each queue attacks the Frontliner in the opposite queue. If either Frontliner dies, the following
card becomes the new Frontliner for that queue. Then, the next card in each queue attacks the Frontliner. Rinse, repeat,
until every card has attacked.

For example:

Alice is hunting Bob. In Bob's invading queue, Alice has a 2/2 knight and a 1/1 Zergling. In Bob's protecting queue, he has
a 3/1 Rager, a 0/4 Wall, and a 1/3 Elf. The queues look like this:

Invading:
Knight (Frontliner), Zergling
Protecting:
Rager (Frontliner), Wall, Elf

In the first round of combat, the Knight and the Rager hit each other. The Knight takes 3 damage and dies, and the Rager takes 2 damage
and dies. The Zergling becomes the new Frontliner of the invading queue, and the Wall becomes hte new frontliner in the protecting
queue.

In the second round of combat, the Wall and the Zergling hit each other. The Wall takes 1 damage and lives, and the Zergling takes
0 damage and lives. Because neither frontliner died, there's no change.

In the third round of combat, the Elf hits the Zergling. Because there's no third character in the invading queue, nobody hits the Wall.
The Zergling takes 1 damage and dies.

Now that there are no more rounds of combat to be resolved (which happens either when the invading queue has no characters or when every
character has attacked once), combat is over.

When combat finishes, the next turn starts and we return to the setup phase.

So how does one win the game? Be the last person who hasn't lost. How do you lose? Let's look at another example of combat.

Alice is hunting Bob. Alice is invading with two zerglings, a rager, and a knight. Bob is protecting with a wall. These are
the queues:

Invading:
Zergling (Frontline), Zergling, Rager, Knight
Protecting:
Wall (Frontline)

In the first round, Alice's first Zergling hits the wall for 1 and the wall hits the Zergling for 0.
In the second round, Alice's second Zergling hits the wall for 1. Bob has no more protectors, so he's done dealing damge.
In the third round, Alice's Rager hits the Wall for 3, killing it. Bob now has no characters in his protector queue.
In the fourth round, Alice's Knight is undefended, which means it hits Bob for 2 damage.

Players start with X life. When they go to 0 life, they lose the game.

When a player loses the game, they are removed from the circle of players. However, any characters that they
had in their prey's invading queue stay in the queue.

Here's an example:

Alice is hunting Bob, and Bob is hunting Charlie. After the setup phase, Bob's realm looks like this:

Invading: Zergling, Zergling, Rager, Knight
Protecting: Wall

Unfortunately for Bob, Alice has been hitting him pretty hard, so he only has 2 health remaining.

Before we go into combat, let's look at what Charlie's realm looks like:

Invading: Knight, Knight (played by Bob)
Protecting: Wall, Zergling

During combat, Bob's protecting Wall will die to Alice's invading Zerglings and Rager, and her Knight will finish him off.
During combat, Bob's invading Knights will kill Charlie's protecting Wall (though Charlie's protecting Zergling will deal
one damage to Bob's first invading Knight)

Bob loses the game, so he's out. However, his surviving Knights are still in the invading queue in Charlie's realm, so he
still has to deal with them on his turn. Furthermore, because Bob is out, Alice is now sitting next to Charlie, and all
of her surviving characters in the invading queue in Bob's realm get whisked into Charlie's realm. So, at the beginning
of the next setup phase, Charlie's realm looks like this:

Invading: Knight, Knight (both played by the late Bob), Zergling, Zergling, Rager, Knight (all played by Charlie's new hunter, Alice)
Protecting: empty

Killing your prey puts a lot of pressure on your new prey, which allows you to either build momentum and start steamrolling, or take
your foot off the gas on invading and instead focus on protecting your own realm (depending on how your hunter is playing).

A final benefit to killing your prey is that you secure your Bounty. When you build a deck, you also choose a Hero. Your Hero
gives passive bonuses like extra draw power, extra starting life, extra damage for Knights, etc etc (some will also have
cool active abilities). In addition to that, each Hero will have a Bounty. When you kill a player, you collect your Bounty.
Bounty could be card draw, life gain, a free card, free devotion or energy, etc, etc.