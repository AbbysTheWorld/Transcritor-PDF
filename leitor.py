import PyPDF2 as pyf
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('Sistema PDF')

        self.arquivo = ''
        self.pastaSalvar = ''

        self.sistemaInfo = customtkinter.CTkLabel(self,text='Esse é um sistema onde o usuario escolhe um arquivo pdf e esse sistema \n Retorna um arquivo com a extensão .txt com todo o texto referente a esse pdf',font=customtkinter.CTkFont(family='arial',size=15,weight='bold'))
        self.sistemaInfo.pack(padx=10,pady=10)

        self.buttonArquivo = customtkinter.CTkButton(self,width=200,text='Escolher arquivo pdf',fg_color='green',hover_color='dark green',command=self.escolher_arquivoPdf,height=40)
        self.buttonArquivo.pack(padx=10,pady=10)

        self.buttonSave = customtkinter.CTkButton(self,width=200,text='Escolha a pasta que deseja salvar o arquivo .txt',fg_color='green',hover_color='dark green',command=self.escolher_pasta,height=40)
        self.buttonSave.pack(padx=10,pady=10)

        self.arquivoSelecionado = customtkinter.CTkLabel(self,text='O arquivo selecionado foi: ...',font=customtkinter.CTkFont(family='arial',size=15,weight='bold'))
        self.arquivoSelecionado.pack(padx=10,pady=10)

        self.pastaSelecionada = customtkinter.CTkLabel(self,text='A pasta selecionado foi: ...',font=customtkinter.CTkFont(family='arial',size=15,weight='bold'))
        self.pastaSelecionada.pack(padx=10,pady=10)

        self.buttonStart = customtkinter.CTkButton(self,width=200,text='Iniciar Sistema',fg_color='blue',hover_color='dark blue',command=self.iniciar_sistema,height=40)
        self.buttonStart.pack(padx=10,pady=10)

        self.Error = customtkinter.CTkLabel(self,text='',font=customtkinter.CTkFont(family='arial',size=20,weight='bold'),text_color='red')
        self.Error.pack(padx=10,pady=10)

    def escolher_arquivoPdf(self):
        file = customtkinter.filedialog.askopenfile()
        if file:
            filename = file.name.split('/')
            filename = filename[len(filename)-1]
            if filename.endswith('.pdf'):
                self.arquivoSelecionado.configure(text=f'O arquivo selecionado foi: {filename}')
                self.arquivo = file.name
            else:
                self.arquivoSelecionado.configure(text='O arquivo selecionado não tem extensão .pdf! \n Selecione um arquivo pdf!')
                self.arquivo = ''
        else:
            self.arquivoSelecionado.configure(text='Nenhum pdf selecionado.')
            self.arquivo = ''

    def escolher_pasta(self):
        pasta = customtkinter.filedialog.askdirectory()
        if pasta:
            self.pastaSalvar = pasta
            self.pastaSelecionada.configure(text=f'A pasta selecionado foi: {pasta}')
        else:
            self.pastaSalvar = ''
            self.pastaSelecionada.configure(text=f'Nenhuma pasta selecionada!')

    def iniciar_sistema(self):
        try:
            self.Error.configure(text='',text_color='red')
            if self.arquivo != '' and self.pastaSalvar != '':
                self.nome_arquivo = self.arquivo
                self.arquivo_pdf = pyf.PdfReader(self.nome_arquivo)
                self.filename = self.nome_arquivo.split('/')
                self.filename = self.filename[len(self.filename)-1]

                for pagina in self.arquivo_pdf.pages:
                    with open(f'{self.pastaSalvar}/Texto_Completo(PDF_{self.filename}).txt','a') as text:
                        text.write(pagina.extract_text())

                self.Error.configure(text='Arquivo .txt criado com sucesso!',text_color='green')
            else:
                self.Error.configure(text='ERROR: Preencha os dois campos acima para prosseguir!',text_color='red')
        except:
            self.Error.configure(text='ERROR: O arquivo pdf não é compatível com nosso sistema... \n uma versão incompleta foi gerada no lugar!',text_color='red')

app = App()
app.mainloop()
