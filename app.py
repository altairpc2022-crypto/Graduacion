from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    
    if request.method == 'POST':
        horas_transporte = float(request.form.get('transporte', 0))
        botellas = int(request.form.get('botellas', 0))
        minutos_ducha = float(request.form.get('ducha', 0))
        
        co2_transporte = horas_transporte * 1.5 * 365
        arboles = round(co2_transporte / 20)
        
        botellas_ano = botellas * 52
        petroleo_ahorrado = round(botellas_ano * 0.25, 1)
        
        agua_ano = minutos_ducha * 12 * 365
        
        mensaje_voz = (
            f"Tu diagnóstico de Eco Impacto 360 es el siguiente. "
            f"Al año generas aproximadamente {int(co2_transporte)} kilos de dióxido de carbono en transporte. "
            f"Para compensarlo, necesitas plantar {arboles} árboles. "
            f"Además, si usas un tomatodo reutilizable, evitarás usar {botellas_ano} botellas de plástico "
            f"y ahorrarás {petroleo_ahorrado} litros de petróleo. "
            f"¡Cuidemos el planeta juntos!"
        )
        
        resultado = {
            'arboles': arboles,
            'co2': int(co2_transporte),
            'botellas_ano': botellas_ano,
            'petroleo': petroleo_ahorrado,
            'agua_ano': int(agua_ano),
            'mensaje_voz': mensaje_voz
        }
        
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)