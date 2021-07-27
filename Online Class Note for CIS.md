## <center>Bill Nace Program Notes </center>

---

## "f'" strings

**example:**

	a = 42
	b = 'Mike'
	print('Hello {}, the number is {}'.format(b,a))

**EQUALS TO THE CODE BELOW**

	s = f'Hello {b}, the number is {a}'
	print(s)

---

## Self

 be used as the first parameter on any object's method 

 self.name = name as attribute

---

## Inheritence(类似class的包涵关系)

below one has super one's attributes **/** one is in one

**example_1:**

- women is a type of human
- human is a type of animal
- animal is a type of living things

**example_2:**

shown in RPG3
when the Player class involve Warriors, we can use `Player.__init__(self)` to use the class above to simply initiate the Warrior without writing all the things again

---

## 实例化

class name can't be used by `object.xxx`
we should create `obj = object()` to in 

---

## init
```
def __init__(self,attr):
	self.attr = attr
```
self is like a specification for this class, which means `self.atrr` can be only used here.

**COMPARING WITH THE CODE BELOW**

```
def __init__(self):
	self.attr = 0
```
attr above is a variable instead of a integer, which could be changed easily later

---

## pygame

- ### rect
- ### blit
- ### font
- ### sprite:

sprite is convenient to use because it could cooperate well with **groups**

as soon as we ask group to do something such as `update()`, every sprite in it can be updated 

sprite is a **"自带的集成的类和方法"**, it's easy to use some build-in functions of it instead of writing it again.

- ### collision:

collision occurs when two sprite occupy the same space

```
pygame.sprite.spritecollide(sprite, group,dokill (= True/False),collided = (pygame.sprite.collide.circle/rect/mask))
```

> If dokill == True, sprites will be removed from the group (group would be reserved). 
> If we want to remove them both, we should use group collide and set both `dokill` to `True`. 

```
groupcollide(group1, group2, dokill1, dokill2, collide = (pygame.sprite.collide.circle/rect/mask))
```

---

## randomness

There is a **loop** for the randomness algorithm. A good algorithm means a really long list that already seemed random.

**Distribution** means the chance of attaining each value.

**For example**, if we run `random.randrange(1,7)`, the chance of getting each number is different. 

The game designer could use this ditribution unfairness to control the **start attributes of game charactors** by adding or substracting the numbers for total.

**For example**, we could ran the randrange several times and get the higher number. So the possibility of getting a better charactor in the game is increasing.

The game designer can also use the distribution to **control the possibility one thing happens** in the game by doing the things below.

```
import random
3
n = randrange(1,100)
if n > 90:
	print('gold')
if 60 <= n <= 90:
	print('silver')
if n <= 60:
	print('cooper')
```
---

## MVC: Model-View-Controller

a common **architectural** style

While using a Github workflow or writing a long script, using MVC would help construct the script and debug.

It is not a strict concept, so there is no "right or wrong" while using it. But using MVC absolutely somewhat make the code better.

**defination:**

- Every class is a **model**, which manages the data and operation on the data.

- **View** provides a way to visualize the data, such as `draw` the frame, `txt`, music, or the bottom (its appearance).

- **Controllers** are the maps to input actions to model or view actions, such as the keyboard/mouse/joystick `events`, network inputs (in multi-player game), or even GPS inputs
---
## Mazes

**Mazes is consisted by cells, which is the smallest geographical element of the maze (a single loxation)**

- **Perfect Mazes** has one and only one path between any two cells -- thus plenty of branches, but no loops.

- **Unicursal maze** don't have branches, there is just a single path from begining to end.

- **Braided maze** has loops and several solutions to the end.

- **Weave Maze** passages go over and under others -- kind of 3d space

---

## Random Mazes Generation Ways

1. **Start with all unlinked cells**, then randomly choose which wall (south, north, east, west) to cancel (also called: carve a passage) Example: `Binary Tree`

2. **Start with an empty surface**, then randomly add walls. Example: `Sidewinder`

---

## More Random Mazes

1. `Aldous-Broder` is a **random walk algorithm**. It starts in a random cell and then link to a random, unvisited neighbor until every cells have been visited. **This algorithm don't have bias**, which means it's a uniform distribution. But it's **inefficient**.

2.  `Wilson's Algorithm` is a **random walk algorithm**. It start with choosing a random cell and mark it as 'visited'. Then start with another random, unvisited cell. This algorithm performs a **loop-erased random work** because it might walk in a cell that's already visited to create a loop. In order to prevent a loop like this, the algorithm will erase any loop. **This algorithm don't have bias**. But it's **inefficient**.

3. `Recursive Backtracker` is a **random walk algorithm**. Starting with a random cell, it randomly choose an **unvisited neighbor**. When it don't have an unvisited neighbor, it would **go back along the path** until it have one. To do this, it use a stack -- a last-in, first-out data structure -- to **keep track of every step** of its path, which is not memory efficient. This is a biased algorithm, tending to show lots of complicated branches, which is good for games, and have long, twisty paths with few dead ends.

---

## Maze Solution Algorithm

*Solution Algorithms can't see the entire maze like human do.*

1. `Dijkstra's Algorithm` finds the 'least-cost' path between starting cells and every other cells in the maze. The methods mentioned bwlow spesically illustrate how to do this. The path shows 1 if linked, shows infinity if not linked. `Frontier` is a collection to hold cells that have the lowest cost and put the root cell in it. Then, it find the cell in the frontier with the smallest value (we call it c here). It remove c from the frontier and find all the unmarked neighbors of c to mark them with value of (1 + c), then add those neighbors to the frontier. 

---

## Dictionary 

- `.pop(key)` is one way to remove one pair of key and value by refering to key because key is unique in the dictionary.

-  `.delete(key)` does the same thing above.

---

## Recursion (递归)

`Recursion` means to run a function inside itself to create a loop. Its advantage is the extreme concision of the codes. But it might take a while to consider how to write the codes.

- There is a Base Part of the function to decide when to stop.
- There is also a running part to see what to do.

---

## Collision Detection

1. `In order to detect the collision between rects`, we could check if **any angle of a rect is inside another** rect. But this is a really inefficient method. Also, this method only check for collisions after each update. However, the actual collision might happen between two frames. 

2. `To optimize the codes above`, we can do a **quickly test to see what's impossible to collide**, and do a throughly test to the remaining objects. *This is useful for some unmovable objects, friendly fires, or objects which are moving in a constant speed together.*

3. `To further optimize the codes above`, we could **ignore some collisions for game-specific geographic reasons**. For example, we could ignore the collision out of screen/display area or the objects in seperate areas. 

4. `An alternative method to dectect the collision between rects` is to detect if one side of one rect overlaps with the opposite side in another rect in a coordinate system.

5. `When calculating shapes like circles`, unlike the basic collision detection method for rectangles mentioned above, we could **compare the distance between two center of circles with the sum of their radius** to see if they collides.

6. `To avoid the wrong collision caused by the blank space of the circle or a rect`, we could **combine several shapes** like rects, triangles ,or circles to create a more precise space. 

7. `An alternative method to avoid the mistake mentioned above` is to **use polygons** to create a really accurate space. But it's relatively slow.

8. `To solve the move-through problem`, we could **use the linear equation of routes of each angle** (y = kx + b) to calculate if these lines cross each other. This could test whether they collide between two frames. 

9. `To detect if one point is in a triangle`, we could **divide the triangle into three parts and see if there total area is equal to the area of the original triangle**.

---

## Sounds/ Musics in a game

These sounds offer both mood and guidiance to the players.

1. Background music offers the mood or the tone in the game.

2. Speed offers hint to push the progress forward.

3. Ambient sound is similar to background music, but it's not that load and gives players a sence of involvement.

4. Sound effect is more subtle and gives players feedbacks of what they have just done.

We use `pygame.mixer` to load and play sound in python. We could use `pygame.init()` to initialize the mixer. There are objects like `Sound` or `Channel` to help us play the music.