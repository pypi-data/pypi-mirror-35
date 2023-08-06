from sgmarkets_api_analytics_rates._obj_from_dict import ObjFromDict
from sgmarkets_api_analytics_rates.request_curves_price import RequestCurvesPrices
from sgmarkets_api_analytics_rates.response_curves_price import ResponseCurvesPrice
from sgmarkets_api_analytics_rates.slice_curves_price import SliceCurvesPrice


dic_endpoint = {
    'v1_curves_price': {
        'request': RequestCurvesPrices,
        'response': ResponseCurvesPrice,
        'slice': SliceCurvesPrice
    }
}

endpoint = ObjFromDict(dic_endpoint)

if __name__ == '__main__':
    ep = endpoint
    ep.request()
