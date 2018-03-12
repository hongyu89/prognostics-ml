'''
A1 Benchmark
------------

This event flow is for generating deep learning model for
classification approach
'''

import h2o
from h2o.estimators import H2ODeepLearningEstimator

print 'A2 Benchmark'
print '------------'

# Initialize H2O server
h2o.init(max_mem_size_GB=5)

# Load train and test data as H2O frames
train = h2o.import_file('processed-data/A2Benchmark_train.csv')
test = h2o.import_file('processed-data/A2Benchmark_test.csv')

# Define input and response columns
response_column = 'is_anomaly'
input_columns = train.col_names
input_columns.remove(response_column)
input_columns.remove('timestamp')

print 'Input columns   :', input_columns
print 'Response column :', response_column

# Explicitly imply response column contains label data
train[response_column] = train[response_column].asfactor()
test[response_column] = test[response_column].asfactor()

# Define model and train model
model = H2ODeepLearningEstimator(hidden=[200, 200], nfolds=10, epochs=100)
model.train(x=input_columns, y=response_column, training_frame=train)

# Test model
performance = model.model_performance(test_data=test)
print performance

'''
Sample Result
-------------

'''


