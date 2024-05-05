#my_frame.py    22Oct2022  crs, organization
import tkinter as tk


root = tk.Tk()
# Start with main frame
main_frame = tk.Frame(root)
main_frame.pack(expand=tk.Y, fill=tk.BOTH)
# Make sub-sections
row_one_frame = tk.Frame(main_frame)
row_one_frame.pack(side=tk.TOP)
row_two_frame = tk.Frame(main_frame)
row_two_frame.pack(side=tk.TOP)
row_three_frame = tk.Frame(main_frame)
                    # Demonstrate expansion/fill
                    # in row three
row_three_frame.pack(side=tk.TOP,
                     expand=tk.Y, fill=tk.BOTH)

# place one label in first row
label_1_1 = tk.Label(row_one_frame, text="Label_1_1")
label_1_1.pack(side=tk.TOP)

# place two labels in second row
label_2_1 = tk.Label(row_two_frame, text="Label_2_1")
label_2_1.pack(side=tk.LEFT)
label_2_2 = tk.Label(row_two_frame, text="Label_2_1")
label_2_2.pack(side=tk.LEFT)

# place three labels in third row
label_3_1 = tk.Label(row_three_frame, text="Label_3_1")
label_3_1.pack(side=tk.LEFT, expand=tk.Y, fill=tk.BOTH)
label_3_2 = tk.Label(row_three_frame, text="Label_3_2")
label_3_2.pack(side=tk.LEFT, expand=tk.Y, fill=tk.BOTH)
label_3_3 = tk.Label(row_three_frame, text="Label_3_3")
label_3_3.pack(side=tk.RIGHT, expand=tk.Y, fill=tk.BOTH)

# keep the window displaying
root.mainloop()
