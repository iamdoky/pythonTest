from flask import Flask,render_template
import day0326.func0326

app = Flask (__name__)

@app.route('/pharmacy.do')
def pharmacy():
    data = day0326.func0326.pharmacy()
    return render_template('pharmacy.html',data=data)

if __name__=='__main__':
    app.run(debug=True,host='203.236.209.95')