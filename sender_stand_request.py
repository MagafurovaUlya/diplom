import configuration
import requests
import data


def post_new_order(body):
    # create order
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body, headers=data.headers)


def get_order_by_track(track):
    # get order data by track
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + '?t=' + str(track))

