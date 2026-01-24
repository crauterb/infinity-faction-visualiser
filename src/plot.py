import matplotlib.pyplot as plt
import numpy as np

from models import COLOR_CODING, SECTORIALS_BY_ARMY, Army, FactionSpread

# Ensures reproducibility of random numbers
rng = np.random.default_rng(123)

def get_label_rotation(angle, offset):
    # Rotation must be specified in degrees :(
    rotation = np.rad2deg(angle + offset)
    if angle <= np.pi:
        alignment = "right"
        rotation = rotation + 180
    else: 
        alignment = "left"
    return rotation, alignment

def add_labels(angles, values, labels, offset, ax):
    
    # This is the space between the end of the bar and the label
    padding = 4
    
    # Iterate over angles, values, and labels, to add all of them.
    for angle, value, label, in zip(angles, values, labels):
        angle = angle
        
        # Obtain text rotation and alignment
        rotation, alignment = get_label_rotation(angle, offset)

        # And finally add the text
        ax.text(
            x=angle, 
            y=value + padding, 
            s=label, 
            ha=alignment, 
            va="center", 
            rotation=rotation, 
            rotation_mode="anchor"
        )

class FactionSpreadPlotter:

    @staticmethod
    def plot(input: FactionSpread):

        # Note: The GUI is created from the OrderedList in models.py,
        #   i.e. it is a list, thusly maintaining the order. 
        #   Thusly we can rely on the order being already correct in the faction spread provided from the GUI!

        ALL_ARMIES = [e.value for e in Army]

        # Determines where to place the first bar. 
        # By default, matplotlib starts at 0 (the first bar is horizontal)
        # but here we say we want to start at pi/2 (90 deg)
        OFFSET = np.pi / 2

        VALUES = [elem * 10 for elem in list(input.played_sectorials.values())]
        COLORS = [
            COLOR_CODING[army] for army, sectorials in SECTORIALS_BY_ARMY.items() for _sectorial in sectorials
        ]
        LABELS = [f"{name.value} ({count})" for (name, count) in input.played_sectorials.items()]
        NUMBER_OF_GROUPS = len(ALL_ARMIES)

        PAD = 3
        ANGLES_N = len(VALUES) + PAD * NUMBER_OF_GROUPS
        ANGLES = np.linspace(0, 2 * np.pi, num=ANGLES_N, endpoint=False)
        WIDTH = (2 * np.pi) / len(ANGLES)

        GROUPS_SIZE = [len(SECTORIALS_BY_ARMY[army]) for army in ALL_ARMIES]

        offset = 0
        IDXS = []
        for size in GROUPS_SIZE:
            IDXS += list(range(offset + PAD, offset + size + PAD))
            offset += size + PAD

        _, ax = plt.subplots(figsize=(10, 10), subplot_kw={"projection": "polar"})
        ax.set_theta_offset(OFFSET)
        ax.set_ylim(-75, 100)
        ax.set_frame_on(False)
        ax.xaxis.grid(False)
        ax.yaxis.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])

        ax.bar(
            ANGLES[IDXS], VALUES, width=WIDTH, color=COLORS, 
            edgecolor="white", linewidth=2
        )

        add_labels(ANGLES[IDXS], VALUES, LABELS, OFFSET, ax)

        offset = 0 
        for group, size in zip(ALL_ARMIES, GROUPS_SIZE):
            # Add line below bars
            x1 = np.linspace(ANGLES[offset + PAD], ANGLES[offset + size + PAD - 1], num=50)
            ax.plot(x1, [-5] * 50, color="#333333")

            total_for_faction = sum([input.played_sectorials[army] for army in SECTORIALS_BY_ARMY[group]])

            # At the position in the Graphics, CA needs to be put into two lines
            if group == "Combined Army":
                label = f"Combined\nArmy\n({total_for_faction})"
            else:
                label = f"{group}\n({total_for_faction})"

            # Tohaa must be shifted slightly to better fit
            if group == "Tohaa":
                text_offset = -14
            else:
                text_offset = -18

            ax.text(
                np.mean(x1), text_offset, label, color="#333333", fontsize=10, 
                fontweight="bold", ha="center", va="center"
            )
            
            # Add reference lines at 20, 40, 60, and 80
            x2 = np.linspace(ANGLES[offset], ANGLES[offset + PAD - 1], num=50)
            ax.plot(x2, [10] * 50, color="#bebebe", lw=0.8)
            ax.plot(x2, [20] * 50, color="#bebebe", lw=0.8)
            ax.plot(x2, [30] * 50, color="#bebebe", lw=0.8)
            ax.plot(x2, [40] * 50, color="#bebebe", lw=0.8)
            ax.plot(x2, [50] * 50, color="#bebebe", lw=0.8)
            
            offset += size + PAD

        plt.title(f'{input.tournament_name} Faction Spread\nTotal of {sum(list(input.played_sectorials.values()))} players', y=-0.05, fontsize=14, fontweight="bold")
        filename = input.tournament_name.replace(" ", "_") + ".png"
        plt.savefig(input.output_folder / filename, dpi=300)
        plt.close("all")