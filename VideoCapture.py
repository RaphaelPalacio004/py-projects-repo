import cv2
import keyboard
import os


def VideoCapture():
    try:
        videoCapture = cv2.VideoCapture(0)
        parentDirectory = r"C:\Users\Admin\Desktop\Py Projects"
        childFolder = "Screen Capture"
        mergePath = os.path.join(parentDirectory, childFolder)
        isPathExisting = True if os.path.exists(mergePath) else False
        userInput = int(input("Type in the number 0 to access the default camera: "))
        if userInput != 0:
            raise ValueError("Incorrect value type is provided.")
        elif isPathExisting:
            os.chdir(mergePath)
            frameWidth = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
            frameHeight = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
            codec = cv2.VideoWriter.fourcc(*"mp4v")
            byDefault = cv2.VideoWriter(
                "default.mp4", codec, 20.0, (frameWidth, frameHeight)
            )
            while 1:
                res, frame = videoCapture.read()
                byDefault.write(frame)
                cv2.imshow("Camera", frame)
                if cv2.waitKey(1) == keyboard.is_pressed("q"):
                    break

            return byDefault

        videoCapture.release()
        byDefault.release()
        cv2.destroyAllWindows()

    except Exception as exc:
        print(f"{exc}")


VideoCapture()
