# This file is part of CocoRicoFM.
#
# CocoRicoFM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CocoRicoFM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CocoRicoFM.  If not, see <http://www.gnu.org/licenses/>.

import urllib.request, urllib.error, urllib.parse
import json
import time
import html.parser
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import async_timeout
import os
import pkg_resources
import gbulb
import ssl
from .playlistparser.plparser.common import parse as plparse

HTTP_SESSION = None
HTTPS_SESSION = None
def obtain_network_session(url):
    global HTTP_SESSION, HTTPS_SESSION
    is_https = url.startswith("https")
    if is_https and HTTPS_SESSION:
        return HTTPS_SESSION
    elif HTTP_SESSION:
        return HTTP_SESSION

    if is_https:
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        connector = aiohttp.TCPConnector(ssl_context=context)
        HTTPS_SESSION = aiohttp.ClientSession(connector=connector)
        return HTTPS_SESSION
    else:
        connector = aiohttp.TCPConnector()
        HTTP_SESSION = aiohttp.ClientSession(connector=connector)
        return HTTP_SESSION

async def close_network_session():
    global HTTP_SESSION, HTTPS_SESSION
    if HTTP_SESSION:
        session = HTTP_SESSION
        HTTP_SESSION = None
        await session.close()
    if HTTPS_SESSION:
        session = HTTPS_SESSION
        HTTPS_SESSION = None
        await session.close()

async def _fetch(url, raw=False):
    session = obtain_network_session(url)
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            if raw:
                return await response.read()
            else:
                return await response.text()

async def fetch(url, raw=False):
    try:
        return await _fetch(url, raw=raw)
    except:
        return ''

STATIONS={}

class MetaRadio(type):
    def __init__(cls, name, bases, dct):
        super(MetaRadio, cls).__init__(name, bases, dct)
        if name not in ("Radio", "RadioFranceWebRadio"):
            if 'name' in dct:
                name = dct['name']
            STATIONS[name] = cls

class SongInfos:
    artist = ""
    album = ""
    title = ""
    cover_url = ""
    default_cover_url = ""
    year = 0
    label = ""
    metadata_fetched = False
    duration = 0
    mbid = ""

    def __init__(self, artist, album, title, year, cover_url=''):
        self.artist = artist
        self.album = album
        self.title = title
        self.initial_metadata = (self.artist, self.album, self.title)
        self.cover_url = cover_url
        self.time_started = time.time()

    async def fetch_cover(self):
        future = asyncio.Future()
        if hasattr(self, '_cover_data'):
            future.set_result(self._cover_data)
            return await future
        elif self.cover_url:
            self._cover_data = await fetch(self.cover_url, raw=True)
            return self._cover_data
        else:
            self._cover_data = pkg_resources.resource_string('cocoricofm', os.path.join('static', 'no-cover.png'))
            future.set_result(self._cover_data)
            return await future

    def update_metadata(self, artist, album, title, duration, mbid, cover_url):
        self.initial_metadata = (self.artist, self.album, self.title)
        self.artist = artist
        self.album = album
        self.title = title
        self.duration = duration
        self.mbid = mbid
        self.cover_url = cover_url

    def __eq__(self, other):
        return (self.initial_metadata == other.initial_metadata)

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return "<SongInfos artist=%r, album=%r, title=%r, cover_url=%r>" % (self.artist, self.album, self.title, self.cover_url)

class Radio(object, metaclass=MetaRadio):
    advising_cache_time = False
    stream_url = ''

    def next_update_timestamp(self):
        return None

    async def now_playing(self):
        future = asyncio.Future()
        future.set_result(SongInfos("", "", "", 0))
        return await future

    async def live_url(self):
        future = asyncio.Future()
        if self.stream_url:
            future.set_result(self.stream_url)
            return await future

        data = await fetch(self.playlist_url, raw=True)
        playlist = plparse(filedata=data)
        self.stream_url = playlist.Tracks[0].File
        future.set_result(self.stream_url)
        return await future

class RadioFranceWebRadio(Radio):
    advising_cache_time = True

    def __init__(self):
        super(RadioFranceWebRadio, self).__init__()
        self._cache_expires = None

    def next_update_timestamp(self):
        return self._cache_expires

    async def now_playing(self):
        now = int(round(time.time()))
        url = "%s?_=%s" % (self.json_metadata_url, now)

        data = await fetch(url)
        try:
            json_data = json.loads(data)
        except:
            return SongInfos('', '', '', 0)
        levels = json_data['levels'][len(json_data['levels']) - 1]
        items = levels['items']
        position = levels['position']
        stepId = items[position]
        song = json_data['steps'][stepId]
        self._cache_expires = song['end']
        mapping = {}
        for (attr, key) in (('artist', 'authors'), ('album', 'titreAlbum'),
                            ('title', 'title'), ('label', 'label')):
            try:
                mapping[attr] = song[key].title()
            except KeyError:
                continue
        try:
            mapping['cover_url'] = song['visual']
        except KeyError:
            pass
        try:
            mapping['year'] = song['anneeEditionMusique']
        except KeyError:
            pass

        return SongInfos(mapping.get('artist', ''), mapping.get('album', ''),
                         mapping.get('title', ''), mapping.get('year', 0),
                         cover_url=mapping.get('cover_url',''))

class FIP(RadioFranceWebRadio):
    stream_url = "http://direct.fipradio.fr/live/fip-midfi.mp3"
    json_metadata_url = "http://www.fipradio.fr/livemeta/7"

class FIPRockWebRadio(RadioFranceWebRadio):
    name = "FIP Autour du Rock"
    stream_url = "http://direct.fipradio.fr/live/fip-webradio1.mp3"
    json_metadata_url = "http://www.fipradio.fr/livemeta/64"

class FIPJazzWebRadio(RadioFranceWebRadio):
    name = "FIP Autour du Jazz"
    stream_url = "http://direct.fipradio.fr/live/fip-webradio2.mp3"
    json_metadata_url = "http://www.fipradio.fr/livemeta/65"

class FIPGrooveWebRadio(RadioFranceWebRadio):
    name = "FIP Autour du Groove"
    stream_url = "http://direct.fipradio.fr/live/fip-webradio3.mp3"
    json_metadata_url = "http://www.fipradio.fr/livemeta/66"

class FIPMondeWebRadio(RadioFranceWebRadio):
    name = "FIP Autour du Monde"
    stream_url = "http://direct.fipradio.fr/live/fip-webradio4.mp3"
    json_metadata_url = "http://www.fipradio.fr/livemeta/69"

class FIPNouveauWebRadio(RadioFranceWebRadio):
    name = "FIP Tout Nouveau"
    stream_url = "http://direct.fipradio.fr/live/fip-webradio5.mp3"
    json_metadata_url = "http://www.fipradio.fr/livemeta/70"

class FIPReggaeWebRadio(RadioFranceWebRadio):
    name = "FIP Reggae"
    stream_url = "http://direct.fipradio.fr/live/fip-webradio6.mp3"
    json_metadata_url = "http://www.fipradio.fr/livemeta/71"

class FIPElectroWebRadio(RadioFranceWebRadio):
    name = "FIP Electro"
    stream_url = "http://direct.fipradio.fr/live/fip-webradio8.mp3"
    json_metadata_url = "http://www.fipradio.fr/livemeta/74"

class FranceInter(Radio):
    stream_url = "http://direct.franceinter.fr/live/franceinter-midfi.mp3"

class FranceMusique(Radio):
    name = "France Musique"
    stream_url = "http://direct.francemusique.fr/live/francemusique-midfi.mp3"

class FranceMusiqueClassiqueEasy(RadioFranceWebRadio):
    name = "France Musique Classique Easy"
    stream_url = "http://direct.francemusique.fr/live/francemusiqueeasyclassique-hifi.mp3"
    json_metadata_url = "https://www.francemusique.fr/livemeta/pull/401"

class FranceMusiqueClassiquePlus(RadioFranceWebRadio):
    name = "France Musique Classique Plus"
    stream_url = "http://direct.francemusique.fr/live/francemusiqueclassiqueplus-hifi.mp3"
    json_metadata_url = "https://www.francemusique.fr/livemeta/pull/402"

class FranceMusiqueConcerts(RadioFranceWebRadio):
    name = "France Musique Concerts"
    stream_url = "http://chai5she.cdn.dvmr.fr/francemusiqueconcertsradiofrance-hifi.mp3"
    json_metadata_url = "https://www.francemusique.fr/livemeta/pull/403"

class FranceMusiqueJazz(RadioFranceWebRadio):
    name = "France Musique Jazz"
    stream_url = "http://chai5she.cdn.dvmr.fr/francemusiquelajazz-hifi.mp3"
    json_metadata_url = "https://www.francemusique.fr/livemeta/pull/405"

class FranceMusiqueContemporaine(RadioFranceWebRadio):
    name = "France Musique Contemporaine"
    stream_url = "http://chai5she.cdn.dvmr.fr/francemusiquelacontemporaine-hifi.mp3"
    json_metadata_url = "https://www.francemusique.fr/livemeta/pull/406"

class FranceMusiqueMonde(RadioFranceWebRadio):
    name = "France Musique du Monde"
    stream_url = "http://chai5she.cdn.dvmr.fr/francemusiqueocoramonde-hifi.mp3"
    json_metadata_url = "https://www.francemusique.fr/livemeta/pull/404"

class FranceMusiqueBO(RadioFranceWebRadio):
    name = "France Musique B.O"
    stream_url = "http://chai5she.cdn.dvmr.fr/francemusiquelevenementielle-hifi.mp3"
    json_metadata_url = "https://www.francemusique.fr/livemeta/pull/407"

class LeMouv(Radio):
    stream_url = "http://direct.mouv.fr/live/mouv-midfi.mp3"

class KCSM(Radio):
    playlist_url = 'http://kcsm.org/KCSM-iTunes-SNS.pls'

    async def now_playing(self):
        url = 'http://kcsm.org/playlist'

        html = await fetch(url, raw=True)
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup('table', {'class': 'listbackground'})[0].findAll('tr')
        artist = rows[0].find('a',{'class':'artist_title'}).text.title()
        title = rows[0].findAll('td')[-1].text.title()
        album = rows[1].find('a').text.title()
        infos = SongInfos(artist, album, title, 0)
        return infos

class TripleJ(Radio):
    playlist_url = 'http://www.abc.net.au/res/streaming/audio/mp3/triplej.pls'

    async def now_playing(self):
        now = int(round(time.time()) / 3e4)
        url =  "http://www.abc.net.au/triplej/feeds/playout/triplej_sydney_playout.xml?_=%s" % now

        html_data = await fetch(url)
        soup = BeautifulSoup(html_data, 'html.parser')
        parser = html.parser.HTMLParser()
        for item in soup('item'):
            if item('playing')[0].text == 'now':
                artist = parser.unescape(item('artistname')[0].text)
                album = parser.unescape(item('albumname')[0].text)
                title = parser.unescape(item('title')[0].text)
                infos = SongInfos(artist, album, title, 0)
                infos.cover_url = parser.unescape(item('albumimage')[0].text)
                return infos
        return SongInfos('', '', '', 0)

class KEXP(Radio):
    stream_url = 'http://live-mp3-128.kexp.org/kexp128.mp3'

    async def now_playing(self):
        url = 'https://legacy-api.kexp.org/play/?limit=5&ordering=-airdate'
        default_cover_url = "http://kexp.org/static/assets/img/default.png"

        data = await fetch(url)
        infos = SongInfos('', '', '', 0)
        infos.default_cover_url = default_cover_url
        try:
            json_data = json.loads(data)
        except json.decoder.JSONDecodeError:
            return infos
        item = json_data['results'][0]
        if item['playtype']['playtypeid'] != 4: # 4 is Air break
            artist = item['artist']['name']
            title = item['track']['name']
            release = item['release']
            if release:
                album = release['name']
            else:
                album = ''
            infos = SongInfos(artist, album, title, 0)
            if release and release['largeimageuri']:
                infos.cover_url = release['largeimageuri']
        return infos

class RadioHelsinki(Radio):
    playlist_url = "http://radio.radiohelsinki.fi/rh256"
    name = "Radio Helsinki"

    async def now_playing(self):
        url = "http://www.radiohelsinki.fi/wp-content/djonline.json"

        data = await fetch(url, raw=True)
        try:
            json_data = json.loads(data)
        except json.decoder.JSONDecodeError:
            return SongInfos('', '', '', 0)
        playing = json_data['last_playing'][0]
        if playing != False:
            infos = SongInfos(playing['artist'], playing['album'], playing['song'], playing['year'])
            infos.label = playing['label']
        else:
            infos = SongInfos('', '', '', 0)

        return infos
