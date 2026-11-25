"""assemble_mix.py on tiny synthetic videos and masters; skipped where ffmpeg is not installed."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[0] / "scripts"))
import assemble_mix as am  # noqa: E402

HAVE_FFMPEG = bool(shutil.which("ffmpeg") and shutil.which("ffprobe"))


def make(d: Path, name: str, seconds: float, fps: int = 30, freq: int = 440, wav_seconds: float | None = None):
    video, wav = d / f"{name}.mp4", d / f"{name}.wav"
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                    "-f", "lavfi", "-i", f"testsrc=size=320x180:rate={fps}:duration={seconds}",
                    "-f", "lavfi", "-i", f"sine=frequency={freq}:duration={seconds}:sample_rate=48000",
                    "-ac", "2", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest",
                    str(video)], check=True)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                    "-f", "lavfi", "-i", f"sine=frequency={freq}:duration={wav_seconds or seconds}:sample_rate=48000",
                    "-ac", "2", "-c:a", "pcm_s24le", str(wav)], check=True)
    return {"video": str(video), "audio": str(wav), "title": name}


@unittest.skipUnless(HAVE_FFMPEG, "ffmpeg is not installed")
class Assemble(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.d = Path(self.dir.name)

    def tearDown(self):
        self.dir.cleanup()

    def test_matching_videos_are_copied_and_the_sound_follows_their_lengths(self):
        songs = [make(self.d, "A", 6), make(self.d, "B", 5, freq=550, wav_seconds=4.9), make(self.d, "C", 4, freq=660)]
        r = am.assemble(songs, self.d / "mix.mp4", -14, 1.0, "128k", "auto")
        self.assertEqual(r["video_mode"], "copy")
        self.assertEqual(r["chapters"][0], "0:00 A")
        self.assertAlmostEqual(r["tracks"][1]["start"], r["tracks"][0]["duration"], places=3)
        self.assertLess(abs(am.audio_length(self.d / "mix.mp4") - r["duration"]), 0.1)

    def test_videos_that_differ_are_encoded_once_in_auto(self):
        songs = [make(self.d, "A", 4), make(self.d, "B", 4, fps=25, freq=550)]
        r = am.assemble(songs, self.d / "mix.mp4", -14, 1.0, "128k", "auto")
        self.assertEqual(r["video_mode"], "encode")
        self.assertIn("B.mp4", r["video_mismatch"])
        self.assertEqual(am.probe_video(self.d / "mix.mp4")["params"]["r_frame_rate"], "30/1")

    def test_copy_refuses_videos_that_differ(self):
        songs = [make(self.d, "A", 4), make(self.d, "B", 4, fps=25, freq=550)]
        with self.assertRaises(am.Refusal):
            am.assemble(songs, self.d / "mix.mp4", -14, 1.0, "128k", "copy")

    def test_a_master_of_another_length_is_refused(self):
        songs = [make(self.d, "A", 4), make(self.d, "B", 6, freq=550, wav_seconds=3)]
        with self.assertRaises(am.Refusal) as e:
            am.assemble(songs, self.d / "mix.mp4", -14, 1.0, "128k", "auto")
        self.assertIn("B.wav", str(e.exception))

    def test_the_command_line_writes_the_tracklist(self):
        spec = self.d / "songs.json"
        spec.write_text(json.dumps([make(self.d, "A", 4), make(self.d, "B", 4, freq=550)]))
        code = am.main(["--songs", str(spec), "--out", str(self.d / "m.mp4"), "--tracklist", str(self.d / "t.json"),
                        "--fade", "0.5"])
        self.assertEqual(code, 0)
        self.assertEqual(len(json.loads((self.d / "t.json").read_text())["tracks"]), 2)


if __name__ == "__main__":
    unittest.main()
