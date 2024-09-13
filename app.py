from flask import Flask, request, render_template, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = '18723h3'  

@app.route('/')
def index():
    if 'username' in session:
    
        return render_template('dapp.html', username=session['username'])
    else:
      
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
       
        username = request.form.get('username')
        password = request.form.get('password')

        session['username'] = username
        return redirect(url_for('index'))  

     return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  
    return redirect(url_for('login'))  

if __name__ == '__main__':
    app.run("0.0.0.0", 8080)
