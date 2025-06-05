from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for tasks
# Each task is a dict with 'id', 'title', and 'completed'
tasks = []
next_id = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Return the list of tasks."""
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    global next_id
    data = request.get_json()
    if not data or 'title' not in data:
        abort(400, 'Missing task title')
    task = {
        'id': next_id,
        'title': data['title'],
        'completed': False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task."""
    data = request.get_json()
    if not data:
        abort(400, 'No data provided')
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['completed'] = data.get('completed', task['completed'])
            return jsonify(task)
    abort(404, 'Task not found')

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task."""
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return '', 204
    abort(404, 'Task not found')

if __name__ == '__main__':
    # Bind to 0.0.0.0 so the app is reachable from outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)
