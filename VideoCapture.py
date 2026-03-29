import cv2
import os
from loguru import logger


class Video:
    def __init__(
        self,
        video_capture,
        parent,
        child,
        merge_directory,
        is_existing,
        user_input,
        frame_width,
        frame_height,
        codec,
        by_default,
        vc_frame,
    ):
        self.video_capture = video_capture
        self.parent = parent
        self.child = child
        self.merge_directory = merge_directory
        self.is_existing = is_existing
        self.user_input = user_input
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.codec = codec
        self.by_default = by_default
        self.vc_frame = vc_frame

    def VideoCapture(self):
        try:
            self.video_capture = cv2.VideoCapture(0)
            self.parent = r"C:\Users\Admin\Desktop\Py Projects"
            self.child = "Screen Capture"
            self.merge_directory = os.path.join(self.parent, self.child)
            self.is_existing = True if os.path.exists(self.merge_directory) else False
            self.user_input = int(
                input("Type in the number 0 to access the default camera: ")
            )
            if self.user_input != 0:
                return logger.warning(
                    "User input should only be the number zero(0) value."
                )
            if self.is_existing:
                os.chdir(self.merge_directory)
                self.frame_width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
                self.frame_height = int(
                    self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
                )
                self.codec = cv2.VideoWriter.fourcc(*"mp4v")
                self.by_default = cv2.VideoWriter(
                    "default.mp4",
                    self.codec,
                    20.0,
                    (self.frame_width, self.frame_height),
                )
            while 1:
                res, self.vc_frame = self.video_capture.read()
                self.by_default.write(self.vc_frame)
                cv2.imshow("Camera", self.vc_frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            self.video_capture.release()
            self.by_default.release()
            cv2.destroyAllWindows()
        except ValueError:
            return logger.exception("The application encountered a value error.")
        except TypeError:
            return logger.exception("The application encountered a type error.")


Result = Video(
    video_capture="",
    parent="",
    child="",
    merge_directory="",
    is_existing=False,
    user_input=int,
    frame_width=int,
    frame_height=int,
    codec=int,
    by_default="",
    vc_frame="",
)
Result.VideoCapture()
