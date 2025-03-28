from fastapi import FastAPI , File , UploadFile 
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model(r'C:/Users/ADMIN/Desktop/Tomato_disease/models/1.keras')

# C:\Users\ADMIN\Desktop\Tomato_disease\models\1.keras
CLASS_NAMES = ['Early blight', 'Late blight', 'Healthy']

@app.get('/ping')
async def ping():
    return 'Hello, I am Good now'

def read_file_as_image(data) -> np.ndarray:

    image = Image.open(BytesIO(data)).resize((128, 128))
    image = np.array(image)

    
    return image

@app.post('/predict')
async def predict(file: UploadFile = File(...)):

    try:
        # Convert to numpy array
        image = read_file_as_image(await file.read())
        image_batch = np.expand_dims(image,0)
        
        prediction = MODEL.predict(image_batch)
        predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
        confidence_level = np.max(prediction[0])


        return {
                'class': predicted_class ,
                'confidence': float(confidence_level)}
    
    except Exception as e:
        return {"error": str(e)}

   

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8001)
