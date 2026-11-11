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

TAILLE_BLOC = 1 << 20  # 1 Mo : lecture par blocs, mémoire constante même sur une grosse transcription.


def transcript_contient(chemin, marqueur="fut-ultimate-team"):
    # Lecture par blocs depuis le début, arrêt dès la première occurrence du marqueur.
    cible = marqueur.encode("utf-8")
    chevauchement = len(cible) - 1  # pour un marqueur à cheval sur deux blocs
    try:
        with open(chemin, "rb") as f:
            precedent = b""
            while True:
                bloc = f.read(TAILLE_BLOC)
                if not bloc:
                    return False
                if cible in precedent + bloc:
                    return True
                precedent = bloc[-chevauchement:] if chevauchement else b""
    except Exception:
        return False


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
            actif = transcript_contient(chemin)
    if actif:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": RAPPEL,
            }
        }, ensure_ascii=True))


if __name__ == "__main__":
    main()
