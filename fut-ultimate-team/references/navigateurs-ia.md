# Piloter un navigateur selon l'IA utilisée

La méthode repose sur la **lecture en temps réel** de sites qui bloquent les robots. Il faut donc une IA capable de **piloter un vrai navigateur**, idéalement **celui du joueur** (connecté à ses comptes, par exemple pour l'Evo Lab de FUT.GG).

Les noms des produits changent vite : **vérifier le nom et la disponibilité actuels** avant de conseiller une option. Celles marquées « à vérifier » n'ont pas été testées avec ce skill.

## Options par famille d'IA

| IA / harnais | Navigateur piloté | Testé avec ce skill |
|---|---|---|
| **Claude** (Claude Code, application Claude) | Extension **Claude in Chrome** : agit dans le Chrome du joueur, avec ses connexions | **Oui** (FC 27, novembre 2026) |
| **ChatGPT** | Mode agent avec navigateur, ou navigateur ChatGPT dédié | À vérifier |
| **Gemini** | Gemini intégré à Chrome / mode agent | À vérifier |
| **Agents de code** (Codex, Gemini CLI, Copilot, Cursor…) | Serveur MCP de navigateur (Playwright, Chrome DevTools…), branché si possible sur le profil Chrome du joueur | À vérifier. Un navigateur « sans tête » et non connecté risque d'être bloqué par les sites |
| **Navigateurs à agent intégré** (Comet…) | Le navigateur lui-même | À vérifier |
| **IA sans accès au web** | Aucun | Le joueur copie les pages ou envoie des captures ; l'IA signale chaque donnée non vérifiée |

## Bonnes pratiques communes

- **Ne jamais contourner un blocage** (API interdites aux robots, erreurs 403, captchas) : lire les pages comme une personne.
- Ouvrir **un nouvel onglet** pour le travail, ne pas toucher aux onglets du joueur, et fermer ses onglets à la fin.
- Grouper les actions quand l'outil le permet (navigation, attente, lecture).
- Attendre que les pages en JavaScript se chargent (environ 2 s sur FUT.GG).
- Préférer une **recherche ciblée d'élément** (« prix de la carte X ») à l'extraction de tout le texte d'une page : les pages de données sont énormes.
- Une action qui modifie le compte du joueur (ajouter un joueur à l'Evo Lab, enregistrer un build) ne se fait **qu'à sa demande**.
- Ne jamais saisir de mot de passe ni de données de paiement à la place du joueur.

## Notes pour Claude in Chrome (testé)

- Charger les outils `mcp__claude-in-chrome__*` en un seul appel de recherche d'outils : `tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `find`, `get_page_text`, `read_page`, `computer`, `browser_batch`, `tabs_close_mcp`.
- `find` avec une description précise (« liste GG Rating : poste, valeur, rôle ») est plus fiable que `get_page_text`.
- `browser_batch` enchaîne navigation, attente et lecture en un seul aller-retour.
- Dans l'Evo Lab, les clics se font avec `computer` (capture d'écran pour repérer les boutons, puis clic aux coordonnées).
- Si `find` échoue juste après une navigation (« page non analysable »), attendre 2 s puis réessayer.
