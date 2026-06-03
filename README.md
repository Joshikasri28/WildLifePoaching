# Wildlife Poaching Detection & Alert System

## Overview

The Wildlife Poaching Detection & Alert System is an AI-powered surveillance solution designed to help protect wildlife from illegal poaching activities. The system uses Computer Vision and Deep Learning techniques to detect suspicious human presence in protected forest areas and automatically alerts authorities for rapid response.

## Problem Statement

Wildlife poaching is one of the major threats to biodiversity and endangered species. Traditional monitoring methods are often limited by manpower and delayed reporting. This project aims to provide real-time detection and automated alerts to improve wildlife protection.

## Features

* Real-time human detection using YOLOv5
* Detection of suspicious activities in protected areas
* Automated SMS alerts using Twilio API
* Live video monitoring through webcam or CCTV feed
* Fast response notification system for forest authorities
* Scalable architecture for deployment in wildlife reserves

## Technology Stack

* Python
* OpenCV
* YOLOv5
* NumPy
* Twilio API
* Computer Vision
* Deep Learning

## System Architecture

1. Capture video from camera source.
2. Process frames using OpenCV.
3. Detect humans using YOLOv5.
4. Identify potential poaching threats.
5. Trigger SMS alerts through Twilio API.
6. Notify forest authorities for immediate action.

## Project Workflow

Video Input → Frame Processing → Human Detection → Threat Analysis → SMS Alert Generation → Authority Notification

## Results

* Real-time human detection capability
* Automated alert generation
* Reduced response time for potential poaching incidents
* Improved wildlife monitoring efficiency

## Future Enhancements

* Weapon detection integration
* Animal species recognition
* GPS location tracking
* Drone-based monitoring
* AI-based behavior analysis
* Mobile application for authorities

## Installation

```bash
git clone https://github.com/yourusername/Wildlife-Poaching-Detection-System.git
cd Wildlife-Poaching-Detection-System
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```
