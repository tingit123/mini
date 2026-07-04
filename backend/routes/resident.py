from flask import Blueprint, request, jsonify
from models.resident import Resident
from database import db
from utils.auth import token_required

resident_bp = Blueprint('resident', __name__)

@resident_bp.route('/', methods=['GET'])
@token_required
def get_residents(current_user):
    residents = Resident.query.all()
    output = []
    for res in residents:
        output.append({
            'id': res.id,
            'full_name': res.full_name,
            'identity_card': res.identity_card,
            'phone_number': res.phone_number,
            'room_id': res.room_id
        })
    return jsonify({'residents': output})
