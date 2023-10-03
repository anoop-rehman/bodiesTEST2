# bodies

right now im just trying out things. currently transformers with tic tac toe to see if it can learn. next is transformers with mcts. also this is rapid prototyping of ideas so far so im functioning more as a prompt engineer.

```console
game1

Current Board:
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[-1.78  2.76  0.66]
 [-6.81  0.64 -0.38]
 [-1.48 -3.54  2.69]]

AI Player 1 making move...

Current Board:
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 1.]

Move Heat Map:
[[-0.62  1.06  0.92]
 [-4.78  0.54 -0.02]
 [-0.95 -2.71  0.94]]

AI Player 2 making move...

Current Board:
[0. 0. 2.]
[0. 0. 0.]
[0. 0. 1.]

Move Heat Map:
[[-0.58  1.05  0.66]
 [-5.    0.74  0.12]
 [-1.08 -2.36  0.73]]

AI Player 1 making move...

Current Board:
[0. 0. 2.]
[0. 1. 0.]
[0. 0. 1.]

Move Heat Map:
[[-1.51  2.04  0.65]
 [-6.16  0.42 -0.39]
 [-1.55 -3.36  2.17]]

AI Player 2 making move...

Current Board:
[0. 0. 2.]
[2. 1. 0.]
[0. 0. 1.]

Move Heat Map:
[[-2.24  3.46  0.51]
 [-7.94  0.95 -0.72]
 [-2.1  -4.28  3.46]]

AI Player 1 making move...

Current Board:
[0. 1. 2.]
[2. 1. 0.]
[0. 0. 1.]

Move Heat Map:
[[-2.73  4.05  0.1 ]
 [-8.95  0.56 -0.91]
 [-2.01 -4.31  4.7 ]]

AI Player 2 making move...

Current Board:
[0. 1. 2.]
[2. 1. 2.]
[0. 0. 1.]

Move Heat Map:
[[-0.81  1.15  0.55]
 [-5.27  0.55 -0.12]
 [-1.46 -2.85  1.01]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move

Final Board:
[1. 1. 2.]
[2. 1. 2.]
[0. 0. 1.]

Player 1 (AI) Wins!
game2

Current Board:
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[-0.96  2.03  0.79]
 [-6.19  0.61 -0.57]
 [-1.48 -3.67  2.31]]

AI Player 1 making move...

Current Board:
[0. 0. 0.]
[0. 0. 0.]
[1. 0. 0.]

Move Heat Map:
[[-1.55  2.27  0.55]
 [-6.82  0.82 -0.33]
 [-1.57 -3.55  2.24]]

AI Player 2 making move...

Current Board:
[0. 0. 0.]
[2. 0. 0.]
[1. 0. 0.]

Move Heat Map:
[[-0.75  1.26  0.73]
 [-5.19  0.79  0.17]
 [-1.37 -2.52  1.1 ]]

AI Player 1 making move...

Current Board:
[1. 0. 0.]
[2. 0. 0.]
[1. 0. 0.]

Move Heat Map:
[[-1.19  1.81  0.6 ]
 [-6.24  0.63 -0.29]
 [-1.5  -2.98  1.65]]

AI Player 2 making move...

Current Board:
[1. 0. 0.]
[2. 0. 2.]
[1. 0. 0.]

Move Heat Map:
[[-1.08  1.93  0.77]
 [-5.81  0.82 -0.23]
 [-1.24 -3.11  1.88]]

AI Player 1 making move...

Current Board:
[1. 0. 0.]
[2. 0. 2.]
[1. 0. 1.]

Move Heat Map:
[[-0.37  1.28  0.44]
 [-5.39  0.76 -0.24]
 [-1.39 -2.79  1.14]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[1. 0. 0.]
[2. 0. 2.]
[1. 2. 1.]

Move Heat Map:
[[-0.95  1.52  0.71]
 [-5.58  0.86  0.04]
 [-1.16 -2.86  1.47]]

AI Player 1 making move...

Current Board:
[1. 1. 0.]
[2. 0. 2.]
[1. 2. 1.]

Move Heat Map:
[[-0.73  1.56  0.53]
 [-5.42  0.67 -0.03]
 [-1.13 -3.04  1.39]]

AI Player 2 making move...

Current Board:
[1. 1. 2.]
[2. 0. 2.]
[1. 2. 1.]

Move Heat Map:
[[-0.9   1.46  0.76]
 [-5.5   0.56  0.01]
 [-1.14 -2.78  1.22]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move

Final Board:
[1. 1. 2.]
[2. 1. 2.]
[1. 2. 1.]

Player 1 (AI) Wins!
game3

Current Board:
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[-0.78  1.34  0.64]
 [-5.55  0.66  0.04]
 [-1.31 -2.81  1.32]]

AI Player 1 making move...

Current Board:
[0. 1. 0.]
[0. 0. 0.]
[0. 0. 0.]

Move Heat Map:
[[-1.99  3.39  0.77]
 [-7.67  1.09 -0.9 ]
 [-1.6  -3.99  3.61]]

AI Player 2 making move...

Current Board:
[0. 1. 0.]
[0. 0. 0.]
[0. 2. 0.]

Move Heat Map:
[[-0.95  1.35  0.59]
 [-5.41  0.91  0.24]
 [-1.31 -3.03  1.3 ]]

AI Player 1 making move...

Current Board:
[0. 1. 0.]
[0. 0. 0.]
[0. 2. 1.]

Move Heat Map:
[[-0.71  1.43  0.57]
 [-5.31  0.68 -0.02]
 [-1.53 -2.65  1.49]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[0. 1. 0.]
[2. 0. 0.]
[0. 2. 1.]

Move Heat Map:
[[-1.87  2.31  0.77]
 [-7.04  0.33 -0.48]
 [-1.29 -3.76  2.65]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move

Current Board:
[0. 1. 1.]
[2. 0. 0.]
[0. 2. 1.]

Move Heat Map:
[[-0.93  1.48  0.55]
 [-5.57  0.89 -0.14]
 [-1.3  -2.91  1.35]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move

Current Board:
[0. 1. 1.]
[2. 0. 0.]
[2. 2. 1.]

Move Heat Map:
[[-1.12  1.93  0.71]
 [-5.75  0.59 -0.34]
 [-1.32 -3.03  1.88]]

AI Player 1 making move...
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move
AI Player 1 trying illegal move, choosing next best move

Current Board:
[0. 1. 1.]
[2. 1. 0.]
[2. 2. 1.]

Move Heat Map:
[[-0.35  0.73  0.89]
 [-4.41  0.74  0.36]
 [-0.98 -2.2   0.25]]

AI Player 2 making move...
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move
AI Player 2 trying illegal move, choosing next worst move

Final Board:
[2. 1. 1.]
[2. 1. 0.]
[2. 2. 1.]

Player 2 (AI) Wins!```
