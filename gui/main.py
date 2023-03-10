from pathlib import Path
import os
import tkinter as tk
import tkinter.filedialog as fd
import subprocess
import sys


def run_telomere():
    current_dir = Path(__file__).resolve().parent.parent
    if "win" in sys.platform:
        r_install_path = os.getenv("R_HOME", "")
        if not r_install_path:
            print("R needs to be installed first")
            exit()
        rscript_path = Path(r_install_path) / "bin" / "Rscript"      
        command_list = [
            str(rscript_path),
            "--vanilla",
            str(current_dir / "Telomere-Analyzer" / "nanotel.R"),
        ]
    else:
        command_list = [
            "Rscript",
            "--vanilla",
            str(current_dir / "Telomere-Analyzer" / "nanotel-multicore-10workers.R"),
        ]

    command_list.extend([input_dir.get(), output_dir.get(), file_type.get()])
    process = subprocess.Popen(
        command_list,
        stdout=subprocess.PIPE,
    )
    for c in iter(lambda: process.stdout.read(1), b""):
        sys.stdout.buffer.write(c)


def get_input():
    input_dir.set(fd.askdirectory())
    window.title(f"Telomere-Analyzer - {input_dir.get()}")


def get_output():
    output_dir.set(fd.askdirectory())


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Telomere-Analyzer")

    window.rowconfigure(0, minsize=100, weight=1)
    window.columnconfigure(1, weight=2)
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

    ent_input = tk.Entry(frm_entries, textvariable=input_dir, width=40)
    ent_output = tk.Entry(frm_entries, textvariable=output_dir, width=40)

    file_type = tk.StringVar()
    file_type.set("Fastq")
    fastq_chkbtn = tk.Radiobutton(
        frm_entries, text="Fastq", value="Fastq", variable=file_type
    )
    fasta_chkbtn = tk.Radiobutton(
        frm_entries, text="Fasta", value="Fasta", variable=file_type
    )
    fastq_chkbtn.grid(row=2, column=0)
    fasta_chkbtn.grid(row=2, column=1)

    ent_input.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="ew")
    ent_output.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="ew")

    frm_labels.grid(row=0, column=0, sticky="nsew")
    frm_entries.grid(row=0, column=1, sticky="nsew")
    frm_buttons.grid(row=0, column=2, sticky="nsew")

    telomere_btn = tk.Button(window, text="Run Telomere Analyzer", command=run_telomere)
    telomere_btn.grid(row=1, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

    window.mainloop()
