import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from figures import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("YLAB Homework №3")

        # Main window geometry
        self.width = 450
        self.height = 250
        self.x = int(self.winfo_screenwidth() / 2 - self.width / 2)
        self.y = int(self.winfo_screenheight() / 2 - self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.resizable(width=False, height=False)

        # Layout
        for c in range(4):
            self.columnconfigure(index=c, weight=1)
        for r in range(6):
            self.rowconfigure(index=r, weight=1)

        # Style
        ttk.Style().configure("TLabel", padding=(0, 5, 0, 5), font="roboto 12")
        ttk.Style().configure("TButton", padding=(0, 5, 0, 5), font="roboto 12")
        ttk.Style().configure("TEnry", padding=(0, 5, 0, 5), font="roboto 12")

        # Start with the main window
        self.show_main()

    def validate(self, value):
        """Check if the value is a positive integer"""

        if (isinstance(value, int) or isinstance(value, float)) and value > 0:
            return True
        else:
            raise ValueError

    def show_main(self):
        """Display the main window"""

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Main window layout
        self.title_label = ttk.Label(self, text="Select figure", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.btn_triangle = ttk.Button(self, text="Triangle", command=self.show_triangle)
        self.btn_triangle.grid(row=1, column=0)

        self.btn_parallelogram = ttk.Button(self, text="Parallelogram", command=self.show_parallelogram)
        self.btn_parallelogram.grid(row=1, column=1)

        self.btn_square = ttk.Button(self, text="Square", command=self.show_square)
        self.btn_square.grid(row=1, column=2)

        self.btn_rhombus = ttk.Button(self, text="Rhombus", command=self.show_rhombus)
        self.btn_rhombus.grid(row=1, column=3)

        self.btn_rectangle = ttk.Button(self, text="Rectangle", command=self.show_rectangle)
        self.btn_rectangle.grid(row=2, column=0)

        self.btn_trapezium = ttk.Button(self, text="Trapezium", command=self.show_trapezium)
        self.btn_trapezium.grid(row=2, column=1)

        self.btn_circle = ttk.Button(self, text="Circle", command=self.show_circle)
        self.btn_circle.grid(row=2, column=2)

        self.btn_pyramid = ttk.Button(self, text="Pyramid", command=self.show_pyramid)
        self.btn_pyramid.grid(row=2, column=3)

        self.btn_cone = ttk.Button(self, text="Cone", command=self.show_cone)
        self.btn_cone.grid(row=3, column=0)

        self.btn_parallelepiped = ttk.Button(self, text="Parallelepiped", command=self.show_parallelepiped)
        self.btn_parallelepiped.grid(row=3, column=1)

        self.btn_cube = ttk.Button(self, text="Cube", command=self.show_cube)
        self.btn_cube.grid(row=3, column=2)

        self.btn_sphere = ttk.Button(self, text="Sphere", command=self.show_sphere)
        self.btn_sphere.grid(row=3, column=3)

        self.btn_cylinder = ttk.Button(self, text="Cylinder", command=self.show_cylinder)
        self.btn_cylinder.grid(row=4, column=0)

    def show_triangle(self):
        """Display the triangle window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get(), self.side_b.get(), self.side_c.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Triangle(self.side_a.get(), self.side_b.get(), self.side_c.get())

                # Get the results of class methods
                self.perimeter = round(self.figure.calc_perimeter(), 2)
                self.area = round(self.figure.calc_area(), 2)
                self.height = round(self.figure.calc_height(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Perimeter: {self.perimeter}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Height: {self.height}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Triangle", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.side_b = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side B:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_b)
        self.side_a_entry.grid(row=2, column=1, sticky="W")

        self.side_c = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side C:")
        self.title_label.grid(row=3, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_c)
        self.side_a_entry.grid(row=3, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_parallelogram(self):
        """Display the parallelogram window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get(), self.side_b.get(), self.height.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Parallelogram(self.side_a.get(), self.side_b.get(), self.height.get())

                # Get the results of class methods
                self.perimeter = round(self.figure.calc_perimeter(), 2)
                self.area = round(self.figure.calc_area(), 2)
                self.angle = round(self.figure.calc_angle(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Perimeter: {self.perimeter}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Angle: {self.angle}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Parallelogram", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.side_b = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side B:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.side_b_entry = ttk.Entry(self, textvariable=self.side_b)
        self.side_b_entry.grid(row=2, column=1, sticky="W")

        self.height = tk.IntVar()
        self.title_label = ttk.Label(self, text="Height:")
        self.title_label.grid(row=3, column=0, sticky="W")
        self.height_entry = ttk.Entry(self, textvariable=self.height)
        self.height_entry.grid(row=3, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_square(self):
        """Display the square window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Square(self.side_a.get())

                # Get the results of class methods
                self.perimeter = round(self.figure.calc_perimeter(), 2)
                self.area = round(self.figure.calc_area(), 2)
                self.incircle_radius = round(self.figure.calc_incircle_radius(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Perimeter: {self.perimeter}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Incircle radius: {self.incircle_radius}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Square", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_rhombus(self):
        """Display the rhombus window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get(), self.height.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Rhombus(self.side_a.get(), self.height.get())

                # Get the results of class methods
                self.perimeter = round(self.figure.calc_perimeter(), 2)
                self.area = round(self.figure.calc_area(), 2)
                self.incircle_radius = round(self.figure.calc_incircle_radius(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Perimeter: {self.perimeter}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Incircle radius: {self.incircle_radius}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Rhombus", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.height = tk.IntVar()
        self.title_label = ttk.Label(self, text="Height:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.height_entry = ttk.Entry(self, textvariable=self.height)
        self.height_entry.grid(row=2, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_rectangle(self):
        """Display the rectangle window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get(), self.side_b.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Rectangle(self.side_a.get(), self.side_b.get())

                # Get the results of class methods
                self.perimeter = round(self.figure.calc_perimeter(), 2)
                self.area = round(self.figure.calc_area(), 2)
                self.diag_len = round(self.figure.calc_diag_len(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Perimeter: {self.perimeter}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Diagonal: {self.diag_len}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Rectangle", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.side_b = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side B:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.side_b_entry = ttk.Entry(self, textvariable=self.side_b)
        self.side_b_entry.grid(row=2, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_trapezium(self):
        """Display the trapezium window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get(), self.side_b.get(), self.side_c.get(), self.side_d.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Trapezium(self.side_a.get(), self.side_b.get(), self.side_c.get(), self.side_d.get())

                # Get the results of class methods
                self.perimeter = round(self.figure.calc_perimeter(), 2)
                self.area = round(self.figure.calc_area(), 2)
                self.height = round(self.figure.calc_height(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Perimeter: {self.perimeter}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Height: {self.height}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Trapezium", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.side_b = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side B:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.side_b_entry = ttk.Entry(self, textvariable=self.side_b)
        self.side_b_entry.grid(row=2, column=1, sticky="W")

        self.side_c = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side C:")
        self.title_label.grid(row=3, column=0, sticky="W")
        self.side_c_entry = ttk.Entry(self, textvariable=self.side_c)
        self.side_c_entry.grid(row=3, column=1, sticky="W")

        self.side_d = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side D:")
        self.title_label.grid(row=4, column=0, sticky="W")
        self.side_d_entry = ttk.Entry(self, textvariable=self.side_d)
        self.side_d_entry.grid(row=4, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_circle(self):
        """Display the circle window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.radius.get(), self.angle.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Circle(self.radius.get(), self.angle.get())

                # Get the results of class methods
                self.area = round(self.figure.calc_area(), 2)
                self.diameter = round(self.figure.calc_diameter(), 2)
                self.arc = round(self.figure.calc_arc_len(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Diameter: {self.diameter}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Arc length: {self.arc}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Circle", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.radius = tk.IntVar()
        self.title_label = ttk.Label(self, text="Radius:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.radius_entry = ttk.Entry(self, textvariable=self.radius)
        self.radius_entry.grid(row=1, column=1, sticky="W")

        self.angle = tk.IntVar()
        self.title_label = ttk.Label(self, text="Angle:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.angle_entry = ttk.Entry(self, textvariable=self.angle)
        self.angle_entry.grid(row=2, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_pyramid(self):
        """Display the pyramid window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get(), self.height.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Pyramid(self.side_a.get(), self.height.get())

                # Get the results of class methods
                self.area = round(self.figure.calc_area(), 2)
                self.volume = round(self.figure.calc_volume(), 2)
                self.inshpere_radius = round(self.figure.calc_insphere_radius(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Volume: {self.volume}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Inscribed sphere radius: {self.inshpere_radius}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Pyramid", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.height = tk.IntVar()
        self.title_label = ttk.Label(self, text="Height:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.height_entry = ttk.Entry(self, textvariable=self.height)
        self.height_entry.grid(row=2, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_cone(self):
        """Display the cone window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.radius.get(), self.height.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Cone(self.radius.get(), self.height.get())

                # Get the results of class methods
                self.area = round(self.figure.calc_area(), 2)
                self.volume = round(self.figure.calc_volume(), 2)
                self.slant = round(self.figure.calc_slant(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Volume: {self.volume}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Slant: {self.slant}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Cone", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.radius = tk.IntVar()
        self.title_label = ttk.Label(self, text="Radius")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.radius_entry = ttk.Entry(self, textvariable=self.radius)
        self.radius_entry.grid(row=1, column=1, sticky="W")

        self.height = tk.IntVar()
        self.title_label = ttk.Label(self, text="Height:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.height_entry = ttk.Entry(self, textvariable=self.height)
        self.height_entry.grid(row=2, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_parallelepiped(self):
        """Display the parallelepiped window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get(), self.side_b.get(), self.side_c.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Parallelepiped(self.side_a.get(), self.side_b.get(), self.side_c.get())

                # Get the results of class methods
                self.area = round(self.figure.calc_area(), 2)
                self.volume = round(self.figure.calc_volume(), 2)
                self.diag_len = round(self.figure.calc_diag_len(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Volume: {self.volume}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Diagonal: {self.diag_len}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Parallelepiped", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.side_b = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side B:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.side_b_entry = ttk.Entry(self, textvariable=self.side_b)
        self.side_b_entry.grid(row=2, column=1, sticky="W")

        self.side_c = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side C:")
        self.title_label.grid(row=3, column=0, sticky="W")
        self.side_c_entry = ttk.Entry(self, textvariable=self.side_c)
        self.side_c_entry.grid(row=3, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_cube(self):
        """Display the cube window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.side_a.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Cube(self.side_a.get())

                # Get the results of class methods
                self.area = round(self.figure.calc_area(), 2)
                self.volume = round(self.figure.calc_volume(), 2)
                self.diag_len = round(self.figure.calc_diag_len(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Volume: {self.volume}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Diagonal: {self.diag_len}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Cube", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.side_a = tk.IntVar()
        self.title_label = ttk.Label(self, text="Side A:")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.side_a_entry = ttk.Entry(self, textvariable=self.side_a)
        self.side_a_entry.grid(row=1, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_sphere(self):
        """Display the sphere window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.radius.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Sphere(self.radius.get())

                # Get the results of class methods
                self.area = round(self.figure.calc_area(), 2)
                self.volume = round(self.figure.calc_volume(), 2)
                self.diameter = round(self.figure.calc_diameter(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Volume: {self.volume}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Diameter: {self.diameter}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Sphere", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.radius = tk.IntVar()
        self.title_label = ttk.Label(self, text="Radius")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.radius_entry = ttk.Entry(self, textvariable=self.radius)
        self.radius_entry.grid(row=1, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")

    def show_cylinder(self):
        """Display the cylinder window"""

        def click_calculate():
            """Calculate button action"""

            try:
                # The value has to be a positive integer
                for var in [self.radius.get(), self.height.get()]:
                    self.validate(var)

                # Create class instance
                self.figure = Cylinder(self.radius.get(), self.height.get())

                # Get the results of class methods
                self.area = round(self.figure.calc_area(), 2)
                self.volume = round(self.figure.calc_volume(), 2)
                self.side_area = round(self.figure.calc_side_area(), 2)

                # Result layout
                self.title_label = ttk.Label(self, text=f"Area: {self.area}")
                self.title_label.grid(row=1, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Volume: {self.volume}")
                self.title_label.grid(row=2, column=3, columnspan=2, sticky="W")

                self.title_label = ttk.Label(self, text=f"Side area: {self.side_area}")
                self.title_label.grid(row=3, column=3, columnspan=2, sticky="W")
            except:
                messagebox.showerror("Error", "Please enter a valid value")

        # Remove all other windows
        for i in self.winfo_children():
            i.destroy()

        # Figure window layout
        self.title_label = ttk.Label(self, text="Cylinder", font="roboto 20")
        self.title_label.grid(row=0, column=0, columnspan=5, sticky="S")

        self.radius = tk.IntVar()
        self.title_label = ttk.Label(self, text="Radius")
        self.title_label.grid(row=1, column=0, sticky="W")
        self.radius_entry = ttk.Entry(self, textvariable=self.radius)
        self.radius_entry.grid(row=1, column=1, sticky="W")

        self.height = tk.IntVar()
        self.title_label = ttk.Label(self, text="Height:")
        self.title_label.grid(row=2, column=0, sticky="W")
        self.height_entry = ttk.Entry(self, textvariable=self.height)
        self.height_entry.grid(row=2, column=1, sticky="W")

        self.btn_calc = ttk.Button(self, text="Calculate", command=click_calculate)
        self.btn_calc.grid(row=5, column=0, sticky="W")

        self.btn_back = ttk.Button(self, text="Back", command=self.show_main)
        self.btn_back.grid(row=5, column=4, sticky="E")


if __name__ == "__main__":
    app = App()
    app.mainloop()