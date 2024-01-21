import io

class StreamReaderWriter:
    def __init__(self, stream, encoding='utf-8'):
        self._stream = stream
        self._encoding = encoding
        assert isinstance(self._stream, io.TextIOWrapper), repr(self._stream)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
        # No need to close the stream here, as it is managed by the 'with' statement

    def read(self, size=-1):
        return self._stream.read(size)

    def readline(self, size=-1):
        return self._stream.readline(size)

    def write(self, data):
        try:
            if not self._stream.closed:
                if isinstance(data, str):
                    self._stream.write(data)
                elif isinstance(data, bytes):
                    self._stream.write(data.decode(self._encoding))
                elif isinstance(data, dict):
                    for key, item in data.items():
                        self._stream.write(str(key))
                        self._stream.write(str(item))
        except Exception as e:
            pass

    def writelines(self, lines):
        try:
            if not self._stream.closed:
                for line in lines:
                    self.write(line)
        except Exception as e:
            pass

    def seek(self, offset, whence=0):
        self._stream.seek(offset, whence)

    def tell(self):
        return self._stream.tell()

    def __iter__(self):
        return iter(self._stream)