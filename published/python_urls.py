from django.conf.urls import patterns, url

import api_docs.views


urlpatterns = patterns(
    '',
    url("(?P<user_guide_chapter>streaming-line-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>overview)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>bar-charts-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>bubble-charts-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>user-guide)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>streaming-double-pendulum-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>heatmaps-contours-and-2dhistograms-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>streaming-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>histograms-and-box-plots-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>streaming-bubbles-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>line-and-scatter-plots-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>python-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>matplotlib-to-plotly-tutorial)/$",
        api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>3d-plots-tutorial)/$",
        api_docs.views.user_guide_template)
)
