from flask import Blueprint, render_template, abort
from flask import current_app
from jinja2 import TemplateNotFound
import pygal

import requests
from .helper import neomanager as neo


searchByIndustry = "match(c :CAMPAIGN)-[:CAMPAIGN_STATUS]->(s :STATUS) return c.industry as industry, count(c.industry) as IndustryCount order by industry ASC"
searchByClient = "match(c :CAMPAIGN)-[:CAMPAIGN_STATUS]->(s :STATUS) return c.Client as Client, count(c.Client) as CampaignCount order by Client ASC"

campaign_blueprint = Blueprint(name='campaign', import_name=__name__, url_prefix='/campaign/')

@campaign_blueprint.route('add/<message>', methods=['GET'])
@campaign_blueprint.route('add/', defaults={'message': 'campaign sem mensagem no add'},methods=['GET'])
@campaign_blueprint.route('/', defaults={'message': 'campaign sem mensagem'}, methods=['GET'])
def add(message):
    current_app.logger.info(message)

    return 'campaign - {}'.format(message)


@campaign_blueprint.route('stats/', defaults={'stat': 'campaign'}, methods=['GET'])
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


@campaign_blueprint.route('stats/industry/', defaults={'stat': 'stats/industry/'}, methods=['GET'])
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
