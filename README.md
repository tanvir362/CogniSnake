# CogniSnake

A tiny sandbox where a thinking snake plans ahead.

CogniSnake isn't about flashy graphics — it's about simple intelligence. The snake looks a few moves forward, scores outcomes by distance to a target, and picks the move that seems best. The code is intentionally small so you can experiment quickly with heuristics, depth, and rendering.

Why this is fun
- Try different scoring functions and watch behavior change.
- Increase search depth to see planning emerge (and the cost explode).
- Swap the terminal renderer for a GUI (there's a small pygame hook included).

Getting started
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
