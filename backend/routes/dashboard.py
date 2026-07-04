from flask import Blueprint, jsonify
from models.room import Room
from models.resident import Resident
from models.invoice import Invoice
from utils.auth import token_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/stats', methods=['GET'])
@token_required
def get_stats(current_user):
    total_rooms = Room.query.count()
    rented_rooms = Room.query.filter_by(status='Rented').count()
    total_residents = Resident.query.count()
    unpaid_invoices = Invoice.query.filter_by(status='Unpaid').count()
    
    return jsonify({
        'total_rooms': total_rooms,
        'rented_rooms': rented_rooms,
        'available_rooms': total_rooms - rented_rooms,
        'total_residents': total_residents,
        'unpaid_invoices': unpaid_invoices
    })
