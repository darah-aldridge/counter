from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "Let's Buy Fruit!"


def sessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    sessionCounter()
    return render_template('index.html')

@app.route('/add_two')
def plusTwo():
        session['counter'] += 1
        return redirect('/')

@app.route('/destory_session')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    