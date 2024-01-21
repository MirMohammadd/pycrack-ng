import os
import sys

sys.path.append(os.getcwd())

cwd = os.getcwd()
import threading
from lib.core.streamhandler import StreamReaderWriter
from lib.core.logger import logger
class Writer:

    def __init__(self, file_path=cwd+"/temp/capture.txt", write_line=False, sensitive=False):
        self._lock = threading.Lock()
        self.file_path = os.path.abspath(file_path)
        self.write_line = write_line
        self.file_stream = open(self.file_path, "w+", encoding="utf-8")
        self.output_file = None
        self.sensitive = sensitive
    
    def _write(self, content):
        try:
            self._lock.acquire()

            with StreamReaderWriter(self.file_stream) as streamer:
                content_str = str(content)
                streamer.write(content_str)
                
                if self.write_line:
                    streamer.writelines([content_str, '\n'])
                    streamer.seek(0)
                    for line in streamer:
                        logger.debug(line)
        except IOError as ex:
            pass
        finally:
            self._lock.release()

        return content
    

writer = Writer()