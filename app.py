from flask import Flask
from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintainance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About VTM')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius=float(form['radius'])
        height=float(form['height'])
        
        pi=3.14
        
        area=(pi*radius**2)+(2*(pi*(radius*height)))
        sqft=area/144
        part=sqft*25
        labor=sqft*15
        total=part+labor
        estimate=total











        return render_template('estimate.html',estimate=total)
    return render_template('estimate.html')
    

if __name__ == '__main__':
    app.run(debug=True)
