from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Page de connexion
@app.route('/')
def login():
    return render_template('login.html')

# Authentification
@app.route('/auth', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    
    # Vérifier les informations d'identification ici (par exemple, dans une base de données)
    authenticated = check_credentials(username, password)
    
    if authenticated:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
    
# Vérification de l'état (health check)
@app.route('/health')
def health_check():
    return 'ok', 200  # Renvoyer une réponse HTTP 200 si l'authentification a réussi

# Page d'accueil
@app.route('/home')
def home():
    return render_template('home.html')

# Fonction pour vérifier les informations d'identification
def check_credentials(username, password):

    if username == 'admin' and password == 'password':
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)