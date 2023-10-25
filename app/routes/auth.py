import base64
import httpx
import urllib.parse
from app.settings import settings
from flask import Blueprint, redirect, request, url_for

bp = Blueprint('auth', __name__)


@bp.get('/login/')
def login():
    scopes = ' '.join([
        'user-read-playback-state', 'user-top-read',
        'user-read-recently-played', 'user-read-private'
    ])
    params = {
        'response_type': 'code',
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'scope': scopes,
        'redirect_uri': url_for('auth.callback', _external=True),
        'state': settings.SPOTIFY_STATE
    }

    return redirect(
        f'https://accounts.spotify.com/authorize?{urllib.parse.urlencode(params)}'
    )


@bp.get('/callback/')
def callback():
    error = request.args.get('error', '')
    state = request.args.get('state', '')
    code = request.args.get('code', '')

    if error != '' or state != settings.SPOTIFY_STATE:
        return 'Ocorreu um erro ao se autenticar nos serviços do Spotify, tente novamente.'

    credentials = f'{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}'

    res = httpx.post(
        'https://accounts.spotify.com/api/token',
        headers={
            'content-type':
            'application/x-www-form-urlencoded',
            'Authorization':
            f'Basic {base64.b64encode(credentials.encode()).decode()}'
        },
        data={
            'code': code,
            'redirect_uri': url_for('auth.callback', _external=True),
            'grant_type': 'authorization_code'
        }
    )

    print(res.json())
    return 'User logged sucessfully!'
