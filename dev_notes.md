Dev notes

1. Open repo with Home assistant forked
1. Update to correct version
2. Modify devcontainer (mount + git fix, see commit: 74259f4c0ae0f7d17415834807b7754c4d69ee51)
3. Open in Visual studio code, rebuild and run devcontainer
4. Run HA with debugging mode: ctrl shift d, play button "Home Assistant"


Install hacs via docker script/guide: https://www.hacs.xyz/docs/use/download/download/
run in ./ha-forked/



https://www.awesome-ha.com/#third-party-add-ons
https://github.com/hacs/default?tab=readme-ov-file


Add integration:
https://my.home-assistant.io/redirect/config_flow_start/?domain=brewfather


hacs repo (not working)
https://my.home-assistant.io/redirect/hacs_repository/?owner=MvdDonk&repository=Brewfather

Current integration:
https://my.home-assistant.io/redirect/integration/?domain=brewfather



github flows/ versioning?


1. Install hacs
2. Add custom repo
3. Download/install brewfather via hacs (url or interface)



TODO:
- Documentatie uitbreiden, voorbeelden, opties beschrijven, nieuwe sesor beschrijven
- Templates voorbeeld gebruik
- version update in manifest gebasseerd op release??? of release basseren op dat versienummer
- registratie repo bij hacs (daarna docs aanpassen met handige links)