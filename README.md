# Portuguese Real Estate Listings - Exploratory Data Analysis (EDA)

This repository contains an EDA project on Portuguese real estate listings data, aimed at uncovering insights on property prices, types, and geographical factors influencing the real estate market in Portugal.

## Table of Contents
- [Dataset Overview](#dataset-overview)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Key Findings](#key-findings)
- [Contributing](#contributing)
- [License](#license)

---

## Dataset Overview

The dataset includes over 100,000 real estate listings collected from Portuguese real estate websites. Each record contains:
- **Price**: Asking price in Euros
- **Location**: District, City, and Town information
- **Type**: Property type (e.g., Apartment, House)
- **Energy Certificate**: Energy efficiency rating of the property
- **Area Measurements**: Including Gross Area, Usable Area, Living Area, Lot Size, etc.
- **Additional Features**: Number of rooms, bedrooms, bathrooms, floor level, parking/garage information, construction year, and more.

The data allows for analyses such as price trends, geographical influences, and energy efficiency impacts on pricing.

---

## Project Structure

The repository follows a modular structure to ensure reusability of code:

portuguese-real-estate-eda/
├── EDA.ipynb                 # Main Jupyter Notebook for the entire EDA workflow
├── data_preprocessing.py     # Script with data cleaning and feature engineering functions
├── visualization.py          # Script with functions for data visualizations
├── requirements.txt          # File with dependencies for the project
├── README.md                 # Project documentation
├── images/                   # Directory for saved images
└── data/                     # Directory for data files
    ├── portugal_housing_chunk_1.csv  # First chunk of the dataset
    └── portugal_housing_chunk_2.csv  # Second chunk of the dataset


### Key Scripts
- **EDA.ipynb**: Main notebook containing the EDA steps and analyses.
- **data_preprocessing.py**: Contains data cleaning and feature engineering functions.
- **visualization.py**: Contains visualization functions for creating plots and maps.

---

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/parhamdehghani/portuguese-real-estate-eda.git
    cd portuguese-real-estate-eda
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the notebook**:
    Open `EDA.ipynb` in a Jupyter Notebook environment and execute each cell to reproduce the EDA.

---

## Usage

1. **Data Preprocessing**: `data_preprocessing.py` contains functions for handling missing values, feature engineering (e.g., price per square meter, property age), and other essential data cleaning steps.

2. **Visualization**: `visualization.py` contains all the plotting functions used for data analysis, such as:
   - `plot_price_distribution()`: Price distribution across listings.
   - `plot_property_type_counts()`: Counts of each property type.
   - `plot_price_vs_area()`: Relationship between property price and area.
   - `plot_district_prices()`: Median price per square meter by district.
   - `plot_correlation_heatmap()`: Correlation heatmap for numerical features.

3. **Interactive Maps**: An interactive map of property locations in Portugal is generated and saved in the `images/` directory.

---

## Key Findings

- **Price Trends**: Analysis of the dataset shows that property prices vary significantly by district, property type, and usable area.
- **Geographical Influences**: Certain districts have notably higher property prices, influenced by factors such as location desirability and property type.
- **Energy Efficiency**: Energy certification impacts property pricing, with more efficient properties typically having higher asking prices.
- **Price per Square Meter**: Reveals key insights into cost-efficiency across different regions and property types.

---

## License

This project is licensed under the MIT License.

---



