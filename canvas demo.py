from tkinter import *

class canvasDemo:
    def __init__(self):
        # Create main window
        window = Tk()
        window.title("Canvas Demo")

        # Create a canvas for drawing shapes
        self.canvas = Canvas(window, width=400, height=300, background="white")
        self.canvas.pack(pady=10)

        # Frame for buttons
        frame = Frame(window)
        frame.pack()

        # Buttons for different shapes
        btRectangle = Button(frame, text="Rectangle", command=self.displayRect)
        btOval = Button(frame, text="Oval", command=self.displayOval)
        btPolygon = Button(frame, text="Polygon", command=self.displayPolygon)
        btArc = Button(frame, text="Arc", command=self.displayArc)
        btLine = Button(frame, text="Line", command=self.displayLine)
        btString = Button(frame, text="String", command=self.displayString)
        btClear = Button(frame, text="Clear", command=self.displayClear)

        # Arrange buttons in grid
        btRectangle.grid(row=1, column=0, padx=5, pady=5)
        btOval.grid(row=1, column=1, padx=5, pady=5)
        btPolygon.grid(row=1, column=2, padx=5, pady=5)
        btArc.grid(row=1, column=3, padx=5, pady=5)
        btLine.grid(row=1, column=4, padx=5, pady=5)
        btClear.grid(row=1, column=5, padx=5, pady=5)
        btString.grid(row=1, column=6, padx=5, pady=5)

        # Start Tkinter main loop
        window.mainloop()

    # Draw a rectangle
    def displayRect(self):
        self.canvas.create_rectangle(50, 50, 350, 200, fill="lightblue", outline="black", width=2, tag="Rectangle")

    # Draw an oval
    def displayOval(self):
        self.canvas.create_oval(50, 50, 350, 200, fill="red", outline="black", width=2, tag="Oval")

    # Draw a polygon
    def displayPolygon(self):
        # x,y pairs for triangle
        self.canvas.create_polygon(200, 50, 350, 200, 50, 200, fill="green", outline="black", width=2, tag="Polygon")

    # Draw an arc
    def displayArc(self):
        # Proper bounding box and angle for visible arc
        self.canvas.create_arc(50, 50, 350, 250, start=0, extent=120, fill="blue", outline="black", width=2, style=ARC, tag="Arc")

    # Draw a line
    def displayLine(self):
        self.canvas.create_line(50, 50, 350, 200, fill="purple", width=2, tag="Line")

    # Draw text
    def displayString(self):
        self.canvas.create_text(200, 150, text="COMING SOON", font=("Arial", 24, "bold"), fill="black", tag="String")

    # Clear all shapes
    def displayClear(self):
        self.canvas.delete("Rectangle", "Oval", "Polygon", "Arc", "Line", "String")


# Run the application
canvasDemo()
