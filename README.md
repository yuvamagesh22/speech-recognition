# Speech Recognition Audio Recorder

A simple Python application for recording audio from your microphone and playing it back. Perfect for capturing voice recordings, testing audio hardware, or building the foundation for speech recognition projects.

## Features

- **Audio Recording**: Record audio directly from your microphone with configurable duration
- **Audio Playback**: Play back recorded audio files with ease
- **WAV Format Support**: Works with standard WAV audio files
- **Simple CLI Interface**: Easy-to-use command-line interface for both recording and playback
- **Configurable Settings**: Adjust sample rate and recording duration as needed

## Requirements

- Python 3.6 or higher
- `sounddevice` - For microphone audio input/output
- `scipy` - For WAV file writing
- `soundfile` - For reading WAV files

## Installation

1. **Clone or download this repository**
   ```bash
   cd speech_recognition
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install sounddevice scipy soundfile
   ```

## Usage

### Recording Audio

To record 6 seconds of audio from your microphone:

```bash
python recorder.py
```

The script will:
- Print "Recording..." to indicate it's capturing audio
- Record for 6 seconds at a sample rate of 44100 Hz
- Save the recording as `recording.wav` in the current directory
- Print "Saved recording.wav" when complete

**Configuration Options** (edit `recorder.py`):
- `sample_rate = 44100` - Adjust the audio quality (higher = better quality, larger file size)
- `duration = 6` - Change recording duration in seconds
- `channels = 1` - Currently set to mono (single channel)

### Playing Back Audio

To play the recorded audio file:

```bash
python player.py
```

The script will:
- Load the `recording.wav` file
- Play the audio through your speakers
- Print "finished" when playback is complete

## File Structure

```
speech_recognition/
├── recorder.py          # Records audio from microphone
├── player.py            # Plays back recorded audio
└── README.md            # This file
```

## Technical Details

### Recorder
- **Library**: `sounddevice` with `scipy.io.wavfile`
- **Sample Rate**: 44100 Hz (CD quality)
- **Duration**: 6 seconds
- **Channels**: 1 (Mono)
- **Data Type**: 16-bit signed integer

### Player
- **Library**: `soundfile` with `sounddevice`
- **Playback**: Real-time audio playback with automatic format detection

## Troubleshooting

**"No audio input detected"**
- Ensure your microphone is connected and enabled
- Check system audio input settings
- Try running with administrator privileges

**"ModuleNotFoundError: No module named 'sounddevice'"**
- Make sure your virtual environment is activated
- Reinstall dependencies: `pip install sounddevice scipy soundfile`

**"Failed to read recording.wav"**
- Ensure `recording.wav` exists in the current directory
- Run `recorder.py` first to create the file

## Future Enhancements

Potential improvements for this project:
- Add command-line arguments for duration and sample rate
- Implement voice activity detection
- Add support for multiple audio formats
- Integrate with speech-to-text APIs
- Add audio visualization during recording
- Implement noise filtering and preprocessing

