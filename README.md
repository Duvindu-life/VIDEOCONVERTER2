# FFmpeg-Based Video Converter

This is a Python-based video converter that leverages the power of FFmpeg to convert video files between different formats. The project provides a simple command-line interface for converting videos and highlights various options available for customization.

## Features

- **Convert video files between various formats**
- **Customizable conversion settings**
- **Batch processing support**
- **Logging and error handling**

## Prerequisites

- **Python 3.6+**
- **FFmpeg**: Ensure FFmpeg is installed and available in your system's PATH. You can download it from [FFmpeg official site](https://ffmpeg.org/download.html).

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ffmpeg-video-converter.git
cd ffmpeg-video-converter
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Conversion

To convert a video file to another format, use the following command:

```bash
python converter.py input_file output_file
```

### Highlighted Options

- **Set Video Codec**: Specify the video codec to use for the output file.
  ```bash
  python converter.py input_file output_file --vcodec libx264
  ```

- **Set Audio Codec**: Specify the audio codec to use for the output file.
  ```bash
  python converter.py input_file output_file --acodec aac
  ```

- **Set Bitrate**: Define the video bitrate for the output file.
  ```bash
  python converter.py input_file output_file --bitrate 1000k
  ```

- **Set Frame Rate**: Define the frame rate for the output file.
  ```bash
  python converter.py input_file output_file --framerate 30
  ```

- **Batch Processing**: Convert all video files in a directory.
  ```bash
  python converter.py --batch input_directory output_directory
  ```

- **Logging**: Enable logging for the conversion process.
  ```bash
  python converter.py input_file output_file --log conversion.log
  ```

### Example

Convert `input.mp4` to `output.avi` using H.264 video codec and AAC audio codec:

```bash
python converter.py input.mp4 output.avi --vcodec libx264 --acodec aac
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FFmpeg](https://ffmpeg.org/) for providing a powerful multimedia framework.
- [Python](https://www.python.org/) for being an awesome programming language.
