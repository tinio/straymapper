import csv
import io


def unicode_csv_reader(csv_data, dialect=csv.excel, **kwargs):
    """Yield rows from a file-like object of UTF-8 encoded bytes.

    ``csv_data`` is typically a Django ``UploadedFile``, whose iteration
    yields bytes; each line is decoded to text before parsing.
    """
    lines = (line.decode('utf-8') if isinstance(line, bytes) else line
             for line in csv_data)
    return csv.reader(lines, dialect=dialect, **kwargs)
