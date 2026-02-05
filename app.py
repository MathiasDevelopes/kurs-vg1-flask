from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World.</h1>"

@app.route('/joke')
def joke():
    return "Why did the chicken cross the road? No idea."

@app.route('/hello/<string:name>')
def hello(name: str):
    return "Hei " + name

# Merk deg at vi bruker <int:num> for tall her, da sikrer vi at det vi får som input er en integer (tall).
@app.route('/calculate/<int:num1>/<string:operator>/<int:num2>')
def calculate(num1: int, operator: str, num2: int):

    # Vi sjekker hvilken operator brukeren har valgt
    # Lett å legge til flere operatorer senere
    # Du kan tenke på dette som en if-statement,
    # match operator betyr egentlig: hva er verdien av operator?
    # Når vi har case 'pluss', er det det samme som å sjekke om operator er lik 'pluss'
    match operator:
        case 'pluss':
            # Pluss sammen tallene
            return str(num1 + num2)
        case 'minus':
            # Subtraher tallene.
            return str(num1 - num2)
        case 'ganger':
            # Gang sammen tallene
            return str(num1 * num2)
        case 'delt':
            # Del num1 på num2.
            # OBS: Her er det viktig at vi sjekker om num2 er 0, siden vi ikke kan dele ting på 0.
            if num2 == 0:
                return "Det er ikke mulig å dele " + str(num1) + " på " + str(num2)

            # Vi bruker / her, som alltid gir desimal (float), selv om resultatet er heltall
            # Eksempel: 4 / 2 = 2.0  og  5 / 2 = 2.5
            return str(num1 / num2)

            # Hvis vi ville hatt heltall, kunne vi brukt // (heltallsdivisjon)
            # Eksempel: 5 // 2 = 2  og -5 // 2 = -3
            # Merk: // runder alltid ned mot minus uendelig, ikke til nærmeste tall
        case 'opphoyd':
            return str(num1 ** num2)
        
        # Hvis brukeren når denne casen, betyr det at operatoren ikke er gyldig.
        # Med andre ord: operator-variabelen har en verdi som ikke finnes i noen av de andre case-blokkene.
        case _:
            return "Ugyldig operatør " + operator

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
