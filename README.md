# Light House Map Libre
An interactive globe showing ~26,000 animated maritime light sequences from [OpenStreetMap](https://www.openstreetmap.org/), rendered with [MapLibre GL JS](https://maplibre.org/) v5.

![Demo time](https://geodienst.github.io/lighthousemap/demo.gif)

It parses `seamark:*` tags from OSM data — including sequence, character, period, colour, and range — and animates them as coloured circles on a Canvas 2D overlay. Lights without an explicit sequence are synthesized from their character type and period.

If you think a lighthouse or beacon is missing, please add or edit it on [OpenStreetMap](https://www.openstreetmap.org/).

## Credits

Originally created by [Geodienst](https://www.geodienst.xyz). This fork replaces Leaflet with MapLibre GL JS globe projection, adds a canvas overlay animation system, and extends light `seamark:light:character` parsing.
