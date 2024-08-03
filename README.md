# OSM to CSV Converter

This script converts OpenStreetMap (OSM) data to CSV format, extracting ways based on specified keywords.

## Requirements

- Python 3
- pandas

## Installation

To install the required packages, you can use `pip`:

```sh
pip install pandas

## Usage

Run the script with the following command:

```sh
python OSM2CSV.py input.osm output.csv "keyword1" "keyword2"
```

- `input.osm`: The OSM file to be processed.
- `output.csv`: The name of the output CSV file.
- `"keyword1" "keyword2"`: Keywords to filter the ways in the OSM file (optional).

## Example

```sh
python3 OSM2CSV.py ims_map.osm "IMS_Oval.csv"
```

This will generate a `IMS_Oval.csv` file containing the ways from `ims_map.osm` that match the specified keywords (if any).

## How It Works

1. The script loads the OSM file and extracts node coordinates.
2. It then scans for ways that contain the specified keywords.
3. The resulting ways and their nodes are saved to a CSV file.

## Files

- `OSM2CSV.py`: The main script to run the conversion.
- `README.md`: This file, containing instructions and information about the project.
- `.gitignore`: (Optional) A file specifying which files and directories to ignore in the repository.

## License

This project is licensed under the Apache-2.0 License.
```

This `README.md` file includes all the necessary sections: Requirements, Installation, Usage, Example, How It Works, Files, and License. It provides a comprehensive guide for users to understand and use your script.
