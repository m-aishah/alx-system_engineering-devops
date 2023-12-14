#!/usr/bin/env python3
''' 
Creates a dashboard using the datadog API and stores the ID in a file.
'''
import requests
import json


# Set your Datadog API key and application key
API_KEY = "*************************0"
APP_KEY = "*****************************7"

# Set the Datadog API endpoint for creating a dashboard
API_ENDPOINT = "https://api.datadoghq.com/api/v1/dashboard"

# Define the dashboard configuration in Python dictionary format
dashboard_config = {
        "title": "Example-Dashboard",
        "description": "",
        "widgets": [
            {
                "definition": {
                    "title": "APM Stats - Request latency HOP",
                    "title_size": "16",
                    "title_align": "left",
                    "show_legend": False,
                    "type": "distribution",
                    "xaxis": {
                        "max": "auto",
                        "include_zero": True,
                        "scale": "linear",
                        "min": "auto"
                    },
                    "yaxis": {
                        "max": "auto",
                        "include_zero": True,
                        "scale": "linear",
                        "min": "auto"
                    },
                    "requests": [
                        {
                            "query": {
                                "primary_tag_value": "*",
                                "stat": "latency_distribution",
                                "data_source": "apm_resource_stats",
                                "name": "query1",
                                "service": "azure-bill-import",
                                "group_by": [
                                    "resource_name"
                                ],
                                "env": "staging",
                                "primary_tag_name": "datacenter",
                                "operation_name": "universal.http.client"
                            },

                            "request_type": "histogram",
                            "style": {
                                "palette": "dog_classic"
                            }
                        }
                    ]
                },
                "layout": {
                    "x": 8,
                    "y": 0,
                    "width": 4,
                    "height": 2
                }
            }
        ],
        "layout_type": "ordered"
}

# Convert the Python dictionary to a JSON string
dashboard_config_json = json.dumps(dashboard_config)

# Define headers for the API request
headers = {
    "Content-Type": "application/json",
    "DD-API-KEY": API_KEY,
    "DD-APPLICATION-KEY": APP_KEY,
}

# Send a POST request to create the dashboard
response = requests.post(API_ENDPOINT, headers=headers, data=dashboard_config_json)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    dashboard_id = response.json()["id"]
    print(f"Dashboard ID: {dashboard_id}")

    # Save the dashboard ID to the answer file
    with open("2-setup_datadog", "w") as answer_file:
        answer_file.write(str(dashboard_id))
else:
    # Print an error message if the request was not successful
    print(f"Failed to create the dashboard. Status code: {response.status_code}")
    print(response.text)

