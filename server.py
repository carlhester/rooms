from flask import Flask, jsonify, request, render_template, abort
import time

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
items11 = []
items12 = []
items13 = []
items14 = []
items = [items0, items1, items2, items3, items4, items5, items6, items7, items8, items9, items10, items11, items12, items13, items14]

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
people11 = []
people12 = []
people13 = []
people14 = []
people = [people0, people1, people2, people3, people4, people5, people6, people7, people8, people9, people10, people11, people12, people13, people14]



roomstuff = {
        1:[items1, people1],
        2:[items2, people2],
        3:[items3, people3],
        4:[items4, people4],
        5:[items5, people5],
        6:[items6, people6],
        7:[items7, people7],
        8:[items8, people8],
        9:[items9, people9],
        10:[items10, people10], 
        11:[items11, people11],
        12:[items12, people12],
        13:[items13, people13],
        14:[items14, people14]
    }

players = []

def refresh_rooms():
    items = [items0, items1, items2, items3, items4, items5, items6, items7, items8, items9, items10]
    people = [people0, people1, people2, people3, people4, people5, people6, people7, people8, people9, people10]

@app.route('/')
def default():
    pass

@app.route('/move/<string:player_name>/<int:room_id>', methods=['GET'])
def player_move_to_room(player_name, room_id):
    for each in people:
        if player_name in each:
            each.remove(player_name)
    people[room_id].append(player_name)
    return jsonify(room_id)
    

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

@app.route('/player/<string:username>', methods=['GET'])
def player_exist(username):
    if username in players:
        for each in people:
            if username in each:
                return jsonify(people.index(each))
    abort(404)

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
