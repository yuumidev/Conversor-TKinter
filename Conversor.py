import tkinter as tk

def conversor():
    try:
        centimetros = float(entry_centimetros.get())

        metros = centimetros / 100

        label_resul.config(text=f'{centimetros} centímetros é igual a {metros} metros.')

    except ValueError:

        label_resul.config(text='Número inválido. Digite um número válido.')

janela = tk.Tk()
janela.title('Conversor de Medidas ^^')
janela.configure(background='#1A4D2E')


label_centimetros = tk.Label(janela, text='Centimetros', background='#1A4D2E', foreground='#E8DFCA')
label_centimetros.grid(row=0, column=0, padx=5, pady=5)

entry_centimetros = tk.Entry(janela, bg='#4F6F52', fg='#E8DFCA')
entry_centimetros.grid(row=0, column=1, padx=5, pady=5)

botao = tk.Button(janela, text='Converter', command=conversor, background='#4F6F52', foreground='#E8DFCA')
botao.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

label_resul = tk.Label(janela, text='', background='#1A4D2E', foreground='#E8DFCA')
label_resul.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

janela.mainloop()