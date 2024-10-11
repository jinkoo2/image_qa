def main():
    import tkinter as tk

    # Create the main application window
    root = tk.Tk()

    # Set window title
    root.title("Hello World App")

    # Set window size (optional)
    root.geometry("300x200")

    # Create a label widget with "Hello World" text
    label = tk.Label(root, text="Hello, World!", font=("Arial", 24))

    # Place the label widget in the window
    label.pack(pady=50)  # pady adds padding above and below the label

    # Run the Tkinter event loop
    root.mainloop()