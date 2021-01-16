from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/eslam'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    todos = db.relationship('Todo', backref='list',lazy=True, passive_deletes=True)

    def __repr__(self):
        return '<TodoList {} {}>'.format(self.id, self.description)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id',), nullable=False)

    def __repr__(self):
        return '<Todo {} {}>'.format(self.id, self.description)


@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({'success': True})


@app.route('/todolists/<todolist_id>', methods=['DELETE'])
def delete_todolist(todolist_id):
    try:
        todolist=TodoList.query.get(todolist_id)
        for todo in todolist.todos:
            db.session.delete(todo)
        db.session.delete(todolist)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({'success': True})   

# note: more conventionally, we would write a
# POST endpoint to /todos for the create endpoint:
# @app.route('/todos', method=['POST'])


@app.route('/todolists/create', methods=['POST'])
def create_todolist():
    error2 = False
    body2 = {}
    try:
        description2 = request.get_json()['description']

        todolist = TodoList(description=description2,completed=False)
        db.session.add(todolist)
        db.session.commit()
        body2['id'] = todolist.id
        body2['description'] = todolist.description
    except:
        error2 = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error2:
        abort(400)
    else:
        return jsonify(body2)


@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        list_id = request.get_json()['list_id']
        todo = Todo(description=description, completed=False, list_id=list_id)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['completed'] = todo.completed
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)


@app.route('/todolists/<todolist_id>/set-completed', methods=['POST'])
def set_completed_todolist(todolist_id):
    try:
        lcompleted = request.get_json()['completed']
        print('completed', lcompleted)
        todolist = TodoList.query.get(todolist_id)
        todolist.completed = lcompleted
        for todo in todolist.todos:
            todo.completed=lcompleted
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        print('completed', completed)
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))

@app.route('/lists/<listid>')
def index2(listid):
    return render_template('index.html', todos=Todo.query.filter(Todo.list_id == listid).order_by('id').all(),
                           lists=TodoList.query.all(),
                           activelist=TodoList.query.get(listid))


@app.route('/')
def index():
    return redirect(url_for('index2', listid=1))


if __name__ == "__main__":
    app.run(debug=True)
