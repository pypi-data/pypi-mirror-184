"""

    iceweather: Look up information about Icelandic weather (observations, forecasts,
    human readable descriptive texts, etc.) using vedur.is xmlweather API.

    Copyright (c) 2019-2023 Miðeind ehf.
    Original author: Sveinbjorn Thordarson

    BSD 3-clause License (see License.txt).

"""

from typing import Iterable, List, Tuple, Dict, Union, Optional, Any, FrozenSet

import xml.etree.ElementTree as ET
import math
import re
import requests
from requests import RequestException

from .stations import STATIONS
from .util import distance

_DEFAULT_LANG: str = "is"
_SUPPORTED_LANGS: FrozenSet[str] = frozenset(("is", "en"))


_ArgType = Union[int, str, Iterable[Union[int, str]]]


def _arg_to_str_list(arg: _ArgType) -> List[str]:
    """Helper function, converts argument to a list of strings."""
    t: List[str]
    if isinstance(arg, (int, str)):
        t = [str(arg)]
    else:
        t = [str(i) for i in arg]
    return t


def _api_call(url: str) -> ET.Element:
    """Use requests to call the vedur.is weather API. Return XML tree."""
    result = requests.get(url)
    if result.status_code != 200:
        raise RequestException(f"API status code {result.status_code} for URL: {url}")

    # Remove HTML line breaks (which cause confusion in the XML parsing)
    t: str = re.sub(r"\s*(<br/>)+\s*", r" ", result.text)

    x_tree = ET.fromstring(t)
    return x_tree


_OBSERVATIONS_URL: str = (
    "https://xmlweather.vedur.is/?op_w=xml&type=obs&lang={0}&view=xml"
    "&ids={1}&params=F;FX;FG;D;T;W;V;N;P;RH;SNC;SND;SED;RTE;TD;R"
)


def observation_for_stations(station_ids: _ArgType, lang: str = _DEFAULT_LANG) -> Dict:
    """
    Returns weather observations for the given station IDs.
    Keys in the resulting dictionary are the following:

    'F'   : { 'is': 'Vindhraði (m/s)',
              'en': 'Wind speed (m/s)'},
    'FX'  : { 'is': 'Mesti vindhraði (m/s)',
              'en': 'Top wind speed (m/s)'},
    'FG'  : { 'is': 'Mesta vindhviða (m/s)',
              'en': 'Top wind gust (m/s)'},
    'D'   : { 'is': 'Vindstefna',
              'en': 'Wind direction'},
    'T'   : { 'is': 'Hiti (°C)',
              'en': 'Air temperature (°C)'},
    'W'   : { 'is': 'Veðurlýsing',
              'en': 'Weather description'},
    'V'   : { 'is': 'Skyggni (km)',
              'en': 'Visibility (km)'},
    'N'   : { 'is': 'Skýjahula (%)',
              'en': 'Cloud cover (%)'},
    'P'   : { 'is': 'Loftþrýstingur (hPa)',
              'en': 'Air pressure'},
    'RH'  : { 'is': 'Rakastig (%)',
              'en': 'Humidity (%)'},
    'SNC' : { 'is': 'Lýsing á snjó',
              'en': 'Snow description'},
    'SND' : { 'is': 'Snjódýpt',
              'en': 'Snow depth'},
    'SED' : { 'is': 'Snjólag',
              'en': 'Snow type'},
    'RTE' : { 'is': 'Vegahiti (°C)',
              'en': 'Road temperature (°C)'},
    'TD'  : { 'is': 'Daggarmark (°C)',
              'en': 'Dew limit (°C)'},
    'R'   : { 'is': 'Uppsöfnuð úrkoma (mm/klst) úr sjálfvirkum mælum',
              'en': 'Cumulative precipitation (mm/h) from automatic measuring units'}
    """
    assert lang in _SUPPORTED_LANGS

    ids = _arg_to_str_list(station_ids)
    x_tree = _api_call(_OBSERVATIONS_URL.format(lang, ";".join(ids)))
    ret_data: Dict[str, List[Dict]] = {"results": []}

    for station in x_tree:
        station_dict: Dict = {**station.attrib}

        for node in station:
            station_dict[node.tag] = node.text or ""

        ret_data["results"].append(station_dict)

    return ret_data


def observation_for_station(
    station_id: Union[str, int], lang: str = _DEFAULT_LANG
) -> Dict:
    """Returns weather observations for the given station ID.
    Wrapper for observation_for_stations."""
    assert lang in _SUPPORTED_LANGS
    assert isinstance(station_id, (str, int))

    return observation_for_stations(station_id, lang)


def observation_for_closest(
    lat: float, lon: float, lang: str = _DEFAULT_LANG, num_stations_to_try: int = 3
) -> Tuple[Dict, Dict]:
    """Returns weather observation from closest weather station given coordinates.
    Tries up to num_stations_to_try stations, returns the first one that works."""
    assert lang in _SUPPORTED_LANGS

    stations = closest_stations(lat, lon, limit=num_stations_to_try)
    for s in stations:
        o = observation_for_station(s["id"], lang=lang)
        if o["results"] and not o["results"][0].get("err") and o["results"][0]["valid"]:
            return o, s
    return observation_for_station(stations[0]["id"], lang=lang), stations[0]


_FORECASTS_URL: str = (
    "https://xmlweather.vedur.is?op_w=xml&type=forec&lang={0}&view=xml"
    "&ids={1}&params=F;FX;FG;D;T;W;V;N;P;RH;SNC;SND;SED;RTE;TD;R"
)


def forecast_for_stations(station_ids: _ArgType, lang: str = _DEFAULT_LANG) -> Dict:
    """Returns weather forecast from given weather station IDs."""
    assert lang in _SUPPORTED_LANGS

    ids = _arg_to_str_list(station_ids)
    x_tree = _api_call(_FORECASTS_URL.format(lang, ";".join(ids)))

    ret_data: Dict[str, List[Dict]] = {"results": []}

    for station in x_tree:
        station_dict: Dict[str, Any] = {**station.attrib, "forecast": []}

        for node in station:
            if node.tag == "forecast":
                forc_dict = dict()

                for x in node:
                    forc_dict[x.tag] = x.text or ""

                station_dict["forecast"].append(forc_dict)

            else:
                station_dict[node.tag] = node.text or ""

        ret_data["results"].append(station_dict)

    return ret_data


def forecast_for_station(
    station_id: Union[str, int], lang: str = _DEFAULT_LANG
) -> Dict:
    """Returns weather forecast from given weather station ID.
    Wrapper for forecast_for_stations."""
    assert lang in _SUPPORTED_LANGS
    assert isinstance(station_id, (str, int))

    return forecast_for_stations(station_id, lang)


def forecast_for_closest(
    lat: float, lon: float, lang=_DEFAULT_LANG, num_stations_to_try: int = 3
) -> Tuple[Dict, Dict]:
    """Returns weather forecast from closest weather station given coordinates."""
    assert lang in _SUPPORTED_LANGS

    stations = closest_stations(lat, lon, limit=num_stations_to_try)
    for s in stations:
        o = forecast_for_station(s["id"], lang=lang)
        if o["results"] and not o["results"][0].get("err") and o["results"][0]["valid"]:
            return o, s

    return forecast_for_station(stations[0]["id"], lang=lang), stations[0]


_TEXT_URL = "https://xmlweather.vedur.is?op_w=xml&type=txt&lang=is&view=xml&ids={0}"


def forecast_text(types: _ArgType) -> Dict:
    """Request a descriptive text from the weather API.

    Text types:

    "2" = "Veðurhorfur á landinu"
    "3" = "Veðurhorfur á höfuðborgarsvæðinu"
    "5" = "Veðurhorfur á landinu næstu daga"
    "6" = "Veðurhorfur á landinu næstu daga"
    "7" = "Weather outlook"
    "9" = "Veðuryfirlit"
    "10" = "Veðurlýsing"
    "11" = "Íslenskar viðvaranir fyrir land"
    "12" = "Veðurhorfur á landinu"
    "14" = "Enskar viðvaranir fyrir land"
    "27" = "Weather forecast for the next several days"
    "30" = "Miðhálendið"
    "31" = "Suðurland"
    "32" = "Faxaflói"
    "33" = "Breiðafjörður"
    "34" = "Vestfirðir"
    "35" = "Strandir og Norðurland vestra"
    "36" = "Norðurlandi eystra"
    "37" = "Austurland að Glettingi"
    "38" = "Austfirðir"
    "39" = "Suðausturland"
    "42" = "General synopsis
    """

    t = _arg_to_str_list(types)

    x_tree = _api_call(_TEXT_URL.format(";".join(t)))

    ret_data: Dict[str, List[Dict]] = {"results": []}

    for text in x_tree:
        text_dict = {**text.attrib}

        for node in text:
            text_dict[node.tag] = node.text or ""

        ret_data["results"].append(text_dict)

    return ret_data


def station_list() -> List[Dict]:
    """Return a list of all weather stations in Iceland."""
    return STATIONS


def closest_stations(lat: float, lon: float, limit: int = 1) -> List[Dict]:
    """Find the weather station closest to the given location."""
    dist_sorted = sorted(
        STATIONS, key=lambda s: distance((lat, lon), (s["lat"], s["lon"]))
    )
    return dist_sorted[:limit]


def id_for_station(station_name: str) -> Optional[int]:
    """Return the numerical ID for a weather station, given its name."""
    for s in STATIONS:
        if s["name"] == station_name:
            return s["id"]
    return None


def station_for_id(station_id: int) -> Optional[Dict]:
    """Return the name of a weather station, given its numerical ID."""
    for s in STATIONS:
        if s["id"] == station_id:
            return s
    return None
