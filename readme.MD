#
### Custom DRF Exception
* Simplified django rest framework error response for showing errors in the ui.
* Each field in the serializer can be mapped to particular field in the serializer.
* Thus when an exception arises from the serializer it can be shown in the frontend effectively.
* This eliminates the process to write complex validations in frontend.

## How to use?
Add the file to your django project folder.
Along with other REST_FRAMEWORK settings add the below inside settings.py file:
    REST_FRAMEWORK = {
        'EXCEPTION_HANDLER': 'drf_custom_exception.custom_drf_exception_handler'
    }

## Exception Structure:

If exception is from serializer validation
<br>
{
<br>
&nbsp;&nbsp;&nbsp;&nbsp;"errors": [
<br>
        {
<br>
&nbsp;&nbsp;&nbsp;&nbsp;"error_code": "DRFE",
<br>
&nbsp;&nbsp;&nbsp;&nbsp;"error_message": "Invalid Input",
<br>
&nbsp;&nbsp;&nbsp;&nbsp;"field_errors": {
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"daughter": [
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"email": [
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Enter a valid email address."
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;],
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"grand-daughter": {
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"email": [
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Enter a valid email address."
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]
<br>
}
<br>
If exception is from within django:
<br>
{
&nbsp;&nbsp;&nbsp;&nbsp;"errors": [
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"error_message": "Pincode is required.",
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"error_code": "U000"
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
<br>
&nbsp;&nbsp;&nbsp;&nbsp;]
<br>
}

## How to handle in frontend?
In the frontend for validation error from serializer error_code DRFE(Django Rest Framework Excpetion)
Use recursion to get individual fields in the field_errors list and show near to the respective input field.


## What is different?
Using this custom exception even nested serializers in drf can have their exception shown in the frontend.
Otherwise if the exception is from within django the error can be shown in an alert or floating panel in frontend.

## Note:
This custom exception is still a work in progress please use with caution in production.
The code is test in drf version 3.12.2. Should work fine with previous versions as well.