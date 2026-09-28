#!/usr/bin/env python3
"""
video-speed-controller — Playback rate scaler and FFmpeg command builder.
"""
import sys
import argparse

def calculate_adjusted_duration(duration_seconds: float, speed_factor: float) -> tuple[float, float]:
    if speed_factor <= 0:
        raise ValueError("Speed factor must be positive")
    new_duration = duration_seconds / speed_factor
    saved_time = duration_seconds - new_duration
    return new_duration, saved_time

def generate_ffmpeg_cmd(input_path: str, output_path: str, speed: float, keep_pitch: bool = True) -> str:
    video_filter = f"setpts={1.0/speed:.4f}*PTS"
    audio_filters = []
    curr = speed
    while curr > 2.0:
        audio_filters.append("atempo=2.0")
        curr /= 2.0
    while curr < 0.5:
        audio_filters.append("atempo=0.5")
        curr /= 0.5
    audio_filters.append(f"atempo={curr:.4f}")
    af_str = ",".join(audio_filters)

    return f'ffmpeg -i "{input_path}" -filter_complex "[0:v]{video_filter}[v];[0:a]{af_str}[a]" -map "[v]" -map "[a]" "{output_path}"'

def main():
    parser = argparse.ArgumentParser(description="Video playback speed calculator & FFmpeg generator")
    parser.add_argument("-i", "--input", help="Path to input video file", default="video.mp4")
    parser.add_argument("-o", "--output", help="Path to output video file", default="video_fast.mp4")
    parser.add_argument("-s", "--speed", type=float, default=1.5, help="Playback speed multiplier (e.g. 1.25, 1.5, 2.0)")
    parser.add_argument("-d", "--duration", type=float, help="Original video duration in minutes", default=60.0)

    args = parser.parse_args()
    dur_sec = args.duration * 60
    new_sec, saved_sec = calculate_adjusted_duration(dur_sec, args.speed)

    print("=" * 60)
    print("  Video Speed & Duration Scaler")
    print("=" * 60)
    print(f"Original Duration : {args.duration:.1f} mins ({dur_sec:.0f}s)")
    print(f"Speed Factor      : {args.speed:.2f}x")
    print(f"Adjusted Duration : {new_sec/60:.1f} mins ({new_sec:.0f}s)")
    print(f"Time Saved        : {saved_sec/60:.1f} mins ({saved_sec:.0f}s)")
    print("-" * 60)
    print("Generated FFmpeg Command:")
    print(generate_ffmpeg_cmd(args.input, args.output, args.speed))
    print("=" * 60)

if __name__ == "__main__":
    main()
