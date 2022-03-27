import streamlit as st

st.title("Predicting GDP per capita for countries using several factors")

"## Exploration"

"### What does the project do?"

"In our dataset, there is information on population height, literacy, infant mortality, etc... that correlate with each other in interesting ways. Our goal will be to predict the wealth of nations, which will be measured in GDP per capita. Looking at same characteristics of the dataset, the GDP per capita ranges from \$500 to \$55,100 and has a standard deviation of $9834"

exploration = st.selectbox("Data Visualizations", ["Correlation map", "Scatterplot trends", "Correlation of crucial features"]) 


if exploration=="Correlation map":

    "### Exploration of data: Correlation table heatmap"

    "First, we created a correlation table to see how different features correlated with the wealth of nations. Some surprising results were that the number of phones per hundred people and male height in cm were highly correlated with GDP per capita. Meanwhile, birthrate and infant mortality were highly negatively correlated"

    st.image('./images/main_correlation.png', 'Correlation table for dataset', width=800)

elif exploration=="Scatterplot trends":

    "### Exploration of data: Scatterplots"

    "Scatterplots clearly demonstrate to us more positive and negative trends in our data. Most surprising to us is that as agricultural goes to zero, GDP becomes exponentially higher. "

    st.image('./images/GDP_Correlation_Graphs.png')

elif exploration=="Correlation of crucial features":

    "### Visualization of crucial features"

    "We isolated the above features that we saw as most important and turned them into their own correlation table, so that we can see how these crucial features affect wealth."

    st.image('./images/GDP_correlation_map.png')

"## Machine Learning"

"### Linear Regression explanation"
"First, we want to try a baseline linear regression. Linear regression assumes that all features are have a linear relation with GDP per capita, and we can fit a line of best fit to predict future values"
st.image('./images/LinearExplanation.png', width=500)

"### Linear regression results"
"Here we have a confusion matrix with the results of the linear regression applied on our testing dataset. A confusion matrix for a classification problem tells us the number of correct and incorrect predictions for every class (for example wealthy). For example, the model may have classified 10 countries with average GDP as average and classified 2 countries with average GDP incorrectly, shown in the below confusion matrix. Linear regression performed exceptionally well on countries with average GDP."

st.image('./images/Linear_CF_matrix.png', width=500)

"By calculating the total correct examples over all examples classified, we get an average accuracy of around 58%. Mean absolute error, or the average difference between predicted and actual GDP per capita, was $3299"

"### Neural Networks expanation"
"Neural networks are one of the most powerful machine learning approaches for data with complicated patterns, but are more prone to overfitting to simple data. "

st.image('./images/NN_CF_matrix_raw.png', width=500)

"For total accuracy, the NN performed at 64.4% accuracy in classification. Mean absolute error is $2311"

"### K Nearest Neighbors: Explanation"
"K Nearest Neighbors looks at data points in the testing set and infers the classification based on similarity to other points of the same class in the training set."

"### K Nearest Neighbors: Results"
"Looking at our confusion matrix below, K Nearest Neighbors performed well on very wealthy and ver poor nations."

st.image('./images/KNN_CF_matrix.png', width=500)

"Overall, the KNN performed at 40.6% accuracy, and a mean absolute error for regression at $5712"

"## Conclusion"
"In conclusion, neural networks clearly performed the best on our dataset for predicting GDP per capita. Positively correlated features like height and phone usage along with negatively correlated features like birthrate and agriculture helped us achieve these results."







