# Coach EA SPORTS FC Ultimate Team : un skill universel pour IA

Un coach Ultimate Team **en français**, pour n'importe quelle IA. Il n'invente pas de données : il **vérifie tout en temps réel** sur les sites de référence, via un navigateur piloté par l'IA, et il s'appuie sur **l'expertise du joueur**.


## Pourquoi ce skill existe

Avant de le créer, une recherche n'avait trouvé **que des bots d'achat-revente** sur le marché des transferts (interdits par EA), et **aucun outil de coaching technique** : compos, rôles, évolutions, DCE, objectifs, events. Ce skill comble ce manque. Il a été construit en jouant, pendant des heures, avec un joueur expert qui a corrigé chaque erreur.

## Le principe : tout vérifier en temps réel

Ultimate Team est un **marché volatil** : prix, cartes, DCE, évolutions et objectifs changent chaque jour. Ce qui existe aujourd'hui n'existera pas demain, et dans un an une nouvelle édition (FC 28…) changera les modes, les noms et peut-être les sites de référence. Le skill sépare donc :
- **la méthode durable** (`SKILL.md`) : sources en temps réel, hiérarchie des sources, comment trouver de nouvelles sources, checklists, erreurs à éviter ;
- **le savoir d'une édition** (`references/fc27.md`) : à remplacer chaque année ;
- **le joueur** (`references/profil-joueur-modele.md`) et **son club** (`references/etat-club-modele.md`) : modèles à remplir.

## Ce qu'il faut

1. Une IA qui peut **piloter un navigateur** (voir `references/navigateurs-ia.md`). Sans accès au web, la méthode fonctionne en mode dégradé : le joueur copie les pages.
2. Idéalement, une IA avec **mémoire** ; dans tous les cas, `references/etat-club.md` (créé depuis `references/etat-club-modele.md`) reste **l'unique état du club** — la mémoire de l'IA n'y fait que pointer.

## Installation

Le dossier suit le standard ouvert **Agent Skills** (`SKILL.md` avec `name` et `description`). Copier le dossier `fut-ultimate-team/` :

| IA / outil | Où copier le dossier |
|---|---|
| **Claude Code** | `~/.claude/skills/` (pour soi) ou `.claude/skills/` (dans un projet) |
| **Application Claude** (claude.ai) | Importer le dossier zippé dans les paramètres des skills |
| **OpenAI Codex, Gemini CLI, GitHub Copilot, Cursor** et autres outils compatibles Agent Skills | `.agents/skills/` dans le projet, ou le dossier de skills propre à l'outil (vérifier sa documentation, les chemins varient) |
| **IA de chat sans skills** (ChatGPT, Gemini, Mistral…) | Coller le contenu de `SKILL.md` dans les instructions personnalisées (GPT personnalisé, Gem, projet…) et joindre les fichiers de `references/` comme documents |

Puis :
1. Copier `references/profil-joueur-modele.md` en `profil-joueur.md` et le remplir.
2. Copier `references/etat-club-modele.md` en `etat-club.md` : c'est **l'unique état du club**, relu à chaque session et mis à jour à chaque décision, quelle que soit la mémoire de l'IA.
3. Si plusieurs IA sont utilisées : après la première session, chaque IA synthétise sa propre mémoire dans `memoires/<son-nom>/SYNTHESE.md` au format `references/synthese-memoire-modele.md` (le dossier est livré vide, voir SKILL.md section 7).
4. Dire à l'IA : « On joue à Ultimate Team, applique le skill ».
5. **Recommandé : installer le rappel de vérification** (voir ci-dessous).

### Rappel de vérification automatique (fortement recommandé)

**Pourquoi :** le skill est lu une fois, au début de la session. Au fil d'une longue conversation, l'IA finit par « meubler » ses réponses avec des avis non vérifiés (« équipe solide », « joueur fort »), surtout dans les messages détendus. C'est arrivé en pratique, alors que la règle était écrite noir sur blanc. La solution qui marche : **un rappel injecté à chaque message**.

**Claude Code** : le script `scripts/fut_rappel.py` (Python 3) ajoute ce rappel à chaque message qui parle d'Ultimate Team, ou dès que la session a chargé le skill. Ajouter dans `~/.claude/settings.json` (en adaptant le chemin vers le dossier du skill) :

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python \"$HOME/.claude/skills/fut-ultimate-team/scripts/fut_rappel.py\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

Sous Windows, écrire le chemin complet, par exemple `C:/Users/<nom>/.claude/skills/fut-ultimate-team/scripts/fut_rappel.py`. S'il y a déjà des hooks, **ajouter** cette entrée sans remplacer les autres. Pour vérifier ou désactiver : commande `/hooks`.

**Autres IA** : si l'outil ne gère pas les hooks, ajouter cette phrase au début des instructions personnalisées : *« À chaque réponse sur Ultimate Team : aucune note, aucun prix, aucune condition, aucun adjectif sur un joueur ou une équipe sans vérification sur le site de référence. Sinon, ne pas juger, ou écrire "non vérifié". »*

## Contenu

| Fichier | Rôle |
|---|---|
| `SKILL.md` | La méthode, valable pour toutes les éditions |
| `references/fc27.md` | Le savoir propre à FC 27 (sites, formations méta, évolutions, DCE, events, glossaire français-anglais) |
| `references/navigateurs-ia.md` | Piloter un navigateur selon l'IA |
| `references/profil-joueur-modele.md` | Modèle de profil du joueur |
| `references/etat-club-modele.md` | Modèle de suivi du club |
| `references/synthese-memoire-modele.md` | Format standard des synthèses de mémoire multi-IA (`memoires/`, livré vide) |
| `scripts/fut_rappel.py` | Hook de Claude Code : rappel de vérification à chaque message (voir Installation) |

## Nouvelle édition (FC 28 et après)

Suivre la section 1 de `SKILL.md` : trouver et valider les nouvelles sources, créer `references/fc28.md` sur le modèle de `fc27.md`, revérifier chaque mécanique.

## Licence : gratuit, pour toujours, et interdit à la revente

Ce skill est publié sous licence **[Creative Commons BY-NC 4.0](../LICENSE)** :
- **Gratuit** : tout le monde peut l'utiliser, le copier, l'adapter et le partager.
- **Citation obligatoire** : toute réutilisation doit citer les auteurs et ce dépôt.
- **Usage commercial interdit** : personne n'a le droit de le vendre, ni de le revendre sous une autre forme (abonnement, application, formation payante…).

Auteurs : **XR1_FLAVINHO**, avec l'aide de Claude (Anthropic).

## Limites honnêtes

- L'IA ne joue pas : le **ressenti du joueur** prime sur les chiffres quand ils divergent.
- Les données de `fc27.md` datent de novembre 2026 : elles servent de modèle et de point de départ, **pas de vérité**.
- Les noms des outils de navigation des autres IA sont à vérifier : seul Claude in Chrome a été testé.
- Aucune automatisation du marché : c'est interdit par EA et ce n'est pas le but.
