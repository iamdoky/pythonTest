from flask import Flask,render_template
import day0327.seoulFunc

app = Flask (__name__)
arr = []

@app.route('/detailPark')
def detailPark(idx):
    i = int(idx)-1
    item = arr[i]
    return render_template('detailPark.html',item=item)


@app.route('/seoul')
def seoul():
    global arr
    arr = day0327.seoulFunc.seoul()
    return render_template('seoul.html',arr=arr)


@app.route('/park')
def park():
    data = day0327.seoulFunc.park_seuol()
    return render_template('park.html',data=data)


if __name__=='__main__':
    app.run(debug=True,host='203.236.209.95')
