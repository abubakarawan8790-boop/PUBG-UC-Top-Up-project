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


