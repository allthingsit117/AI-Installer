#!/usr/bin/env python3

import os
import random
import time
import sys

thinking_bar = "[{}] {:<3} {}".format("#" * 20, "100%", "✔")
fun_messages = [
    "💬 Ok, so why'd the rockerboy's output kick him out of the apartment?",
    "💬 Cause he wasn't chippin' in. Hahaa!",
    "💬 Fun fact: Grab something to drink, this is going to be awhile.",
    "💬 Fun fact: I have a cat.",
    "💬 Don't worry, it hasn't frozen."
]

def simulate_progress(task_name, seconds=2):
    print(f"[+] {task_name}...")
    for _ in range(seconds):
        sys.stdout.write("\r    [")
        for i in range(20):
            sys.stdout.write("#")
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write("] 100% ✔\n")
    time.sleep(0.5)

def show_random_message():
    message = random.choice(fun_messages)
    print(message)
    time.sleep(random.randint(2, 5))
    print("[+] Done!           ")
    print(thinking_bar)
    time.sleep(1)

def main():
    os.system("clear")
    print("[*] Starting AI-Installer...\n")
    
    # Install curl first
    print("[+] Installing certificates and curl...")
    simulate_progress("Installing certificates and curl", 2)
    os.system("sudo apt update -y")
    os.system("sudo apt install ca-certificates curl -y")

    show_random_message()

    # Install Ollama
    print("[+] Installing Ollama...")
    simulate_progress("Running: curl -fsSL https://ollama.com/install.sh | sh", 4)
    os.system("curl -fsSL https://ollama.com/install.sh | sh")

    show_random_message()

    # Create keyring directory
    print("[+] Creating keyring directory...")
    simulate_progress("Creating /etc/apt/keyrings", 2)
    os.system("sudo mkdir -p /etc/apt/keyrings")

    show_random_message()

    # Add Docker GPG key
    print("[+] Downloading Docker GPG key...")
    simulate_progress("Downloading Docker GPG", 2)
    os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg")

    show_random_message()

    # Add Docker repo
    print("[+] Adding Docker repo to sources...")
    simulate_progress("Adding Docker repo", 2)
    os.system('echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')

    show_random_message()

    # Update apt sources
    print("[+] Refreshing apt sources...")
    simulate_progress("Refreshing apt sources", 2)
    os.system("sudo apt update -y")

    show_random_message()

    # Install Docker
    print("[+] Installing Docker and plugins...")
    simulate_progress("Installing Docker", 3)
    os.system("sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y")

    show_random_message()

    # Launch Open WebUI container
    print("[+] Launching Open WebUI container...")
    simulate_progress("Launching Open WebUI container", 3)
    os.system("sudo docker run -d -p 3000:3000 --gpus all --name open-webui --restart always -e OLLAMA_HOST='http://host.docker.internal:11434' ghcr.io/open-webui/open-webui:main")

    show_random_message()

    print("\n✅ All steps completed! Docker, Ollama, and Open WebUI are now running on your local server.")
    print("👉 Reminder: To run an AI model, use:")
    print("    ollama pull <your-model-name>")
    print("    ollama run <your-model-name>")
    print("\n🌐 Access the local WebUI at: http://localhost:3000\n")

if __name__ == "__main__":
    main()
