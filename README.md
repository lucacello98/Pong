**# Pong Game**

This is a simple implementation of the classic Pong game using Python's `turtle` graphics library. The game features two paddles, a ball, a scoreboard, and basic collision detection.

**## Features**

- **Two-player gameplay:** Control paddles using keyboard inputs.
- **Ball movement:** The ball moves and bounces off the top/bottom of the screen and paddles.
- **Scoring:** Points are scored when the ball crosses the left or right boundaries.
- **Resetting the ball:** The ball resets to the center after scoring.
- **Simple controls:** 
  - Right paddle: Use the **Up** and **Down** arrow keys.
  - Left paddle: Use the **W** and **S** keys.

**## Requirements**

- Python 3.x
- `turtle` library (comes pre-installed with Python)

**## How to Play**

1. Clone or download the repository to your local machine.
2. Run the `main.py` file in your Python environment.
3. Use the **Up** and **Down** arrow keys to move the right paddle.
4. Use the **W** and **S** keys to move the left paddle.
5. The first player to score wins by getting the ball past the opponent's paddle.
6. The scoreboard will update after each point.

**## Game Loop**

The game runs continuously with the following logic:
- The ball moves automatically.
- It bounces off the top and bottom of the screen.
- If the ball collides with a paddle, it bounces in the opposite direction.
- If the ball goes past a paddle, the opponent scores a point, and the ball resets.

