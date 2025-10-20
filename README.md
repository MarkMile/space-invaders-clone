# alien-invasion-clone (Pygame)

A **classic arcade-style space shooter** built with **Python** and **Pygame**.

Dodge incoming enemies, fire lasers, and try to survive as long as you can while racking up points.

## 💡 Project Motivation

I built this project to deepen my understanding of game loops, object-oriented design, and Pygame mechanics — all while recreating one of my favorite classic arcade experiences.

It’s a fun and interactive way to practice real-time rendering, collision detection, and animation in Python.

## 🚀 Features

- 🛸 Smooth Pygame graphics and animation
- 💥 Laser shooting and alien collision detection
- 👾 Multiple alien types and wave progression
- 🧠 Game stats tracking and scoreboard
- 🔘 Start button and game-over screen
- ⚙️ Modular, extensible architecture (easy to add new features)

## 🧩 How It Works

The game runs inside a **main game loop**, which:

- Listens for player input (keyboard, mouse).
- Updates all objects (ship, bullets, aliens).
- Detects collisions between bullets and aliens.
- Draws the updated frame to the screen each cycle.

When all aliens are destroyed, a new wave spawns — faster and harder. The player loses if an alien reaches the bottom or the ship is hit.

## 🗂️ Project Structure

`alien-invasion/`<br>
`│`<br>
`├── alien_invasion.py   # Main entry point; runs the game loop`<br>
`├── alien.py            # Defines the Alien class and movement behavior`<br>
`├── bullet.py           # Manages bullets fired by the player`<br>
`├── button.py           # Handles Play button functionality`<br>
`├── game_stats.py       # Tracks score, lives, and game state`<br>
`├── scoreboard.py       # Displays score and high score`<br>
`├── settings.py         # Holds configurable game settings`<br>
`├── ship.py             # Controls player movement and rendering`<br>
`│`<br>
`├── images/             # Sprite and background assets`<br>
`│   ├── alien1_frame1.png`<br>
`│   ├── alien1_frame2.png`<br>
`│   ├── alien2_frame1.png`<br>
`│   ├── alien2_frame2.png`<br>
`│   ├── alien3_frame1.png`<br>
`│   ├── alien3_frame2.png`<br>
`│   ├── background_image.png`<br>
`│   ├── ship.png`<br>
`│   ├── ship_white.png`<br>
`│   └── ships_left.png`<br>
`│`<br>
`├── font/`<br>
`│   └── RetroGaming.ttf`<br>
`│`<br>
`└── README.md`<br>

## 🖥️ Technologies Used

- **Python 3.x**
- **Pygame** – game engine for rendering and input handling
- **OOP principles** – modular design for reusability
- **Event-driven architecture** – smooth input and updates

## 📦 Installation

1. Clone the repository:<br>
  `git clone https://github.com/MarkMile/alien-invasion-clone.git`<br>
  `cd alien-invasion-clone`

3. Install dependencies:<br>
  `pip install pygame`

4. Run the game:<br>
  `python alien_invasion.py`

## 🕹️ Controls

| Key     | Action                                    |
| ------- | ----------------------------------------- |
| ⬅️ / ➡️ | Move the ship left or right               |
| SPACE   | Fire a bullet                             |
| Q       | Quit the game                             |
| Mouse   | Click “Play” to start or restart the game |

## 📘 Gameplay Instructions

1. Launch the game using `python alien_invasion.py`.
2. Click the Play button to begin.
3. Move the ship left and right using the arrow keys.
4. Press SPACE to fire bullets and destroy incoming aliens.
5. Earn points for each alien destroyed — higher levels spawn faster enemies.
6. The game ends when all lives are lost.

## 📷 Preview

## 🛠️ Future Improvements

- Add sound effects and background music 🎵
- Include boss fights or power-ups
- Save high scores between sessions

## 🧑‍💻 Author
**Marko Miletic**<br>
📫[LinkedIn](https://www.linkedin.com/in/marko1987/)
