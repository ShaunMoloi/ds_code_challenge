
<img src="img/city_emblem.png" alt="City Logo"/>

# Submission by Shaun Moloi for City of Cape Town - Data Science Challenge

## Description

This repository contains code scripts for my submission for the Senior Professional Officer: Data Science role in the Organisational Performance Management Department. Code has primarily been written in Python, jupyter notebooks are also provided. The purpose of this challenge is to evaluate the skills of prospective Data Scientists, Engineers and Analysts for positions in the City of Cape Town's Data Science unit. 

## Challenge

### 1. Data Transformation 
Joining the file `city-hex-polygons-8.geojson` to the service request dataset, such that each service request is assigned to a single H3 hexagon. For any requests where the `Latitude` and `Longitude` fields are empty, set the index value to `0`.

### 2. Predictive Analytic Tasks 
2.1 *Time series challenge*: Predicting the weekly number of expected service requests per hex for the next 4 weeks.
2.2 *Introspection challenge*: Predicting the number of requests per Notification  per hex in the last 12 months and identifying the key drivers of these servce requests. 
 
## Running the files

### 1. Data Transformation
In the terminal, run 'python NAME.py'
