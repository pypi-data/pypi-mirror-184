import time
from datetime import datetime
from typing import List, Dict, Union, Type

from mext import models, enums
from mext.models.model import Model

from mext.exceptions import *
from mext.provider import Provider

# Copy from https://github.com/Proxymiity/MangaDex.py

INCLUDE_ALL = ["cover_art", "manga", "chapter", "scanlation_group",
               "author", "artist", "user", "leader", "member"]


class MangadexLinkNames(enums.AttributeEnum):
    Anilist = 'al'
    AnimePlanet = 'ap'
    Bookwalker = 'bw'
    Mangaupdates = 'mu'
    Novelupdates = 'nu'
    Kitsu = 'kt'
    Amazon = 'amz'
    eBookJapan = 'ebj'
    MyAnimeList = 'mal'
    CDJapan = 'cdj'
    Raw = 'raw'
    OfficialEnglishTL = 'engtl'


mangadex_language_map = {
    'zh-hk': 'zh',
    'zh-ro': 'zh',
    'ja-ro': 'ja',
    'ko-ro': 'ko',
}


class MangadexOrg(Provider):

    def __init__(self, *args, **kwargs):
        self.language = "en"
        super(MangadexOrg, self).__init__(*args, **kwargs)

        self.rate_limit = 0.25
        self.api_url = "https://api.mangadex.org"
        self.net_api_url = "https://api.mangadex.network"

    def process_url(self, url):
        super().process_url(url)

    def get_uuid(self, url):
        self.process_url(url)
        return self.parsed_url.path.split('/')[2]

    def populate_manga_data(self, data) -> models.Manga:
        manga = models.Manga(self)

        manga.id = data.get("id")
        manga.url = f"https://{self.siteUrl}/title/{manga.id}"

        _attrs = data.get("attributes")
        _rel = data.get("relationships", [])

        manga.title = _attrs.get("title").get("en")
        if not manga.title:
            return None

        manga.alts = [list(alt_dict.values())[0]
                      for alt_dict in _attrs.get("altTitles")]
        manga.description = _attrs.get("description").get("en")

        _original_language = _attrs.get("originalLanguage").lower()

        if _original_language in mangadex_language_map:
            manga.language = mangadex_language_map[_original_language]
        else:
            manga.language = _original_language

        manga.comic_type = enums.ComicTypesLanguage[
            data.get("type").lower()
        ].name.title()
        # manga.last_chapter = _attrs.get("lastChapter")

        demo_genre = models.Genre(self)
        demo_genre.name = (
            _attrs.get("publicationDemographic") or ""
        ).title()

        manga.status = enums.StatusTypes(
            _attrs.get("status").lower()
        ).name
        manga.year = int(_attrs.get("year") or manga.year)
        
        _content_rating = _attrs.get("contentRating") or enums.ContentRatingTypes.Safe
        manga.content_rating = enums.ContentRatingTypes(_content_rating).value

        manga.created_at = datetime.fromisoformat(_attrs.get("createdAt"))
        manga.updated_at = datetime.fromisoformat(_attrs.get("updatedAt"))

        try:
            links = []

            if _attrs.get("links"):

                for link_key, link_value in _attrs.get("links").items():
                    link = models.Link(self)
                    link.name = MangadexLinkNames(link_key).name
                    link.link = link_value
                    links.append(link)

                manga.links = links
        except Exception as e:
            print("Exception getting Link:\n", e)

        try:
            genres = []

            if _attrs.get("tags"):

                for genre_attr in _attrs.get("tags"):
                    genre = models.Genre(self)
                    genre.name = genre_attr["attributes"]["name"].get("en")

                    if not genre.name:
                        continue

                    genres.append(genre)
                manga.genres = genres
        except Exception as e:
            print("Exception getting Genre:\n", e)

        try:
            authors = []

            _author_list = [
                x["attributes"] for x in _rel if x["type"] == "author"
            ]

            for author_rel in _author_list:
                author = models.Person(self)
                author.name = author_rel["name"]
                authors.append(author)

            manga.authors = authors
        except (IndexError, KeyError) as e:
            print("Exception getting Authors:\n", e)

        try:
            artists = []

            _artist_list = [
                x["attributes"] for x in _rel if x["type"] == "artist"
            ]
            for artist_rel in _artist_list:
                artist = models.Person(self)
                artist.name = artist_rel["name"]
                artists.append(artist)

            manga.artists = artists
        except (IndexError, KeyError) as e:
            print("Exception getting Artists:\n", e)

        try:
            covers = []
            _cover_list = [
                x["attributes"] for x in _rel if x["type"] == "cover_art"
            ]

            for cover_rel in _cover_list:
                cover = models.Cover(self)
                cover.volume = float(cover_rel.get("volume") or 0)
                cover.filename = cover_rel.get("fileName")
                cover.image_link = f"https://uploads.mangadex.org/covers/{manga.id}/{cover.filename}"
                covers.append(cover)

            manga.all_covers = covers

            if covers:
                manga.current_cover = covers[-1]

        except (IndexError, KeyError) as e:
            print("Exception getting Covers:\n", e)

        return manga

    def populate_chapter_data(self, data):
        chapter = models.Chapter(self)
        chapter.id = data.get("id")
        chapter.url = f"https://{self.siteUrl}/chapter/{chapter.id}"

        _attrs = data.get("attributes")
        _rel = data.get("relationships", [])
        chapter.volume = float(_attrs.get("volume") or 0)
        chapter.number = (_attrs.get("chapter") or "")
        chapter.page_count = int(_attrs.get("pages"))

        chapter.name = (_attrs.get("title") or "")
        chapter.language = _attrs.get("translatedLanguage").lower()
        chapter.created_at = datetime.fromisoformat(
            _attrs.get("publishAt")
        )
        chapter.updated_at = datetime.fromisoformat(
            _attrs.get("updatedAt")
        )

        return chapter

    def get_latest(self, url: str, params: Dict) -> List[models.Manga]:
        includes = INCLUDE_ALL
        params = params or {}
        if includes:
            params = {"includes[]": includes}
        params = {
            **params,
            "translatedLanguage[]": "en",
            "order[readableAt]": "desc",
            "limit": 100,
        }
        req = self.client.http.get(
            f"{self.api_url}/chapter",
            params=params
        )
        if req.status_code == 200:
            resp = req.json()
            data_list = resp["data"]

            latest_list = []
            for data in data_list:

                _rel = data["relationships"]
                _manga = [
                    x for x in _rel if x["type"] == "manga"
                ][0]

                manga = self.populate_manga_data(_manga)
                if not manga:
                    continue

                latest_list.append(manga)

            return latest_list
        elif req.status_code == 404:
            raise NoContentError(req)
        else:
            raise APIError(req)

    def get_manga(self, url, params) -> models.Manga:

        uuid = self.get_uuid(url)
        includes = INCLUDE_ALL
        params = params or {}
        if includes:
            params = {"includes[]": includes}
        req = self.client.http.get(
            f"{self.api_url}/manga/{uuid}", params=params)
        if req.status_code == 200:
            resp = req.json()
            data = resp["data"]

            manga = self.populate_manga_data(data)
            if not manga:
                raise Exception(f"Error getting manga details for ID {uuid}")

            manga.url = url

            return manga
        elif req.status_code == 404:
            raise NoContentError(req)
        else:
            raise APIError(req)

    def get_chapter(self, url, params) -> models.Chapter:
        uuid = self.get_uuid(url)
        includes = INCLUDE_ALL
        params = params or {}
        if includes:
            params = {"includes[]": includes}
        req = self.client.http.get(
            f"{self.api_url}/chapter/{uuid}",
            params=params
        )
        if req.status_code == 200:
            resp = req.json()
            data = resp["data"]

            chapter = self.populate_chapter_data(data)
            chapter.url = url

            return self.read_chapter(chapter)
        elif req.status_code == 404:
            raise NoContentError(req)
        else:
            raise APIError(req)

    def get_manga_chapters(self, url, params) -> List[models.Chapter]:
        uuid = self.get_uuid(url)
        includes = INCLUDE_ALL
        params = params or {
            "translatedLanguage[]": "en",
            "order[chapter]": "desc",
        }
        if includes:
            params["includes[]"] = includes
        return self._retrieve_chapters(
            f"{self.api_url}/manga/{uuid}/feed",
            models.Chapter,
            call_limit=100,
            params=params
        )

    def get_cover(self, url, params) -> models.Cover:
        uuid = self.get_uuid(url)
        req = self.client.http.get(f"{self.api_url}/cover/{uuid}")
        if req.status_code == 200:
            resp = req.json()
            return models.Cover(resp["data"], self)
        elif req.status_code == 404:
            raise NoContentError(req)
        else:
            raise APIError(req)

    def read_chapter(self, chapter: models.Chapter) -> models.Chapter:
        uuid = chapter.id
        params = {"forcePort443": False}
        req = self.client.http.get(
            f"{self.api_url}/at-home/server/{uuid}", params=params
        )
        if req.status_code == 200:
            data = req.json()

            base_url = data.get("baseUrl")
            _ch = data.get("chapter")
            hash = _ch.get("hash")
            files = _ch.get("data")
            pages = []

            for filename in files:
                page = models.Page(self)
                page.image_link = f"{base_url}/data/{hash}/{filename}"
                pages.append(page)

            chapter.pages = pages

            return chapter
        else:
            raise APIError(req)

    def _retrieve_chapters(self, url: str, chapter: models.Chapter,
                           limit: int = 0, call_limit: int = 500,
                           params: dict = None) -> List[models.Chapter]:
        params = params or {}
        data = []
        offset = 0
        resp = None
        remaining = True
        if "limit" in params:
            params.pop("limit")
        if "offset" in params:
            params.pop("offset")
        while remaining:
            p = {
                "limit": limit if limit <= call_limit and
                limit != 0 else call_limit,
                "offset": offset
            }
            p = {**p, **params}
            req = self.client.http.get(url, params=p)
            if req.status_code == 200:
                resp = req.json()
                data += [x for x in resp["data"]]
            elif req.status_code == 204:
                pass
            else:
                raise APIError(req)
            if limit and len(data) >= limit:
                break
            if resp is not None:
                remaining = resp["total"] > offset + call_limit
                offset += call_limit
            else:
                remaining = False
            if remaining:
                time.sleep(self.rate_limit)
        if not data:
            raise NoResultsError()
        return [self.populate_chapter_data(x) for x in data if int(x["attributes"]["pages"]) > 0]
