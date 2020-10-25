from flask import Flask, render_template, send_from_directory , request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html') # but be sure this html file must be in template folder

# Dynamically
@app.route('/<string:page>')
def html_page(page):
    return render_template(page) # but be sure this html file must be in templates folder

# saving the data to the computer in txt file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        txt_file=database.write(f"'\n{name} , {email} , {subject} , {message}")

# # saving the data to the computer in csv file
def write_to_csv(data):
    with open('databse2.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(database2, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([name,email,subject,message])
       # csv_file=databse2.write(f"\n'{name} , {email} , {subject} , {message}")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
            data = request.form.to_dict()
            names = request.form['name']
            write_to_file(data)
            write_to_csv(data)
            return render_template('/thankyou.html', name = names)
        except:
            return "didn't saved to database"
        #return redirect('/thankyou.html', name = names)
    else:
        return 'Something went wrong'
#  <form action="submit_form" method ="get" class="reveal-content"> - modify this as like here in contact.html

# these are static type parameters
'''

@app.route('/index.html')
@app.route('/index.html')
def index():
    return render_template('index.html') # but be sure this html file must be in templete folder

@app.route('/works.html')
def works():
    return render_template('works.html') # but be sure this html file must be in templete folder

@app.route('/templates/work.html')
def work():
    return render_template('work.html') # but be sure this html file must be in templete folder
@app.route('/about.html')
def about():
    return render_template('about.html') # but be sure this html file must be in templete folder

@app.route('/contact.html')
def contact():
    return render_template('contact.html') # but be sure this html file must be in templete folder

@app.route('/components.html')
def components():
    return render_template('components.html') # but be sure this html file must be in templete folder
'''
