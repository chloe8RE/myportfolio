# Capstone
*By: Chloe Loh, GA DSI 38*
___________________________________

## File structure
1) code
   - 1.0 Introduction
   - 2.0 Data Cleaning
   - 3.0 EDA
   - 4.1 Modelling_Time_Series
   - 4.2 Modelling_Regression
   - 5.0 CBA_Conclusion
2) pkl
3) data
4) presentation slides


## Context

[Demand Forecasting](https://en.wikipedia.org/wiki/Demand_forecasting) refers to the process of making sales estimation about customer demand for a specific product and services over a certain time period.  It is crucial process in business environment as it provides both quantitative and qualitative insights of the product positioning in the target market so as to faciliate companies to make informed decisions on business growth, strategies, pricing and marketing initiatives. Failing of which leads to detrimental impact on customer satisfaction, business competitiveness, profitability and longevity. 

Importance
1. Resources optimization: If the company is able to identify expected demand levels for its product or services, it allows them to make necessary preparations.
2. Efficient inventory management: Accurate demand forecasting help companies kept stocks at right balance.  Insufficient stocks resulted in customer dissatisfaction and revenue loss, and may lead to loss of future businesses.  On the other hand, overstocking incurs additional storage and logistics costs and would lead to stock obsolescence.
3. Operational efficiency : Efficient production planning also reduces waste and lowers production costs, contributing to higher margins.
4. SME business: Demand forecasting is particularly crucial for small- and medium-sized enterprises (SMEs).  Flawed demand planning may cost the loss of opportunity to fill big orders.  Excessively ambitious forecasts, on the other hand, leads to scaling too rapidly for demand that could not materialize as expected. 
5. Customer satisfaction: Demand forecasting enables businesses to meet customer demand consistently and timely.

Challenges
1. Data collection: historical data not easily available or can be time consuming to 
2. Human errors and bias: personal judgement and stakeholders conflicting interests
3. Data quality: formats and details required are not easily available.  Some require lots of cleaning. 
4. **Seasonality**: demand and customer perference changes rapidly
5. **Complexity**: external factors affecting demand and it can be hard to collect and model.
6. Lack expertise: data analysis, statistics and domain knowlegde, as well as technology capability
8. Supply chain: global sourcing and interdependency.  

### Problem Statement

I would like to explore machine learning algorithms to develop an effective **short-term demand forecasting model** to help organizations to plan for demand surge for next 3 months, as current rule-based not able to predict seasonality and cannot handle complex and nonlinear relationships.  Demand surge happens when there are upcoming promotions or special events (Superbowl, Amazon Prime Day etc) so that they can swiftly act upon inventory planning and logistics to minimize costs.  

## Methodology

### Sources

**Data sources**<br>
Online business sales order quantity: https://www.kaggle.com/datasets/earthfromtop/amazon-sales-fy202021

**Information sources**

1. https://en.wikipedia.org/wiki/Demand_forecasting
2. https://medium.com/@futureanalytica/importance-of-demand-forecasting-86c1a4753dc0
3. https://www.netsuite.com/portal/resource/articles/inventory-management/demand-forecasting.shtml
4. https://www.thefulfillmentlab.com/blog/demand-forecasting
5. https://www.unitedstateszipcodes.org/
6. https://www.machinelearningplus.com/time-series/time-series-analysis-python/
7. https://machinelearningmastery.com/random-forest-for-time-series-forecasting/
8. https://machinelearningmastery.com/time-series-forecasting-with-prophet-in-python/


### Workflow

Below is capstone workflow:

![workflow.png](attachment:c2ad9374-58d8-4360-b589-b98f4f32ebb0.png)

### Models

The data models used can be split into 2 main categories: Time Series Forecasting models and Regression Models.

* **Time Series**
   - The classical methods, ARIMA, ARIMAX, SARIMA and SARIMAX, are used for modelling.
   - ARIMA and SARIMA refers to univariate time series forecasting models that are capable of capturing short-term patterns and seasonality with a limited past history data of 12 months.  The models consider recent past observations and don't rely on large amounts of historical data like other machine learning approaches.
   - ARIMAX and SARIMAX are the extension of traditional ARIMA and SARIMA respecitively. These extended models include both past values of target responses and additional features to make prediction of future values.  It accounts for features that are exogenous which means external factors that might be potential demand driver. This enables incorporating external factors to establish relationships between the factors and demand, so that I could utilize the features available in the datasets in modelling.<br>
<br>
* **Regression**
   - Random Forest is an ensemble decision tree model that is used for classification and regression predictive modelling.
   - it can capture complex relationships in dataset and they are robust for short-term forecasts. 
   - It adopts random input variable selection to create decision trees hence prediction errors from each tree is more different and less correlated. The final prediction is drawn by averaged across all decision trees and I believe this would result in better performance than other bagged decision tree models.
   - While Random Forest model is quite immune to statistical assumption that observations are independent of each other, it tend to not fit very well for increasing and decreasing trends and seasonality which usually encountered with time series analysis. 

### Metrics

**Root Mean Square Error (RMSE)**

For optimisation and selection of models, RMSE is used due to the reasons as follows: <br>
1. Simplicity: RMSE is a relatively simple and straightforward metric to compute, making it practical for evaluation of forecasting models.
2. Popularity: RMSE is a widely accepted metric in the field of time series forecasting and machine learning to compare the performance of different models across the industry.
3. Interpretability: RMSE is expressed in the same units as the target variable (order quantity), which makes it easy to interpret and stakeholders are able to grasp the magnitude of forecasting errors.
4. Sensitivity to errors: RMSE assigns more weight to larger errors (as errors are squared) compared to other metrics like MAE (mean absolute error) and MAPE (mean absolute percentage error).
   - In this case, the target variable (order quantity) has a range of peaks and lulls, larger errors are expected at the peak in absolute values.
   - Furthermore, we are more focused on capturing the demand spikes. Therefore RMSE is particularly suitable for highlighting larger forecasting errors that have significant financial impact in supply chain management.
   
## EDA findings

1. This dataset covers only 12 months from Oct-2020 to Sep-2021.
2. Age of customer on average 46 years old which is aligned with the mean 47 y/o. The demographics of customers for this business are made up of matured adults with high purchasing power, likely focus on quality over quantity, which explains the high value pricing of product sold. 
3. There are 13 types of order status hence I need to deep dive to check which constitute to completed sales.
4. There are 47,932 types of SKU indicating massive products database commonly seen in company that have grown over a period of time. SKU (Stock Keeping Unit) refers to unique identifier assigned to a product for inventory management and tracking. Management by SKU is essential as it helps with store layouts, multi-channel listings, invoicing and orders tracking.
5. This business manages 15 categories with Mobiles and Tablets being their top seller. Each product category has its unique demand seasonality, purchasing patterns (buy in bulk or small quantity), sourcing requirement and customer clusters. Hence it is better to start small with forecasting one product category. 
6. The availability of various payment methods provide convenience and options to customer, hence has a impact on driving sales demand.
7. The business has large customer base of 64,000 as indicated under "Full Name". Successful customer relationship management enables cross-selling and up-selling, which can be faciliated by machine learning Recommender System whereby customer ratings can provide informative feedback. This is part of future work.
8. this business can leverage on zipcodes details to deepdive location analysis study to drive targeted promotions and product development. 

### Product Category

1. Mobiles & Tablets leads the sales chart in term of order quantity for all order statuses and completed sales orders. It made up of 46,046 order quantity out of 250,887 total completed orders which constitutes to 18%.
2. Men's Fashion ranks second place, takes up 14% of total completed orders. Appliances made up of 13% of total completed orders.
3. These top 3 product categories, in aggregate, made up of 45% of total completed orders, which is almost half the order quantity. Hence this warrant attention and efforts in demand planning by focusing at top 3 categories.
4. There is positive correlation between order quantity and year suggesting growth in total order quantity which is a good sign albeit a weak positive.
5. Price and order quantity has weak inverse correlation. This provide some insight into Price Elasticity of Demand for products offered.
6. A detailed price sensitivity study on each SKU is required to get good understanding of price impact on demand.

### Trends

1. There are a couple of outliers (based on high threshold set at 1,299 units), particularly the peak occur around last week of 2020-12, which in all likelihood, driven by Christmas and Thanksgiving festive season.
2. Another few outliers (smaller peaks) happen on 2021-03 and 2021-05, also some time between mid 2021-03 to end 2021-04.
3. Low demand (almost flatline) are seen in 2020-10 and from mid 2021-06 till the end 2021-09, probably is common for this particular online reseller to experience such cyclical business pattern.
4. The top 3 categories (Mobiles & Tablets, Men's Fashion, and Appliances) follows similar trends as the overall trends, particularly the peak in Dec-2020.
5. All of the top 5 categories exhibits similar flat demand from mid June-2021 onwards.

### Seasonality

1. Trend is not linear, instead it is a series of peaks and lulls.
2. Seasonality is visible within a month. Width between cycles is a week looking at peak-to-peak and trough-to-trough
3. Residuals are unusually high during end Dec-2020 when there was a peak in the last 2 weeks of the month, and also smaller peak in Mar-2021 and mid May-2021.
4. Correlation heatmap shows high order quantity in Sundays of December hence high positive correlation between Sundays and December.
5. The correlation of order quantity with other days of week and month are weak.
6. Noticed that 27th of the month has highest sales order, followed by 20th and 1st of the month.
7. Top 5 categories show a similar upward trend towards the end of the month. This is highly likely due to Christmas and Thanksgiving festive season.

## Model Comparison

1. Based on model performance evaluation, SARIMAX model is less overfitting than SARIMA model with lesser differential values between train and test RMSE as compared to ARIMA/ARIMAX models.
2. SARIMAX model yields better results, demonstrates stronger predictive capability for short term 60 to 90 days of foreacasting window.
3. Per observation on linegraph above, SARIMAX model is able to predict the uptrend within these short intervals. The spikes in demand lies in the quarter Oct-2020 to Dec-2020 with max order quantity of 4,261 units hence RMSE 196 is 4.6% relative forecasting errors to max order quantity.
4. Short term forecasting face more challenges than longer term forecasting because it is sensitive to recent fluctuations and unforeseen events. Therefore the RMSE derived from SARIMAX model is considered acceptable for short-term forecasting with expected variablity.
5. Short term foreacasting is also useful for highly competitive and fast-paced ecommerce industry, to be adopted in conjuction with long term forecasting as immediate changes can be made to the models to get quick and relatively accutate results.
6. Random Forecast model enables hyperparameter tuning to ensure no overfitting and underfitting issues.
7. Hyperparameters can be adjusted according to the forecasted periods (60 days, 90 days or any other) to achive optimal results for each specific period.
8. Random forest model shows that shorter periods yield better model performance with better generalization of data. It also faciliate feature importance study to allow organization to identify driver for order quantity in a specific periods.

**Best Model** Random Forest Regression model shows the better fit and yields the lowest RMSE on test data hence it is our best model. Incorporating exogenous factors into modelling help contributed to lower RMSE. And Random Forest Regressor handle complexity better and generalize to new data better than time series models.

## Conclusion
Based on model comparison, the best fit model is Random Forest model with RMSE of 186. This model is able to handle complex relationship of features and predict seasonality from limited historical data due to its robust algorithms and hyperparameter tuning features. It also extract features importance with payment method 'easypay' being the highest importance followed by discount and pricing.

This finding from feature importance from Random Forest model complements the EDA which highlights the price and discounts relationship with demand.

EDA also shows that Sundays and December month play a signicant role on driving the demand.

As time series model produces overfitting results, it suggests that demand are less time dependant but more driven by liberate pricing effort, discounts program as well as payment method made available to customer for convenience of purchasing.

Over-forecasting is better than under-forecasting in terms of future revenue loss which could be exponentially costly and affect the longevitiy of business. The model would be able to understand the seasonality and patterns better to make more accurate results with lower errors if there are more historical data of longer horizon instead of just 1 year.

Other external factors are not available from the datasets which could be the main driver of demand. These factors can be economic condition, holidays, festive promotions such as Christmas, Black Friday or Amazon Prime Day which are the initiatives by external parties.

## Recommendation and Future Works

It is recommended to collect more historical data to train the model. Also, efforts should focus on improving the data quality used for modeling. Identify and address any data anomalies, missing values, or outliers to optimize model performance.

Feature engineering to create interactive terms between features or variables to further fine-tune the model performance.

We could gather more information on products attributes such as color, brand and size. Other information that would help with accurate demand forecasting are promotions program, other co-purchased products (market basket analysis), holiday seasons, special events (Formula 1 race, Olympics Game etc), weather data as well as external economic indicators (GDP, unemployment rate, interest rate)

We could train the datasets on other advanced models such as XGBoost or Prophet models and continue to finetune the models until optimum results.