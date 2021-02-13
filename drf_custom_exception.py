from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.views import exception_handler


def get_structured_error_response(unstructured_error_response):
    error_list = []
    if type(unstructured_error_response) == list:
        return str(unstructured_error_response[0])
    for key, value in unstructured_error_response.items():
        key_string = str(key)
        if type(value) == ErrorDetail:
            error_list.append({key_string: str(value)})
        elif type(value) == list:
            if type(value[0]) == dict:
                error_list.append(
                    {key_string: get_structured_error_response(value[0])})
            else:
                error_list.append({key_string: str(value[0])})
        elif type(value) == dict:
            error_list.append(
                    {key_string: get_structured_error_response(value)})
    return error_list


def custom_drf_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        customized_response = {}
        customized_response['errors'] = []
        if type(response.data) == list:
            error = {'error_code': "",
                     'error_message': response.data[0], 'field_errors': []}
            customized_response['errors'].append(error)
        elif type(exc) == ValidationError:
            field_errors = get_structured_error_response(response.data)
            error = {'error_code': "DRFE",
                     'error_message': "Invalid Input", 'field_errors': field_errors}
            customized_response['errors'].append(error)
        else:
            for key, value in response.data.items():
                error = {'error_code': "",
                         'error_message': f"{str(key).replace('_',' ').title()}:{str(value[0] if type(value) == list else value)}", 'field_errors': []}
                customized_response['errors'].append(error)
        response.data = customized_response
    return response
