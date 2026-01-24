import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pathlib

from models import (
    Army,
    Sectorial,
    SECTORIALS_BY_ARMY,
    FactionSpread,
)
from plot import FactionSpreadPlotter


class InfinityFactionVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Infinity Faction Spread Visualiser")
        self.geometry("1000x750")

        self._sectorial_vars: dict[Sectorial, tk.IntVar] = {}
        self._tournament_name = tk.StringVar()
        self._output_folder = tk.StringVar(value=str(pathlib.Path.cwd()))

        self._build_ui()

    # ------------------------------------------------------------------ UI BUILD

    def _build_ui(self):
        main_frame = ttk.Frame(self, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self._bind_mousewheel(canvas)

        for army, sectorials in SECTORIALS_BY_ARMY.items():
            self._create_army_group(scroll_frame, army, sectorials)

        self._build_bottom_controls()

    def _create_army_group(
        self,
        parent: ttk.Frame,
        army: Army,
        sectorials: tuple[Sectorial, ...],
    ):
        group_box = ttk.LabelFrame(parent, text=army.value, padding=10)
        group_box.pack(fill=tk.X, expand=True, pady=6)

        for idx, sectorial in enumerate(sectorials):
            row = idx // 2
            col = (idx % 2) * 2

            var = tk.IntVar(value=0)
            self._sectorial_vars[sectorial] = var

            ttk.Label(
                group_box,
                text=sectorial.value,
                anchor="w",
            ).grid(
                row=row,
                column=col,
                sticky="w",
                padx=(0, 6),
                pady=2,
            )

            ttk.Entry(
                group_box,
                textvariable=var,
                width=6,
            ).grid(
                row=row,
                column=col + 1,
                sticky="w",
                padx=(0, 16),
                pady=2,
            )

        group_box.columnconfigure(0, weight=1)
        group_box.columnconfigure(2, weight=1)

    def _build_bottom_controls(self):
        bottom = ttk.Frame(self, padding=10)
        bottom.pack(fill=tk.X)

        # Tournament name
        ttk.Label(bottom, text="Tournament name:").grid(
            row=0, column=0, sticky="w"
        )
        ttk.Entry(
            bottom,
            textvariable=self._tournament_name,
            width=40,
        ).grid(
            row=0, column=1, sticky="w", padx=(5, 20)
        )

        # Output folder
        ttk.Label(bottom, text="Output folder:").grid(
            row=1, column=0, sticky="w"
        )
        ttk.Entry(
            bottom,
            textvariable=self._output_folder,
            width=40,
        ).grid(
            row=1, column=1, sticky="w", padx=(5, 5)
        )
        ttk.Button(
            bottom,
            text="Browse",
            command=self._select_output_folder,
        ).grid(
            row=1, column=2, sticky="w"
        )

        # Buttons
        button_frame = ttk.Frame(bottom)
        button_frame.grid(row=0, column=3, rowspan=2, sticky="e")

        ttk.Button(
            button_frame,
            text="Draw",
            command=self._on_draw,
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Close",
            command=self.destroy,
        ).pack(side=tk.LEFT)

        bottom.columnconfigure(1, weight=1)

    # ------------------------------------------------------------------ EVENTS

    def _select_output_folder(self):
        path = filedialog.askdirectory()
        if path:
            self._output_folder.set(path)

    def _on_draw(self):
        if not self._tournament_name.get().strip():
            messagebox.showerror(
                "Missing tournament name",
                "Please enter a tournament name.",
            )
            return

        if not self._output_folder.get():
            messagebox.showerror(
                "Missing output folder",
                "Please select an output folder.",
            )
            return

        spread = FactionSpread(
            tournament_name=self._tournament_name.get().strip(),
            output_folder=pathlib.Path(self._output_folder.get()),
            played_sectorials={
                sectorial: var.get()
                for sectorial, var in self._sectorial_vars.items()
            },
        )
        FactionSpreadPlotter.plot(spread)

        messagebox.showinfo(
            "Draw",
            "FactionSpread object created successfully.",
        )

    # ------------------------------------------------------------------ SCROLLING

    def _bind_mousewheel(self, canvas: tk.Canvas):
        def _on_mousewheel(event):
            if event.delta:
                canvas.yview_scroll(int(-event.delta / 120), "units")
            elif event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all("<Button-4>", _on_mousewheel)
        canvas.bind_all("<Button-5>", _on_mousewheel)


if __name__ == "__main__":
    app = InfinityFactionVisualizer()
    app.mainloop()
