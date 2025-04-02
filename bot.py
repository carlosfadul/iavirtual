import tensorflow as tf
import numpy as np
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
#Esta version funciona
# Configura TensorFlow ANTES de crear el modelo
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)

# Define el conjunto de datos de entrada y salida
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Crea y entrena el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(celsius, fahrenheit, epochs=500, verbose=False)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "¡Hola! Envíame un valor en grados Celsius y te diré su equivalente en Fahrenheit."
    )

async def convert_temperature(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        celsius_value = float(update.message.text)
        # Ejecuta model.predict en un hilo separado
        fahrenheit_value = await asyncio.to_thread(
            model.predict, 
            np.array([celsius_value]), 
            verbose=0
        )
        response = f"{celsius_value}°C son aproximadamente {fahrenheit_value[0][0]:.2f}°F."
        await update.message.reply_text(response)
    except ValueError:
        await update.message.reply_text("Por favor, envíame un número válido.")
    except Exception as e:
        print(f"Error: {e}")
        await update.message.reply_text("Ocurrió un error al procesar tu solicitud.")

def main() -> None:
    application = Application.builder().token("7857348997:AAHRuIN1Hzs04aSQuPINmMkwH6-MFW1F2bU").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_temperature))
    
    print("Bot en funcionamiento...")
    application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())