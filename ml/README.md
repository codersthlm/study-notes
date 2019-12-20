* Decision Trees


CART is an algorthm. C4.5.

Will people wait for a table at an restaurant. Split on different feautures as an decision. Information and entropy. Low entropy is good. Because we are sure of our decision.



* Decision forest. Create a lot of decision treess and take the majority votefrom the result from the trees.




---------------------------

Image Processing with Python

Matplotlib.

Numpy.







Neural Networks and Deep Learning (Coursera)

-AI is the new electrocity.


Example. Nearal netwaork. Housing prices. Given input feauteres as wealth, size, zip, etc. And some hidden layers we can get an output on price. Every input feature is connected to the next layer with som weight.

Most success in supervised learning at the moment.

Will you click on an add.

Computer vision.

Speach Recokniotion.


Logistic regrssion is used for binary classification. Is this a cat? 1 or 0.


Lets take a 64 by 64 image. It is represented with 3 matrixes. RGB. We convert these matrixis to a feature vector with one column and 64*64*3 columns.
Use m to denote the number of training examples.


Define the matrix X having m columns of x. And n rows.
Define Y as row vector with m columns.


Logistic regression y = sigmoid(wtx + b). wt = w transpose.   sigmoid = 1/1 -e-x .

Lossfunction is using log. Cosfunction is J(w, b) and a sumation of the Loss.

We wandt to minimize the cost function J(w,b)

Vectorisation. Instead of for loops we use numpy built in functionality like the dot product.

So for vector a and np.dot(a,b)

For locistic regression z = np.dot (w, x) + b  can use gpu and parrallism. 
  

numpy is the fundamental package for scientific computing with Python.
h5py is a common package to interact with a dataset that is stored on an H5 file.
matplotlib is a famous library to plot graphs in Python.
PIL and scipy are used here to test your model with your own picture at the end.






# Train the logistic regression classifier
clf = sklearn.linear_model.LogisticRegressionCV();
clf.fit(X.T, Y.T);



# Plot the decision boundary for logistic regression
plot_decision_boundary(lambda x: clf.predict(x), X, Y)
plt.title("Logistic Regression")

# Print accuracy
LR_predictions = clf.predict(X.T)
print ('Accuracy of logistic regression: %d ' % float((np.dot(Y,LR_predictions) + np.dot(1-Y,1-LR_predictions))/float(Y.size)*100) +
       '% ' + "(percentage of correctly labelled datapoints)")

47% accuracy:


Interpretation: The dataset is not linearly separable, so logistic regression doesn't perform well. Hopefully a neural network will do better. Let's try this now!
