import cv2
from pyzbar import pyzbar

def scan_qr_code():
    # Initializing the camera from open cv
    cap = cv2.VideoCapture(0)

    # data storage and looping variables.
    storage = []
    qr_code_detected = False

    while True:
        # Reading the qr code
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        qr_codes = pyzbar.decode(gray)

        # Decoding the code
        for qr_code in qr_codes:
            # Extract the data from the QR code and printing it
            storage.append(qr_code.data.decode('utf-8'))
            print(storage)

            # Breaking loop
            qr_code_detected = True
            break

        # Displaying the camera window
        cv2.imshow("QR Code Scanner", frame)

        # Breaking loop if the qr is detected or if user presses q/ 1
        if qr_code_detected or cv2.waitKey(1) == ord("q"):
            break

    # Releasing the camera
    cap.release()
    cv2.destroyAllWindows()


scan_qr_code()
