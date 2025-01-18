import cv2
import time
import mediapipe as mp
import paho.mqtt.client as mqtt

# Configuração do MediaPipe
mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# Configuração do MQTT
broker_address = "broker.hivemq.com"  # Endereço do broker MQTT
port: 1883  # Porta padrão
topic = "seu/topico/aqui"  # Seu tópico do broker

client = mqtt.Client()
client.connect(broker_address)

def ligar():
    client.publish(topic, "ligar")
    print('TV ligada')

def desligar():
    client.publish(topic, "desligar")
    print('TV desligada')


# Função para detectar gestos
def detectar_gesto(landmarks):
    if not landmarks:
        return None

    # Punho fechado
    if (
        landmarks[8].y > landmarks[6].y and  # Indicador dobrado
        landmarks[12].y > landmarks[10].y and  # Médio dobrado
        landmarks[16].y > landmarks[14].y and  # Anelar dobrado
        landmarks[20].y > landmarks[18].y and  # Mínimo dobrado
        landmarks[4].y > landmarks[3].y  # Polegar dobrado
    ):
        return "punho fechado"

    # Mão aberta
    if (
        landmarks[8].y < landmarks[6].y and  # Indicador estendido
        landmarks[12].y < landmarks[10].y and  # Médio estendido
        landmarks[16].y < landmarks[14].y and  # Anelar estendido
        landmarks[20].y < landmarks[18].y and  # Mínimo estendido
        landmarks[4].y < landmarks[3].y  # Polegar estendido
    ):
        return "mão aberta"

    return None

# Configuração da câmera
capture = cv2.VideoCapture(0)
previous_gesture = None
previous_time = 0.0

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = holistic_model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Desenho dos landmarks
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Exibir coordenadas dos landmarks
        for idx, landmark in enumerate(results.right_hand_landmarks.landmark):
            h, w, _ = image.shape
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            cv2.putText(image, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        # Detecta gesto
        gesture = detectar_gesto(results.right_hand_landmarks.landmark)

        if gesture and gesture != previous_gesture:
            if gesture == "mão aberta":
                print("Ligando TV")
                ligar()
            elif gesture == "punho fechado":
                print("Desligando TV")
                desligar()
            previous_gesture = gesture
        
        '''
        # Exibir coordenadas dos landmarks
        for idx, landmark in enumerate(results.right_hand_landmarks.landmark):
            print(f"Landmark {idx}: (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")
        '''
        
    # Exibe FPS e imagem
    currentTime = time.time()
    fps = 1 / (currentTime - previous_time) if previous_time else 0
    cv2.putText(image, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    previous_time = currentTime  # Update as float

    cv2.imshow('Detecção de Gestos', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
