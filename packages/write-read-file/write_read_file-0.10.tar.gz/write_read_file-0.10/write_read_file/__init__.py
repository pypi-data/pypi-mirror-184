from isiter import isiter
from touchtouch import touch
from flatten_any_dict_iterable_or_whatsoever import fla_tu

def write_utf8(path, data, endofline="\n"):
    touch(path)
    with open(path, mode="w", encoding="utf-8") as f:
        for _ in fla_tu([data]):
            f.write(str(_[0]))
            f.write(endofline)


def write_bytes(path, data, endofline=None):
    touch(path)
    isit = isiter(data)
    with open(path, mode="wb") as f:
        if isit:
            for _ in fla_tu([data]):
                f.write(_[0])
                if endofline is not None:
                    f.write(endofline)
        else:
            f.write(data)


def read_bytes(path):
    with open(path, mode="rb") as f:
        data = f.read()
    return data


def copy_file(src, dst):
    with open(dst, "wb") as outfile:
        with open(src, "rb") as infile:
            for line in infile:
                outfile.write(line)


def read_and_decode(path, decodeformat="utf-8", on_encoding_errors="replace"):
    asbytes = read_bytes(path)
    return asbytes.decode(decodeformat, errors=on_encoding_errors)


def iterread_bytes(path, chunksize=8192):
    with open(path, mode="rb") as f:
        while chunk := f.read(chunksize):
            yield chunk


def iterread_text(path, encoding="utf-8", strip_newline=True, ignore_empty_lines=True):
    with open(path, mode="r", encoding=encoding) as f:
        for line in f.readlines():
            if strip_newline:
                line = line.rstrip()
            if ignore_empty_lines:
                if line == "":
                    continue
            yield line


