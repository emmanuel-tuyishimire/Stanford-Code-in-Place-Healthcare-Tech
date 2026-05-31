from graphics import Canvas
import random

CANVAS_WIDTH = 750 
CANVAS_HEIGHT = 600

BED_WIDTH = 60
BED_HEIGHT = 100

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # 1. Draw the Floor (Background)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "lightgray")
    
    # 2. Draw the Central Nurses' Station
    canvas.create_rectangle(275, 250, 475, 350, "lightblue")
    canvas.create_text(295, 290, text="NURSES' STATION", font="Arial", font_size=16)
    
    # 3. Top Row (Beds 1-5)
    for i in range(5):
        x_position = 30 + (i * 140) 
        y_position = 50
        
        if random.choice([True, False]):
            bed_color = "salmon"      # Occupied (Red)
        else:
            bed_color = "lightgreen"  # Available (Green)
            
        draw_bed(canvas, x_position, y_position, "Bed " + str(i + 1), bed_color)
        
    # 4. Bottom Row (Beds 6-10)
    for i in range(5):
        x_position = 30 + (i * 140) 
        y_position = 450
        
        if random.choice([True, False]):
            bed_color = "salmon"
        else:
            bed_color = "lightgreen"
            
        draw_bed(canvas, x_position, y_position, "Bed " + str(i + 6), bed_color)

    # 5. Milestone 4: Critical Supplies
    # Draw a Crash Cart (Red Oval) on the left of the Nurses' Station
    canvas.create_oval(190, 275, 240, 325, "red")
    canvas.create_text(180, 335, text="Crash Cart", font="Arial", font_size=12)
    
    # Draw a Medication Cart (Blue Rectangle) on the right
    canvas.create_rectangle(510, 280, 550, 320, "royalblue")
    canvas.create_text(500, 335, text="Med Cart", font="Arial", font_size=12)


def draw_bed(canvas, x, y, bed_name, color):
    """
    A helper function that draws a single bed with its occupancy color.
    """
    canvas.create_rectangle(x, y, x + BED_WIDTH, y + BED_HEIGHT, color)
    
    # Draw a little pillow at the top of the bed
    canvas.create_rectangle(x + 10, y + 10, x + BED_WIDTH - 10, y + 35, "white")
    
    # Write the bed number below the bed
    canvas.create_text(x + 10, y + BED_HEIGHT + 10, text=bed_name, font="Arial", font_size=12)


if __name__ == '__main__':
    main()