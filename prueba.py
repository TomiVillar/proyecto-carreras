import tkinter as tk

def ventana_alta():
    # Ventana
    ventana = tk.Tk()
    ventana.title("Formulario de contacto para ISAUI")
    ventana.geometry("1366x768")
    ventana.configure(bg="grey")
    ventana.resizable(False, False)

    variable = tk.StringVar(value="-1")  # Valor predeterminado -1

    # Marco
    frame = tk.LabelFrame(ventana, text="Seleccione la carrera", bg="lightgrey", font=('Calibri', 20), borderwidth=5)
    frame.grid(row=0, column=0, padx=60, pady=50)

    # Radio buttons
    btn_software = tk.Radiobutton(frame, text="Desarrollo de Software", variable=variable, value="1", bg="lightgrey", font=('Calibri', 13))
    btn_software.grid(row=1, column=3, padx=10, pady=10)
    
    btn_enfermeria = tk.Radiobutton(frame, text="Enfermería", variable=variable, value="2", bg="lightgrey", font=('Calibri', 13))
    btn_enfermeria.grid(row=1, column=4, padx=10, pady=10)
    
    btn_disenio = tk.Radiobutton(frame, text="Diseño de Espacios", variable=variable, value="3", bg="lightgrey", font=('Calibri', 13))
    btn_disenio.grid(row=1, column=5, padx=10, pady=10)
    
    btn_guia = tk.Radiobutton(frame, text="Guía en Turismo", variable=variable, value="5", bg="lightgrey", font=('Calibri', 13))
    btn_guia.grid(row=1, column=6, padx=10, pady=10)
    
    btn_guia_turismo_hoteleria = tk.Radiobutton(frame, text="Guía de Turismo y Hotelería", variable=variable, value="6", bg="lightgrey", font=('Calibri', 13))
    btn_guia_turismo_hoteleria.grid(row=1, column=7, padx=10, pady=10)
    
    btn_trekking = tk.Radiobutton(frame, text="Guía de Trekking y Guía de Montaña", variable=variable, value="4", bg="lightgrey", font=('Calibri', 13))
    btn_trekking.grid(row=1, column=8, padx=10, pady=10)

    ventana.mainloop()

ventana_alta()