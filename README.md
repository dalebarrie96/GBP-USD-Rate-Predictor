# GBP-USD-Rate-Predictor
Starting a basic regression machine learning project to try predict when i should buy my USD

19/9/2018 <br />
historical data from investing.com:

https://www.investing.com/currencies/gbp-usd-historical-data

20/9/2018 <br />
I Trained the data using scikit learns linear regression model but im only getting 87-89% accuracy. I was originally hoping to hit around 95% ish since the range is pretty small. <br />

Iv read about a few other methods like support vector regression.. i plan on trying that and if im still not getting the results then possibly look into writing my own model.

21/9/18 <br />
I Done some of this yesterday but hey ho...
<br /><br />
I had a go with Scikit learns SVR and was getting a big range of accuracys. SVM with a polynomial kernal got me 60% accuracy but LinearSVC managed to get me back up to 89/90%. I Think ill go back to the linear model for now, maybe add a few more years of data reduce forcast size and that will hopefully get me to the 95%. TensorFlow has a linear regression model that im considering implementing if all else fails. <br /> <br />

Okay so i ran the predictions and first impressions are looking good. The training data stopped on 20/9/2018 and when running the latest model it predicted the price for today to be 1.3059577 with google giving the rate as 1.31 and investing.com giving 1.3069. Im pretty happy with this so far considering there was a considerable drop in the rate which the model predicted. Ill update this as the days go onsee how it goes.
