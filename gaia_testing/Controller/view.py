import json
from flask import Blueprint, request, jsonify
from Services.utility import convertToJson

utility = Blueprint('utility', __name__)

@utility.route('/ToJson', methods=['POST'])
def xmlToJson():    
    try:
        payload = json.loads(request.data)
        _xml = payload['xml']
        _json = convertToJson(_xml)
        if 'exception' in _json:
            return jsonify({'error': str(_json)}),400        
        
        return jsonify(_json),200
    
    except Exception as e:
        return jsonify({"error": str(e)}),400
