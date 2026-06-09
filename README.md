# Dia dos Namorados

Site romântico em Flask com três páginas: convite interativo, mural de artistas e playlist em polaroids.

## Páginas

| Rota | Descrição |
|------|-----------|
| `/` | Página inicial com botões "Sim" e "Não" |
| `/artistas` | Polaroids dos artistas favoritos com links para o Spotify |
| `/musicas` | Mural com as músicas da playlist em formato polaroid |

## Requisitos

- Python 3.10 ou superior
- pip

## Como rodar

1. Clone o repositório:

```bash
git clone https://github.com/Nandesdevs/Dia_dos_Namorados.git
cd Dia_dos_Namorados
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie o servidor:

```bash
python app.py
```

4. Abra no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Estrutura do projeto

```
Dia_dos_Namorados/
├── app.py                  # Servidor Flask
├── requirements.txt
├── static/
│   ├── tracks.json         # Lista de músicas (nome, artista, capa)
│   ├── style.css
│   ├── style-artistas.css
│   ├── style-musicas.css
│   ├── imagens/            # Imagens da página inicial
│   ├── imagens_site_artistas/
│   └── som/                # Áudio da página inicial
└── templates/
    ├── index.html
    ├── artistas.html
    └── musicas.html
```

## Atualizar a playlist

As músicas ficam em `static/tracks.json`. Cada item segue este formato:

```json
{
  "name": "Nome da música",
  "artist": "Nome do artista",
  "cover": "https://url-da-capa.jpg"
}
```

Para atualizar, edite o arquivo manualmente ou exporte a playlist do Spotify (CSV) e converta para esse JSON.

## Licença

Veja o arquivo [LICENSE](LICENSE).
