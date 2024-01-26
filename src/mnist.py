import tensorflow as tf


def main() -> None:
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(x=x_train, y=y_train, epochs=5)

    test_loss, test_acc = model.evaluate(x=x_test, y=y_test, verbose=0)

    print("Metrics")
    print(f"Test Loss: {test_loss*100:.2f}%")
    print(f"Test Accuracy: {test_acc*100:.2f}%")


if __name__ == "__main__":
    main()
