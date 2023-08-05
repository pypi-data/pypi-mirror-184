import logging
import sys
import os
import json
import requests
from typing import Optional
from urllib.parse import urljoin

def merge_dict(a, b, path=[]):
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dict(a[key], b[key], path + [str(key)])
            elif isinstance(a[key], list) and isinstance(b[key], dict):
                a[key] = list(set(a[key]).union(b[key]))
            elif isinstance(b[key], type(a[key])):
                pass # no change
            else:
                raise Exception(f"Conflict at {'.'.join(path + [str(key)])}")
        else:
            a[key] = b[key]
    return a


"""API documentation found at https://popcornofficial.docs.apiary.io/ and https://popcorn-official.github.io/popcorn-api/identifiers.html"""
class PopcornTime:
    _CONFIG = {}
    _config_file = os.path.dirname(__file__) + "/config.json"

    def __init__(self, languages: list[str]=["en","fr"]) -> None:
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        self.log.addHandler(logging.StreamHandler(sys.stdout))

        self._languages = languages

        with open(self._config_file, "r") as file:
            config = json.loads("".join(file.readlines()))
            if not "apis" in config:
                config["apis"] = []
            if not "cam_keywords" in config:
                config["cam_keywords"] = []
            
            self._CONFIG = config

    def _save_config(self) -> None:
        with open(self._config_file, "w") as file:
            config = json.dumps(self._CONFIG, indent=4)
            file.write(config)

    @property
    def _APIS(self) -> list[str]:
        return self._CONFIG["apis"]
    
    @property
    def _CAM_KEYWORDS(self) -> list[str]:
        return self._CONFIG["cam_keywords"]

    @_APIS.setter
    def _APIS(self, apis: list[str]):
        self._CONFIG["apis"] = apis
        self._save_config()
    
    @_CAM_KEYWORDS.setter
    def _CAM_KEYWORDS(self, keywords: list[str]):
        self._CONFIG["cam_keywords"] = keywords
        self._save_config()

    def _get(self, url: str, **kwargs) -> Optional[list | dict]:
        """Performs a get request to the target url

        Parameters
        ----------
        url : target url

        Returns
        -------
        Optional[list | dict]
            response under the form of a list or a dict
        """
        try:
            req = requests.get(url, **kwargs)
        except requests.exceptions.ConnectionError as e:
            self.log.error(f'Request to {url!r} failed with {e.__class__.__name__!r}')
            return None

        if req.status_code != 200:
            self.log.error(f'Request to {url!r} failed with status code {req.status_code!r}')
            return None
        return req.json()

    def _api_urls(self, path: str) -> list[str]:
        """Gets a url with specified path for every known api

        Parameters
        ----------
        path : target path

        Returns
        -------
        list[str]
            list of all target urls
        """

        return [urljoin(url, path) for url in self._APIS]

    def _get_api_page(self, search: Optional[str], urls: list[str], lang: Optional[str]) -> Optional[list[dict]]:
        """Gets a page of movies/shows/animes from the apis

        Parameters
        ----------
        urls : list[str]
            api urls

        Returns
        -------
        list[dict]
            list containing the combined items from the apis
        """

        if not urls:
            return None

        params = {
            "sort": "trending",
            "limit": 50,
            "order": -1
        }

        if search:
            params["keywords"] = search

        if lang:
            params["contentLocale"] = lang
        else:
            params["showAll"] = 1

        items = {}
        for url in urls:
            res: list[dict] = self._get(url, params=params)
            if not res:
                continue
            for item in res:
                if item["_id"] in items:
                    items[item["_id"]] = merge_dict(items[item["_id"]], item)
                else:
                    items[item["_id"]] = item

        return [m for m in items.values()]

    def _get_api_item(self, urls: list[str], lang: Optional[str]) -> Optional[dict]:
        """Gets details about a movie/show/anime from the apis

        Parameters
        ----------
        urls : list[str]
            api urls

        Returns
        -------
        dict
            dict containing the combined items from the apis
        """

        if not urls:
            return None

        params = {"showAll": 1}

        movie = {}
        for url in urls:
            res: dict = self._get(url, params=params)
            if not res:
                continue
            movie = merge_dict(movie, res)

        return movie


    def get_movies_page(self, *, search: Optional[str]=None, page: int=1, lang: Optional[str]=None) -> Optional[list[dict]]:
        """Gets a page of movies from the apis

        Parameters
        ----------
        page : int, optional
            page number, by default 0

        Returns
        -------
        list[dict]
            list containing each movie's informations
        """
        
        return self._get_api_page(search, self._api_urls(f"/movies/{page}"), lang)

    def get_movie(self, movie_id: str) -> Optional[dict]:
        """Gets a movie's info from the apis

        Parameters
        ----------
        movie_id : str
            id of the movie (same as the imdb id)

        Returns
        -------
        Optional[dict]
            dict containing the movie's informations
        """
        return self._get_api_item(self._api_urls(f"/movie/{movie_id}"), None)

    def get_shows_page(self, *, search: Optional[str]=None, page: int=1, lang: Optional[str]=None) -> Optional[list[dict]]:
        """Gets a page of shows from the apis

        Parameters
        ----------
        page : int, optional
            page number, by default 0

        Returns
        -------
        list[dict]
            list containing each show's informations
        """

        return self._get_api_page(search, self._api_urls(f"/shows/{page}"), lang)

    def get_show(self, show_id: str) -> Optional[dict]:
        """Gets a show's info from the apis

        Parameters
        ----------
        show_id : str
            id of the show (same as the imdb id)

        Returns
        -------
        Optional[dict]
            dict containing the show's informations
        """
        return self._get_api_item(self._api_urls(f"/show/{show_id}"), None)

    def get_animes_page(self, *, search: Optional[str]=None, page: int=1, lang: Optional[str]=None) -> Optional[list[dict]]:
        """Gets a page of animes from the apis

        Parameters
        ----------
        page : int, optional
            page number, by default 0

        Returns
        -------
        list[dict]
            list containing each anime's informations
        """
        
        return self._get_api_page(search, self._api_urls(f"/animes/{page}"), lang)

    def get_anime(self, anime_id: str) -> Optional[dict]:
        """Gets a anime's info from the apis

        Parameters
        ----------
        anime_id : str
            id of the anime (same as the imdb id)

        Returns
        -------
        Optional[dict]
            dict containing the anime's informations
        """
        return self._get_api_item(self._api_urls(f"/anime/{anime_id}"), None)

    def remove_cam_torrents(self, torrents: dict) -> tuple[dict, dict]:
        """Tries to split the torrents filmed by cameras inside the cinema
        and the ones from normal original sources (success may vary)

        Parameters
        ----------
        torrents : dict
            The torrents to split

        Returns
        -------
        tuple[dict, dict]
            [0]: The non cam torrents
            [1]: the cam torrents
        """

        cam_torrents = {}
        non_cam_torrents = {}
        
        for quality, torrent in torrents.items():
            url = torrent['url']
            if any(keyword in url for keyword in self._CAM_KEYWORDS):
                cam_torrents[quality] = torrent
            else:
                non_cam_torrents[quality] = torrent

        return cam_torrents, non_cam_torrents

    def filter_languages(self, api_res: list[dict]):
        pass