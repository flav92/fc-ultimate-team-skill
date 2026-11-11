# Coach EA SPORTS FC Ultimate Team : un skill universel pour IA

Un coach Ultimate Team **en français**, pour n'importe quelle IA. Il n'invente pas de données : il **vérifie tout en temps réel** sur les sites de référence, via un navigateur piloté par l'IA, et il s'appuie sur **l'expertise du joueur**.


## Pourquoi ce skill existe

Avant de le créer, une recherche n'avait trouvé **que des bots d'achat-revente** sur le marché des transferts (interdits par EA), et **aucun outil de coaching technique** : compos (les compositions d'équipe), rôles, évolutions (« Evolutions » en jeu : faire progresser une carte via des défis), DCE (les « Squad Building Challenges », défis de création d'équipe), objectifs, events (événements à durée limitée). Ce skill comble ce manque. Il a été construit en jouant, pendant des heures, avec un joueur expert qui a corrigé chaque erreur.

## Le principe : tout vérifier en temps réel

Ultimate Team est un **marché volatil** : prix, cartes, DCE, évolutions et objectifs changent chaque jour. Ce qui existe aujourd'hui n'existera pas demain, et dans un an une nouvelle édition (FC 28…) changera les modes, les noms et peut-être les sites de référence. Le skill sépare donc :
- **la méthode durable** (`SKILL.md`) : sources en temps réel, hiérarchie des sources, comment trouver de nouvelles sources, checklists, erreurs à éviter ;
- **le savoir d'une édition** (`references/fc27.md`) : à remplacer chaque année ;
- **le joueur** (`references/profil-joueur-modele.md`) et **son club** (`references/etat-club-modele.md`) : modèles à remplir.

## Ce qu'il faut

1. Une IA qui peut **piloter un navigateur** (voir `references/navigateurs-ia.md`). Sans navigateur piloté, la méthode ne marche pas telle quelle : l'IA coach à partir des pages copiées ou des captures fournies par le joueur, et signale chaque donnée non vérifiée.
2. Idéalement, une IA avec **mémoire** ; dans tous les cas, `references/etat-club.md` (créé depuis `references/etat-club-modele.md`) reste **l'unique état du club**, requis pour toutes les IA — la mémoire de l'IA n'y fait que pointer.

## Installation

Le dossier suit le standard ouvert **Agent Skills** (`SKILL.md` avec `name` et `description`).

Récupérer le dépôt : `git clone https://github.com/flav92/fc-ultimate-team-skill.git` (ou télécharger le ZIP : une fois décompressé, le dossier s'appelle `fc-ultimate-team-skill-main/` et le dossier du skill est `fc-ultimate-team-skill-main/fut-ultimate-team/`).

Copier le dossier `fut-ultimate-team/` :

| IA / outil | Où copier le dossier |
|---|---|
| **Claude Code** | `~/.claude/skills/` (pour soi) ou `.claude/skills/` (dans un projet) |
| **Application Claude** (claude.ai) | Importer le dossier zippé dans les paramètres des skills |
| **OpenAI Codex, Gemini CLI, GitHub Copilot, Cursor** et autres outils compatibles Agent Skills | `.agents/skills/` dans le projet, ou le dossier de skills propre à l'outil (vérifier sa documentation, les chemins varient) |
| **IA de chat sans skills** (ChatGPT, Gemini, Mistral…) | Coller le contenu de `SKILL.md` dans les instructions personnalisées (GPT personnalisé, Gem, projet…) et joindre les fichiers de `references/` comme documents. À chaque début de session : joindre aussi l'état du club **à jour** et les synthèses disponibles ; à la fin : demander les mises à jour en blocs Markdown avec leur chemin de destination (voir SKILL.md, section 7) |

Puis :
1. Copier `references/profil-joueur-modele.md` en `references/profil-joueur.md` et le remplir.
2. Copier `references/etat-club-modele.md` en `references/etat-club.md` : c'est **l'unique état du club**, relu à chaque session et mis à jour à chaque décision, quelle que soit la mémoire de l'IA. **Pour démarrer, il suffit de remplir : plateforme, équipe actuelle, crédits, évolutions en cours** ; écrire « à confirmer » sur le reste (prix exacts, objectifs…).
3. Si plusieurs IA sont utilisées : après la première session, chaque IA synthétise sa propre mémoire dans `memoires/<son-nom>/SYNTHESE.md` au format `references/synthese-memoire-modele.md` (le dossier `memoires/` n'existe pas dans le dépôt : l'IA qui a accès aux fichiers le crée au premier enregistrement ; sinon, demander au joueur de le créer — voir SKILL.md section 7).
4. Dire à l'IA : « On joue à Ultimate Team, applique le skill ».
5. **Recommandé : installer le rappel de vérification** (voir ci-dessous).

L'arborescence attendue après installation (les fichiers remplis vivent dans `references/`, à côté des modèles) :

```
fut-ultimate-team/
├── SKILL.md
├── README.md
├── LICENSE
├── scripts/
│   └── fut_rappel.py
└── references/
    ├── fc27.md
    ├── navigateurs-ia.md
    ├── profil-joueur-modele.md
    ├── profil-joueur.md          ← rempli (privé, ne jamais publier)
    ├── etat-club-modele.md
    ├── etat-club.md              ← rempli (privé, ne jamais publier)
    └── synthese-memoire-modele.md

fut-ultimate-team/memoires/
└── <nom-ia>/SYNTHESE.md          ← créé au premier enregistrement (privé)
```

**Si le skill est installé dans un autre dépôt Git** (et non en copie autonome), reprendre les exclusions du `.gitignore` d'origine pour ne jamais publier les fichiers privés : `references/profil-joueur.md`, `references/etat-club.md`, `references/_ancienne-version*.md`, `memoires/`. En copie autonome, la licence se trouve dans le dossier du skill (`fut-ultimate-team/LICENSE`).

### Rappel de vérification automatique (fortement recommandé)

**Pourquoi :** le skill est lu une fois, au début de la session. Au fil d'une longue conversation, l'IA finit par « meubler » ses réponses avec des avis non vérifiés (« équipe solide », « joueur fort »), surtout dans les messages détendus. C'est arrivé en pratique, alors que la règle était écrite noir sur blanc. La solution qui marche : **un rappel injecté à chaque message**.

**Claude Code** : le script `scripts/fut_rappel.py` (Python 3) ajoute ce rappel à chaque message qui parle d'Ultimate Team, ou dès que la session a chargé le skill. Prérequis : `python --version` doit afficher une version de Python 3 (sinon, installer Python). Ajouter dans `~/.claude/settings.json` (en adaptant le chemin au dossier où le skill est réellement installé : niveau utilisateur ou projet) :

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

**Test :** dans une nouvelle session, envoyer un message contenant « Ultimate Team » : le rappel doit apparaître. Envoyer ensuite un message neutre (« bonjour ») dans une session où le skill a été chargé : le rappel doit apparaître aussi. Dans une session sans skill chargé, le message neutre ne déclenche rien (comportement attendu).

**Limites :** sur un message **neutre** (sans mot-clé), le rappel exige que le script puisse lire la transcription ; un message contenant un mot-clé déclenche le rappel même sans transcription. Sur une très longue session, chaque message neutre re-scanne la transcription (par blocs d'environ 1 Mo depuis le début du fichier, en s'arrêtant dès qu'il trouve le marqueur, en mémoire constante). La continuité dépend aussi du `timeout` du hook (10 s ici).

**Autres IA** : si l'outil ne gère pas les hooks, ajouter cette phrase au début des instructions personnalisées : *« À chaque réponse sur Ultimate Team : aucune note, aucun prix, aucune condition, aucun adjectif sur un joueur ou une équipe sans vérification sur le site de référence. Sinon, ne pas juger, ou écrire "non vérifié". »*

## Contenu

| Fichier | Rôle |
|---|---|
| `SKILL.md` | La méthode, valable pour toutes les éditions |
| `references/fc27.md` | Le savoir propre à FC 27 (sites, formations méta, évolutions, DCE, events, glossaire français-anglais) |
| `references/navigateurs-ia.md` | Piloter un navigateur selon l'IA |
| `references/profil-joueur-modele.md` | Modèle de profil du joueur |
| `references/etat-club-modele.md` | Modèle de suivi du club |
| `references/synthese-memoire-modele.md` | Format standard des synthèses de mémoire multi-IA (`memoires/`, absent du dépôt : créé au premier enregistrement) |
| `scripts/fut_rappel.py` | Hook de Claude Code : rappel de vérification à chaque message (voir Installation) |

## Nouvelle édition (FC 28 et après)

Suivre la section 1 de `SKILL.md` : trouver et valider les nouvelles sources, créer `references/fc28.md` sur le modèle de `fc27.md`, revérifier chaque mécanique.

## Licence : gratuit, pour toujours, et interdit à la revente

Ce skill est publié sous licence **[Creative Commons BY-NC 4.0](LICENSE)** :
- **Gratuit** : tout le monde peut l'utiliser, le copier, l'adapter et le partager.
- **Citation obligatoire** : toute réutilisation doit citer les auteurs et ce dépôt.
- **Usage commercial interdit** : personne n'a le droit de le vendre, ni de le revendre sous une autre forme (abonnement, application, formation payante…).

Auteurs : **XR1_FLAVINHO**, avec l'aide de Claude (Anthropic).

## Limites honnêtes

- L'IA ne joue pas : le **ressenti du joueur** prime sur les chiffres quand ils divergent.
- Les données de `fc27.md` datent de novembre 2026 : elles servent de modèle et de point de départ, **pas de vérité**.
- Les noms des outils de navigation des autres IA sont à vérifier : seul Claude in Chrome a été testé.
- Aucune automatisation du marché : c'est interdit par EA et ce n'est pas le but.
