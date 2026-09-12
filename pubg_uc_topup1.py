

import tkinter as tk
from tkinter import ttk, messagebox


BG_DARK = "#0d1117"
BG_PANEL = "#161b22"
BG_CARD = "#1c2129"
BG_CARD_SELECTED = "#2b2410"
ACCENT_YELLOW = "#f2b705"
ACCENT_YELLOW_HOVER = "#ffd23f"
TEXT_PRIMARY = "#f5f5f5"
TEXT_SECONDARY = "#9aa5b1"
SUCCESS = "#3ddc84"
ERROR = "#ff5c5c"
BORDER = "#2a313c"

FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_SUB = ("Segoe UI", 10)
FONT_LABEL = ("Segoe UI", 11, "bold")
FONT_ENTRY = ("Segoe UI", 12)
FONT_CARD_UC = ("Segoe UI", 13, "bold")
FONT_CARD_PRICE = ("Segoe UI", 11)
FONT_STATUS = ("Segoe UI", 9)
FONT_BTN = ("Segoe UI", 12, "bold")

PRICES = {30: 124, 60: 249, 300: 1249, 600: 2499, 1500: 6249, 3000: 12499}



def draw_logo(canvas):
    """Draws a simple stylised helmet + crosshair emblem."""
    canvas.create_oval(8, 8, 72, 72, fill=ACCENT_YELLOW, outline="")
    canvas.create_arc(16, 20, 64, 68, start=0, extent=180,
                       fill=BG_DARK, outline="", style="pieslice")
    canvas.create_rectangle(16, 40, 64, 48, fill=BG_DARK, outline="")
    canvas.create_oval(34, 34, 46, 46, outline=BG_DARK, width=2)
    canvas.create_line(40, 26, 40, 34, fill=BG_DARK, width=2)
    canvas.create_line(40, 46, 40, 54, fill=BG_DARK, width=2)
    canvas.create_line(26, 40, 34, 40, fill=BG_DARK, width=2)
    canvas.create_line(46, 40, 54, 40, fill=BG_DARK, width=2)



class UCTopUpApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PUBG Mobile UC Top-Up")
        self.geometry("480x760")
        self.minsize(440, 700)
        self.configure(bg=BG_DARK)

        self.selected_uc = tk.IntVar(value=0)
        self.uc_cards = {}
        self.id_status_var = tk.StringVar(value="")
        self.num_status_var = tk.StringVar(value="")

        self._build_style()
        self._build_scroll_container()
        self._build_header()
        self._build_id_section()
        self._build_package_section()
        self._build_payment_section()
        self._build_submit_section()

    
    def _build_scroll_container(self):
        outer = tk.Frame(self, bg=BG_DARK)
        outer.pack(fill="both", expand=True)

        canvas = tk.Canvas(outer, bg=BG_DARK, highlightthickness=0)
        scrollbar = tk.Scrollbar(outer, orient="vertical", command=canvas.yview,
                                  bg=BG_PANEL, troughcolor=BG_DARK)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        
        self.container = tk.Frame(canvas, bg=BG_DARK)
        window_id = canvas.create_window((0, 0), window=self.container, anchor="nw")

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_canvas_configure(event):
            # Make the inner frame match the canvas width so widgets can fill("x")
            canvas.itemconfig(window_id, width=event.width)

        self.container.bind("<Configure>", on_frame_configure)
        canvas.bind("<Configure>", on_canvas_configure)

        
        def on_mousewheel(event):
            if event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")
            else:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)
        canvas.bind_all("<Button-4>", on_mousewheel)
        canvas.bind_all("<Button-5>", on_mousewheel)

    
    def _build_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Dark.TFrame", background=BG_DARK)
        style.configure("Panel.TFrame", background=BG_PANEL)
        style.configure(
            "Yellow.Horizontal.TProgressbar",
            troughcolor=BG_PANEL, background=ACCENT_YELLOW,
        )

    
    def _build_header(self):
        header = tk.Frame(self.container, bg=BG_DARK)
        header.pack(fill="x", padx=20, pady=(20, 10))

        canvas = tk.Canvas(header, width=80, height=80, bg=BG_DARK,
                            highlightthickness=0)
        canvas.pack(side="left")
        draw_logo(canvas)

        text_frame = tk.Frame(header, bg=BG_DARK)
        text_frame.pack(side="left", padx=14)
        tk.Label(text_frame, text="UC TOP-UP", font=FONT_TITLE,
                  fg=ACCENT_YELLOW, bg=BG_DARK).pack(anchor="w")
        tk.Label(text_frame, text="Battle Royale Currency Recharge",
                  font=FONT_SUB, fg=TEXT_SECONDARY, bg=BG_DARK).pack(anchor="w")

        tk.Frame(self.container, bg=BORDER, height=2).pack(fill="x", padx=20, pady=(4, 10))

    
    def _section_label(self, text):
        tk.Label(self.container, text=text, font=FONT_LABEL, fg=TEXT_PRIMARY,
                  bg=BG_DARK).pack(anchor="w", padx=20, pady=(6, 4))

    
    def _build_id_section(self):
        self._section_label("① Enter Your PUBG Mobile Unique ID")

        card = tk.Frame(self.container, bg=BG_PANEL, highlightbackground=BORDER,
                         highlightthickness=1)
        card.pack(fill="x", padx=20, pady=(0, 6))

        self.id_entry = tk.Entry(
            card, font=FONT_ENTRY, bg=BG_CARD, fg=TEXT_PRIMARY,
            insertbackground=ACCENT_YELLOW, relief="flat",
            highlightthickness=0, justify="left",
        )
        self.id_entry.pack(fill="x", padx=14, pady=12, ipady=6)
        self.id_entry.bind("<KeyRelease>", lambda e: self._validate_id(live=True))
        self._add_placeholder(self.id_entry, "e.g. 5123456789")

        self.id_status_label = tk.Label(
            self.container, textvariable=self.id_status_var, font=FONT_STATUS,
            bg=BG_DARK, anchor="w",
        )
        self.id_status_label.pack(fill="x", padx=22)

    
    def _add_placeholder(self, entry, text):
        entry.insert(0, text)
        entry.config(fg=TEXT_SECONDARY)

        def on_focus_in(_):
            if entry.get() == text:
                entry.delete(0, tk.END)
                entry.config(fg=TEXT_PRIMARY)

        def on_focus_out(_):
            if not entry.get():
                entry.insert(0, text)
                entry.config(fg=TEXT_SECONDARY)

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        entry._placeholder = text

    def _real_value(self, entry):
        val = entry.get().strip()
        return "" if val == entry._placeholder else val

    
    def _validate_id(self, live=False):
        try:
            value = self._real_value(self.id_entry)
            if not value:
                self.id_status_var.set("")
                return False
            if not value.isdigit():
                raise ValueError
            if len(value) == 9 or len(value) == 10:
                self.id_status_var.set("✔ Your ID is valid. Make sure to read it carefully once.")
                self.id_status_label.config(fg=SUCCESS)
                return True
            else:
                raise ValueError
        except Exception:
            self.id_status_var.set("✖ Please enter a valid ID (9 or 10 digits).")
            self.id_status_label.config(fg=ERROR)
            return False

    
    def _build_package_section(self):
        self._section_label("② Choose a UC Package")

        grid = tk.Frame(self.container, bg=BG_DARK)
        grid.pack(fill="x", padx=20)
        grid.columnconfigure((0, 1), weight=1)

        for i, (uc, pkr) in enumerate(PRICES.items()):
            row, col = divmod(i, 2)
            card = tk.Frame(grid, bg=BG_CARD, highlightbackground=BORDER,
                             highlightthickness=1, cursor="hand2")
            card.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

            uc_label = tk.Label(card, text=f"{uc} UC", font=FONT_CARD_UC,
                                 fg=ACCENT_YELLOW, bg=BG_CARD)
            uc_label.pack(pady=(12, 2))
            price_label = tk.Label(card, text=f"Rs. {pkr} PKR",
                                    font=FONT_CARD_PRICE, fg=TEXT_SECONDARY,
                                    bg=BG_CARD)
            price_label.pack(pady=(0, 12))

            widgets = (card, uc_label, price_label)
            for w in widgets:
                w.bind("<Button-1>", lambda e, u=uc: self._select_package(u))
            self.uc_cards[uc] = widgets

    def _select_package(self, uc):
        self.selected_uc.set(uc)
        for pkg, (card, uc_label, price_label) in self.uc_cards.items():
            if pkg == uc:
                card.config(bg=BG_CARD_SELECTED, highlightbackground=ACCENT_YELLOW)
                uc_label.config(bg=BG_CARD_SELECTED)
                price_label.config(bg=BG_CARD_SELECTED, fg=TEXT_PRIMARY)
            else:
                card.config(bg=BG_CARD, highlightbackground=BORDER)
                uc_label.config(bg=BG_CARD)
                price_label.config(bg=BG_CARD, fg=TEXT_SECONDARY)

    
    def _build_payment_section(self):
        self._section_label("③ Enter JazzCash / EasyPaisa Number")

        card = tk.Frame(self.container, bg=BG_PANEL, highlightbackground=BORDER,
                         highlightthickness=1)
        card.pack(fill="x", padx=20, pady=(0, 6))

        self.provider_var = tk.StringVar(value="JazzCash")
        provider_frame = tk.Frame(card, bg=BG_PANEL)
        provider_frame.pack(fill="x", padx=14, pady=(12, 0))

        for provider in ("JazzCash", "EasyPaisa"):
            rb = tk.Radiobutton(
                provider_frame, text=provider, value=provider,
                variable=self.provider_var, font=FONT_SUB,
                bg=BG_PANEL, fg=TEXT_PRIMARY, selectcolor=BG_CARD,
                activebackground=BG_PANEL, activeforeground=ACCENT_YELLOW,
                highlightthickness=0,
            )
            rb.pack(side="left", padx=(0, 16))

        self.num_entry = tk.Entry(
            card, font=FONT_ENTRY, bg=BG_CARD, fg=TEXT_PRIMARY,
            insertbackground=ACCENT_YELLOW, relief="flat",
            highlightthickness=0,
        )
        self.num_entry.pack(fill="x", padx=14, pady=12, ipady=6)
        self.num_entry.bind("<KeyRelease>", lambda e: self._validate_number(live=True))
        self._add_placeholder(self.num_entry, "03XXXXXXXXX")

        self.num_status_label = tk.Label(
            self.container, textvariable=self.num_status_var, font=FONT_STATUS,
            bg=BG_DARK, anchor="w",
        )
        self.num_status_label.pack(fill="x", padx=22)

    
    def _validate_number(self, live=False):
        try:
            value = self._real_value(self.num_entry)
            if not value:
                self.num_status_var.set("")
                return False
            if not value.isdigit():
                raise ValueError
            if len(value) == 11:
                self.num_status_var.set("✔ Your number is valid.")
                self.num_status_label.config(fg=SUCCESS)
                return True
            else:
                raise ValueError
        except Exception:
            self.num_status_var.set("✖ Please enter a valid 11-digit number.")
            self.num_status_label.config(fg=ERROR)
            return False

    
    def _build_submit_section(self):
        wrapper = tk.Frame(self.container, bg=BG_DARK)
        wrapper.pack(fill="x", padx=20, pady=18)

        self.submit_btn = tk.Button(
            wrapper, text="CONFIRM ORDER", font=FONT_BTN,
            bg=ACCENT_YELLOW, fg=BG_DARK, activebackground=ACCENT_YELLOW_HOVER,
            activeforeground=BG_DARK, relief="flat", cursor="hand2",
            command=self._submit,
        )
        self.submit_btn.pack(fill="x", ipady=10)

        self.footer_var = tk.StringVar(value="")
        tk.Label(self.container, textvariable=self.footer_var, font=FONT_SUB,
                  fg=TEXT_SECONDARY, bg=BG_DARK, wraplength=440,
                  justify="left").pack(fill="x", padx=20, pady=(0, 16))

    def _submit(self):
        id_ok = self._validate_id()
        num_ok = self._validate_number()
        uc = self.selected_uc.get()

        if not id_ok:
            messagebox.showerror("Invalid ID", "Please enter a valid Unique ID (9 or 10 digits).")
            return
        if uc == 0:
            messagebox.showwarning("No Package Selected", "Please choose a UC package before continuing.")
            return
        if not num_ok:
            messagebox.showerror("Invalid Number", "Please enter a valid 11-digit JazzCash/EasyPaisa number.")
            return

        pkr = PRICES[uc]
        provider = self.provider_var.get()
        number = self._real_value(self.num_entry)
        player_id = self._real_value(self.id_entry)

        summary = (
            f"Player ID: {player_id}\n"
            f"Package:   {uc} UC — Rs. {pkr} PKR\n"
            f"Paying via: {provider} ({number})\n\n"
            "Check your app to confirm the payment.\nThank You!"
        )
        self.footer_var.set(summary)
        messagebox.showinfo("Order Confirmed", summary)


if __name__ == "__main__":
    app = UCTopUpApp()
    app.mainloop()
