from flask import Blueprint
from ..models import Projects, Feedback, MiniApps

api = Blueprint('api', __name__, url_prefix='/api')

@api.get('/project-previews')
def project_previews():
    projects = Projects.query.all()
    fithub = Projects.query.filter_by(title="FitHub").first()
    pokemon = Projects.query.filter_by(title="Pokemon Battle X").first()
    realpeace = Projects.query.filter_by(title="RealPeace Website").first()
    p_list = [p.to_dict() for p in projects]
    return {
        "data": p_list,
        "fithub": fithub.to_dict(),
        "pokemon": pokemon.to_dict(),
        "realpeace": realpeace.to_dict()
    }
    
@api.get('/timezone-app')
def timezone_app():
    mini_app = MiniApps.query.filter_by(title="TimeZone App").first()
    return {
        "data": mini_app.to_dict()
    }
    
@api.get('/pick-a-pokemon')
def pick_a_pokemon():
    mini_app = MiniApps.query.filter_by(title="Pick-A-Pokemon").first()
    return {
        "data": mini_app.to_dict()
    }
    
@api.get('/geo-weather-app')
def geo_weather_app():
    mini_app = MiniApps.query.filter_by(title="Geo-Weather App").first()
    return {
        "data": mini_app.to_dict()
    }
    
@api.get('/mini-apps')
def mini_apps():
    timezone = MiniApps.query.filter_by(title="TimeZone App").first()
    pokemon = MiniApps.query.filter_by(title="Pick-A-Pokemon").first()
    geoweather = MiniApps.query.filter_by(title="Geo-Weather App").first()
    return {
        "timezone": timezone.to_dict(),
        "pokemon": pokemon.to_dict(),
        "geoweather": geoweather.to_dict()
    }
