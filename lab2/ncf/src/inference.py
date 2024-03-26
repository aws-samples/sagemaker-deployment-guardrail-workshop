import json
import requests

def order_item_predictions(e):
    return e['prediction']    

def handler(data, context):
    """Handle request.
    Args:
        data (obj): the request data
        context (Context): an object containing request and configuration details
    Returns:
        (bytes, string): data to return to client, (optional) response content type
    """
    processed_input = _process_input(data, context)
    processed_input_json = json.loads(processed_input)
    instances =  processed_input_json['instances']
    item_ids = []
    for instance in instances:
        one_hot_encoded_item_id = instance['input_2']
        item_id = one_hot_encoded_item_id.index(1)
        item_ids.append(item_id)

    response = requests.post(context.rest_uri, data=processed_input)
    prediction, response_content_type = _process_output(response, context)
    
    pred_str = prediction.decode('utf-8')
    pred_json = json.loads(pred_str)
    prediction_scores = pred_json['predictions']

    item_prediction_scores = [ { "item_id" : i, "prediction" : p[0] } for (i, p) in zip(item_ids, prediction_scores) ]
    item_prediction_scores.sort(key=order_item_predictions, reverse=True)
    item_prediction = {}
    item_prediction['predictions'] = item_prediction_scores
    item_prediction_str = json.dumps(item_prediction)
    return item_prediction_str, response_content_type


def _process_input(data, context):
    if context.request_content_type == 'application/json':
        # pass through json (assumes it's correctly formed)
        d = data.read().decode('utf-8')
        return d if len(d) else ''

    raise ValueError('{{"error": "unsupported content type {}"}}'.format(
        context.request_content_type or "unknown"))


def _process_output(data, context):
    if data.status_code != 200:
        raise ValueError(data.content.decode('utf-8'))

    response_content_type = context.accept_header
    prediction = data.content
    return prediction, response_content_type