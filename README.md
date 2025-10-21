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
`├── space_invaders.py   # Main entry point`<br>
`├── invader.py          # Invader class and movement behavior`<br>
`├── bullet.py           # Player projectiles`<br>
`├── button_ui.py        # Handles button functionality`<br>
`├── game_stats.py       # Tracks stats and progress`<br>
`├── scoreboard_ui.py    # Displays score and highscore`<br>
`├── config.py           # Holds configurable game settings`<br>
`├── starfighter.py             # Controls player movement and rendering`<br>
`│`<br>
`├── images/             # Sprite and background assets`<br>
`│   ├── invader1_frame1.png`<br>
`│   ├── invader1_frame2.png`<br>
`│   ├── invader2_frame1.png`<br>
`│   ├── invader2_frame2.png`<br>
`│   ├── invader3_frame1.png`<br>
`│   ├── invader3_frame2.png`<br>
`│   ├── background_image.png`<br>
`│   ├── ships_left.png`<br>
`│   ├── space-invaders-preview.png`<br>
`│   └── starfighter.png`<br>
`│`<br>
`├── font/`<br>
`│   └── RetroGaming.ttf`<br>
`│`<br>
`└── README.md`<br>

## 🖥️ Technologies Used

- **Python 3.10**
- **Pygame** – game engine for rendering and input handling
- **OOP principles** – modular design for reusability
- **Event-driven architecture** – smooth input and updates

## 📦 Installation

1. Clone the repository:<br>
  `git clone https://github.com/MarkMile/space-invaders-clone.git`<br>
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

1. Launch the game using `python space_invaders.py`.
2. Click the Play button to begin.
3. Move the ship left and right using the arrow keys.
4. Press SPACE to fire bullets and destroy incoming aliens.
5. Earn points for each alien destroyed — higher levels spawn faster enemies.
6. The game ends when all lives are lost.

## 📷 Preview

![space-invaders-preview](https://github.com/MarkMile/space-invaders-clone/blob/main/images/space-invaders-preview.png?raw=true)

## 🛠️ Future Improvements

- Add sound effects and background music 🎵
- Include boss fights or power-ups
- Save high scores between sessions

## 🧑‍💻 Author
**Marko Miletic**<br>
📫[LinkedIn](https://www.linkedin.com/in/marko1987/)
