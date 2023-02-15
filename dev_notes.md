Dev notes
1. https://developers.home-assistant.io/docs/development_environment/
2. Ctrl + shift + p --> Tasks: Run Task --> Run Home assistant core
3. or F5 for debug
4. https://developers.home-assistant.io/docs/add-ons/testing/
5. in .devcontainer  "postStartCommand": "bash devcontainer_bootstrap",  is replaced by  "postStartCommand": "sudo -E bash devcontainer_bootstrap"  
6. in .vscode/tasks.json  "command": "supervisor_run", is replaced by "command": "sudo chmod a+x /usr/bin/supervisor* && sudo -E supervisor_run",
7. in VSCode run task: Start Home Assistant
8. Enable advanced mode on user account
5. Install hacs: https://hacs.xyz/docs/setup/download/ (OS/Supervised)
6. Restart
7. Go to integrations add HACS
8. Go to HACS -> Custom repositories
9. Add dev branche