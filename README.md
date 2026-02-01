# Lighthouse Map Libre
An interactive globe showing ~26,000 animated maritime light sequences from [OpenStreetMap](https://www.openstreetmap.org/), rendered with [MapLibre GL JS](https://maplibre.org/) v5.

<video src="demo-WA.mp4" autoplay loop muted playsinline></video>

It parses `seamark:*` tags from OSM data — including sequence, character, period, colour, and range — and animates them as coloured circles on a Canvas 2D overlay. Lights without an explicit sequence are synthesized from their character type and period.

If you think a lighthouse or beacon is missing, please add or edit it on [OpenStreetMap](https://www.openstreetmap.org/).

## Evaluated OSM Tags

The following `seamark:light:*` tags are used to determine light animations. Tags under the `seamark:light:1:*` namespace are also supported and normalized automatically.

| Tag | Purpose |
|-----|---------|
| `seamark:light:sequence` | Explicit on/off timing pattern, e.g. `1.5+(4),1.5+(13)` |
| `seamark:light:character` | Light type: F, Fl, LFl, Oc, Iso, Q, VQ, UQ, IQ, IVQ, IUQ, Mo, Al.* |
| `seamark:light:period` | Total cycle duration in seconds — used with `character` to synthesize a sequence |
| `seamark:light:colour` | Light colour(s), semicolon-separated for multi-colour lights (e.g. `white;red`) |
| `seamark:light:group` | Number of flashes per group, or Morse letter for Mo characters |
| `seamark:light:range` | Nominal range in nautical miles — controls rendered circle size |

## Credits

Originally forked from an implemenation by [Geodienst](https://www.geodienst.xyz).