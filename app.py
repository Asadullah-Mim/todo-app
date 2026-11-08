import os 
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, ToDo

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db.init_app(app)


    
with app.app_context():
    db.create_all()
    

@app.route('/')
def index():
    # Parameters
    filter_status = request.args.get('filter', 'all')
    sort_by = request.args.get('sort', 'id')
    search_query = request.args.get('search', '')
    
    query = ToDo.query
    
    #search by title
    if search_query:
        query = query.filter(ToDo.title.ilike(f'%{search_query}%'))
    
    #Filter by status
    if filter_status == 'pending':
        query = query.filter_by(complete=False)
    elif filter_status == 'completed':
        query = query.filter_by(complete=True)
    
    #Sort tasks
    if sort_by == 'due_date':
        query = query.order_by(ToDo.due_date.asc())
    elif sort_by == 'priority':
        query = query.order_by(ToDo.priority.desc())
    else:
        query = query.order_by(ToDo.id.asc())
    
    todo_list = query.all()
    
    current_time = datetime.now()
    
    return render_template('index.html', todo_list=todo_list, filter_status=filter_status, sort_by=sort_by, search_query=search_query, current_time=current_time)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date_str = request.form.get('due_time')
    priority = request.form.get('priority', 'Medium')
    
    due_date_str = request.form.get('due_date')
    
    due_date = None
    if due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M')
    
    if title:
        new_task = ToDo(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            complete=False
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>', methods=['GET','POST'] )
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    if todo:
        todo.complete = not todo.complete
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['GET','POST'])
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('index'))
    
    

if __name__ == "__main__":
    app.run(debug = True)