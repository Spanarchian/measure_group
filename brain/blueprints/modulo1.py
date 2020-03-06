# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import current_app
from jinja2 import TemplateNotFound
import pygal

modulo1_blueprint = Blueprint(name='modulo1', import_name=__name__, url_prefix='/modulo1/')


@modulo1_blueprint.route('/', methods=['GET'])
def index():
    return 'modulo1'



@modulo1_blueprint.route('stats/', defaults={'stat': 'campaign'}, methods=['GET'])
def stats(stat):
    current_app.logger.info(stat)
    try:
        gauge_chart = pygal.Gauge(human_readable=True)
        gauge_chart.title = 'DeltaBlue V8 benchmark results'
        gauge_chart.range = [0, 10000]
        gauge_chart.add('Chrome', 8212)
        gauge_chart.add('Firefox', 8099)
        gauge_chart.add('Opera', 2933)
        gauge_chart.add('IE', 41)
        gauge_chart.render()
        return gauge_chart.render_response()
    except TemplateNotFound:
        abort(404)


@modulo1_blueprint.route('stats/industry/', defaults={'stat': 'stats/industry/'}, methods=['GET'])
def stats_industry(stat):
    current_app.logger.info(stat)
    try:
        gauge_chart = pygal.Gauge(human_readable=True)
        gauge_chart.title = 'Industry benchmark - results'
        gauge_chart.range = [0, 100]
        gauge_chart.add('Pharma %', 82)
        gauge_chart.add('Engineering %', 69)
        gauge_chart.add('Media %', 29)
        gauge_chart.add('Travel %', 41)
        gauge_chart.render()
        return gauge_chart.render_response()
    except TemplateNotFound:
        abort(404)
