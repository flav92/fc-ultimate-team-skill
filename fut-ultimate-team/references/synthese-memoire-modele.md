# Modèle : synthèse de mémoire (format standard)

> Ce modèle définit le format de `memoires/<nom-ia>/SYNTHESE.md`. Il ne contient aucune donnée personnelle : chaque IA le copie et le remplit avec le résumé de SA propre mémoire.
> Règles : dater chaque item ; porter le statut de chaque info ; pointer vers les fichiers du skill plutôt que recopier ; en cas de contestation, la mémoire brute de l'IA et les transcriptions font foi, jamais la synthèse ; régénérer après chaque mise à jour de mémoire.
> **Statuts (SKILL.md section 7, par fiabilité) :** confirmé en jeu (vu en jeu) > vérifié (source temps réel, datée) > vérifié (site en retard, ex. FUTBIN) > déclaré (parole du joueur : *fait* à vérifier, *préférence* appliquée telle quelle) > déduit (règle tirée des choix passés, à revalider) > supposé.
> **Colonnes :** « Remplace (date) » = la date de l'entrée précédente qu'on vient de remplacer, « — » si aucune ; « Origine » = d'où vient la règle (déclarée / déduite de <choix, date> / recadrage du <date>) ; « Dernière validation » = la date de la dernière confirmation avec le joueur.

# Synthèse de mémoire — <nom de l'IA> (projet : <projet>)

Mis à jour le : <date> (par <IA>)

## Décisions (datées, avec raison et statut)
| Date | Décision | Raison | Statut | Remplace (date) |
|---|---|---|---|---|
| 2026-11-10 *(exemple fictif à retirer)* | Garder le gardien actuel du club | préféré du joueur | déclaré (préférence) | — |

## Règles validées (origine, statut, dernière validation)
| Règle | Origine (déclarée / déduite de / recadrage du) | Statut | Dernière validation | Remplace (date) |
|---|---|---|---|---|
| Reprendre les DCE avant de vendre un fourrage *(exemple fictif à retirer)* | déduite des ventes du 2026-11-09 | confirmé en jeu | 2026-11-10 | 2026-11-09 |
|  |  |  |  |  |

## Préférences et non-négociables
<!-- Pointeurs vers les fichiers de référence du skill ; ne recopier que ce qui n'existe nulle part ailleurs. Chaque préférence porte sa date. -->

## Déductions en attente de revalidation
| Déduction | Statut | Preuves (choix et dates) | Revalidée (date) ? |
|---|---|---|---|
| Préfère garder les pépites du club plutôt que les vendre *(exemple fictif à retirer)* | déduit | 3 ventes refusées (2026-11-08, 2026-11-09, 2026-11-10) | non |

## Journal des sessions (3 lignes max, le plus récent en haut)
- **<date> (<IA>)** : fait ; fait ; prochain.
