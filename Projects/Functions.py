#!/usr/bin/env python
# coding: utf-8

# # Linear Regression

# In[ ]:


def line_of_best_fit():
  
  import numpy as np #Importing numpy (pronouced - num-pi), it is a numerical python proccesing library, you can do a lot of math with it
  import matplotlib.pyplot as plt # Importing matplotlib.pyplot as plt, this is a plotting library
  import sklearn # Importing scikit-learn, this is a library that has lots of machine learning algorithms inclduing things like classification, regression, clustering, and nlp
  from sklearn.linear_model import LinearRegression # Basically, this model holds the equation for LinearRegression, and uses machine learning algorithms to figure out the line of best fit


  # Getting the Inputs with a while loop
  X = [] # Creating empty lists to append the inputs to for X
  y = [] # Creating empty lists to append the inputs to for y

  while True: # The while statement says that go through everything under me while tire, so it's just a loop that g
    x_in = float(input('X point: ')) # Asking for inputs, then making them integers for X
    y_in = float(input('Y point: ')) # Asking for inputs, then making them integers for y

    
    question = input('Is that it?  ') # Now, we will ask the question, "Is that it? "

    X.append(x_in) # We will append the values inputed into the variable x_in, to the empty lists that we created earlier
    y.append(y_in) # We will append the values inputed into the variable y_in, to the empty lists that we created earlier

    if question == 'yes': # We are asking an if statement that says, if the answer to the question is yes, break out of the loop, and do the next thing (everything in the loop is under the while that is indented in) 
      break
    
    else: # If it is anything else, we will continue, meaning that we will just go to the top of the loop and start over again, and repeat all the steps we did
      continue

  # Turning our lists into numpy arrays
  X = np.array(X).reshape(-1,1) # reshaping them to the way scikit-learn likes them, notice everytime you need to use the package numpy, you need to call np. This is the same for all libraries.
  y = np.array(y).reshape(-1,1) # reshaping them to the way scikit-learn likes them  

  lr_model = LinearRegression() # Creating an instance of our model, you have to do this for all models

  lr_model.fit(X, y) # Fitting the X and y points to the model, it will figure out the line of best fit

  y_int = round(float(lr_model.intercept_), 2) # Rounding to the second decimal place
  slope = round(float(lr_model.coef_), 2) # Rounding to the second decimal place

  print(f"y-intercept is around: {y_int}") # Printing the y-intercept
  print(f"Slope is around: {slope}") # Printing the slope

  preds = lr_model.predict(X) # Predicting on our X values, to generate y values, this will be the line of best fit

  plt.scatter(X, y) # Scatter plot of X and y
  plt.plot(X, preds) # Line of best fit
  plt.grid(True) # Grid to make it easier to see

  print(f"Your equation is: y = {slope}x + {y_int}") #Printing our entire equation


# In[ ]:


line_of_best_fit()


# # Mean, Median, Mode

# In[ ]:


def mean_median_mode_stdev():
  import statistics

  data = []

  while True:
    data_in = float(input('Data: '))

    question = input('Is that it? ').lower()

    data.append(data_in)

    if question == 'yes':
      print(f"Mean: {statistics.mean(data)}")
      print(f"Median: {statistics.median(data)}")
      print(f"Mode: {statistics.mode(data)}")
      print(f"Standard Deviation: {statistics.stdev(data)}")
      break
    else:
      continue


# In[ ]:


mean_median_mode_stdev()


# # Pythagorean Theorem

# In[ ]:


def pythagorean_thereom():
  question = str(input("What are you solving for? ").lower())

  if question == "hypotenuse":
    import math

    shorter_leg = float(input('Length of shorter leg: '))
    longer_leg = float(input('Length of longer leg: '))

    hypotenuse_length = math.sqrt(shorter_leg**2 + longer_leg**2)

    print(f"Hypotenuse Length: {round(hypotenuse_length, 2)}")
  
  if question == "longer leg":

    import math

    hypotenuse_length = float(input("Hypotenuse Length: "))
    shorter_leg = float(input("Shorter Leg: "))

    a = shorter_leg * shorter_leg
    b = hypotenuse_length * hypotenuse_length

    c = b-a

    c = math.sqrt(c)

    print(f"The longer leg length is: {round(c,2)}")

  if question == "shorter leg":
    import math 

    longer_leg = float(input('Longer Leg Length: '))
    hypotenuse_length = float(input('Hypotenuse Length: '))

    a = longer_leg *longer_leg 
    b = hypotenuse_length * hypotenuse_length

    c = b-a

    c = math.sqrt(c)

    print(f"The shorter leg length is: {round(c,2)}")


# In[ ]:


pythagorean_thereom()


# # Perpendicular Line (on hold)

# In[ ]:


equation = input("Equation (slope-intercept): ")

if int(len(equation.replace(" ", "").lstrip())) == 4:
  y_int = equation[3]
  x = equation[0]

  print(f"Your equation would be: -1/{x}x+{y_int}, for a perpendicular line")

if int(len(equation.replace(" ", "").lstrip())) == 6:
  y_int = equation[7]
  x = equation[4]

  print(f"Your equation would be: -1/{x}x+{y_int}, for a perpendicular line")

if int(len(equation.replace(" ", "").lstrip())) == 5:
  y_int = equation[4]
  x = equation[1]

  print(f"Your equation would be: 1/{x}x+{y_int}, for a perpendicular line")

if int(len(equation.replace(" ", "").lstrip())) == 7:
  y_int = equation[8]
  x = equation[5]

  print(f"Your equation would be: 1/{x}x+{y_int}, for a perpendicular line")





# In[ ]:


equation = input('Equation: ')
len(equation)


# In[ ]:


equation = input('Equation: ')
len(equation)
print(int(len(equation.replace(" ", "").lstrip())))


# In[ ]:


y_1 = float(equation[1]+equation[2]) *-1
slope = float(equation[6])
x_1 = float(equation[9] + equation[10])

y_int = y_1 + (slope*x_1)
s = str(slope) + equation[8]

print(f"Your equation would be -1/{s}+{int(y_int)}")


# In[ ]:


equation = input("Equation (point-slope): ")

if int(len(equation.replace(" ", "").lstrip())) == 10:
  y_1 = float(equation[1]+equation[2]) *-1
  slope = float(equation[6])
  x_1 = float(equation[9] + equation[10])

  y_int = y_1 + (slope*x_1)
  s = str(slope) + equation[8]

  print(f"Your equation would be -1/{s}+{int(y_int)}")


# # Quadratic Formula

# In[ ]:


def quadratic_formula():
  from uncertainties import ufloat
  import math

  a = float(input("What is the value A: "))
  b = float(input("What is the value B: "))
  c = float(input("What is the value C: "))

  sqrt = (b*b - 4*a*c)
  if sqrt < 0:
    sqrt = -1*sqrt
    x = -1*b + math.sqrt(sqrt) / 2*a
    print(f"Your X value is: {x}")

  else:
    x = -1*b - math.sqrt(sqrt) / 2*a

    print(f"Your X value is: {x}")


# In[ ]:


math.sqrt(4)


# In[ ]:


get_ipython().system('pip install  uncertainties')


# # Slope

# # Amazon Review 

# In[ ]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')


# In[ ]:


sid = SentimentIntensityAnalyzer()


# In[ ]:


def review_analyzer():


  from nltk.sentiment.vader import SentimentIntensityAnalyzer

  nltk.download('vader_lexicon')


  review = input('Review: ')
  sid_score = list(sid.polarity_scores(review).values())
  if sid_score[3] < -10:
    print('The review is negative')

  if sid_score[3] ==  (0+10) or (0-10):
    print('The review is nuetral')

  if sid_score[3] > 10:
    print('The review is positive') 


# In[ ]:


review_analyzer()

