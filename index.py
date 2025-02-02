from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Template HTML que inclui o VLibras
    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tradução para Libras</title>
        <script src="https://vlibras.gov.br/app/vlibras-plugin.js"></script>
    </head>
    <body>
        <div vw="true" class="enabled">
            <div vw-access-button="true"></div>
            <div vw-plugin-wrapper="true" class="active"></div>
        </div>
        <script>
            new window.VLibras.Widget('https://vlibras.gov.br/app');
        </script>

        <h1>Texto traduzido para Libras</h1>
        <p>Este é um exemplo de tradução de texto para Libras usando VLibras.</p>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
