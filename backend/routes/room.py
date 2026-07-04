from flask import Blueprint, request, jsonify
from models.room import Room
from database import db
from utils.auth import token_required

room_bp = Blueprint('room', __name__)

@room_bp.route('/', methods=['GET'])
@token_required
def get_rooms(current_user):
    rooms = Room.query.all()
    output = []
    for room in rooms:
        output.append({
            'id': room.id,
            'room_number': room.room_number,
            'floor': room.floor,
            'area': float(room.area) if room.area else None,
            'rent_price': float(room.rent_price) if room.rent_price else None,
            'status': room.status
        })
    return jsonify({'rooms': output})

@room_bp.route('/', methods=['POST'])
@token_required
def create_room(current_user):
    data = request.get_json()
    new_room = Room(
        room_number=data['room_number'],
        floor=data.get('floor'),
        area=data.get('area'),
        rent_price=data.get('rent_price'),
        status=data.get('status', 'Available')
    )
    db.session.add(new_room)
    db.session.commit()
    return jsonify({'message': 'Room created successfully!'}), 201
