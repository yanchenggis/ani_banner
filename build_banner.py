html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>KL 3D Buildings</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src='https://unpkg.com/maplibre-gl@3.6.2/dist/maplibre-gl.js'></script>
    <link href='https://unpkg.com/maplibre-gl@3.6.2/dist/maplibre-gl.css' rel='stylesheet' />
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
<div id="map"></div>
<script>
    const map = new maplibregl.Map({
        container: 'map',
        style: 'https://tiles.openfreemap.org/styles/liberty',
        center: [101.7118, 3.1578],
        zoom: 16,
        pitch: 60,
        bearing: -17
    });

    map.on('load', () => {
        // Add 3D buildings
        map.addLayer({
            'id': '3d-buildings',
            'source': 'openmaptiles',
            'source-layer': 'building',
            'type': 'fill-extrusion',
            'minzoom': 14,
            'paint': {
                'fill-extrusion-color': [
                    'interpolate',
                    ['linear'],
                    ['get', 'render_height'],
                    0, '#e0e0e0',
                    50, '#90caf9',
                    100, '#42a5f5',
                    200, '#1976d2',
                    300, '#0d47a1',
                    450, '#ffd700'
                ],
                'fill-extrusion-height': ['get', 'render_height'],
                'fill-extrusion-base': ['get', 'render_min_height'],
                'fill-extrusion-opacity': 0.9
            }
        });
    });
</script>
</body>
</html>
"""

# Save and open in browser
with open('kl_3d_buildings.html', 'w') as f:
    f.write(html_content)

print("Open kl_3d_buildings.html in your browser!")