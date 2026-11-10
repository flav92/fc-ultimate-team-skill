# Hook UserPromptSubmit : rappel de vérification pour le coaching Ultimate Team.
# Se déclenche si le message parle de FUT, ou si la session a chargé le skill fut-ultimate-team.
import json
import re
import sys

MOTS = re.compile(
    r"\b(fut|ultimate team|fc ?2\d|rivals?|champions|dce|sbc|evo(lution)?s?|evolab|"
    r"fut\.?gg|futbin|collectif|compo|pack|cr[ée]dits?|tournoi|objectifs?|passe de combat)\b",
    re.IGNORECASE,
)

RAPPEL = (
    "RAPPEL FUT (hook) : dans ta réponse, aucune note, aucun prix, aucun club, aucune condition, "
    "aucun style d'accélération et AUCUN ADJECTIF sur un joueur ou une équipe (solide, fort, faible, "
    "méta...) sans l'avoir vérifié sur FUT.GG dans cette session. Conditions d'objectif : recopier le "
    "texte exact. Si ce n'est pas vérifié : ne pas juger, ou écrire « non vérifié ». Relire chaque "
    "phrase factuelle avant d'envoyer."
)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    prompt = data.get("prompt", "") or ""
    actif = bool(MOTS.search(prompt))
    if not actif:
        chemin = data.get("transcript_path")
        if chemin:
            try:
                with open(chemin, encoding="utf-8", errors="ignore") as f:
                    actif = "fut-ultimate-team" in f.read()
            except Exception:
                pass
    if actif:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": RAPPEL,
            }
        }, ensure_ascii=True))


if __name__ == "__main__":
    main()
