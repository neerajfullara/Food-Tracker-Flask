from flask import Flask, render_template, g,request
from datetime import datetime
from databasefile import connect_db, get_db

app = Flask(__name__)

# It check if there's sqlite3_db in there.
# If there is then it will close it at the end of every request at the end of every route.
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()


# These are for home and the root/main page
@app.route('/', methods=['GET','POST'])
def index():

    db = get_db()
    if request.method == 'POST':
        date = request.form['date']
        database_date = datetime.strptime(date, '%Y-%m-%d') # date is converted to '%Y-%m-%d' from '%d-%m-%Y'
        final_database_date = datetime.strftime(database_date, '%Y%m%d')

        db.execute('insert into date_log (entry_date) values (?)', [final_database_date])
        db.commit()
        # return final_database_date
    cur = db.execute('''select date_log.entry_date, sum(food.protein) as protein, sum(food.carbohydrates) as carbohydrates, sum(food.fat) as fat, sum(food.calories) as calories from 
                     date_log left join food_date on food_date.log_date_id = date_log.id 
                     left join food on food.id = food_date.food_id group by date_log.id order by date_log.entry_date desc''')
    results = cur.fetchall()

    # This will formate the date shown in the page from %Y%m%d to %B %d, %Y. 
    # ex 20030110 to January 10, 2003
    formated_result = []
    for i in results:
        single_date = {}
        single_date['entry_date'] = i['entry_date']
        single_date['protein'] = i['protein']
        single_date['carbohydrates'] = i['carbohydrates']
        single_date['fat'] = i['fat']
        single_date['calories'] = i['calories']
        unformatted = datetime.strptime(str(i['entry_date']), '%Y%m%d')
        single_date['pr_date'] = datetime.strftime(unformatted, '%B %d, %Y')

        formated_result.append(single_date)

    return render_template('home.html', results = formated_result)

# This is for days page
@app.route('/days/<date>', methods = ['GET', "POST"])
def days(date):

    db = get_db()
    cur = db.execute('select id, entry_date from date_log where entry_date = ?', [date])
    date_result = cur.fetchone()

    # This will add the foodID and logDateID into the database table (food_date)
    if request.method == 'POST':
        db.execute('insert into food_date(food_id, log_date_id) values(?, ?)',[request.form['food-select'], date_result['id']])
        db.commit()

    unformatted_date = datetime.strptime(str(date_result['entry_date']), '%Y%m%d')
    formated_dates = datetime.strftime(unformatted_date, '%B %d, %Y')

    food_cur = db.execute('select id, name from food')
    food_results = food_cur.fetchall()

    log_cur = db.execute('''select food.name, food.protein, food.carbohydrates, food.fat, food.calories from date_log 
                         join food_date on food_date.log_date_id = date_log.id 
                         join food on food.id = food_date.food_id where date_log.entry_date = ?''', [date])
    log_results = log_cur.fetchall()

    totals = {}
    totals['protein'] = 0
    totals['carbohydrates'] = 0
    totals['fat'] = 0
    totals['calories'] = 0
    for food in log_results:
        totals['protein'] += food['protein']
        totals['carbohydrates'] += food['carbohydrates']
        totals['fat'] += food['fat']
        totals['calories'] += food['calories']

    return render_template('days.html',entry_date=date_result['entry_date'], formated_date = formated_dates, food_results=food_results, log_results=log_results, totals=totals)

# This is for days page
@app.route('/foodadd', methods=['GET','POST'])
def foodadd():

    db = get_db()
    if request.method=='POST':

        # Added Food items into database and calculated calories
        name=request.form['food-name']
        protein=int(request.form['protein'])
        carbohydrates=int(request.form['carbohydrates'])
        fat=int(request.form['fat'])
        
        calories = (protein*4 )+ (carbohydrates*4) + (fat*9)

        # Taking values from name, protein, carbohydrates, fat and calories and adding them into database
        db.execute('''insert into food (name, protein, carbohydrates, fat, calories) 
                   values (?, ?, ?, ?, ?)''', [name, protein, carbohydrates, fat, calories])
        db.commit()

    cur = db.execute('select name, protein, carbohydrates, fat, calories from food')
    results = cur.fetchall()

    return render_template('foodadd.html', results = results)

if __name__ == '__main__':
    app.run(debug=True)