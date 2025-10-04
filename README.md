# CogniSnake

CogniSnake simulates an intelligent snake that makes real-time decisions to navigate toward moving food. It uses simple scoring and simulation to choose its next move based on the current state of the environment.

## Features

- Real-time decision-making using simulation
- Configurable planning depth and board size
- Simple enough for experiment
- Works in the terminal or with a simple Pygame-based GUI

## Getting Started
1. Clone the repository:

```bash
git clone https://github.com/tanvir362/CogniSnake.git
cd CogniSnake
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run the terminal demo:

```bash
python main.py
```

Tips
- Tweak `STEP`, `WIDTH`, `HEIGHT`, and the simulate depth to explore trade-offs.

Files of interest
- `snake.py` — core logic, simulation, and terminal rendering.
- `main.py` — a lightweight pygame frontend that uses the same model.
- `constants.py` — grid and step configuration.
