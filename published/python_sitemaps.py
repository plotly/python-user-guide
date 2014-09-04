import os

from django.conf import settings


def items():
    items = [
        dict(
            location='/python/streaming-line-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'streaming-line-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/overview/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'overview',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/bar-charts-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'bar-charts-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/bubble-charts-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'bubble-charts-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/user-guide/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'user-guide',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/streaming-double-pendulum-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'streaming-double-pendulum-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/heatmaps-contours-and-2dhistograms-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'heatmaps-contours-and-2dhistograms-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/streaming-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'streaming-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/histograms-and-box-plots-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'histograms-and-box-plots-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/streaming-bubbles-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'streaming-bubbles-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/line-and-scatter-plots-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'line-and-scatter-plots-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/python-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'python-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/matplotlib-to-plotly-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                'matplotlib-to-plotly-tutorial',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/python/3d-plots-tutorial/',
            lmfile=os.path.join(
                settings.TOP_DIR, 'shelly',
                'templates', 'api_docs', 'includes',
                'user_guide',
                'python',
                '3d-plots-tutorial',
                'body.html'),
            priority=0.5
        )
    ]
    return items
