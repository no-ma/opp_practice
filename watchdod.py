import time
import sys
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


#LoggingEvenHandlerを上書きして動作を変更
class LoggingEventHandler2(LoggingEventHandler):
    def on_created(self, event):    
        print("生成されました。" + event.src_path)


if __name__ == "__main__":
    path = '../OPP_PRACTICE'
    event_handler = LoggingEventHandler2()
    observer = Observer()       #監視オブジェクト生成
    observer.schedule(          #監視設定
        event_handler,
        path,
        recursive=True
        )
    observer.start()            #監視開始
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()