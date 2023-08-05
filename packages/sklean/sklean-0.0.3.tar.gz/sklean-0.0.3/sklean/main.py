def randomforest():
  print( 
  """
  import pandas as pd
  from sklearn.model_selection import train_test_split
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.metrics import accuracy_score
  from sklearn.model_selection import train_test_split

  data = pd.read_csv('bank_marketing.csv')

  # Choose the dependent and Independent variables
  X = data[['age','marital','ever_defaulted','housing_loan','Personal_loan']]
  Y = data[['y']]
  # Train, test/validation split
  X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.20, 
  random_state = 42)
  test_df = pd.concat ([X_test,y_test],axis =1 )

  # Initialize and train your model
  clf = RandomForestClassifier(random_state = 42) 
  clf.fit(X_train, y_train)
  # Predict the test data based on the trained model
  rf_pred = clf.predict(X_test)
  accuracy_score(y_test, rf_pred)
  """)
  return ""

def adaboost():
  print(
  """
  import pandas as pd
  from sklearn.model_selection import train_test_split
  from sklearn.ensemble import AdaBoostClassifier
  from sklearn.metrics import accuracy_score
  from sklearn.model_selection import train_test_split

  data = pd.read_csv('bank_marketing.csv')

  # Choose the dependent and Independent variables
  X = data[['age','marital','ever_defaulted','housing_loan','Personal_loan']]
  Y = data[['y']]
  # Train, test/validation split
  X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.20, 
  random_state = 42)
  test_df = pd.concat ([X_test,y_test],axis =1 )

  # Initialize and train your model
  abc = AdaBoostClassifier(random_state=0)
  abc_model = abc.fit(X_train, y_train)
  # Predict the test data based on the trained model
  abc_pred = abc_model.predict(X_test)
  accuracy_score(y_test, abc_pred)
  """)
  return ""

def ann():
  print(
  """
  import tensorflow as tf
  from tensorflow import keras
  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler()
  import pandas as pd
  from sklearn.metrics import accuracy_score

  data = pd.read_csv('bank_marketing.csv')

  from sklearn.model_selection import train_test_split

  col_to_scale =['age']
  data[col_to_scale] = scaler.fit_transform(data[col_to_scale])
  data.head()
  # Choose the independent and dependent variable
  X = data.drop('y',axis = 1)
  Y = data['y']
  # Train, test/validation split
  X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.20, 
  random_state = 42)
  test_df = pd.concat ([X_test,y_test],axis =1 )

  # Create the network
  model = keras.Sequential([
  keras.layers.Dense(3, input_shape = (5,),activation = 'relu'),
  keras.layers.Dense(2, input_shape = (3,),activation = 'relu'), 
  keras.layers.Dense(1,activation = 'sigmoid'),
  ])
  # Compile the network 
  model.compile(optimizer ='adam',
  loss = 'binary_crossentropy',
  metrics = ['accuracy']
  )

  # train the model
  model.fit(X_train,y_train,epochs = 5)
  """)
  return ""

def gradientboosting():
  print(
  """
  import pandas as pd
  from sklearn.model_selection import train_test_split
  from sklearn.ensemble import GradientBoostingClassifier
  from sklearn.metrics import accuracy_score
  from sklearn.model_selection import train_test_split

  data = pd.read_csv('bank_marketing.csv')

  # Choose the dependent and Independent variables
  X = data[['age','marital','ever_defaulted','housing_loan','Personal_loan']]
  Y = data[['y']]
  # Train, test/validation split
  X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.20, 
  random_state = 42)
  test_df = pd.concat ([X_test,y_test],axis =1 )

  # Initialize and train your model
  gbcl = GradientBoostingClassifier(random_state = 42)
  gbcl.fit(X_train, y_train)
  # Predict the test data based on the trained model
  gbcl_pred = gbcl.predict(X_test)
  accuracy_score(y_test, gbcl_pred)
  """)
  return ""

def xgboost():
  print(
  """  
  import pandas as pd
  from sklearn.model_selection import train_test_split
  from xgboost import XGBClassifier
  from sklearn.metrics import accuracy_score

  data = pd.read_csv('bank_marketing.csv')

  # Choose the dependent and Independent variables
  X = data[['age','marital','ever_defaulted','housing_loan','Personal_loan']]
  Y = data[['y']]
  # Train, test/validation split
  X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.20, 
  random_state = 42)
  test_df = pd.concat ([X_test,y_test],axis =1 )

  # Initialize and train your model
  model = XGBClassifier()
  model.fit(X_train,y_train)
  # Predict the test data based on the trained model
  xgbc_pred = model.predict(X_test)
  accuracy_score(y_test, xgbc_pred)
  """)
  return ""