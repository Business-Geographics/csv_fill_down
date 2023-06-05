import csv
import logging
import sys
import copy

log = logging.getLogger(__name__)


def save_to_csv(out_file: str, data: list, header=None):
    log.info(f"Writing to CSV {out_file}")

    # If no header provided, get field names from first data item
    modified_header = header
    if not modified_header:
        modified_header = []
        [modified_header.append(k) for k in data[0].keys()]

    # Write to csv
    try:
        with open(out_file, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=modified_header, extrasaction="ignore", dialect=csv.excel)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(e)


def load_from_csv_file(csv_path):
    log.info(f"Getting csv from {csv_path}")
    out_list = []
    with open(csv_path, encoding="utf-8", errors="ignore") as csv_file:
        for row in csv.DictReader(csv_file):
            out_list.append(dict(row))
    return out_list


def fill_down(in_csv_data: list):
    log.info("Filling data down")
    out_csv_data = []
    fill_data: dict = in_csv_data[0]
    cols = fill_data.keys()

    for row_idx in range(len(in_csv_data)):
        if row_idx % 10000 == 0:
            log.debug(f"{round(((row_idx / float(len(in_csv_data))) * 100),2) }% complete")

        row: dict = in_csv_data[row_idx]
        for col in cols:
            if row[col] is not None and row[col] != "":
                fill_data[col] = row[col]
        out_csv_data.append(copy.deepcopy(fill_data))

    return out_csv_data


if __name__ == "__main__":
    consoleHandler = logging.StreamHandler(sys.stdout)
    log.addHandler(consoleHandler)
    log.setLevel(logging.DEBUG)

    # Check that user has entered two arguments
    if len(sys.argv) < 3:  # 3 arguments: filename, in-csv, out-csv
        log.error("ERROR: Script needs two arguments: input CSV and output CSV")
        sys.exit()

    in_path: str = sys.argv[1]
    out_path: str = sys.argv[2]

    in_data = load_from_csv_file(in_path)
    out_data = fill_down(in_data)
    save_to_csv(out_path, out_data)
