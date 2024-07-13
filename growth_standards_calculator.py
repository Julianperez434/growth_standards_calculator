import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import sys

class Person():
    """
    A class to represent a person and manage height and BMI.

    :param gender: Gender of the person
    :param age: Age of the person
    :param height: Height of the person in centimeters
    :param weight: Weight of the person in kilograms
    """
    def __init__(self, gender: str = "F", age: int = 5, height: float = 50.0, weight: float = 5.0) -> None:
        self.gender: str = gender
        self.age: int = age
        self.height: float = height
        self.weight: float = weight


    @property
    def gender(self) -> str:
        return self._gender


    @gender.setter
    def gender(self, gender: str) -> None:
        """
        Set the gender of the person

        :param gender: Gender of the person
        :raises ValueError: If the gender is not one of the allowed values
        """
        valid_genders: list[str] = ['F', 'M', "Male", "Female"]
        user_gender = gender.strip().title()
        if user_gender in valid_genders:
            self._gender = user_gender
        else:
            raise ValueError("Invalid gender.")


    @property
    def age(self) -> int:
        return self._age


    @age.setter
    def age(self, age: int) -> None:
        """
        Set the age of the person

        :param age: Age of the person
        :raises ValueError: If the age is not within the valid range
        """
        if 5 <= age <= 19:
            self._age = age
        else:
            raise ValueError("Age must be between 5 and 19.")


    @property
    def height(self) -> float:
        return self._height


    @height.setter
    def height(self, height: float) -> None:
        """
        Set the height of the person

        :param height: Height of the person in centimeters
        :raises ValueError: If the height cannot be converted to a float
        """
        try:
            user_height = float(height)
            if 50 <= user_height <= 250:
                self._height = user_height
            else:
                raise ValueError("Height should be between 50 CM and 250 CM")
        except ValueError:
            raise ValueError("Height must be a valid number.")


    @property
    def weight(self) -> float:
        return self._weight


    @weight.setter
    def weight(self, weight: float) -> None:
        """
        Set the weight of the person

        :param weight: Weight of the person in kilograms
        :raises ValueError: If the weight cannot be converted to a float
        """
        try:
            user_weight = float(weight)
            if 5 <= user_weight <= 250:
                self._weight = user_weight
            else:
                raise ValueError("Weight should be between 5 kg and 250 kg")
        except ValueError:
            raise ValueError("Weight must be a valid number")


    def print_main_menu(self) -> None:
        """
        Print the main menu for user.

        :returns: None
        """
        print("\n")
        print("=" * 30)
        print("+-- GROWTH STANDARDS CALCULATOR (5 to 19 years) --+\n")
        print("1. Height for age")
        print("2. BMI for age")
        print("3. Help")
        print("4. Exit")
        print("=" * 30)


    def get_option(self) -> int:
        """
        Get the user's menu selection.

        :returns: The selected option as integer
        :raises ValueError: If the input is not an integer
        """
        while True:
            try:
                return int(input("Select an option: "))
            except ValueError:
                print("Only use numbers")
                time.sleep(1)


    def set_height_for_age(self) -> None:
        """
        Set the height for age prompting user for gender, age and height.

        :returns: None
        """
        self.set_gender()
        self.set_age()
        self.set_height()


    def set_gender(self) -> None:
        """
        Prompt the user to enter their gender

        :returns: None
        """
        while True:
            try:
                gender = input("Type gender ['M', 'Male', 'F', 'Female']: ").strip().title()
                self.gender = gender
                break
            except ValueError:
                print("Invalid gender. Try again.")
                time.sleep(1)


    def set_age(self) -> None:
        """
        Prompt the user to enter their age.

        :returns: None
        """
        while True:
            try:
                age = int(input("Type age [5-19]: "))
                if age >= 5 and age <= 19:
                    self.age = age
                    break
                else:
                    print("Invalid age. Try again.")
            except ValueError:
                print("Invalid age. Try again.")
                time.sleep(1)

    def set_height(self) -> None:
        """
        Prompt the user to enter their height.

        :returns: None
        """
        while True:
            try:
                height = float(input("Type height in CM: "))
                self.height = height
                break
            except ValueError:
                print("Invalid height. Try again.")
                time.sleep(1)

    def set_weight(self) -> None:
        """
        Prompt the user to enter their weight.

        :returns: None
        """
        while True:
            try:
                weight = float(input("Type weight in KG: "))
                self.weight = weight
                break
            except ValueError:
                print("Invalid weight. Try again.")
                time.sleep(1)

    def generate_height_for_age_plot(self) -> None:
        """
        Generate and save a plot based on height for age

        :returns: None
        """
        if self.gender == 'M' or self.gender == 'Male':
            data_file = "height_data_boys.csv"
            title = "Height for Age Boys (5 to 19 years old)"
        else:
            data_file = "height_data_girls.csv"
            title = "Height for Age Girls (5 to 19 years old)"

        df = pd.read_csv(data_file)
        ages = df["age"].values
        height_minus_2 = df["height_minus_2"].values
        height_minus_1 = df["height_minus_1"].values
        height_median = df["height_median"].values
        height_plus_1 = df["height_plus_1"].values
        height_plus_2 = df["height_plus_2"].values

        plt.figure(figsize=(10, 6))

        plt.plot(ages, height_plus_2, label="+2", color="red", linestyle="--")
        plt.plot(ages, height_plus_1, label="+1", color="orange")
        plt.plot(ages, height_median, label="Median", color="green")
        plt.plot(ages, height_minus_1, label="-1", color="orange")
        plt.plot(ages, height_minus_2, label="-2", color="red", linestyle="--")

        plt.plot(self.age, self.height, label="You", marker="o", color="black", markersize="8")

        plt.title(title)
        plt.xlabel("Age (years)")
        plt.ylabel("Height (cm)")
        plt.legend()

        plt.grid(True)
        plt.tight_layout()
        plt.savefig("plot.png")

        print("\n")
        print("Plot created succesfully. Go to plot.png\n")
        time.sleep(2)


    def generate_bmi_for_age_plot(self) -> None:
        """
        Generate and save a plot based on BMI for age

        :returns: None
        """
        if self.gender == 'M' or self.gender == 'Male':
            data_file = "bmi_data_boys.csv"
            title = "BMI for Age Boys (5 to 19 years old)"
        else:
            data_file = "bmi_data_girls.csv"
            title = "BMI for Age Girls (5 to 19 years old)"

        df = pd.read_csv(data_file)
        ages = df["age"].values
        bmi_minus_3 = df["bmi_minus_3"].values
        bmi_minus_2 = df["bmi_minus_2"].values
        bmi_minus_1 = df["bmi_minus_1"].values
        bmi_median = df["bmi_median"].values
        bmi_plus_1 = df["bmi_plus_1"].values
        bmi_plus_2 = df["bmi_plus_2"].values
        bmi_plus_3 = df["bmi_plus_3"].values

        plt.figure(figsize=(10, 6))

        plt.plot(ages, bmi_plus_3, label="+3", color="black", linestyle="--")
        plt.plot(ages, bmi_plus_2, label="+2", color="red")
        plt.plot(ages, bmi_plus_1, label="+1", color="orange")
        plt.plot(ages, bmi_median, label="Median", color="green")
        plt.plot(ages, bmi_minus_1, label="-1", color="orange")
        plt.plot(ages, bmi_minus_2, label="-2", color="red")
        plt.plot(ages, bmi_minus_3, label="-3", color="black", linestyle="--")

        bmi = self.calculate_bmi()
        plt.plot(self.age, bmi, label="You", marker="o", color="black", markersize="8")

        plt.title(title)
        plt.xlabel("Age (years)")
        plt.ylabel("BMI (kg/m^2)")
        plt.legend()

        plt.grid(True)
        plt.tight_layout()
        plt.savefig("plot.png")

        print("\n")
        print("Plot created succesfully. Go to plot.png\n")
        time.sleep(2)



    def print_instructions(self) -> None:
        """
        Print the instructions.

        :returns: None
        """
        print("\n")
        print("=" * 30)
        print("+-- INSTRUCTIONS --+\n")
        print("Height/BMI for age\n")
        print("This program generates a plot using data from WHO,")
        print("based on your data generates a dot to compare it")
        print("the file generated is called plot.png\n")
        print("You can update WHO's info by editing the csv files.")
        print("=" * 30)
        print("\n")

        while True:
            answer: str = input("Continue? (Y): ")
            if answer.lower() == 'y' or answer.lower == 'yes':
                break

    def calculate_bmi(self):
        """
        Calculate Body Mass Index - BMI.

        :returns: BMI value of the person
        """
        height_in_meters: float = self.height / 100
        bmi: float = self.weight / (height_in_meters ** 2)
        return bmi



    def run(self) -> None:
        """
        Run the main program.

        :Returns: None
        :raises SystemExit: Exits the program when option 4 is selected
        """
        while True:
            self.print_main_menu()
            option: int = self.get_option()
            match option:
                case 1:
                    self.set_height_for_age()
                    self.generate_height_for_age_plot()
                case 2:
                    self.set_height_for_age()
                    self.set_weight()
                    self.generate_bmi_for_age_plot()
                case 3:
                    self.print_instructions()
                case 4:
                    sys.exit("Program successfully closed")
                case _:
                    print("Only select a valid option from the menu")
                    time.sleep(2)


def main() -> None:
    """
    Create csv files, a Person object and start the program.

    :returns: None
    """
    generate_csv_files()
    person: Person = Person()
    person.run()


def generate_csv_files() -> None:
    """
    Generate all the csv files needed

    :returns: 0 if all files are generated
    """
    print("generating csv files, this can take a moment...")
    time.sleep(2)
    generate_height_boys_csv()
    generate_height_girls_csv()
    generate_bmi_boys_csv()
    generate_bmi_girls_csv()
    print("csv files generated successfully.")
    time.sleep(1)
    return 0

def generate_height_boys_csv() -> int:
    # Data by WHO
    data = {
        "age": list(range(5, 20)),
        "height_minus_2": [101.6, 106.7, 111.8, 116.6, 121.3, 125.8, 130.5, 135.8, 142.1, 148.7, 154.3, 158.3, 160.8, 162.1, 162.8],
        "height_minus_1": [105.5, 110.8, 116.3, 121.4, 126.3, 131.2, 136.1, 141.7, 148.3, 155.2, 160.9, 164.8, 167.2, 168.4, 169.0],
        "height_median": [110.3, 116.0, 121.7, 127.3, 132.6, 137.8, 143.1, 149.1, 156.0, 163.2, 169.0, 172.9, 175.2, 176.1, 176.5],
        "height_plus_1": [115.0, 121.1, 127.2, 133.1, 138.8, 144.4, 150.1, 156.4, 163.7, 171.2, 177.0, 181.0, 183.1, 183.9, 184.1],
        "height_plus_2": [118.9, 125.2, 131.7, 137.9, 143.9, 149.8, 155.8, 162.4, 170.0, 177.6, 183.6, 187.5, 189.5, 190.2, 190.3]
    }

    df = pd.DataFrame(data)
    df.to_csv("height_data_boys.csv", index=False)
    print("height_data_boys.csv file generated successfully.")
    time.sleep(1)
    return 0

def generate_height_girls_csv() -> int:
    # data by WHO
    data = {
        "age": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        "height_minus_2": [100.6, 105.5, 110.5, 115.7, 121.0, 126.6, 132.5, 138.4, 143.3, 146.7, 148.7, 149.8, 150.3, 150.6, 150.9],
        "height_minus_1": [104.7, 109.8, 115.1, 120.5, 126.2, 132.0, 138.1, 144.1, 149.2, 152.6, 154.5, 155.5, 155.9, 156.2, 156.4],
        "height_median": [109.6, 115.1, 120.8, 126.6, 132.5, 138.6, 145.0, 151.2, 156.4, 159.8, 161.7, 162.5, 162.9, 163.1, 163.2],
        "height_plus_1": [114.5, 120.4, 126.5, 132.6, 138.8, 145.3, 151.9, 158.3, 163.6, 167.0, 168.8, 169.6, 169.8, 169.9, 169.9],
        "height_plus_2": [118.6, 124.8, 131.1, 137.5, 144.0, 150.7, 157.5, 164.1, 169.4, 172.8, 174.6, 175.3, 175.4, 175.5, 175.5]
    }

    df = pd.DataFrame(data)
    df.to_csv("height_data_girls.csv", index=False)
    print("height_data_girls.csv file generated succesfully.")
    time.sleep(1)
    return 0

def generate_bmi_boys_csv() -> int:
    # Data by WHO
    data = {
        "age": list(range(5, 20)),
        "bmi_minus_3": [12.1, 12.1, 12.3, 12.4, 12.6, 12.8, 13.1, 13.4, 13.8, 14.3, 14.7, 15.1, 15.4, 15.7, 15.9],
        "bmi_minus_2": [13.0, 13.0, 13.1, 13.3, 13.5, 13.7, 14.1, 14.5, 14.9, 15.5, 16.0, 16.5, 16.9, 17.3, 17.6],
        "bmi_minus_1": [14.1, 14.1, 14.2, 14.4, 14.6, 14.9, 15.3, 15.8, 16.4, 17.0, 17.6, 18.2, 18.8, 19.2, 19.6],
        "bmi_median": [15.3, 15.3, 15.5, 15.7, 16.0, 16.4, 16.9, 17.5, 18.2, 19.0, 19.8, 20.5, 21.1, 21.7, 22.2],
        "bmi_plus_1": [16.6, 16.8, 17.0, 17.4, 17.9, 18.5, 19.2, 19.9, 20.8, 21.8, 22.7, 23.5, 24.3, 24.9, 25.4],
        "bmi_plus_2": [18.3, 18.5, 19.0, 19.7, 20.5, 21.4, 22.5, 23.6, 24.8, 25.9, 27.0, 27.9, 28.6, 29.2, 29.7],
        "bmi_plus_3": [20.2, 20.7, 21.6, 22.8, 24.3, 26.1, 28.0, 30.0, 31.7, 33.1, 34.1, 34.8, 35.2, 35.4, 35.5]
    }

    df = pd.DataFrame(data)
    df.to_csv("bmi_data_boys.csv", index=False)
    print("bmi_data_boys.csv file generated succesfully.")
    time.sleep(1)
    return 0

def generate_bmi_girls_csv() -> int:
    # Data by WHO
    data = {
        "age": list(range(5, 20)),
        "bmi_minus_3": [11.8, 11.7, 11.8, 11.9, 12.1, 12.4, 12.7, 13.2, 13.6, 14.0, 14.4, 14.6, 14.7, 14.7, 14.7],
        "bmi_minus_2": [12.7, 12.7, 12.7, 12.9, 13.1, 13.5, 13.9, 14.4, 14.9, 15.4, 15.9, 16.2, 16.4, 16.4, 16.5],
        "bmi_minus_1": [13.9, 13.9, 13.9, 14.1, 14.4, 14.8, 15.3, 16.0, 16.6, 17.2, 17.8, 18.2, 18.4, 18.6, 18.7],
        "bmi_median": [15.2, 15.3, 15.4, 15.7, 16.1, 16.6, 17.2, 18.0, 18.8, 19.6, 20.2, 20.7, 21.0, 21.3, 21.4],
        "bmi_plus_1": [16.9, 17.0, 17.3, 17.7, 18.3, 19.0, 19.9, 20.8, 21.8, 22.7, 23.5, 24.1, 24.5, 24.8, 25.0],
        "bmi_plus_2": [18.9, 19.2, 19.8, 20.6, 21.5, 22.6, 23.7, 25.0, 26.2, 27.3, 28.2, 28.9, 29.3, 29.5, 29.7],
        "bmi_plus_3": [21.3, 22.1, 23.3, 24.8, 26.5, 28.4, 30.2, 31.9, 33.4, 34.7, 35.5, 36.1, 36.3, 36.3, 36.2]
    }

    df = pd.DataFrame(data)
    df.to_csv("bmi_data_girls.csv", index=False)
    print("bmi_data_girls.csv file generated succesfully.")
    time.sleep(1)
    return 0


if __name__ == "__main__":
    main()



