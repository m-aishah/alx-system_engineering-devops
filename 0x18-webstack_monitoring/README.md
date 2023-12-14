# 0x18. Webstack monitoring

## Overview

“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of data-ism, monitoring how our software systems are doing is an essential aspect. The goal of this project is to implement tools for measuring and monitoring both application and server aspects of a web stack.

## Web Stack Monitoring Categories:

<b>1. Application Monitoring:</b>

- Gathering data about running software.

- Ensuring software behaves as expected.


<b>2. Server Monitoring:</b>

- Gathering data about virtual or physical servers.

- Ensuring servers are not overloaded (e.g., CPU, memory, disk, or network overload).


## Concepts

This project explores concepts related to monitoring and servers. Key concepts include:

- Monitoring

- Server


## Tasks

<b>0. Sign up for Datadog and install datadog-agent </b>

- Description: For this task head to https://www.datadoghq.com/ and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.


<b>1. Monitor some metrics. </b>

- Description: Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.


<b>2. Create a dashboard</b>

- Description: Now create a dashboard with different metrics displayed in order to get a few different visualizations.

	- Create a new dashboard

	- Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like

	- Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API


- File: [2-setup_datadog](./2-setup_datadog)
