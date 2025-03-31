from flask import Flask, app

no app

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar_gravidade', methods=['POST'])
def processar_gravidade():
    data = request.get_json()  # Captura os dados JSON enviados pelo AJAX
    gravidade = data.get('gravidade')  # Obtém a gravidade selecionada

    if gravidade in ['3', '5']:
        return jsonify({'resposta': f'Gravidade selecionada: {gravidade}'})
    else:
        return jsonify({'resposta': 'Nenhuma gravidade 3 ou 5 selecionada.'})

if __name__ == '__main__':
    app.run(debug=True)




no html
<form method="POST" action="/processar_gravidade">
    <h2>GRAVIDADE</h2>
    <div class="btn-group1" role="group1" aria-label="Basic radio toggle button group1">
        <input type="radio" class="btn-check" name="gravidade" id="nao" value="nao" autocomplete="off" checked>
        <label class="btn btn-outline-primary" for="nao">NÃO SELECIONADO</label>

        <input type="radio" class="btn-check" name="gravidade" id="3" value="3" autocomplete="off">
        <label class="btn btn-outline-primary" for="3">Até 3/5</label>

        <input type="radio" class="btn-check" name="gravidade" id="5" value="5" autocomplete="off">
        <label class="btn btn-outline-primary" for="5">Até 5/5</label>
    </div>

    <button type="submit">Enviar</button>
</form>


no Flask
@app.route('/processar_gravidade', methods=['POST'])
def processar_gravidade():
    gravidade = request.form.get('gravidade')  # Obtém o valor do formulário

    if gravidade in ['3', '5']:
        return f'<h2>Gravidade selecionada: {gravidade}</h2>'
    else:
        return '<h2>Nenhuma gravidade 3 ou 5 selecionada.</h2>'

#####

<form method="POST" action="/processar_gravidade">
    <h2>GRAVIDADE</h2>

    <div class="btn-group1" role="group1" aria-label="Basic radio toggle button group1">
        <input type="radio" class="btn-check" name="gravidade" id="nao" value="nao" autocomplete="off" checked>
        <label class="btn btn-outline-primary" for="nao">NÃO SELECIONADO</label>

        <input type="radio" class="btn-check" name="gravidade" id="3" value="3" autocomplete="off">
        <label class="btn btn-outline-primary" for="3">Até 3/5</label>

        <input type="radio" class="btn-check" name="gravidade" id="5" value="5" autocomplete="off">
        <label class="btn btn-outline-primary" for="5">Até 5/5</label>
    </div>

    <button type="submit">Enviar</button>
</form>





<fieldset>
  <legend>Your age</legend>
  <div>
    <label for="lt20">19 or under</label>
    <input type="radio" name="age" id="lt20" value="lt20">
  </div>
  <div>
    <label for="20to39">20 to 39</label>
    <input type="radio" name="age" id="20to39" value="20to39">
  </div>
  <div>
    <label for="40to59">40 to 59</label>
    <input type="radio" name="age" id="40to59" value="40to59">
  </div>
  <div>
    <label for="gt59">60 or over</label>
    <input type="radio" name="age" id="gt59" value="gt59">
  </div>
  </fieldset>



<h2>OBJETO</h2>

<h3><div class="btn-group1" role="group1" aria-label="Basic radio toggle button group1">
  <input type="radio" class="btn-check" name="objeto" id="nao" autocomplete="off" checked>
  <label class="btn btn-outline-primary" for="btnradio1">NÃO SELECIONADO</label>

  <input type="radio" class="btn-check" name="objeto" id="Hetero" autocomplete="off">
  <label class="btn btn-outline-primary" for="btnradio2">Hetero Agressividade</label>

  <input type="radio" class="btn-check" name="objeto" id="Auto" autocomplete="off">
  <label class="btn btn-outline-primary" for="btnradio3">Auto Agressividade</label>
</div></h3>