from flask import Flask, render_template, jsonify, request
from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data1.db'
db = SQLAlchemy(app)
@app.route('/bitselect', methods=['POST'])
def bitselect():
        '''
        this function is because of the design of the experiment
        the first bit corresponds to 32 bit representation
        the second bit corresponds to 64 bit representation
        it initializes the database and then later renders the page accordingly
        '''

        bit = request.form['dropddbit']
        if bit == '0':
                return render_template('experiment.html')
        elif bit == '1':
                db.create_all()
                cursor = db.engine.execute('SELECT * FROM numbers')
                data = cursor.fetchall()
                return render_template('experiment.html', bit=32, showanswer=-1, data01=bit, data02=data)
        elif bit == '2':
                db.create_all()
                cursor = db.engine.execute('SELECT * FROM numbers')
                data = cursor.fetchall()
                return render_template('experiment.html', bit=64, showanswer=-1, data01=bit, data02=data)

@app.route('/numberselect', methods=['GET', 'POST'])
def numselect():
        '''
        bit representation hidbit is for the number
        num is i=the number chosen
        then you initialize the database
        as all is stores in a list of one row so we access  [0][0]
        and then we store data01 data02 according to what should have been in the database
        it finally selects and puts the table in dropdown of the html page
        '''
        bit = request.form['hidbit']
        num = request.form['dropddnumber']
        if num == '---Select a number---':
        	return render_template('experiment.html')
        else:
                db.create_all()
                cursor = db.engine.execute("SELECT * FROM numbers WHERE Numb = " + num)
                dataind = cursor.fetchall()[0][0]
                cursor = db.engine.execute('SELECT * FROM numbers')
                data = cursor.fetchall()
                return render_template('experiment.html', showanswer=0, data11=num, data12=dataind, data01=bit, data02=data)

@app.route('/checkAnswers', methods=['GET', 'POST'])
def check():
        '''
        It validates all the dropdowns according to the answer.
        This function is there mainly so that the final output of the design is given
        And finally according to the answer the output is given
        '''
        checkans = request.form['hidans']
        bit = request.form['hidbit1']
        num = request.form['hidnum']
        ind = request.form['hidind']
        sign = request.form['sm']
        ex = request.form['exp']
        mant = request.form['mantes']
        db.create_all()
        cursor = db.engine.execute('SELECT * FROM numbers')
        data = cursor.fetchall()
        cursor = db.engine.execute('SELECT * FROM numbers WHERE Numb = ' + num)
        datanum = cursor.fetchall()
        c = 0
        if datanum[0][2] == int(sign):
                if datanum[0][3] == ex:
                        if datanum[0][4] == mant:
                                    c = 1
        if c == 0:
                return render_template('experiment.html', showanswer=1, valid=0, data01=bit, data11=num, data02=data)
        else:
                return render_template('experiment.html', showanswer=1, valid=1, data01=bit, data11=num, data02=data)		
