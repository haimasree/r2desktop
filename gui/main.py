import tkinter as tk
import tkinter.filedialog as fd

# def increase():
#     value=int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"

# def decrease():
#     value=int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"

# window = tk.Tk()
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")

# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)

# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")

# window.mainloop()

# def fahrenheit_to_celsius():
#     """Convert the value for Fahrenheit to Celsius and insert the
#     result into lbl_result.
#     """
#     fahrenheit = ent_temperature.get()
#     celsius = (5 / 9) * (float(fahrenheit) - 32)
#     lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# window = tk.Tk()
# window.title("Temparature converter")
# window.resizable(width=False, height=False)
# frm_entry = tk.Frame(master=window)
# ent_temperature = tk.Entry(master=frm_entry, width=10)
# lbl_temp = tk.Label(master=frm_entry, text="F")
# ent_temperature.grid(row=0, column=0, sticky="e")
# lbl_temp.grid(row=0, column=1, sticky="w")

# btn_convert = tk.Button(
#     master=window,
#     text="\N{RIGHTWARDS BLACK ARROW}",
#     command=fahrenheit_to_celsius
# )
# lbl_result = tk.Label(master=window, text="C")

# frm_entry.grid(row=0, column=0, padx=10)
# btn_convert.grid(row=0, column=1, pady=10)
# lbl_result.grid(row=0, column=2, padx=10)

# window.mainloop()
def run_telomere():
    print("Run Telomere analyzer")


def get_input():
    input_dir.set(fd.askdirectory())
    window.title(f"Telomere-Analyzer - {input_dir}")


def get_output():
    output_dir.set(fd.askdirectory())
    window.title(f"Telomere-Analyzer - {output_dir}")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Telomere-Analyzer")

    window.rowconfigure(0, minsize=150, weight=1)
    window.columnconfigure(1, minsize=150, weight=1)

    input_dir = tk.StringVar()
    output_dir = tk.StringVar()

    frm_entries = tk.Frame(window, relief=tk.RAISED, bd=2)
    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    frm_labels = tk.Frame(window, relief=tk.RAISED, bd=2)

    btn_open = tk.Button(frm_buttons, text="Open", command=get_input)
    btn_save = tk.Button(frm_buttons, text="Select", command=get_output)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    lbl_input = tk.Label(frm_labels, text="Input directory", padx=5, pady=5)
    lbl_output = tk.Label(frm_labels, text="Output directory", padx=5, pady=5)
    lbl_filetype = tk.Label(frm_labels, text="Choose file type", padx=5)

    lbl_input.grid(row=0, column=0)
    lbl_output.grid(row=1, column=0)
    lbl_filetype.grid(row=2, column=0)

    ent_input = tk.Entry(frm_entries, textvariable=input_dir)
    ent_output = tk.Entry(frm_entries, textvariable=output_dir)

    file_type = tk.StringVar()
    file_type.set("Fasta")
    fasta_chkbtn = tk.Radiobutton(
        frm_entries, text="Fasta", value="Fasta", variable=file_type
    )
    fastq_chkbtn = tk.Radiobutton(
        frm_entries, text="Fastq", value="Fastq", variable=file_type
    )
    fasta_chkbtn.grid(row=2, column=0)
    fastq_chkbtn.grid(row=2, column=1)

    ent_input.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
    ent_output.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

    frm_labels.grid(row=0, column=0, sticky="nsew")
    frm_entries.grid(row=0, column=1, sticky="nsew")
    frm_buttons.grid(row=0, column=2, sticky="nsew")

    telomere_btn = tk.Button(window, text="Run Telomere Analyzer", command=run_telomere)
    telomere_btn.grid(row=1, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

    window.mainloop()
