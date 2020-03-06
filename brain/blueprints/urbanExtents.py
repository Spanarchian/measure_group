# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import current_app

urbanExtents_blueprint = Blueprint(name='urbanExtents', import_name=__name__, url_prefix='/urbanExtents/')


@urbanExtents_blueprint.route('add/<message>', methods=['GET'])
@urbanExtents_blueprint.route('add/', defaults={'message': 'sem mensagem no add'},methods=['GET'])
@urbanExtents_blueprint.route('/', defaults={'message': 'sem mensagem'}, methods=['GET'])
def add(message):
    return 'Urban Extents - {}'.format(message)

