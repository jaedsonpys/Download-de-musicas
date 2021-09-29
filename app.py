from download import PyTube

def download_media(urls):
    for url in urls:
        # Obtendo informações do vídeo/música
        download = PyTube()

        info_media = download.get_info(url[0])

        if info_media is False:
            print('\033[31mOcorreu um erro ao obter informações sobre o vídeo. Verifique a URL.\033[m\n')
            return False

        print('\n\033[32mInformações:\033[m\n')
        print(f'Título: {info_media["title"]}')
        print(f'Tamanho: {info_media["size"]}')

        print('\n\033[47;30m Baixando... \033[m')

        if url[1]:
            response = download.download_audio(url[0])
        else:
            response = download.download_video(url[0])

        if response is False:
            print('\033[31mOcorreu um erro ao baixar o vídeo. Verifique a URL.\033[m\n')
            return False

        print('\n\033[32mFinalizado!\033[m')

def welcome():
    print('\n\033[47;30m Bem vindo! \033[m\n')
    print('@autor: Jaedson Silva')
    print('@github: jaedsonpys\n')

    print('[ 1 ] Baixar')
    print('[ 2 ] Sair\n')

    while True:
        try:
            option = int(input('Digite sua opção: '))
        except:
            print('\033[31mDigite um valor númerico!\033[m\n')
            continue
        else:
            if option == 1:
                break
            elif option == 2:
                print('\n\033[47;30m Até mais, volte logo! \033[m\n')
                exit()
            else:
                print('\033[31mOpção inválida! Tente novamente.\033[m\n')
                continue


    print('''Faça o download de músicas e vídeos direto da linha de comando!
Copie o link de um vídeo e coloque abaixo.\n''')

    urls = []

    while True:
        url = str(input('Digite uma URL válida: ')).strip()

        while True:
            type_media = str(input('Baixar em formato de música? [S/N]: ')).lower().strip()
            if type_media == 's':
                urls.append((url, True))
                break
            elif type_media == 'n':
                urls.append((url, False))
                break
            else:
                print('\033[31mOpção inválida, tente novamente!\033[m\n')
                continue
        
        while True:
            user_continue = str(input('\nQuer adicionar outra URL? [S/N]: ')).lower().strip()
            if user_continue == 's':
                break
            elif user_continue == 'n':
                download_media(urls)
                welcome()
            else:
                print('\033[31mOpção inválida. Tente novamente!\033[m\n')

welcome()