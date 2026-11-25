"""assemble_mix.py on tiny synthetic videos; skipped where ffmpeg is not installed."""

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


def make(path: Path, seconds: float, fps: int = 30, freq: int = 440) -> None:
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                    "-f", "lavfi", "-i", f"testsrc=size=320x180:rate={fps}:duration={seconds}",
                    "-f", "lavfi", "-i", f"sine=frequency={freq}:duration={seconds}:sample_rate=48000",
                    "-ac", "2", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest",
                    str(path)], check=True)


@unittest.skipUnless(HAVE_FFMPEG, "ffmpeg is not installed")
class Assemble(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.d = Path(self.dir.name)

    def tearDown(self):
        self.dir.cleanup()

    def songs(self, *specs):
        out = []
        for i, (secs, fps) in enumerate(specs):
            f = self.d / f"s{i}.mp4"
            make(f, secs, fps, 300 + 100 * i)
            out.append({"file": str(f), "title": f"Song {i}"})
        return out

    def test_joins_songs_with_chapters_and_lengths_that_add_up(self):
        songs = self.songs((6, 30), (5, 30), (4, 30))
        result = am.assemble(songs, self.d / "mix.mp4", -14, -1.5, 1.0, "128k")
        self.assertEqual([t["title"] for t in result["tracks"]], ["Song 0", "Song 1", "Song 2"])
        self.assertAlmostEqual(result["duration"], sum(t["duration"] for t in result["tracks"]), delta=0.5)
        self.assertEqual(result["chapters"][0], "0:00 Song 0")
        self.assertTrue(result["chapters"][1].startswith("0:0"))
        # The video stream was copied, not re-encoded: same codec and frame rate as the inputs.
        p = am.probe(self.d / "mix.mp4")
        self.assertEqual((p["video"]["codec_name"], p["video"]["r_frame_rate"]), ("h264", "30/1"))

    def test_a_song_with_other_parameters_is_refused_by_name(self):
        songs = self.songs((4, 30), (4, 25))
        with self.assertRaises(am.Refusal) as e:
            am.assemble(songs, self.d / "mix.mp4", -14, -1.5, 1.0, "128k")
        self.assertIn("s1.mp4", str(e.exception))
        self.assertFalse((self.d / "mix.mp4").exists())

    def test_one_song_is_not_a_mix(self):
        with self.assertRaises(am.Refusal):
            am.assemble(self.songs((4, 30)), self.d / "mix.mp4", -14, -1.5, 1.0, "128k")

    def test_the_command_line_writes_the_tracklist(self):
        songs = self.songs((4, 30), (4, 30))
        spec = self.d / "songs.json"
        spec.write_text(json.dumps(songs))
        code = am.main(["--songs", str(spec), "--out", str(self.d / "m.mp4"),
                        "--tracklist", str(self.d / "t.json"), "--fade", "0.5"])
        self.assertEqual(code, 0)
        self.assertEqual(len(json.loads((self.d / "t.json").read_text())["tracks"]), 2)


if __name__ == "__main__":
    unittest.main()
