# Video Speed Controller 🎥⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![CI](https://github.com/theanubis/media-playback-optimizer/actions/workflows/ci.yml/badge.svg)](https://github.com/theanubis/media-playback-optimizer/actions)

A command-line tool that calculates exact runtime savings and synthesizes ready-to-run FFmpeg commands for acceleration with automated pitch correction.

## Features
- 🚀 **Accurate Time Savings**: Calculates exact time saved for audiobooks, lectures, and footage.
- 🔊 **Pitch Correction**: Chains `atempo` audio filter algorithms to avoid high-pitch distortion.
- ⚡ **Zero External Dependencies**: Pure Python standard library with optional FFmpeg integration.

## Usage
```bash
python speed_ctrl.py -i input.mp4 -o fast.mp4 -s 1.75 -d 45
```

## License
MIT License.
