from django.urls import path, re_path, include
from rest_framework import routers

from .views import (
    package_views,
    source_views,
    disinformation_type_views,
    Deserializer,
    WebContext,
    WebHome,
    WebArticle
)

from .viewsets import (
    FactCheckViewset,
    SourceViewset,
    DisinformationTypeViewset,
    TagViewset,
    UserViewset
)

# Django REST
router = routers.DefaultRouter()
router.register(
    r'fact-check', FactCheckViewset, base_name='fakenews-fact-check')
router.register(
    r'source', SourceViewset, base_name='fakenews-source')
router.register(
    r'tag', TagViewset, base_name='fakenews-tag')
router.register(
    r'user', UserViewset, base_name='fakenews-user')
router.register(
    r'disinformation-type',
    DisinformationTypeViewset,
    base_name='fakenews-disinformation_type'
)
router.register(r'user', UserViewset, base_name='fakenews-user')

urlpatterns = [
    # CMS – Package
    re_path(
        r'^cms/?$',
        package_views["home"].as_view(),
        name='fakenews-cms-home'
    ),
    path(
        'cms/<int:page>/',
        package_views["list"].as_view(),
        name='fakenews-cms-page'
    ),
    path(
        'cms/<slug:slug>/edit',
        package_views["update"].as_view(),
        name='fakenews-cms-package-edit'
    ),
    path(
        'cms/new',
        package_views["create"].as_view(),
        name='fakenews-cms-package-new'
    ),

    # CMS – Source
    path(
        'cms/source/',
        source_views["list"].as_view(),
        name='fakenews-cms-source'
    ),
    path(
        'cms/source/new',
        source_views["create"].as_view(),
        name='fakenews-cms-source-new'
    ),
    path(
        'cms/source/<int:pk>/edit',
        source_views["update"].as_view(),
        name='fakenews-cms-source-update'
    ),

    # CMS – Disinformation Type
    path(
        'cms/type/',
        disinformation_type_views["list"].as_view(),
        name='fakenews-cms-disinformation_type'
    ),
    path(
        'cms/type/new',
        disinformation_type_views["create"].as_view(),
        name='fakenews-cms-disinformation_type-new'
    ),
    path(
        'cms/type/<int:pk>/edit',
        disinformation_type_views["update"].as_view(),
        name='fakenews-cms-disinformation_type-update'
    ),

    # Django Rest API Views
    path(
        'api/package/',
        Deserializer.as_view(),
        name='fakenews-cms-deserializer'
    ),
    path(
        'api/context/',
        WebContext.as_view(),
        name='fakenews-web-context'
    ),
    path('api/', include(router.urls)),

    # Web URLs
    # path(
    #     '',
    #     WebHome.as_view(),
    #     name='fakenews-web-home'
    # ),
    # path(
    #     '<slug:slug>',
    #     WebArticle.as_view(),
    #     name='fakenews-web-artcile'
    # ),
]
