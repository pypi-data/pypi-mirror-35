#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Top-level package for Trainline."""

import requests
from requests import ConnectionError
import json
from datetime import datetime, timedelta
import pytz
import time

__author__ = """Thibault Ducret"""
__email__ = 'hello@tducret.com'
__version__ = '0.0.1'

_SEARCH_URL = "https://www.trainline.eu/api/v5_1/search"
_DEFAULT_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
_BIRTHDATE_FORMAT = '%d/%m/%Y'
_READABLE_DATE_FORMAT = "%d/%m/%Y %H:%M"
_DEFAULT_SEARCH_TIMEZONE = 'Europe/Paris'
_MAX_SERVER_RETRY = 3  # If a request is rejected, retry X times
_TIME_AFTER_FAILED_REQUEST = 10  # and wait Y seconds after a rejected request

ENFANT_PLUS = "ENFANT_PLUS"
JEUNE = "JEUNE"
_AVAILABLE_CARDS = [ENFANT_PLUS, JEUNE]


class Client(object):
    """ Do the requests with the servers """
    def __init__(self):
        self.session = requests.session()
        self.headers = {
                    'Accept': 'application/json',
                    'User-Agent': 'CaptainTrain/43(4302) Android/4.4.2(19)',
                    'Accept-Language': 'fr',
                    'Content-Type': 'application/json; charset=UTF-8',
                    'Host': 'www.trainline.eu',
                    }

    def _get(self, url, expected_status_code=200):
        ret = self.session.get(url=url, headers=self.headers)
        if (ret.status_code != expected_status_code):
            raise ConnectionError(
                'Status code {status} for url {url}\n{content}'.format(
                    status=ret.status_code, url=url, content=ret.text))
        return ret

    def _post(self, url, post_data, expected_status_code=200):
        trials = 0
        while trials <= _MAX_SERVER_RETRY:
            trials += 1
            ret = self.session.post(url=url,
                                    headers=self.headers,
                                    data=post_data)
            if (ret.status_code == expected_status_code):
                break
            else:
                time.sleep(_TIME_AFTER_FAILED_REQUEST)

        if (ret.status_code != expected_status_code):
                raise ConnectionError(
                    'Status code {status} for url {url}\n{content}'.format(
                        status=ret.status_code, url=url, content=ret.text))
        return ret


class Trainline(object):
    """ Class to... """
    def __init__(self):
        pass

    def search(self, departure_station_id, arrival_station_id, departure_date):
        """ Search on Trainline """
        data = {
              "local_currency": "EUR",
              "search": {
                "passengers": [
                  {
                    "id": "90ec4e55-f6f1-4298-bb02-7dd88fe33fca",
                    "age": 26,
                    "cards": [],
                    "label": "90ec4e55-f6f1-4298-bb02-7dd88fe33fca"
                  }
                ],
                "arrival_station_id": arrival_station_id,
                "departure_date": departure_date,
                "departure_station_id": departure_station_id,
                "systems": [
                  "benerail",
                  "busbud",
                  "db",
                  "hkx",
                  "idtgv",
                  "locomore",
                  "ntv",
                  "ocebo",
                  "ouigo",
                  "ravel",
                  "renfe",
                  "sncf",
                  "timetable",
                  "trenitalia",
                  "westbahn",
                  "flixbus",
                  "pao_ouigo",
                  "pao_sncf",
                  "leoexpress",
                  "city_airport_train",
                  "obb",
                  "distribusion"
                ]
              }
            }
        post_data = json.dumps(data)
        c = Client()
        ret = c._post(url=_SEARCH_URL, post_data=post_data)
        return ret


class Trips(object):
    """ Class to represent a list of trips """
    def __init__(self, trip_list):
        self.trips = trip_list

    def csv(self):
        csv_str = "departure_date;arrival_date;duration;number_of_segments;\
price;currency\n"
        for trip in self.trips:
            trip_duration = (trip.arrival_date_obj-trip.departure_date_obj)
            csv_str += "{dep};{arr};{dur};{seg};{price};{curr}\n".format(
                dep=trip.departure_date_obj.strftime(_READABLE_DATE_FORMAT),
                arr=trip.arrival_date_obj.strftime(_READABLE_DATE_FORMAT),
                dur=_strfdelta(trip_duration, "{hours:02d}h{minutes:02d}"),
                seg=len(trip.segments),
                price=str(trip.price).replace(".", ","),  # For French Excel
                curr=trip.currency,
                )
        return csv_str

    def __len__(self):
        return len(self.trips)

    def __getitem__(self, key):
        """ Method to access the object as a list
        (ex : trips[1]) """
        return self.trips[key]


class Trip(object):
    """ Class to represent a trip, composed of one or more segments """
    def __init__(self, mydict):
        expected = {
            "id": str,
            "departure_date": str,
            "departure_station_id": str,
            "arrival_date": str,
            "arrival_station_id": str,
            "price": float,
            "currency": str,
            "segment_ids": list,
            "segments": list,
        }

        for expected_param, expected_type in expected.items():
            param_value = mydict.get(expected_param)
            if type(param_value) is not expected_type:
                raise TypeError("Type {} expected for {}, {} received".format(
                    expected_type, expected_param, type(param_value)))
            setattr(self, expected_param, param_value)

        # Remove ':' in the +02:00 offset (=> +0200). It caused problem with
        # Python 3.6 version of strptime
        self.departure_date = _fix_date_offset_format(self.departure_date)
        self.arrival_date = _fix_date_offset_format(self.arrival_date)

        self.departure_date_obj = _str_datetime_to_datetime_obj(
            str_datetime=self.departure_date)
        self.arrival_date_obj = _str_datetime_to_datetime_obj(
            str_datetime=self.arrival_date)

        if self.price < 0:
            raise ValueError("price cannot be < 0, {} received".format(
                self.price))

    def __str__(self):
        return("{} → {} : {} {} ({} segments) [id : {}]".format(
            self.departure_date, self.arrival_date, self.price, self.currency,
            len(self.segment_ids), self.id))

    # __hash__ and __eq__ methods are defined to allow to remove duplicates
    # in the results with list(set(trip_list))
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash((self.id))


class Passenger(object):
    """ Class to represent a passenger """
    def __init__(self, birthdate, cards=[]):
        self.birthdate = birthdate
        self.birthdate_obj = _str_date_to_date_obj(
            str_date=self.birthdate,
            date_format=_BIRTHDATE_FORMAT)

        for card in cards:
            if card not in _AVAILABLE_CARDS:
                raise KeyError("Card '{}' unknown, [{}] available".format(
                    card, ",".join(_AVAILABLE_CARDS)))
        self.cards = cards

    def __str__(self):
        return(repr(self))

    def __repr__(self):
        return("Passenger(birthdate={}, cards=[{}])".format(
            self.birthdate,
            ",".join(self.cards)))


class Segment(object):
    """ Class to represent a segment
    (a trip is composed of one or more segment) """
    def __init__(self, mydict):
        expected = {
            "id": str,
            "departure_date": str,
            "departure_station_id": str,
            "arrival_date": str,
            "arrival_station_id": str,
            "transportation_mean": str,
            "carrier": str,
            "train_number": str,
            "travel_class": str,
            "trip_id": str,
            "comfort_class_ids": list,
            "comfort_classes": list,
        }

        for expected_param, expected_type in expected.items():
            param_value = mydict.get(expected_param)
            if type(param_value) is not expected_type:
                raise TypeError("Type {} expected for {}, {} received".format(
                    expected_type, expected_param, type(param_value)))
            setattr(self, expected_param, param_value)

        # Remove ':' in the +02:00 offset (=> +0200). It caused problem with
        # Python 3.6 version of strptime
        self.departure_date = _fix_date_offset_format(self.departure_date)
        self.arrival_date = _fix_date_offset_format(self.arrival_date)

        self.departure_date_obj = _str_datetime_to_datetime_obj(
            str_datetime=self.departure_date)
        self.arrival_date_obj = _str_datetime_to_datetime_obj(
            str_datetime=self.arrival_date)

        self.bicycle_with_reservation = \
            self._check_extra_value("bicycle_with_reservation")
        self.bicycle_without_reservation = \
            self._check_extra_value("bicycle_without_reservation")

    def __str__(self):
        return("{} → {} : {} ({}) ({} comfort_class) [id : {}]".format(
            self.departure_date, self.arrival_date,
            self.transportation_mean, self.carrier,
            len(self.comfort_class_ids), self.id))

    # __hash__ and __eq__ methods are defined to allow to remove duplicates
    # in the results with list(set(segment_list))
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash((self.id))

    def _check_extra_value(self, value):
        """ Returns True if the segment has an extra
        with the specified value """
        res = False
        for comfort_class in self.comfort_classes:
            for extra in comfort_class.extras:
                if extra.get("value", "") == value:
                    res = True
                    break
        return res


class ComfortClass(object):
    """ Class to represent a comfort_class
    (a trip is composed of one or more segment,
    each one composed of one or more comfort_class) """
    def __init__(self, mydict):
        expected = {
            "id": str,
            "name": str,
            "description": str,
            "title": str,
            "options": dict,
            "segment_id": str,
            "condition_id": str,
        }

        for expected_param, expected_type in expected.items():
            param_value = mydict.get(expected_param)
            if type(param_value) is not expected_type:
                raise TypeError("Type {} expected for {}, {} received".format(
                    expected_type, expected_param, type(param_value)))
            setattr(self, expected_param, param_value)

        self.extras = self.options.get("extras", [])

    def __str__(self):
        return("{} {} ({}) ({} extras) [id : {}]".format(
            self.name,
            self.title,
            self.description,
            len(self.extras),
            self.id))

    # __hash__ and __eq__ methods are defined to allow to remove duplicates
    # in the results with list(set(comfort_class_list))
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash((self.id))


def _str_datetime_to_datetime_obj(str_datetime,
                                  date_format=_DEFAULT_DATE_FORMAT):
    """ Check the expected format of the string date and returns a datetime
    object """
    try:
        datetime_obj = datetime.strptime(str_datetime, date_format)
    except:
        raise TypeError("date must match the format {}, received : {}".format(
            date_format, str_datetime))
    if datetime_obj.tzinfo is None:
        tz = pytz.timezone(_DEFAULT_SEARCH_TIMEZONE)
        datetime_obj = tz.localize(datetime_obj)
    return datetime_obj


def _str_date_to_date_obj(str_date, date_format=_BIRTHDATE_FORMAT):
    """ Check the expected format of the string date and returns a datetime
    object """
    try:
        date_obj = datetime.strptime(str_date, date_format)
    except:
        raise TypeError("date must match the format {}, received : {}".format(
            date_format, str_date))
    return date_obj


def _fix_date_offset_format(date_str):
    """ Remove ':' in the UTC offset, for example :
    >>> print(_fix_date_offset_format("2018-10-15T08:49:00+02:00"))
    2018-10-15T08:49:00+0200
    """
    return date_str[:-3]+date_str[-2:]


def get_station_id(station_name):
    # TODO : Use trainline station database instead
    # https://github.com/trainline-eu/stations
    # https://raw.githubusercontent.com/trainline-eu/stations/master/stations.csv
    _AVAILABLE_STATIONS = {
        "Toulouse": "5306",
        "Toulouse Matabiau": "5311",
        "Bordeaux": "827",
        "Bordeaux St-Jean": "828",
        "Carcassonne": "1119",
        "Paris": "4916",
        "Narbonne": "5806",
    }
    return _AVAILABLE_STATIONS[station_name]


def search(departure_station, arrival_station,
           from_date, to_date, passengers=[],
           transportation_mean=None,
           bicycle_without_reservation_only=None,
           bicycle_with_reservation_only=None,
           bicycle_with_or_without_reservation=None):
    t = Trainline()

    departure_station_id = get_station_id(departure_station)
    arrival_station_id = get_station_id(arrival_station)

    from_date_obj = _str_datetime_to_datetime_obj(
        str_datetime=from_date, date_format=_READABLE_DATE_FORMAT)

    to_date_obj = _str_datetime_to_datetime_obj(
        str_datetime=to_date, date_format=_READABLE_DATE_FORMAT)

    trip_list = []

    search_date = from_date_obj

    while True:

        last_search_date = search_date
        departure_date = search_date.strftime(_DEFAULT_DATE_FORMAT)

        ret = t.search(
            departure_station_id=departure_station_id,
            arrival_station_id=arrival_station_id,
            departure_date=departure_date)
        j = json.loads(ret.text)
        trips = _get_trips(search_results_obj=j)
        trip_list += trips

        # Check the departure date of the last trip found
        # If it is after the 'to_date', we can stop searching
        if trips[-1].departure_date_obj > to_date_obj:
            break
        else:
            search_date = trips[-1].departure_date_obj
            # If we get a date earlier than the last search date,
            # it means that we may be searching during the night,
            # so we must increment the search_date till we have a
            # trip posterior to 'to_date'
            # Probably the next day in this case
            if search_date <= last_search_date:
                search_date = last_search_date + timedelta(hours=4)
    trip_list = list(set(trip_list))  # Remove duplicate trips in the list

    # Filter the list
    bicycle_w_or_wout_reservation = bicycle_with_or_without_reservation
    filtered_trip_list = _filter_trips(
        trip_list=trip_list,
        from_date_obj=from_date_obj,
        to_date_obj=to_date_obj,
        transportation_mean=transportation_mean,
        bicycle_without_reservation_only=bicycle_without_reservation_only,
        bicycle_with_reservation_only=bicycle_with_reservation_only,
        bicycle_with_or_without_reservation=bicycle_w_or_wout_reservation)

    # Sort by date
    filtered_trip_list = sorted(filtered_trip_list,
                                key=lambda trip: trip.departure_date_obj)

    trip_list_obj = Trips(filtered_trip_list)
    return trip_list_obj


def _convert_date_format(origin_date_str,
                         origin_date_format, target_date_format):
    """ Convert a date string to another format, for example :
    >>> print(_convert_date_format(origin_date_str="01/01/2002 08:00",\
origin_date_format="%d/%m/%Y %H:%M", target_date_format="%Y-%m-%dT%H:%M:%S%z"))
    2002-01-01T08:00:00+0100
    """
    date_obj = _str_datetime_to_datetime_obj(str_datetime=origin_date_str,
                                             date_format=origin_date_format)
    return date_obj.strftime(target_date_format)


def _get_trips(search_results_obj):
    """ Get trips from the json object of search results """
    segment_obj_list = _get_segments(search_results_obj)
    trips = search_results_obj.get("trips")
    trip_obj_list = []
    for trip in trips:
        dict_trip = {
            "id": trip.get("id"),
            "departure_date": trip.get("departure_date"),
            "departure_station_id": trip.get("departure_station_id"),
            "arrival_date": trip.get("arrival_date"),
            "arrival_station_id": trip.get("arrival_station_id"),
            "price": float(trip.get("cents"))/100,
            "currency": trip.get("currency"),
            "segment_ids": trip.get("segment_ids"),
        }
        segments = []
        for segment_id in dict_trip["segment_ids"]:
            segment_found = _get_segment_from_id(
                segment_obj_list=segment_obj_list,
                segment_id=segment_id)
            if segment_found:
                segments.append(segment_found)
            else:
                # Remove the id if the object is invalid or not found
                dict_trip["segment_ids"].remove(segment_id)
        dict_trip["segments"] = segments

        trip_obj = Trip(dict_trip)
        trip_obj_list.append(trip_obj)
    return trip_obj_list


def _get_segments(search_results_obj):
    """ Get segments from the json object of search results """
    comfort_class_obj_list = _get_comfort_classes(search_results_obj)
    segments = search_results_obj.get("segments")
    segment_obj_list = []
    for segment in segments:
        comfort_class_ids = segment.get("comfort_class_ids")
        if comfort_class_ids is None:
            comfort_class_ids = []
        dict_segment = {
            "id": segment.get("id"),
            "departure_date": segment.get("departure_date"),
            "departure_station_id": segment.get("departure_station_id"),
            "arrival_date": segment.get("arrival_date"),
            "arrival_station_id": segment.get("arrival_station_id"),
            "transportation_mean": segment.get("transportation_mean"),
            "carrier": segment.get("carrier"),
            "train_number": segment.get("train_number"),
            "travel_class": segment.get("travel_class"),
            "trip_id": segment.get("trip_id"),
            "comfort_class_ids": comfort_class_ids,
        }
        comfort_classes = []
        for comfort_class_id in dict_segment["comfort_class_ids"]:
            comfort_class_found = _get_comfort_class_from_id(
                comfort_class_obj_list=comfort_class_obj_list,
                comfort_class_id=comfort_class_id)
            if comfort_class_found:
                comfort_classes.append(comfort_class_found)
            else:
                # Remove the id if the object is invalid or not found
                dict_segment["comfort_class_ids"].remove(comfort_class_id)
        dict_segment["comfort_classes"] = comfort_classes
        try:
            segment_obj = Segment(dict_segment)
            segment_obj_list.append(segment_obj)
        except TypeError:
            pass
            # Do not add a segment if it is not contain all the required fields
    return segment_obj_list


def _get_segment_from_id(segment_obj_list, segment_id):
    """ Get a segment from a list, based on a segment id """
    found_segment_obj = None
    for segment_obj in segment_obj_list:
        if segment_obj.id == segment_id:
            found_segment_obj = segment_obj
            break
    return found_segment_obj


def _get_comfort_classes(search_results_obj):
    """ Get comfort classes from the json object of search results """
    comfort_classes = search_results_obj.get("comfort_classes")
    if comfort_classes is None:
        comfort_classes = []
    comfort_class_obj_list = []
    for comfort_class in comfort_classes:
        description = comfort_class.get("description")
        if description is None:
            description = ""
        title = comfort_class.get("title")
        if title is None:
            title = ""
        dict_comfort_class = {
            "id": comfort_class.get("id"),
            "name": comfort_class.get("name"),
            "description": description,
            "title": title,
            "options": comfort_class.get("options"),
            "segment_id": comfort_class.get("segment_id"),
            "condition_id": comfort_class.get("condition_id"),
        }
        comfort_class_obj = ComfortClass(dict_comfort_class)
        comfort_class_obj_list.append(comfort_class_obj)
    return comfort_class_obj_list


def _get_comfort_class_from_id(comfort_class_obj_list, comfort_class_id):
    """ Get a comfort_class from a list, based on a comfort_class id """
    found_comfort_class_obj = None
    for comfort_class_obj in comfort_class_obj_list:
        if comfort_class_obj.id == comfort_class_id:
            found_comfort_class_obj = comfort_class_obj
            break
    return found_comfort_class_obj


def _filter_trips(trip_list, from_date_obj=None, to_date_obj=None,
                  min_price=0.1, max_price=None, transportation_mean=None,
                  min_segment_nb=1, max_segment_nb=None,
                  bicycle_without_reservation_only=None,
                  bicycle_with_reservation_only=None,
                  bicycle_with_or_without_reservation=None):
    """ Filter a list of trips, based on different attributes, such as
    from_date or min_price. Returns the filtered list """
    filtered_trip_list = []
    for trip in trip_list:
        to_be_filtered = False

        # Price
        if trip.price < min_price:
            to_be_filtered = True
        if max_price:
            if trip.price > max_price:
                to_be_filtered = True

        # Date
        if from_date_obj:
            if trip.departure_date_obj < from_date_obj:
                to_be_filtered = True
        if to_date_obj:
            if trip.departure_date_obj > to_date_obj:
                to_be_filtered = True

        # Transportation mean
        if transportation_mean:
            for segment in trip.segments:
                if segment.transportation_mean != transportation_mean:
                    to_be_filtered = True
                    break

        # Number of segments
        if min_segment_nb:
            if len(trip.segments) < min_segment_nb:
                to_be_filtered = True
        if max_segment_nb:
            if len(trip.segments) > max_segment_nb:
                to_be_filtered = True

        # Bicycle
        # All segments of the trip must respect the bicycle conditions
        if bicycle_with_reservation_only:
            for segment in trip.segments:
                if segment.bicycle_with_reservation != \
                   bicycle_with_reservation_only:
                    to_be_filtered = True
                    break

        if bicycle_without_reservation_only:
            for segment in trip.segments:
                if segment.bicycle_without_reservation != \
                   bicycle_without_reservation_only:
                    to_be_filtered = True
                    break

        if bicycle_with_or_without_reservation:
            for segment in trip.segments:
                condition = (segment.bicycle_with_reservation or
                             segment.bicycle_without_reservation)
                if condition != bicycle_with_or_without_reservation:
                    to_be_filtered = True
                    break

        # Add to list if it has not been filtered
        if not to_be_filtered:
            filtered_trip_list.append(trip)
    return filtered_trip_list


def _strfdelta(tdelta, fmt):
    """ Format a timedelta object """
    # Thanks to https://stackoverflow.com/questions/8906926
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)
