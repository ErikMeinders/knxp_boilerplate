# knxp_boilerplate
Boilerplate for knx_platformio projects.

## usage

This repo is a GitHub template. Make your own repo using this template and start building from there.

This template is provided to jump-start a project using knx_platformio, a framework for building KNX devices. 

## platformio.ini

Please find all necessary compiler options and supported defines for the boilerplate/library in the \[env\]section. It should be pretty self-explanatory. Note that envs are provided for ESP8266 as well as for ESP32. Also, -dev and -prod environments are provided using different build and deployment options. It is assumed that prod environments are updated Over The Air in this example.

## xml-tools

To program your KNX device using ETS, you need a .knxprod file. This can be created using KaenX, which takes an XML file as input. To get you started with the XML file, xml-tools are provided.

mkxml.py takes a template XML file and a settings file and 'merges' the two. That should help you getting started with the XML file.

## src

Contains knx_app.cpp which implements your app. It is based on the base-class _knxpp and contains an example of each function you're likely to override.

## include 

knx_app.h defines the application class and constants. It shows all methods you could potentially override with some documentation.