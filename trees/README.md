#Description

This program draws unique trees by generating their genetic codes according to the rules of L-systems. The tree of Pythagoras is taken as a basis.

#Theory

*Pythagorean tree:*
- variables: 0, 1
- constants: [, ]
- axiom: 0
- rules: (1 → 11), (0 → 1[0]0)

*Meaning of the commands:*
- 0: draw a segment ending with a leaf
- 1: draw a segment
- [: put the position and drawing angle on the stack, rotate to the left 45 degrees
- ]: read the position and angle from the stack, rotate to the right 45 degrees

#Results:

###Summer tree
![summer tree](https://github.com/Jeant1k/NatureInspiredAlgorithms/assets/108530450/e3c96a2d-0d1d-4189-98f7-410deb028d9c)

###Autumn tree
![autumn tree](https://github.com/Jeant1k/NatureInspiredAlgorithms/assets/108530450/2ab5d314-549d-4265-a017-2bf9cfe6dbbd)

###Baobab
![baobab](https://github.com/Jeant1k/NatureInspiredAlgorithms/assets/108530450/3cb786f5-888e-42a2-85d9-8446b4c54b78)

###Bonsai
![bonsai](https://github.com/Jeant1k/NatureInspiredAlgorithms/assets/108530450/3f6d3a14-87b5-4b68-a276-6cadc1b9b79c)
