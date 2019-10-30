driven_factors = {
    "MaritalStatus":[
        (1.1, 'Never Married'),
        (1, "Widowed Young"),
        (1.2,"Widowed Old"),
        (1, "Divorced"),
        (0.8, "Married"),
    ],
    "Race":[
        (0.861, "W"),
        (0.891, "B"),
        (1.828,"I"),
        (0.54, "A"),
        (0.87, "H"),
    ],
    "Education":[
        (1.29, "Less than high school"),
        (0.98, "High school"),
        (0.72, "More than high school"),
    ],
    "BMI":[
        (1, "Underweight"),
        (1, "Normal"),
        (1.1, "Overweight"),
        (1.7, "Obese I"),
        (2, "Obese II"),
        (2.5, "Extreme Obesity"),
    ],
    "Alcohol":[
        (1, "Never"),
        (1, "Rarely"),
        (1.05, "2-3 Drinks a Week"),
        (1.15, "3-7 Drinks a Week"),
        (1.3, "8+ Drinks a Week"),
    ],
    "Physical Activity":[
        (1.3, "Never"),
        (1.1, "Rarely"),
        (1, "2-3 Days a Week"),
        (0.90, "3-7 Days a Week"),
        (0.77, "8+ Days a Week"),
    ],
    "A1c":lambda a1c: 1.16 ** (a1c-6.5),
}

