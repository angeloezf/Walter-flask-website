from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/introducao')
def introducao():
  return render_template('introducao.html')

@app.route('/di')
def di():
  return render_template('DI.html')
  
@app.route('/tea')
def tea():
  return render_template('TEA.html')

@app.route('/tod')
def tod():
  return render_template('TOD.html')

@app.route('/tdah')
def tdah():
  return render_template('TDAH.html')

@app.route('/alns')
def alns():
  return render_template('ALNS.html')

@app.route('/te')
def te():
  return render_template('TE.html')

@app.route('/tme')
def tme():
  return render_template('TME.html')
  
@app.route('/tddh')
def tddh():
  return render_template('TDDH.html')

@app.route('/tei')
def tei():
  return render_template('TEI.html')

@app.route('/tept')
def tept():
  return render_template('TEPT.html')

@app.route('/tdi')
def tdi():
  return render_template('TDI.html')

@app.route('/tdpm')
def tdpm():
  return render_template('TDPM.html')

@app.route('/tpb')
def tpb():
  return render_template('TPB.html')

@app.route('/tpa')
def tpa():
  return render_template('TPA.html')

@app.route('/tc')
def tc():
  return render_template('TC.html')

@app.route('/tdm')
def tdm():
  return render_template('TDM.html')

@app.route('/tbmania')
def tbmania():
  return render_template('TB_Mania.html')

@app.route('/tbmisto')
def tbmisto():
  return render_template('TB_Misto.html')

@app.route('/esquizofrenia')
def esquizofrenia():
  return render_template('Esquizofrenia.html')

@app.route('/catatonia')
def catatonia():
  return render_template('Catatonia.html')

@app.route('/tratamento')
def tratamento():
  return render_template('Tratamento.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  