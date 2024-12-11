import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard
from kerastuner.tuners import RandomSearch
from sklearn.metrics import r2_score
import os

def build_model(hp):
    model = Sequential()
    model.add(LSTM(units=hp.Int('units', min_value=32, max_value=512, step=32), return_sequences=True, input_shape=(None, 1)))
    model.add(LSTM(units=hp.Int('units', min_value=32, max_value=512, step=32)))
    model.add(Dense(1))

    model.compile(
        optimizer=tf.keras.optimizers.Adam(hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])),
        loss='mse',
        metrics=['mse', 'mape', r2_score]
    )

    return model

def train_model(data):
    log_dir = os.path.join("tensorboard", "logs")
    tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

    tuner = RandomSearch(
        build_model,
        objective='val_loss',
        max_trials=5,
        executions_per_trial=3,
        directory='kerastuner',
        project_name='sales_forecasting'
    )

    tuner.search_space_summary()

    tuner.search(data['x_train'], data['y_train'], epochs=50, validation_data=(data['x_val'], data['y_val']), callbacks=[tensorboard_callback])

    tuner.results_summary()

    best_model = tuner.get_best_models(num_models=1)[0]

    best_model.save('models/best_model.h5')
    best_model.save('models/best_model.keras')

    return best_model
