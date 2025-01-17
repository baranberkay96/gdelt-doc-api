# Changelog

## 1.4.0
Validate `timespan` filter parameter to make sure it's an allowed value
Catch API errors when a query string is invalid and return them to the user

## 1.3.3
Fix a bug in `multi_repeat` which meant any filter using `OR` would fail

## 1.3.2
Fix a bug in `multi_repeat` which caused a bad response from the API which could not be parsed

## 1.3.1
Fix bug when only the first of the filter conditions (eg. keyword, near, etc.) was used

## 1.3.0
Recursively load the JSON response to remove improper characters

## 1.2.0
Add support for filtering by timespan instead of start and end date

## 1.1.0
Adds support for multiple repeat filters

## 1.0.0
First version released