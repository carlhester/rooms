from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

items0 = []
items1 = []
items2 = []
items3 = []
items4 = []
items5 = []
items6 = []
items7 = []
items8 = []
items9 = []
items10 = ['pumpkin', 'halloween trinkets']
items = [items0, items1, items2, items3, items4, items5, items6, items7, items8, items9, items10]

people0 = []
people1 = []
people2 = []
people3 = []
people4 = []
people5 = []
people6 = []
people7 = []
people8 = []
people9 = []
people10 = []
people = [people0, people1, people2, people3, people4, people5, people6, people7, people8, people9, people10]



roomstuff = {
        1:[items1, people1],
        2:[items2, people2],
        3:[items2, people2],
        4:[items2, people2],
        5:[items2, people2],
        6:[items2, people2],
        7:[items2, people2],
        8:[items2, people2],
        9:[items2, people2],
        10:[items10, people10]
    }

players = []

@app.route('/')
def default():
    pass

@app.route('/items/<int:room_id>', methods=['GET'])
def items_in_room(room_id):
    if room_id in roomstuff:
        return jsonify(roomstuff[room_id])
    return jsonify('False')

@app.route('/createplayer/<string:username>/<int:location>', methods=['GET'])
def create_player(username, location):
    if username not in players:
        players.append(username)
        people[location].append(username)
        return jsonify(username)


@app.route('/who', methods=['GET'])
def who():
    results = []
    for i in xrange(len(items)):
        results.append(i)
        results.append(items[i])
    for p in xrange(len(people)):
        results.append(p)
        results.append(people[p])
    return jsonify(results)

app.run(port=5000)
