from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))
sgd = SGD(learning_rate=0.01)
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=sgd,
    metrics=['accuracy']
)
model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=1)
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1] * 100))

