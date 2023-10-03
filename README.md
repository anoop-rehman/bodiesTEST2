# bodies

right now im just trying out things. currently transformers with tic tac toe to see if it can learn. next is transformers with mcts. also this is rapid prototyping of ideas so far so im functioning more as a prompt engineer.

```console
game1

Current Board:
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[-0.13 -0.46  0.78]
 [ 0.25  0.23  0.49]
 [-8.44  0.46  0.77]]

AI Player 1 making move...

Current Board:
[0. 0. 1.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[-0.12  0.17  0.66]
 [-0.04 -0.18  0.64]
 [-9.8   0.32  0.59]]

AI Player 2 making move...

Current Board:
[0. 0. 1.]
[0. 0. 0.]
[2. 0. 0.]

Move Heat Map:
[[-0.79 -1.96  0.7 ]
 [ 0.32  0.43  1.33]
 [-7.06  0.62  1.77]]

AI Player 1 making move...

Current Board:
[0. 0. 1.]
[0. 0. 0.]
[2. 0. 1.]

Move Heat Map:
[[-0.16 -0.51  0.84]
 [ 0.17  0.31  0.75]
 [-8.34  0.62  1.04]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[0. 2. 1.]
[0. 0. 0.]
[2. 0. 1.]

Move Heat Map:
[[  0.53   2.41   1.  ]
 [ -0.48  -0.4    0.03]
 [-10.71   0.26  -0.29]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move

Current Board:
[1. 2. 1.]
[0. 0. 0.]
[2. 0. 1.]

Move Heat Map:
[[-0.15 -1.18  0.7 ]
 [ 0.38  0.44  0.84]
 [-7.73  0.59  1.34]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[1. 2. 1.]
[2. 0. 0.]
[2. 0. 1.]

Move Heat Map:
[[ 0.54  1.51  0.69]
 [-0.19 -0.12  0.19]
 [-9.95  0.39  0.47]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move

Current Board:
[1. 2. 1.]
[2. 0. 0.]
[2. 1. 1.]

Move Heat Map:
[[-0.05 -0.16  0.64]
 [-0.03  0.15  0.74]
 [-8.4   0.31  0.75]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[1. 2. 1.]
[2. 2. 0.]
[2. 1. 1.]

Move Heat Map:
[[-0.64 -1.93  0.64]
 [ 0.47  0.6   1.04]
 [-6.53  0.41  1.47]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move

Final Board:
[1. 2. 1.]
[2. 2. 1.]
[2. 1. 1.]

Player 1 (AI) Wins!
game2

Current Board:
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[  0.34   0.89   0.64]
 [ -0.2   -0.1    0.28]
 [-10.09   0.36   0.3 ]]

AI Player 1 making move...

Current Board:
[0. 1. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[-0.37 -1.72  0.74]
 [ 0.41  0.61  0.99]
 [-7.23  0.67  1.42]]

AI Player 2 making move...

Current Board:
[0. 1. 0.]
[0. 0. 0.]
[2. 0. 0.]

Move Heat Map:
[[-0.64  0.23  0.98]
 [ 0.11 -0.02  1.  ]
 [-9.65  0.55  0.89]]

AI Player 1 making move...

Current Board:
[0. 1. 0.]
[0. 0. 1.]
[2. 0. 0.]

Move Heat Map:
[[  0.06   1.94   0.88]
 [ -0.39  -0.66   0.23]
 [-11.32   0.13  -0.08]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[0. 1. 0.]
[0. 2. 1.]
[2. 0. 0.]

Move Heat Map:
[[-0.11 -1.72  0.66]
 [ 0.29  0.44  0.94]
 [-7.    0.55  1.36]]

AI Player 1 making move...

Current Board:
[0. 1. 0.]
[0. 2. 1.]
[2. 0. 1.]

Move Heat Map:
[[ 0.42  0.61  0.78]
 [-0.12 -0.03  0.43]
 [-8.98  0.37  0.71]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[0. 1. 0.]
[2. 2. 1.]
[2. 0. 1.]

Move Heat Map:
[[ 0.07  0.67  0.66]
 [-0.06 -0.16  0.4 ]
 [-9.7   0.37  0.6 ]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move

Final Board:
[0. 1. 1.]
[2. 2. 1.]
[2. 0. 1.]

Player 1 (AI) Wins!
game3

Current Board:
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[  0.66   2.53   0.69]
 [ -0.58  -0.46  -0.3 ]
 [-11.29   0.19  -0.23]]

AI Player 1 making move...

Current Board:
[0. 1. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[-0.21 -0.87  0.81]
 [ 0.24  0.27  0.78]
 [-7.77  0.55  0.94]]

AI Player 2 making move...

Current Board:
[0. 1. 0.]
[0. 0. 0.]
[2. 0. 0.]

Move Heat Map:
[[ 0.14 -0.04  0.64]
 [-0.05  0.07  0.6 ]
 [-9.13  0.48  0.7 ]]

AI Player 1 making move...

Current Board:
[0. 1. 0.]
[0. 0. 0.]
[2. 0. 1.]

Move Heat Map:
[[-0.24 -3.11  0.8 ]
 [ 0.38  0.75  1.28]
 [-5.14  0.74  2.07]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[2. 1. 0.]
[0. 0. 0.]
[2. 0. 1.]

Move Heat Map:
[[ -0.15   2.88   0.92]
 [ -0.67  -0.67  -0.09]
 [-12.26   0.02  -0.77]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move

Current Board:
[2. 1. 1.]
[0. 0. 0.]
[2. 0. 1.]

Move Heat Map:
[[ 0.03  0.85  0.68]
 [-0.34 -0.33  0.45]
 [-9.98  0.21  0.24]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move

Final Board:
[2. 1. 1.]
[2. 0. 0.]
[2. 0. 1.]

Player 2 (AI) Wins!```
