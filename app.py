from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this for production!

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name', '').strip().lower()
        if name == 'zoro':
            session['authenticated'] = True
            flash('Hurrayyyy!!seems like you got it right...', 'success')
            return redirect(url_for('congrats'))
        else:
            flash('you dont remember it, do you? try again', 'error')
    return render_template('login.html')

@app.route('/congrats')
def congrats():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('congrats.html')

@app.route('/feelings.html')
def feelings():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('feelings.html')  # Go to congrats first!

@app.route('/confession')
def confession():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('confession.html')

@app.route('/memories')
def memories():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('memories.html')

@app.route('/promise')
def promise():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('promise.html')

@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    flash('Logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()

