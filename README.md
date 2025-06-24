
# Predicting-Temperature-Using-Machine-Learning

This project is a machine learning-based system designed to predict ambient temperature using key environmental and geographical inputs. By analyzing features like district, pressure, humidity, wind speed, and temperature extremes, the model provides accurate temperature forecasts. The user-friendly web interface allows users to select a district, automatically fill in coordinates, and quickly obtain predictions for informed decision-making.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Project Structure](#project-structure)
- [Author](#author)

## Introduction

Climate and weather play a vital role in our daily lives, influencing agriculture, transportation, health, and infrastructure. Accurate temperature prediction is crucial for making informed decisions in these sectors. This project aims to develop a machine learning-based Temperature Prediction System that forecasts the expected temperature based on various environmental and geographical inputs.

To make the system user-friendly, we developed a web-based interface where users can select a district, and the system automatically fills in its latitude and longitude. After entering the environmental parameters, users can predict the temperature with a single click. This solution demonstrates the practical application of data science and machine learning in environmental analytics and decision support systems.

**Note: This Project is for Educational Purposes Only**

The system takes inputs such as district, latitude, longitude, maximum and minimum temperature, pressure, humidity, and wind speed to predict the actual temperature (Temp_2m) in a given location. By leveraging historical weather data and geographical coordinates, the model learns the complex relationships between these variables and provides a reliable temperature prediction.
The results obtained from this project are based on a specific dataset and machine learning model, and should not be considered as definitive or accurate predictions for real-world scenarios.

## Features
- Predicts ambient temperature based on environmental and geographical factors.
- Provides insights into how district location, pressure, humidity, wind speed, and temperature extremes influence overall temperature conditions.
- Auto-fills latitude and longitude values based on selected district, improving ease of use and accuracy.
- User-friendly interface for inputting weather data and generating instant temperature predictions.
- Supports all districts of Nepal, ensuring location-specific forecasting.
- Enables decision-making in agriculture, local planning, and weather-related activities using machine learning.

## Installation

1. Clone the repository: `git clone https://github.com/00Bhuwan/temp_new.git`
2. Navigate to the project directory: `cd temp_new`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Run the application: `python application.py`
2. Access the web interface in your browser at `http://localhost:5000`
3. Fill in district, latitude, longitude, maximum and minimum temperature, pressure, humidity, and wind speed to predict the actual temperature.

## Dataset

The dataset used for training the machine learning model is sourced from [Kaggle - Nepal Daily Climate ]
(https://www.kaggle.com/datasets/saimondahal/nepal-daily-climate-1981-2019). The dataset contains data on Nepal's climate on different parameters. These data were obtained from the NASA Langley Research Center (LaRC) POWER Project funded through the NASA Earth Science/Applied Science Program and extracted using NASA's power access API.

These data are extracted with respect to meteorological stations in Nepal. Data is extracted for 93 weather stations spanning 62 districts in Nepal.

## Model Training

The machine learning model is trained using a supervised learning algorithm, such as a decision tree or random forest, to predict the temperature based on the input features. The dataset is split into training and testing sets to evaluate the model's performance.

## Results

The trained model achieved an accuracy of 85% in predicting temperature. The results demonstrate the significant impact of factors such as Longitude, Latitude, MaxTemperature, MinTemperature, Pressure, Humidity_2m, WindSpeed.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License]. See the [LICENSE](./LICENSE) file for details.

## Project Structure

The project has the following structure:
    
    ├───artifacts
    ├───Notebook
    │ └───data
    ├───src
    │ ├───components
    │ └───pipeline
    └───templates

- `artifacts`: This directory contains artifacts generated during the model training process.
-- since the actual data is very large. I kept it in gitignore so download the data from source and put it in respective folder i.e. Notebook\data\dailyclimate.csv
- `Notebook`: This directory contains notebooks used for data exploration and analysis.
- `src`: This directory contains the source code for the project.
  - `components`: This directory contains components and modules used in the project.
  - `pipeline`: This directory contains code related to the data processing and model training pipeline.
- `templates`: This directory contains HTML templates used in the web application.

## Author
Bhuwan Joshi, You can also visit my GitHub profile: @00bhuwan

Feel free to reach out with any questions or feedback regarding the project.
