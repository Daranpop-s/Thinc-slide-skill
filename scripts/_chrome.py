"""Shared helpers: find Chrome on macOS / Windows / Linux, start it headless, stop it cleanly. No shell tools needed."""
import os, sys, shutil, pathlib, subprocess

# Thai in LINT lines / paths must not crash a Windows console (cp1252/cp874)
for s in (sys.stdout, sys.stderr):
    try: s.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

def find_chrome():
    """$CHROME wins. Else the usual install paths for this OS. Else anything named chrome/chromium on PATH."""
    env = os.environ.get("CHROME")
    if env:
        if pathlib.Path(env).exists() or shutil.which(env): return shutil.which(env) or env
        raise SystemExit(f"CHROME={env} does not exist")
    c = []
    if sys.platform == "darwin":
        c += ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              os.path.expanduser("~/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
              "/Applications/Chromium.app/Contents/MacOS/Chromium",
              "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"]
    elif os.name == "nt":
        for base in (os.environ.get("PROGRAMFILES", r"C:\Program Files"),
                     os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)"),
                     os.environ.get("LOCALAPPDATA", "")):
            if base:
                c += [os.path.join(base, r"Google\Chrome\Application\chrome.exe"),
                      os.path.join(base, r"Microsoft\Edge\Application\msedge.exe")]   # Edge ships with Windows; same engine
    else:
        c += ["/opt/pw-browsers/chromium"]
    for p in c:
        if p and pathlib.Path(p).exists(): return p
    for n in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"):
        if shutil.which(n): return shutil.which(n)
    raise SystemExit("Chrome not found. Install Google Chrome, or set CHROME to its full path.")

def base_args(user_data_dir):
    a = [find_chrome(), "--headless=new", "--disable-gpu", f"--user-data-dir={user_data_dir}"]
    if hasattr(os, "geteuid") and os.geteuid() == 0: a.insert(1, "--no-sandbox")   # root on Linux/cloud refuses to start without it
    return a

def stop(p):
    """Kill Chrome and its helper processes (whole tree) on any OS."""
    if p.poll() is not None: return
    if os.name == "nt":
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(p.pid)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        try: os.killpg(p.pid, 9)
        except Exception: p.kill()

def popen(args):
    """Start Chrome in its own process group so stop() can take down the helpers too."""
    kw = dict(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.name == "nt": kw["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
    else: kw["start_new_session"] = True
    return subprocess.Popen(args, **kw)
