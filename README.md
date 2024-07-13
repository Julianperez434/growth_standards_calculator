# GROWTH STANDARDS CALCULATOR
#### Video Demo: <https://youtu.be/OwqfotIyoNw>
#### Description
This Python program calculates and visualizes growth standards for children and adolescents (ages 5 to 19 years) based on data from the World Health Organization (WHO). It allows users to input their gender, age, height, and weight, and generates plots comparing their measurements against WHO growth standards.

## Getting Started

To run this program, clone this repository and execute the following command:

```bash
python growth_standards_calculator.py
```

## Requirements

#### Libraries: `numpy`, `pandas`, `matplotlib`

Install the required libraries using pip:

```bash
pip install numpy pandas matplotlib
```

## Functionality

This program provides the following functionality:

1. **Height for Age Calculation and Plotting**: Calculates and plots height-for-age based on user input and WHO data.
2. **BMI for Age Calculation and Plotting**: Calculates and plots BMI-for-age based on user input and WHO data.
3. **Instructions for using the Program**: Provides guidance on how to interact with the program and which csv files are required.
4. **Exiting the Program**: Allows users to exit the program after completing their calculations.

When executed, the program generates the CSV files:

- `height_data_boys.csv`
- `height_data_girls.csv`
- `bmi_data_boys.csv`
- `bmi_data_girls.csv`

These files contain WHO growth data for boys and girls, which are used to generate plots.

## Class: Person

The `Person` class represents an individual, encapsulates attributes such as gender, age, height, and weight. It includes methods for input validation and calculation of Body Mass Index (BMI).

## Attributes

- `gender`: Gender of the person ('Male' or 'Female').
- `age`: Age of the person (5 to 19 years).
- `height`: Height of the person in centimeters (50 to 250 cm).
- `weight`: Weight of the person in kilograms (5 to 250 kg).

## Methods

- `set_height_for_age()`: Set height for age based on user input.
- `set_weight()`: Set weight based on user input.
- `generate_height_for_age_plot()`: Generate height-for-age plot comparing user's height against WHO standards.
- `generate_bmi_for_age_plot()`: Generate BMI-for-age plot comparing user's BMI against WHO standards.
- `print_instructions()`: Print program instructions on how to interact with the program and CSV files.

## CSV File Generation

This program includes functions to generate CSV files

- `generate_height_boys_csv()`
- `generate_height_girls_csv()`
- `generate_bmi_boys_csv()`
- `generate_bmi_girls_csv()`

These files are based on WHO data and serve as inputs for plotting functions.

## Usage

1. **Select an option** from the main menu:

- Option 1: Calculate and plot height for age
- Option 2: Calculate and plot BMI for age
- Option 3: View program instructions
- Option 4: Exit the program

2. **Input** gender, age, height, and weight when prompted.

3. **Plot Generation:** The program generates a plot `plot.png` comparing the user's measurements against WHO growth standards.

4. **Instructions:** Read program instructions for further guidance about updating csv data.

## Notes

> [!IMPORTANT]
> Ensure CSV files `height_data_boys.csv`, `height_data_girls.csv`, `bmi_data_boys.csv`, `bmi_data_girls.csv` are present in the directory for correct program operation.

> [!TIP]
> Update CSV files to reflect updated WHO growth standards, if needed.

## Future improvements

In the future, this program capabilities can be expanded by:

- Allowing input of fractions (months) instead of whole years.
- Extending age ranges less than 5 and beyond 19 years.
