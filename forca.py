import string
from tkinter import *
from PIL import ImageTk, Image
from random import choice


class Forca(Tk):
    def __init__(self):
        Tk.__init__(self)
        x = 600
        y = 600
        self.geometry(f"{x}x{y}+"
                      f"{int(self.winfo_screenwidth() / 2 - x + 1800)}+{int(self.winfo_screenheight() / 2 - y / 2)}")
        self.title("Forca")
        self.iconphoto(True, PhotoImage(file="Da.png"))

        forca_frame = LabelFrame(self, text="Forca", width=500, height=500)
        forca_frame.pack()
        # Imagem inicial da forca
        self.img = ImageTk.PhotoImage(Image.open("forca_inicio.png"))
        self.img_forca = Label(forca_frame, image=self.img)
        self.img_forca.pack()

        # Palavras para jogar
        self.palavras = ["banana", "carro", "morango", "sofa", "carruagem", "casa"]

        # Iniciar o jogo
        self.frame_btn_iniciar = Frame(self)
        self.frame_btn_iniciar.pack()
        self.botao_iniciar = Button(self.frame_btn_iniciar, text="Iniciar o jogo", command=self.iniciar)
        self.botao_iniciar.pack(pady=20)

        # Posiciona as letras para escolher
        self.letrastop = Frame(self)
        self.letrasbot = Frame(self)
        self.letrastop.pack()
        self.letrasbot.pack()

        # Contador para os erros
        self.erros = 0
        # lista para armazenar os botões das letras
        self.btn = []

    def iniciar(self):
        # Destroi o botão iniciar
        self.botao_iniciar.destroy()
        # Escolhe uma palavra
        palavra = choice(self.palavras)
        # Cria a palavra com os traços do tomanho da palavra
        palavra_escondida = list("_" * len(palavra))
        # Exibe os traços
        palavra_traco = Label(self.frame_btn_iniciar, text=palavra_escondida, font=20)
        palavra_traco.pack(pady=20)

        # Alfabeto para adicionar no botões
        alfabeto = list(string.ascii_lowercase.upper())
        for i, l in enumerate(alfabeto):
            # Separa a quantidade de botões em cada linha parando no M
            if l <= "M":
                # Cria os botões e armazena em uma lista para poder alterar deopis
                # Botões de A até M
                self.btn.append(Button(self.letrastop, text=l, font=20, command=lambda letra=l: verifica_letra(letra)))
                self.btn[i].pack(side=LEFT, pady=2, padx=2)
            else:
                # Cria os botões e armazena em uma lista para poder alterar deopis
                # Botões de N até Z
                self.btn.append(Button(self.letrasbot, text=l, font=20, command=lambda letra=l: verifica_letra(letra)))
                self.btn[i].pack(side=LEFT, pady=2, padx=2)

        # Sempre que clicar em um botão, irá verificar se a letra escolhida está contida na palavra
        def verifica_letra(letra):
            # Faz uma iteração por todos os botões para poder encontrar e desabilitar a lerta que já foi escolhida
            for i, le in enumerate(self.btn):
                # Usando a função cget("text") podemos verificar o texto existente no botão
                # para checar se existe na palavra
                if le.cget("text") == letra:
                    # Sempre que uma letra for escolhida, ela será desabilitada
                    self.btn[i]["state"] = DISABLED
                    # Se a lerta estiver na palavra...
                    if letra in palavra.upper():
                        # pinta ela de verde
                        self.btn[i]["background"] = "#c3fcad"
                        # Faz uma iteração pela palavra se sempre que encontrar a letra escolhida, faz a alteração
                        # na palavra escondida e exibe na posição correta.
                        for i, l in enumerate(palavra.upper()):
                            if letra == l:
                                palavra_escondida[i] = l
                        # Atualiza a palavra
                        palavra_traco.config(text=" ".join(palavra_escondida))

                        # Se as palavras forem iguais...
                        if "".join(palavra_escondida) == palavra.upper():
                            # Destrói todos os botões
                            for b in self.btn:
                                b.destroy()

                            # Exibe uma mensagem de parabéns
                            msg_vitoria = Label(self.letrastop, text=f"Parabéns, você acertou a palavra!!", font=25)
                            msg_vitoria.pack()
                            # Cria um botão para jogar novamente
                            Button(self.letrasbot, text="Jogar Novamente", command=self.jogar_novamente, font=20)\
                                .pack(side=LEFT, padx=(0, 5), pady=5)
                            # Cria um botão para sair do jogo
                            Button(self.letrasbot, text="Sair", command=self.quit, font=20)\
                                .pack(side=LEFT, pady=5)
                    else: # Mas se a letra não for escolhida
                        # Pinta de vermelho
                        self.btn[i]["background"] = "#ffb9ae"
                        # Soma quantos palpites foram dados
                        self.erros += 1
                        # Atualiza a imagem de acordo com a quantidade de erros
                        if self.erros == 1:
                            self.img = ImageTk.PhotoImage(Image.open("erro1.png"))
                            self.img_forca.config(image=self.img)
                        if self.erros == 2:
                            self.img = ImageTk.PhotoImage(Image.open("erro2.png"))
                            self.img_forca.config(image=self.img)
                        if self.erros == 3:
                            self.img = ImageTk.PhotoImage(Image.open("erro3.png"))
                            self.img_forca.config(image=self.img)
                        if self.erros == 4:
                            self.img = ImageTk.PhotoImage(Image.open("erro4.png"))
                            self.img_forca.config(image=self.img)
                        if self.erros == 5:
                            self.img = ImageTk.PhotoImage(Image.open("erro5.png"))
                            self.img_forca.config(image=self.img)
                        if self.erros == 6:
                            self.img = ImageTk.PhotoImage(Image.open("erro6.png"))
                            self.img_forca.config(image=self.img)
                        if self.erros == 7:
                            self.img = ImageTk.PhotoImage(Image.open("fim.png"))
                            self.img_forca.config(image=self.img)
                            # Quando der 7 erros, uma mensagem aparece dizendo que a pessoa não consegui acertar
                            # e mostra qual era a palavra correta
                            palavra_traco.config(text=f"Você não conseguiu adivinhar, a palavra era {palavra.upper()}")
                            # E desabilita todas as Letras.
                            for le in self.btn:
                                le.destroy()
                            # Cria um botão para jogar novamente
                            Button(self.letrasbot, text="Jogar Novamente", command=self.jogar_novamente, font=20) \
                                .pack(side=LEFT, padx=(0, 5), pady=5)
                            # Cria um botão para sair do jogo
                            Button(self.letrasbot, text="Sair", command=self.quit, font=20) \
                                .pack(side=LEFT, pady=5)

    def jogar_novamente(self):
        self.destroy()
        Forca()


if __name__ == '__main__':
    app = Forca()
    app.mainloop()
