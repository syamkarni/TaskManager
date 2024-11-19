from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

#####backend configuration#######
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
################################


##### Database model #######
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default="pending", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

with app.app_context():
    db.create_all()
################################



###All api routes here###
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date.strftime('%Y-%m-%d'),
        "status": task.status,
        "created_at": task.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": task.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    } for task in tasks])

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date.strftime('%Y-%m-%d'),
        "status": task.status,
        "created_at": task.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": task.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(
        title=data['title'],
        description=data['description'],
        due_date=datetime.strptime(data['due_date'], '%Y-%m-%d'),
        status=data.get('status', 'pending')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created", "task_id": new_task.id}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    if 'due_date' in data:
        task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
    task.status = data.get('status', task.status)
    db.session.commit()
    return jsonify({"message": "Task updated"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})

@app.route('/tasks/<int:id>/complete', methods=['PATCH'])
def mark_task_complete(id):
    task = Task.query.get_or_404(id)
    task.status = 'completed'
    db.session.commit()
    return jsonify({"message": "Task marked as complete"})

################################


if __name__ == '__main__':
    app.run(debug=True)
