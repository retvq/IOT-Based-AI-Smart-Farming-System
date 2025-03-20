# IoT-Based AI Smart Farming System

## Project Description
This system combines IoT technology and artificial intelligence to transform agriculture. It provides real-time monitoring of environmental parameters such as soil moisture, temperature, and humidity. Using AI, the system analyzes crop health, detects diseases, and optimizes irrigation schedules. The goal is to enhance crop yield, conserve water, and support sustainable farming practices.

## Features
- Real-time monitoring of soil moisture, temperature, and humidity
- AI-powered crop health analysis and disease detection
- Automated irrigation control based on real-time data and AI insights
- User-friendly dashboard for data visualization and system control

## Technologies Used
- **Hardware**:
  - Arduino Uno
  - ESP32
  - Soil moisture sensors
  - DHT11 temperature and humidity sensor
  - Water pump
- **Software**:
  - Python
  - TensorFlow (for AI models)
  - Node-RED (for workflow automation)
  - ThingsBoard (for dashboard visualization)
  - AWS IoT Core (for cloud connectivity)

## Installation Instructions

### 1. Hardware Setup
- Connect the soil moisture sensor to analog pin **A0** on the Arduino.
- Attach the DHT11 sensor to digital pin **2**.
- Wire the water pump to digital pin **3** via a relay module for safe operation.
- Upload the Arduino sketch (`smart_farming.ino`) to the microcontroller using the Arduino IDE.

### 2. Software Setup
- Install Python 3 and the required libraries by running:
  ```bash
  pip install -r requirements.txt
  ```
- Install and set up **Node-RED**, then import the provided flow configuration (`node_red_flow.json`).
- Configure **ThingsBoard** (or your preferred dashboard platform) by following its setup documentation.
- Train or use pre-trained AI models for crop health analysis (details in the `models/` directory, if provided).

## Usage
1. Power on the Arduino and ensure it has an active internet connection.
2. Open the dashboard using the provided URL to monitor real-time data.
3. The system will automatically adjust irrigation based on soil moisture levels and AI recommendations.
4. Check the dashboard for alerts about detected crop diseases or anomalies.

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Make your changes or improvements.
3. Submit a pull request with a clear description of your updates.

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.
