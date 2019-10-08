from flask import *
import pandas as pd
import os
import re
app = Flask(__name__)

@app.route("/")
def show_tables():
    filename = 'example2.xlsx'
    data = pd.read_excel(filename,sheetname='Sheet1')
    data = data.fillna('')
    return render_template('index.html',tables=[re.sub(' mytable', '" id="example', data.to_html(classes='mytable'))],
    titles = ['Excel Data to Flask'])



@app.route('/insert', methods= ['POST','GET'])
def insert():
    q1 = request.form['num1']
    q2 = request.form['num2']
    print(q1,q2)
    df = pd.DataFrame({'a': [q1],
                       'b': [q2]})

    book = pd.read_excel('example2.xlsx')
    writer = pd.ExcelWriter('example2.xlsx', engine='openpyxl')
    book.to_excel(writer, startrow=0, index=False)
    df.to_excel(writer, startrow=len(book) + 1, header=False, index=False)
    writer.save()
    return redirect('/')

@app.route('/save', methods= ['POST','GET'])
def save():
    url = 'http://127.0.0.1:5000/'
    urll = request.get_data()
    print(urll)
    data = pd.read_html(urll)
    print(data)
    writer = pd.ExcelWriter('example2.xlsx', engine='openpyxl')
    data[0].drop('Unnamed: 0', axis=1).to_excel(writer, sheet_name='Sheet1', index=False)

    writer.save()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
