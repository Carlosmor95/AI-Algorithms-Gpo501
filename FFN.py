import json
import numpy as np
import tensorflow as tf
from flask import jsonify

def train_and_save_model(training_data_json, saved_model_path):
    data = training_data_json

    X_train = np.array([entry['features'] for entry in data['data']])
    y_train = np.array([entry['label'] for entry in data['data']])

    X_test = np.random.rand(10, 2)
    y_test = np.random.randint(2, size=(10, 1))

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=50, batch_size=8, validation_data=(X_test, y_test))

    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test Loss: {loss:.4f}")
    print(f"Test Accuracy: {accuracy * 100:.2f}%")

    model.save(saved_model_path)
    print(f"Model saved at {saved_model_path}")

    predictions = model.predict(X_test)

    print("Predictions:")
    print(predictions)

    results = {
        "predictions": predictions.tolist(),
        "test_loss": float(loss),
        "test_accuracy": float(accuracy)
    }

    return jsonify(results)
