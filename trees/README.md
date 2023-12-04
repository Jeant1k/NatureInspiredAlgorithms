This program draws unique trees by generating their genetic codes according to the rules of L-systems. The tree of Pythagoras is taken as a basis.

Pythagorean tree:
- variables: 0, 1
- constants: [, ]
- axiom: 0
- rules: (1 → 11), (0 → 1[0]0)

Meaning of the commands:
- 0: draw a segment ending with a leaf
- 1: draw a segment
- [: put the position and drawing angle on the stack, rotate to the left 45 degrees
- ]: read the position and angle from the stack, rotate to the right 45 degrees
