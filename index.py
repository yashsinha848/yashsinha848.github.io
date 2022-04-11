from flask import Flask, render_template , redirect
app = Flask(__name__)

@app.route("/")
def hello():
    #return "hello world"
    return render_template('index.html')

@app.route("/parent")
def parent():
    return render_template('parent-diseases.html')
@app.route("/bloodpressure")
def bloodpressure():
    return render_template('bloodpressure.html')
@app.route("/bronchitis")
def bronchitis():
    return render_template("bronchitis.html")
@app.route("/childfrontpage")
def childfrontpage():
    return render_template("childfrontpage.html")
@app.route("/activities")
def activities():
    return render_template("activities.html")
@app.route("/food")
def food():
    return render_template("newfood.html")
@app.route("/indoor")
def indoor():
    return render_template("indoor.html")
@app.route("/dance")
def dance():
    return redirect("https://www.youtube.com/watch?v=Qs8JfVqx9WA")
@app.route("/outdoor")
def outdoor():
    return render_template("outdoor.html")
@app.route("/hopscotch")
def hopscotch():
    return redirect("https://www.youtube.com/watch?v=fZzswQaICfM")
@app.route("/quiz")
def quiz():
    return redirect("http://take.quiz-maker.com/Q3Z92S52P")
app.run(debug=True)
