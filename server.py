from flask import Flask, render_template, request, flash, redirect, session, url_for, make_response
import calculate
app = Flask(__name__)
app.secret_key = "yuhipkoopktfyiuhokilyhk"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cost', methods=["GET", "POST"])
def cost():
    if not session.get('email'):
        return redirect('/login')
    if request.method == "GET":
        return render_template('cost.html')
    elif request.method == "POST":
        cost = request.form.get('cost')
        return redirect(url_for('calculated_tip', cost=cost))


@app.route('/tip/<float:cost>', methods=["GET", "POST"])
def calculated_tip(cost):
    if not session.get('email'):
        return redirect('/login')
    if request.method == "GET":
        percents = range(0,26,5)
        tips = calculate.tips(cost, percents)
        tips = zip(percents, tips)
        return render_template('calculated.html', 
                               tips=tips,
                               cost=cost)
    elif request.method == "POST":
        tip_amount = request.form.get('tip')
        resp = make_response(redirect('/tip/now'))
        resp.set_cookie('tip_amount', str(tip_amount))
        return resp

@app.route('/tip/now', methods= ['GET', 'POST'])
def tip_now():
    if not session.get('email'):
        return redirect('/login')
    if not request.cookies.get('tip_amount'):
        return redirect('/cost')
    if request.method == "GET":
        return render_template('tipNow.html')
    elif request.method == "POST":
        flash('Thanks for high tippability')
        resp = make_response(redirect(url_for("home")))
        resp.set_cookie('tip_amount', '', expires=0)
        return resp

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        print request.form
        email = request.form.get('email')
        password = request.form.get('password')
        # Pretend to validate
        # Validation successful
        session['email'] = email
        flash('Login was successful. Hi '+ email)
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5001)