# PUBG Mobile UC Top-Up (Tkinter GUI)

A desktop GUI application built with Python's Tkinter that simulates a UC (Unknown Cash) top-up form for PUBG Mobile. It provides a dark-themed, mobile-store-style interface where a user can enter their Player ID, pick a UC package, provide a JazzCash/EasyPaisa number, and confirm an order summary.

> **Note:** This is a UI/front-end simulation only. It does **not** process real payments or connect to any PUBG Mobile / game servers — it simply validates input and displays an order summary.

## Preview

A single-window, scrollable form with:
- A stylized logo and header
- Player ID input with live validation
- A grid of selectable UC packages with pricing
- Payment provider selection (JazzCash / EasyPaisa) with number validation
- A "Confirm Order" button that displays an order summary

## Features

- 🎨 Dark, game-store-inspired theme
- 📜 Scrollable layout (mouse wheel supported on Windows/Linux/macOS)
- ✅ Live validation for:
  - Player Unique ID (9 or 10 digits)
  - Payment number (11 digits)
- 💳 Choice between **JazzCash** and **EasyPaisa**
- 📦 Six UC packages with PKR pricing (editable in code)
- 🧾 Order summary shown on confirmation

## Requirements

- Python 3.7+
- Tkinter (included with most standard Python installations)

No external/third-party packages are required.

### Installing Tkinter (if missing)

- **Windows / macOS:** Tkinter ships with the official Python installer — no extra steps needed.
- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get install python3-tk
  ```
- **Linux (Fedora):**
  ```bash
  sudo dnf install python3-tkinter
  ```

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```
2. Run the app:
   ```bash
   python pubg_uc_topup1.py
   ```

## Usage

1. Enter your PUBG Mobile Unique ID (9 or 10 digits).
2. Select a UC package from the grid.
3. Choose JazzCash or EasyPaisa and enter your 11-digit number.
4. Click **CONFIRM ORDER** to see a summary of your order.

## Configuration

UC package amounts and prices can be changed by editing the `PRICES` dictionary near the top of the script:

```python
PRICES = {30: 124, 60: 249, 300: 1249, 600: 2499, 1500: 6249, 3000: 12499}
```

Colors, fonts, and window size can also be adjusted via the constants defined at the top of the file (`BG_DARK`, `ACCENT_YELLOW`, `FONT_TITLE`, etc.).

## Project Structure

```
.
├── pubg_uc_topup1.py   # Main application
└── README.md
```

## Disclaimer

This project is an independent, unofficial UI demo created for educational/portfolio purposes. It is **not affiliated with, endorsed by, or connected to** PUBG Mobile, Krafton, Tencent, JazzCash, or EasyPaisa in any way. No real transactions occur.

## License

You can license this project as you like (e.g., MIT). Add a `LICENSE` file to the repository if you intend to open-source it.
