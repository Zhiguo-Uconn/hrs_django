driven_factors = {
    "MaritalStatus":{
        'Never Married': 1.1,
        'Widowed Young <40': 1,
        'Widowed Old >40': 1.2,
        'Divorced Male': 1,
        'Divorced Female': 1,
        'Married': 0.8,
    },
    "Race":{
        'White': 0.713028169,
        'Black': 1.073943662,
        'American Indian': 1.311619718,
        'Asian': 0.792253521,
        'Hispanic': 1.10915493,
    },
    "Education":{
        'Less than high school': 1.21192053,
        'High school': 1.003311258,
        'More than high school': 0.784768212,
    },
    "BMI":{
        'Underweight': 0.833333333,
        'Normal': 1,
        'Overweight': 1.25,
        'Obese I': 2.166666667,
        'Obesity II': 3.083333333,
        'Extreme Obesity': 4.666666667,
    },
    "Alcohol":{
        'Never': 1,
        'Rarely': 0.8,
        '2-3 Drinks a Week': 0.7,
        '3-7Drinks a Week': 1.1,
        '8+ Drinks a Week': 2,
    },
    "Physical Activity":{
        'Never': 1.3,
        'Rarely': 1.1,
        '1-2 Days a Week': 1,
        '3-4 Days a Week': 0.909090909,
        '5+ Days a Week': 0.769230769,
    },
    "A1c":lambda a1c: 1.16 ** (a1c-6.5),
}

