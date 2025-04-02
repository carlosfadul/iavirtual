import tensorflow as tf
import numpy as np
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Define el conjunto de datos de entrada y salida
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Crea y entrena el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(celsius, fahrenheit, epochs=500, verbose=False)

# Función para manejar el comando /start
def start(update, context):
    update.message.reply_text("¡Hola! Envíame un valor en grados Celsius y te diré su equivalente en Fahrenheit.")

# Función para manejar los mensajes del usuario
def convert_temperature(update, context):
    try:
        # Convierte el mensaje del usuario a un número
        celsius_value = float(update.message.text)
        # Realiza la predicción
        fahrenheit_value = model.predict(np.array([celsius_value]))[0][0]
        # Responde con el resultado
        update.message.reply_text(f"{celsius_value}°C son aproximadamente {fahrenheit_value:.2f}°F.")
    except ValueError:
        update.message.reply_text("Por favor, envíame un número válido.")

# Configura el bot
def main():
    # Reemplaza 'YOUR_TOKEN_HERE' con el token de tu bot
    updater = Updater("7857348997:AAHRuIN1Hzs04aSQuPINmMkwH6-MFW1F2bU")
    dp = updater.dispatcher

    # Maneja el comando /start
    dp.add_handler(CommandHandler("start", start))
    # Maneja los mensajes de texto
    dp.add_handler(MessageHandler(filters.text & ~filters.command, convert_temperature))

    # Inicia el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()