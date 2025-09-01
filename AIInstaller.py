#!/usr/bin/env python3
import os
import time
import random
import itertools
import threading
import sys

# Spinner for "thinking" animation
def spinner_running(done_event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done_event.is_set():
            break
        sys.stdout.write(f'\r[+] Working... {c} ')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r[+] Done!           \n')

# Simulate progress bar
def simulate_progress(task_name, duration=3):
    print(f"[+] {task_name}...")
    for i in range(0, 101, 5):
        bar = ('#' * (i // 5)).ljust(20)
        print(f"    [{bar}] {i}%", end='\r')
        time.sleep(duration / 20.0)
    print(f"    [{'#' * 20}] 100% ✔\n")

# Show random friendly messages
def show_friendly_messages():
    messages = [
        "Ok, so why'd the rockerboy's output kick him out of the apartment?",
        "Cause he wasn't chippin' in. Hahaa!",
        "Fun fact: Grab something to drink, this is going to be awhile.",
        "Fun fact: I have a cat.",
        "Don't worry, it hasn't frozen."
    ]
    for msg in messages:
        time.sleep(random.randint(3, 8))
        print(f"💬 {msg}")
        thinking_animation(3)

# Simple thinking animation after messages
def thinking_animation(duration=3):
    done = threading.Event()
    t = threading.Thread(target=spinner_running, args=(done,))
    t.start()
    time.sleep(duration)
    done.set()
    t.join()

def main():
    print("[+] Installing Ollama...")
    simulate_progress("Running: curl -fsSL https://ollama.com/install.sh | sh", 4)
    os.system("curl -fsSL https://ollama.com/install.sh | sh")

    print("[+] Updating apt...")
    simulate_progress("Updating apt", 2)
    os.system("sudo apt update -y")

    print("[+] Installing certificates and curl...")
    simulate_progress("Installing certificates and curl", 2)
    os.system("sudo apt install ca-certificates curl -y")

    print("[+] Creating keyring directory...")
    simulate_progress("Creating /etc/apt/keyrings", 1)
    os.system("sudo install -m 0755 -d /etc/apt/keyrings")

    print("[+] Downloading Docker GPG key...")
    simulate_progress("Downloading Docker GPG", 2)
    os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | "
              "sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg")
    os.system("sudo chmod a+r /etc/apt/keyrings/docker.gpg")

    print("[+] Adding Docker repo to sources...")
    simulate_progress("Adding Docker repo", 1)
    os.system('echo '
              '"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] '
              'https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | '
              'sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')

    print("[+] Refreshing apt sources...")
    simulate_progress("Refreshing apt sources", 2)
    os.system("sudo apt update -y")

    print("[+] Installing Docker and plugins...")
    simulate_progress("Installing Docker", 4)
    os.system("sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y")

    print("[+] Launching Open WebUI container...")
    simulate_progress("Launching Open WebUI container", 3)
    show_friendly_messages()
    os.system("sudo docker run -d -p 3000:3000 --gpus all -v ollama:/root/.ollama -v open-webui:/app/backend/data "
              "--add-host=host.docker.internal:host-gateway --name open-webui --restart always "
              "ghcr.io/open-webui/open-webui:main")

    print("\n✅ All steps completed! Docker, Ollama, and Open WebUI are now running on your local server.")
    print("👉 Reminder: To run an AI model, use:")
    print("    ollama pull <your-model-name>")
    print("    ollama run <your-model-name>\n")
    print("🌐 Access the local WebUI at: http://localhost:3000")

if __name__ == "__main__":
    main()
