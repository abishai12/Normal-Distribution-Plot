# Normal Distribution Visualiser

Interactive Python tool to visualise the normal distribution curve from user inputs.

Built to answer a simple question: how can complicated data be made easy to understand for other people?

## What it does

- Takes user inputs for **mean**, **standard deviation**, **min x** and **max x** via a GUI
- Plots the normal distribution PDF curve
- Draws a dashed red line at the mean to show symmetry
- Validates inputs - if max x < min x, an error message is shown in the GUI instead of plotting incorrectly

## Tech Stack

- Python
- CustomTkinter - dark mode GUI
- Matplotlib - plotting
- NumPy, Math - calculations

## The Maths Behind It

The curve is coded manually using the general equation, not using a library call:

```
f(x) = (1 / (deviation * sqrt(2 * pi))) * e^(-0.5 * ((x - mean) / deviation)^2)
```

What I found when exploring it:

- Changing the **mean** shifts the curve left / right
- Increasing the **standard deviation** makes the curve wider and the peak height shorter, because the area under the curve stays at 1
- The curve has an asymptote at y = 0, the tails are infinite but probability density is highest near the mean (the expected value)

This comes from reading Keller - Statistics for Management and Economics.

## How to Run

```bash
pip install customtkinter matplotlib numpy
python main.py
```

Enter values in the GUI and click **Visualise**.

## What I Learned

- Implementing a mathematical formula from first principles in code
- Breaking a project into parts: getting and checking values (`GetandCheckValues()`), generating x/y data, plotting
- Making a tool usable for others - validation and error feedback, not just plotting for myself
- Why visualisation helps understanding: seeing the effect of mean and deviation is clearer than reading the formula alone

## Future Improvements

- Allow decimal inputs for mean / deviation (currently uses int)
- Handle deviation = 0 to avoid division by zero
- Use NumPy vectorisation instead of looping with a 0.01 step for speed
